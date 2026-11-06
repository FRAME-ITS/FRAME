"""Group A fixes on a copy of the FRAME model (SQLite). usage: fixA.py model.qea [--apply]"""
import sqlite3, sys, re, uuid
path = sys.argv[1]; APPLY = '--apply' in sys.argv
c = sqlite3.connect(path); c.row_factory = sqlite3.Row
pk = {r[0]: (r[1], r[2]) for r in c.execute('select Package_ID, Name, Parent_ID from t_package')}
def top(p):
    s = []
    while p in pk and pk[p][1] != 0: s.append(pk[p][0]); p = pk[p][1]
    return (list(reversed(s)) + [''])[0]
O = {r['Object_ID']: dict(name=(r['Name'] or '').strip(), st=r['Stereotype'] or '', top=top(r['Package_ID'])) for r in c.execute('select Object_ID, Name, Stereotype, Package_ID from t_object')}
norm = lambda s: (s or '').lower().replace(' ', '')
REPO = 'Frame Repository'
log = []
def xref_set(guid, desc):
    r = c.execute("select XrefID from t_xref where Client=? and Name='Stereotypes'", (guid,)).fetchone()
    if r: c.execute('update t_xref set Description=? where XrefID=?', (desc, r[0]))
    else:
        c.execute("insert into t_xref (XrefID, Name, Type, Visibility, Partition, Client, Description) values (?,?,?,?,?,?,?)",
                  ('{' + str(uuid.uuid4()).upper() + '}', 'Stereotypes', 'connector property', 'Public', '0', guid, desc))
def delete(k, why):
    log.append(('delete', why, k['ea_guid']))
    if APPLY:
        c.execute('delete from t_diagramlinks where ConnectorID=?', (k['Connector_ID'],))
        c.execute('delete from t_xref where Client=?', (k['ea_guid'],))
        c.execute('delete from t_connectortag where ElementID=?', (k['Connector_ID'],))
        c.execute('delete from t_connector where Connector_ID=?', (k['Connector_ID'],))
def swap_geom(g):
    if not g: return g
    d = dict(re.findall(r'(SX|SY|EX|EY)=(-?\d+)', g))
    if not d: return g
    rep = {'SX': d.get('EX', '0'), 'SY': d.get('EY', '0'), 'EX': d.get('SX', '0'), 'EY': d.get('SY', '0')}
    g = re.sub(r'\b(SX|SY|EX|EY)=(-?\d+)', lambda m: f'{m.group(1)}={rep[m.group(1)]}', g)
    return re.sub(r'EDGE=(\d)', lambda m: 'EDGE=' + {'1': '3', '3': '1', '2': '4', '4': '2'}.get(m.group(1), m.group(1)), g, 1)
def reverse(k, why):
    log.append(('reverse', why, k['ea_guid']))
    if APPLY:
        c.execute('''update t_connector set Start_Object_ID=End_Object_ID, End_Object_ID=Start_Object_ID,
                     Start_Edge=End_Edge, End_Edge=Start_Edge, PtStartX=PtEndX, PtEndX=PtStartX, PtStartY=PtEndY, PtEndY=PtStartY
                     where Connector_ID=?''', (k['Connector_ID'],))
        for dl in c.execute('select Instance_ID, Geometry, Style, Path from t_diagramlinks where ConnectorID=?', (k['Connector_ID'],)).fetchall():
            st = dl['Style'] or ''
            so, eo = re.search(r'SOID=([^;]*);', st), re.search(r'EOID=([^;]*);', st)
            if so and eo:
                st = st.replace(f'SOID={so.group(1)};', 'SOID=@@;').replace(f'EOID={eo.group(1)};', f'EOID={so.group(1)};').replace('SOID=@@;', f'SOID={eo.group(1)};')
            path = ';'.join(reversed([p for p in (dl['Path'] or '').split(';') if p])) + (';' if dl['Path'] else '') if dl['Path'] else dl['Path']
            c.execute('update t_diagramlinks set Geometry=?, Style=?, Path=? where Instance_ID=?', (swap_geom(dl['Geometry']), st, path, dl['Instance_ID']))
def retype(k, ctype, stereo, fq, why, template_sql):
    log.append(('retype', why, k['ea_guid']))
    if APPLY:
        t = c.execute(template_sql).fetchone()
        c.execute('''update t_connector set Connector_Type=?, Stereotype=?, SubType=?, Direction=?, SourceIsAggregate=?, DestIsAggregate=?,
                     SourceIsNavigable=?, DestIsNavigable=?, Btm_Mid_Label=? where Connector_ID=?''',
                  (ctype, stereo, t['SubType'], t['Direction'], t['SourceIsAggregate'], t['DestIsAggregate'], t['SourceIsNavigable'], t['DestIsNavigable'], t['Btm_Mid_Label'], k['Connector_ID']))
        xref_set(k['ea_guid'], f'@STEREO;Name={stereo};FQName={fq};@ENDSTEREO;')
T_COMP = """select c.* from t_connector c join t_object s on s.Object_ID=c.Start_Object_ID join t_object e on e.Object_ID=c.End_Object_ID
            where c.Stereotype='componentof' and s.Stereotype='FRAME_Low_Level_Data_Flow' and e.Stereotype='FRAME_High_Level_Data_Flow' limit 1"""
T_SERV = """select c.* from t_connector c join t_xref x on x.Client=c.ea_guid where x.Description like '%FQName=FRAME_Profile::served by;%' limit 1"""
FLOWLV = {'FRAME_Low_Level_Data_Flow': 0, 'FRAME_High_Level_Data_Flow': 1}
FUNCLV = {'FRAME_Low_Level_Function': 0, 'FRAME_High_Level_Function': 1, 'FRAME_Functional_Area': 2, 'FRAME_System': 3}
pairs = {}
for r in c.execute('select Connector_ID, Start_Object_ID, End_Object_ID, Stereotype, Connector_Type from t_connector'):
    pairs.setdefault((r[1], r[2], norm(r[3]) or r[4]), []).append(r[0])
handled = set()
def fix_direction(k, why):
    key_wrong = (k['Start_Object_ID'], k['End_Object_ID'], norm(k['Stereotype']))
    key_right = (k['End_Object_ID'], k['Start_Object_ID'], norm(k['Stereotype']))
    if key_wrong in handled or pairs.get(key_right):
        delete(k, why.replace('reversed', 'duplicate removed (correct link exists)'))
    else:
        reverse(k, why); handled.add(key_wrong)
for k in c.execute('select * from t_connector').fetchall():
    s, t = O.get(k['Start_Object_ID']), O.get(k['End_Object_ID'])
    st = norm(k['Stereotype'])
    desc = lambda: f"{k['Connector_Type']} «{k['Stereotype']}» {s['name'] if s else '?'} ({s['st'] if s else '-'}) → {t['name'] if t else '?'} ({t['st'] if t else '-'})"
    if not s or not t:
        delete(k, 'A1 dangling: ' + desc()); continue
    if REPO not in (s['top'], t['top']):
        continue
    if k['Start_Object_ID'] == k['End_Object_ID']:
        delete(k, 'A2 self-reference: ' + desc()); continue
    if k['Connector_Type'] == 'Generalization' and (s['st'] in FLOWLV or t['st'] in FLOWLV):
        if FLOWLV.get(s['st'], 9) > FLOWLV.get(t['st'], 9): reverse(k, 'A3 orientation part→whole: ' + desc())
        retype(k, 'Aggregation', 'componentof', 'FRAME_Profile::componentof', 'A3 Generalization → «componentof» (#79): ' + desc(), T_COMP); continue
    if st == 'componentof':
        if s['st'] == 'FRAME_High_Level_Data_Flow' and t['st'] == 'FRAME_Low_Level_Data_Flow':
            fix_direction(k, 'A4 whole→part reversed (#80): ' + desc())
        elif s['st'] in FUNCLV and t['st'] in FUNCLV and FUNCLV[s['st']] > FUNCLV[t['st']]:
            fix_direction(k, 'A4 whole→part reversed: ' + desc())
    if s['st'] == 'FRAME_User_Need' and t['st'] == 'FRAME_Low_Level_Function' and st in ('componentof', 'belongsto'):
        retype(k, 'Association', 'served by', 'FRAME_Profile::served by', 'A5 → «served by»: ' + desc(), T_SERV)
from collections import Counter
print(Counter(w.split(' ')[0] for _, w, _ in log))
for a, w, g in log: print(f'{a:8} {w}  {g}')
if APPLY: c.commit(); print('APPLIED')
