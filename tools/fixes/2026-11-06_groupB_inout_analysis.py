"""Group B analysis (no changes to the model): proposes a fix for every IN/OUT connector that contradicts the
FRAME convention (IN: producer → flow, OUT: flow → consumer), with the evidence and a confidence level.
usage: analyseB.py model.qea report.md report.csv"""
import sqlite3, sys, re, csv
from collections import defaultdict
path, out_md, out_csv = sys.argv[1:4]
c = sqlite3.connect(f'file:{path}?mode=ro', uri=True); c.row_factory = sqlite3.Row
pk = {r[0]: (r[1], r[2]) for r in c.execute('select Package_ID, Name, Parent_ID from t_package')}
def top(p):
    s = []
    while p in pk and pk[p][1] != 0: s.append(pk[p][0]); p = pk[p][1]
    return (list(reversed(s)) + [''])[0]
O = {r['Object_ID']: dict(name=(r['Name'] or '').strip(), st=r['Stereotype'] or '', top=top(r['Package_ID'])) for r in c.execute('select Object_ID, Name, Stereotype, Package_ID from t_object')}
FLOW = {'FRAME_Low_Level_Data_Flow', 'FRAME_High_Level_Data_Flow'}
END = {'FRAME_Low_Level_Function', 'FRAME_High_Level_Function', 'FRAME_Functional_Area', 'FRAME_System', 'FRAME_Terminator', 'FRAME_Datastore'}
FA = {'1': 'pepf', '2': 'psef', '3': 'mt', '4': 'mpto', '5': 'pshvs', '6': 'ptja', '7': 'psle', '8': 'mffo', '9': 'pscs'}
def area(name):
    m = re.match(r'F(\d)', name)
    return FA.get(m.group(1)) if m else None
links = []
for k in c.execute("select Connector_ID, ea_guid, Stereotype, Start_Object_ID, End_Object_ID from t_connector where upper(Stereotype) in ('IN','OUT')"):
    s, t = O.get(k['Start_Object_ID']), O.get(k['End_Object_ID'])
    if not s or not t: continue
    if s['st'] in FLOW and t['st'] in END: flow, ep, fid, eid, cur_dir = t and s, t, k['Start_Object_ID'], k['End_Object_ID'], 'flow→ep'
    elif t['st'] in FLOW and s['st'] in END: flow, ep, fid, eid, cur_dir = t, s, k['End_Object_ID'], k['Start_Object_ID'], 'ep→flow'
    else: continue
    lab = k['Stereotype'].upper()
    ok = (lab == 'IN' and cur_dir == 'ep→flow') or (lab == 'OUT' and cur_dir == 'flow→ep')
    links.append(dict(guid=k['ea_guid'], lab=lab, dir=cur_dir, flow=flow, ep=ep, fid=fid, eid=eid, ok=ok))
role_by_flow = defaultdict(dict)  # flow id -> endpoint id -> 'producer'/'consumer' from correct links
for l in links:
    if l['ok']:
        role_by_flow[l['fid']][l['eid']] = 'producer' if l['lab'] == 'IN' else 'consumer'
def name_role(flow, ep):
    """Role of the endpoint derived from the FRAME data flow naming convention."""
    n = flow['name']
    if ep['st'] == 'FRAME_Terminator':
        if re.match(r'^f[a-z]', n): return 'producer', f'flow name "{n[:12]}…" = from terminator'
        if re.match(r'^t[a-z]', n): return 'consumer', f'flow name "{n[:12]}…" = to terminator'
        return None, ''
    a = area(ep['name'])
    if ep['st'] == 'FRAME_Functional_Area' and not a:
        m = re.search(r'F(\d)', ep['name']); a = FA.get(m.group(1)) if m else None
    if not a: return None, ''
    m = re.match(r'^([a-z]+)\.([a-z]+)[-_]', n)
    if m:
        if m.group(1) == a and m.group(2) != a: return 'producer', f'flow {m.group(1)}→{m.group(2)}, function in {a}'
        if m.group(2) == a and m.group(1) != a: return 'consumer', f'flow {m.group(1)}→{m.group(2)}, function in {a}'
    if re.match(r'^f[a-z]+[.-]', n) and not n.startswith(a + '.'): return 'consumer', f'flow "{n[:12]}…" from a terminator into the system'
    if re.match(r'^t[a-z]+[.-]', n) and not n.startswith(a + '.'): return 'producer', f'flow "{n[:12]}…" from the system to a terminator'
    return None, ''
rows = []
for l in links:
    if l['ok']: continue
    nr, why_n = name_role(l['flow'], l['ep'])
    others = {r for e, r in role_by_flow[l['fid']].items() if e != l['eid']}
    or_ = None; why_o = ''
    if others == {'producer'}: or_, why_o = 'consumer', 'flow already has a producer'
    elif others == {'consumer'} and l['ep']['st'] != 'FRAME_Terminator': or_, why_o = 'producer', 'flow already has a consumer'
    label_role = 'producer' if l['lab'] == 'IN' else 'consumer'      # what the label says
    dir_role = 'producer' if l['dir'] == 'ep→flow' else 'consumer'   # what the direction says
    evidence = [x for x in (nr, or_) if x]
    if nr and or_ and nr != or_: role, conf = None, 'conflict'
    elif evidence: role, conf = evidence[0], 'high' if (nr and or_) else 'medium'
    else: role, conf = None, 'unknown'
    if role is None: action = 'review in EA'
    elif role == dir_role: action = f'relabel «{l["lab"]}» → «{"OUT" if l["lab"] == "IN" else "IN"}»'
    elif role == label_role: action = 'reverse direction (keep label)'
    else: action = 'review in EA'
    rows.append(dict(scope='FRAME Repository' if 'Frame Repository' in (l['flow']['top'], l['ep']['top']) else l['flow']['top'],
                     guid=l['guid'], label=l['lab'], direction=l['dir'].replace('ep', l['ep']['st'].replace('FRAME_', '')),
                     flow=l['flow']['name'], endpoint=l['ep']['name'], role=role or '?', confidence=conf, action=action,
                     evidence='; '.join(x for x in (why_n, why_o) if x)))
rows.sort(key=lambda r: (r['scope'] != 'FRAME Repository', {'high': 0, 'medium': 1, 'conflict': 2, 'unknown': 3}[r['confidence']], r['flow']))
with open(out_csv, 'w', newline='', encoding='utf-8-sig') as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0]), delimiter=';'); w.writeheader(); w.writerows(rows)
from collections import Counter
cnt = Counter((r['scope'] == 'FRAME Repository', r['confidence'], r['action'].split(' ')[0]) for r in rows)
md = ['# Proposal – IN/OUT connectors against the convention (#69)', '',
      'Convention (prevailing use in V5.2): **«IN» producer → data flow**, **«OUT» data flow → consumer** – the arrow follows the data.',
      'For every deviating connector the role of the function/terminator is derived from the data flow naming convention',
      '(`f<terminator>-…` from, `t<terminator>-…` to a terminator, `abc.def-…` from area abc to area def) and from the other links of the same flow.', '',
      f'{len(rows)} connectors. **No change has been made yet** – group B is applied only after review.', '',
      '| Scope | Confidence | Proposed action | Count |', '|---|---|---|---|']
md += [f'| {"FRAME Repository" if rep else "Reference architectures"} | {conf} | {act} | {n} |' for (rep, conf, act), n in sorted(cnt.items(), key=lambda x: (not x[0][0], x[0][1], x[0][2]))]
md += ['', '| Scope | Flow | Endpoint | Now | Proposed | Confidence | Evidence |', '|---|---|---|---|---|---|---|']
md += [f'| {r["scope"]} | {r["flow"]} | {r["endpoint"]} | «{r["label"]}» {r["direction"]} | {r["action"]} | {r["confidence"]} | {r["evidence"]} |' for r in rows]
open(out_md, 'w', encoding='utf-8', newline='\n').write('\n'.join(md) + '\n')
print(len(rows), 'rows'); [print(n, k) for k, n in sorted(cnt.items())]
