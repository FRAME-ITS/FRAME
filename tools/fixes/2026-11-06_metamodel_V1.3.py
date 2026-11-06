"""Align the FRAME Meta Model diagram with technology V1.3.

usage: 2026-11-06_metamodel_V1.3.py model.qea report.md [--apply]
  - element 'Requirement' had the misspelt stereotype FRAME_Reqirement → FRAME_Requirement
  - connectors drawn opposite to the V1.3 rule are reversed (function hierarchy «component of», user-need hierarchy
    «belongs to», IN/OUT of the terminator)
  - User_Need → UserNeedTopic (plain Association) becomes «belongs to»
Connectors of the meta model for which V1.3 has no rule are listed, not changed (they need a decision).
"""
import sys, os, re, sqlite3
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from mdg import rules
path, rep = sys.argv[1:3]; APPLY = '--apply' in sys.argv
rl, defined = rules(open('drafts/latest/toolbox/FRAME_Technology_V1.3.xml', 'rb').read().decode('cp1252'))
R = {(a, b, c) for a, b, c in rl}
c = sqlite3.connect(path); c.row_factory = sqlite3.Row
M = [r[0] for r in c.execute("select Package_ID from t_package where Name in ('FRAME_Metamodel', 'FRAME Meta Model')")]
q = ','.join(map(str, M)); log = []

for o in c.execute(f"select Object_ID, ea_guid, Name from t_object where Package_ID in ({q}) and Stereotype='FRAME_Reqirement'").fetchall():
    c.execute("update t_object set Stereotype='FRAME_Requirement' where Object_ID=?", (o['Object_ID'],))
    c.execute("update t_xref set Description=replace(replace(Description,'Name=FRAME_Reqirement;','Name=FRAME_Requirement;'),'::FRAME_Reqirement;','::FRAME_Requirement;') where Client=? and Name='Stereotypes'", (o['ea_guid'],))
    log.append(f'element {o["Name"]}: stereotype FRAME_Reqirement → FRAME_Requirement')

def swap_geom(g):
    d = dict(re.findall(r'(SX|SY|EX|EY)=(-?\d+)', g or ''))
    if not d: return g
    r = {'SX': d.get('EX', '0'), 'SY': d.get('EY', '0'), 'EX': d.get('SX', '0'), 'EY': d.get('SY', '0')}
    g = re.sub(r'\b(SX|SY|EX|EY)=(-?\d+)', lambda m: f'{m.group(1)}={r[m.group(1)]}', g)
    return re.sub(r'EDGE=(\d)', lambda m: 'EDGE=' + {'1': '3', '3': '1', '2': '4', '4': '2'}.get(m.group(1), m.group(1)), g, 1)
def reverse(k):
    c.execute('''update t_connector set Start_Object_ID=End_Object_ID, End_Object_ID=Start_Object_ID, Start_Edge=End_Edge,
                 End_Edge=Start_Edge, PtStartX=PtEndX, PtEndX=PtStartX, PtStartY=PtEndY, PtEndY=PtStartY where Connector_ID=?''', (k,))
    for dl in c.execute('select Instance_ID, Geometry, Style, Path from t_diagramlinks where ConnectorID=?', (k,)).fetchall():
        st = dl['Style'] or ''
        so, eo = re.search(r'SOID=([^;]*);', st), re.search(r'EOID=([^;]*);', st)
        if so and eo:
            st = st.replace(f'SOID={so.group(1)};', 'SOID=@@;').replace(f'EOID={eo.group(1)};', f'EOID={so.group(1)};').replace('SOID=@@;', f'SOID={eo.group(1)};')
        p = dl['Path']; p = ';'.join(reversed([x for x in p.split(';') if x])) + ';' if p else p
        c.execute('update t_diagramlinks set Geometry=?, Style=?, Path=? where Instance_ID=?', (swap_geom(dl['Geometry']), st, p, dl['Instance_ID']))

T_BEL = c.execute("""select k.* from t_connector k join t_object a on a.Object_ID=k.Start_Object_ID join t_object b on b.Object_ID=k.End_Object_ID
                     where k.Stereotype='belongs to' and a.Stereotype='FRAME_User_Need' and b.Stereotype='FRAME_User_Need_Topic' limit 1""").fetchone()
xd = c.execute("select Description from t_xref where Client=? and Name='Stereotypes'", (T_BEL['ea_guid'],)).fetchone()[0]
open_items = []
for k in c.execute(f"""select k.Connector_ID, k.ea_guid, k.Connector_Type ty, k.Stereotype st, x.Stereotype a, x.Name an, y.Stereotype b, y.Name bn
                       from t_connector k join t_object x on x.Object_ID=k.Start_Object_ID join t_object y on y.Object_ID=k.End_Object_ID
                       where x.Package_ID in ({q}) or y.Package_ID in ({q})""").fetchall():
    st, a, b = k['st'], k['a'], k['b']
    if (st, a, b) in R: continue
    if (st, b, a) in R:
        reverse(k['Connector_ID']); log.append(f'reversed: «{st}» {k["an"]} → {k["bn"]}  becomes  {k["bn"]} → {k["an"]}'); continue
    if not st and k['ty'] == 'Association' and ('belongs to', a, b) in R:
        c.execute('update t_connector set Stereotype=?, Btm_Mid_Label=?, Direction=?, SourceStyle=?, DestStyle=? where Connector_ID=?',
                  ('belongs to', T_BEL['Btm_Mid_Label'], T_BEL['Direction'], T_BEL['SourceStyle'], T_BEL['DestStyle'], k['Connector_ID']))
        c.execute("delete from t_xref where Client=? and Name='Stereotypes'", (k['ea_guid'],))
        c.execute("insert into t_xref (XrefID, Name, Type, Visibility, Partition, Client, Supplier, Description) values (?,?,?,?,?,?,?,?)",
                  ('{%s}' % __import__('uuid').uuid4().__str__().upper(), 'Stereotypes', 'connector property', 'Public', '0', k['ea_guid'], '<none>', xd))
        log.append(f'Association → «belongs to»: {k["an"]} → {k["bn"]}'); continue
    open_items.append(f'{k["ty"]} «{st or ""}» {k["an"]} ({(a or "")[6:]}) → {k["bn"]} ({(b or "")[6:]})')
md = ['# FRAME Meta Model aligned with technology V1.3', '', 'Script: `tools/fixes/2026-11-06_metamodel_V1.3.py`.', ''] + [f'- {l}' for l in log]
md += ['', f'## Meta-model connectors without a V1.3 rule ({len(open_items)}) – need a decision', ''] + [f'- {l}' for l in sorted(open_items)]
open(rep, 'w', encoding='utf-8', newline='\n').write('\n'.join(md) + '\n')
print('\n'.join(md[4:]))
if APPLY:
    c.commit(); print('APPLIED')
