"""Check the FRAME model against its modelling conventions.

Usage:  python tools/check.py [model/FRAME.qea] [report.md] [--strict]

The rules are derived from how the FRAME Repository (V5.2) is modelled; the prevailing pattern is taken
as the convention and deviations are reported. Rules are linked to the GitHub issues they relate to.
  Errors   – a deviation that breaks the meaning of the model (direction, missing end, wrong link type).
  Warnings – worth a look (naming variants, unused elements, incomplete functions, release hygiene).
With --strict the script exits with code 1 when there are errors (for CI once the model is clean).

Conventions (FRAME Repository V5.2):
  «IN»   Association  function / terminator / data store / functional area / system  →  data flow
  «OUT»  Association  data flow  →  function / terminator / data store / functional area / system
  «component of» Aggregation  part → whole  (low-level → high-level data flow, high-level → high-level data flow,
                             low-level → high-level function → functional area → system, sub-terminator → terminator)
  «served by» Association     User Need → low-level function
"""
import sys, os, sqlite3
from collections import defaultdict, Counter
sys.path.insert(0, os.path.dirname(__file__))
from frame_model import package_paths, MODEL

REPO = 'Frame Repository'
META = ('FRAME Meta Model', 'FRAME Toolsetup')   # define stereotypes and their links – not part of the architecture
FLOW = {'FRAME_Low_Level_Data_Flow': 0, 'FRAME_High_Level_Data_Flow': 1}
FUNC = {'FRAME_Low_Level_Function': 0, 'FRAME_High_Level_Function': 1, 'FRAME_Functional_Area': 2, 'FRAME_System': 3}
ENDPOINT = set(FUNC) | {'FRAME_Terminator', 'FRAME_Datastore'}
ISSUE = {'dangling': '', 'self-reference': '#62', 'in-out': '#69', 'componentof': '#80, #81', 'generalization': '#79',
         'servedby': '', 'stereotype-spelling': '#86', 'unused-flow': '#76', 'function-flows': '', 'function-parent': '',
         'context-diagram': '#91', 'duplicate': '', 'release-hygiene': ''}
norm = lambda s: (s or '').lower().replace(' ', '')


def main(argv):
    strict = '--strict' in argv
    args = [a for a in argv if a != '--strict']
    model = args[0] if args else MODEL
    out = args[1] if len(args) > 1 else None
    c = sqlite3.connect(f'file:{model}?mode=ro', uri=True)
    c.row_factory = sqlite3.Row
    pk, ppath = package_paths(c)
    obj = {r['Object_ID']: dict(id=r['Object_ID'], name=(r['Name'] or '').strip(), type=r['Object_Type'], st=r['Stereotype'] or '',
                                pkg=ppath(r['Package_ID']), guid=r['ea_guid'])
           for r in c.execute('select Object_ID, Name, Object_Type, Stereotype, Package_ID, ea_guid from t_object')}
    con = [dict(type=r['Connector_Type'], st=r['Stereotype'] or '', s=obj.get(r['Start_Object_ID']), t=obj.get(r['End_Object_ID']), guid=r['ea_guid'])
           for r in c.execute('select Connector_Type, Stereotype, Start_Object_ID, End_Object_ID, ea_guid from t_connector')]
    on_diagram = defaultdict(set)
    for d, o in c.execute('select d.Name, o.Object_ID from t_diagramobjects o join t_diagram d on d.Diagram_ID = o.Diagram_ID'):
        on_diagram[o].add(d)
    errors, warnings = [], []
    E = lambda rule, msg: errors.append((rule, msg))
    W = lambda rule, msg: warnings.append((rule, msg))
    where = lambda o: o['pkg'].split('/')[0] if o['pkg'] else '(root)'
    label = lambda o: f'{o["st"].replace("FRAME_", "") or o["type"]} **{o["name"]}** ({where(o)})'

    # --- connectors
    spelling = defaultdict(Counter)
    for k in con:
        s, t = k['s'], k['t']
        if k['st']:
            spelling[norm(k['st'])][k['st']] += 1
        if not s or not t:
            E('dangling', f'{k["type"]} «{k["st"]}» {k["guid"]} has a missing end'); continue
        if s['pkg'].startswith(META) or t['pkg'].startswith(META) or not s['pkg'] or not t['pkg']:
            continue
        # deviations inside the FRAME Repository are errors; in reference architectures and other packages warnings
        R = E if (s['pkg'].startswith(REPO) or t['pkg'].startswith(REPO)) else W
        if s['id'] == t['id'] and k['type'] not in ('Dependency',) and s['type'] != 'Package':
            R('self-reference', f'{label(s)} has a {k["type"]} «{k["st"]}» to itself')
        st = norm(k['st'])
        if k['type'] == 'Association' and st in ('in', 'out'):
            sf, tf = s['st'] in FLOW, t['st'] in FLOW
            if sf != tf and (s['st'] in ENDPOINT or t['st'] in ENDPOINT):
                want = 'IN' if tf else 'OUT'
                if st != want.lower():
                    R('in-out', f'«{k["st"]}» {label(s)} → {t["name"]}: expected «{want}» for this direction (or reverse the connector)')
        if st == 'componentof':
            if s['st'] in FLOW and t['st'] in FLOW and (FLOW[s['st']] > FLOW[t['st']] or FLOW[s['st']] == FLOW[t['st']] == 0):
                R('componentof', f'«{k["st"]}» {label(s)} → {t["name"]} ({t["st"].replace("FRAME_", "")}) runs whole → part or between low-level flows')
            elif s['st'] in FUNC and t['st'] in FUNC and FUNC[s['st']] > FUNC[t['st']]:
                R('componentof', f'«{k["st"]}» {label(s)} → {t["name"]} ({t["st"].replace("FRAME_", "")}) runs whole → part')
        if k['type'] == 'Generalization' and (s['st'] in FLOW or t['st'] in FLOW):
            R('generalization', f'Generalization {label(s)} → {t["name"]}: data flows are linked by «component of»')
        if s['st'] == 'FRAME_User_Need' and t['st'] in FUNC and st != 'servedby':
            R('servedby', f'{label(s)} → {t["name"]} is {k["type"]} «{k["st"]}», expected Association «served by»')
    for n, variants in spelling.items():
        if len(variants) > 1:
            W('stereotype-spelling', 'connector stereotype written in ' + str(len(variants)) + ' ways: '
              + ', '.join(f'«{v}» {cnt}×' for v, cnt in variants.most_common()))

    # --- FRAME Repository completeness
    links = defaultdict(list)
    for k in con:
        if k['s'] and k['t']:
            links[k['s']['id']].append((k, k['t'])); links[k['t']['id']].append((k, k['s']))
    repo = [o for o in obj.values() if o['pkg'].startswith(REPO)]
    for o in repo:
        if o['st'] in FLOW and not on_diagram[o['id']]:
            W('unused-flow', f'{label(o)} is not shown in any diagram')
        if o['st'] == 'FRAME_Low_Level_Function':
            sts = {norm(k['st']) for k, other in links[o['id']] if other['st'] in FLOW}
            missing = [x.upper() for x in ('in', 'out') if x not in sts]
            if missing:
                W('function-flows', f'{label(o)} has no {" and ".join(missing)} data flows')
            if not any(norm(k['st']) == 'componentof' and k['s']['id'] == o['id'] for k, _ in links[o['id']]):
                W('function-parent', f'{label(o)} is not «component of» a high-level function or functional area')
    ctx = {o for o, ds in on_diagram.items() if any('Context Diagram' in (d or '') for d in ds)}
    if ctx:
        for o in repo:
            sub = any(norm(k['st']) == 'componentof' and k['s']['id'] == o['id'] and other['st'] == 'FRAME_Terminator' for k, other in links[o['id']])
            if o['st'] == 'FRAME_Terminator' and o['id'] not in ctx and o['type'] == 'Actor' and not sub:
                if any(other['st'] == 'FRAME_High_Level_Data_Flow' for _, other in links[o['id']]):
                    W('context-diagram', f'{label(o)} has high-level data flows but is not in the FRAME Context Diagram')
    seen = defaultdict(list)
    for o in repo:
        if o['st'] and o['name']:
            seen[(o['st'], o['name'])].append(o)
    for (st, n), lst in seen.items():
        if len(lst) > 1:
            W('duplicate', f'{len(lst)}× {st.replace("FRAME_", "")} **{n}** in the FRAME Repository')

    # --- release hygiene
    for pid, (name, parent) in pk.items():
        if 'test' in name.lower() and parent in pk and pk[parent][1] == 0:
            W('release-hygiene', f'top-level package **{name}** looks like a test package – remove before a release')

    # --- report
    md = [f'# Model check – {os.path.basename(model)}', '', f'**{len(errors)} errors, {len(warnings)} warnings**', '',
          '| Rule | Related issue | Errors | Warnings |', '|---|---|---|---|']
    ce, cw = Counter(r for r, _ in errors), Counter(r for r, _ in warnings)
    md += [f'| {r} | {ISSUE.get(r, "")} | {ce[r]} | {cw[r]} |' for r in sorted(set(ce) | set(cw))]
    md.append('')
    for title, items in (('Errors', errors), ('Warnings', warnings)):
        if not items:
            continue
        md += [f'## {title}', '']
        groups = defaultdict(list)
        for r, m in items:
            groups[r].append(m)
        for r in sorted(groups):
            md.append(f'<details><summary><b>{r}</b> ({len(groups[r])})</summary>\n')
            md += [f'- {m}' for m in sorted(groups[r])]
            md.append('\n</details>\n')
    text = '\n'.join(md) + '\n'
    if out:
        open(out, 'w', encoding='utf-8', newline='\n').write(text); print(f'{len(errors)} errors, {len(warnings)} warnings → {out}')
    else:
        sys.stdout.write(text)
    return 1 if (strict and errors) else 0


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))
