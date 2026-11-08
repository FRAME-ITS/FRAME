"""Reference architectures, second pass (decided 2026-11-06): links that got a FRAME relationship in V1.3 (contains, use,
triggers, delivers value to, Specification «defines» Requirement) and deletion of links that should not exist.
Based on 2026-11-06_ra_links_V1.3.py.

usage: 2026-11-06_ra_links_2_V1.3.py model.qea report.md [--apply]
Each mapping below was decided by the git maintainer (2026-11-06). A link is retyped (connector type, stereotype, label,
direction and end styles taken from an existing link of the target kind) and, where the V1.3 rule runs the other way,
its ends are swapped (diagram geometry follows). Links that would duplicate an existing FRAME link are deleted instead.
The NAP element 'Vision' had the undefined stereotype FRAME_Vision and becomes FRAME_ITS_Vision first.
"""
import sys, os, re, sqlite3, uuid
from collections import Counter
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from frame_model import package_paths
path, rep = sys.argv[1:3]; APPLY = '--apply' in sys.argv
c = sqlite3.connect(path); c.row_factory = sqlite3.Row
guid = lambda: '{' + str(uuid.uuid4()).upper() + '}'
F = lambda s: 'FRAME_' + s
# (RA, view prefix or '', connector type, old stereotype or None, source, target, new stereotype, reverse)
MAP = [
    # ITS Service Added Value → Stakeholder: «delivers value to» replaces «defines» (also in the FRAME Meta Model)
    ('*', '', 'Association', 'defines', 'ITS_Service_Added_Value', 'Stakeholder', 'delivers value to', False),
    ('', '', 'Usage', 'Instantiate', 'ITS_Service_Added_Value', 'Stakeholder', 'delivers value to', False),
    ('', '', 'Association', None, 'Stakeholder', 'ITS_Service_Added_Value', 'delivers value to', True),
    # Application «contains» LL function / data store / physical data flow
    ('', '', 'Usage', None, 'Application', 'Low_Level_Function', 'contains', False),
    ('', '', 'Dependency', None, 'Application', 'Low_Level_Function', 'contains', False),
    ('', '', 'Usage', None, 'Application', 'Datastore', 'contains', False),
    ('', '', 'Usage', None, 'Application', 'Physical_Data_Flow', 'contains', False),
    ('', '', 'Usage', None, 'Physical_Data_Flow', 'Application', 'contains', True),
    # LL data flow «contains» Information Object
    ('', '', 'Usage', None, 'Low_Level_Data_Flow', 'Information_Object', 'contains', False),
    ('', '', 'Usage', None, 'Information_Object', 'Low_Level_Data_Flow', 'contains', True),
    ('', '', 'Abstraction', None, 'Information_Object', 'Low_Level_Data_Flow', 'contains', True),
    # Component / Terminator «use» Physical Data Flow (one link for both directions; IN+OUT pairs collapse into one)
    ('', '', 'Usage', None, 'Terminator', 'Physical_Data_Flow', 'use', False),
    ('', '', 'Usage', None, 'Physical_Data_Flow', 'Terminator', 'use', True),
    ('', '', 'Association', 'IN', 'Component', 'Physical_Data_Flow', 'use', False),
    ('', '', 'Association', 'OUT', 'Physical_Data_Flow', 'Component', 'use', True),
    ('', '', 'Usage', None, 'Component', 'Physical_Data_Flow', 'use', False),
    ('', '', 'Usage', None, 'Physical_Data_Flow', 'Component', 'use', True),
    # National Body: process «triggers» process
    ('National Body Reference Architecture', '', 'Dependency', None, 'ITS_Service_Process', 'ITS_Service_Process', 'triggers', False),
    ('National Body Reference Architecture', '', 'Usage', 'Call', 'ITS_Service_Process', 'ITS_Service_Process', 'triggers', False),
    ('National Body Reference Architecture', '', 'Usage', 'Instantiate', 'ITS_Service_Process', 'ITS_Service_Process', 'triggers', False),
    ('National Body Reference Architecture', '', 'Dependency', None, 'ITS_Business_Process', 'ITS_Business_Process', 'triggers', False),
    # eCall: Requirement → Specification is the wrong way round: Specification «defines» Requirement
    ('eCall Reference Architecture', '', 'Association', None, 'Requirement', 'Specification', 'defines', True),
]
pk, ppath = package_paths(c)
log = []
# NAP Vision element
for o in c.execute("select Object_ID, ea_guid, Name, Package_ID from t_object where Stereotype='FRAME_Vision'").fetchall():
    c.execute("update t_object set Stereotype='FRAME_ITS_Vision' where Object_ID=?", (o['Object_ID'],))
    d = '@STEREO;Name=FRAME_ITS_Vision;FQName=FRAME_Profile::FRAME_ITS_Vision;@ENDSTEREO;'
    if c.execute("select 1 from t_xref where Client=? and Name='Stereotypes'", (o['ea_guid'],)).fetchone():
        c.execute("update t_xref set Description=? where Client=? and Name='Stereotypes'", (d, o['ea_guid']))
    else:
        c.execute("insert into t_xref (XrefID, Name, Type, Visibility, Partition, Client, Supplier, Description) values (?,?,?,?,?,?,?,?)",
                  (guid(), 'Stereotypes', 'element property', 'Public', '0', o['ea_guid'], '<none>', d))
    log.append(('NAP element', f'{o["Name"]} ({ppath(o["Package_ID"])}): stereotype FRAME_Vision → FRAME_ITS_Vision', 1))

def template(st, s, t):
    q = """select k.* from t_connector k join t_object a on a.Object_ID=k.Start_Object_ID join t_object b on b.Object_ID=k.End_Object_ID
           join t_xref x on x.Client=k.ea_guid and x.Name='Stereotypes' and x.Description like ?
           where k.Stereotype=? {} limit 1"""
    like = f'%FQName=FRAME_Profile::{st};%'
    return (c.execute(q.format('and a.Stereotype=? and b.Stereotype=?'), (like, st, s, t)).fetchone()
            or c.execute(q.format(''), (like, st)).fetchone()
            or c.execute(q.format(''), ('%FQName=FRAME_Profile::use;%', 'use')).fetchone())   # new stereotypes: defined like «use»

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
COLS = ('Connector_Type', 'Stereotype', 'Direction', 'Btm_Mid_Label', 'SourceStyle', 'DestStyle', 'SourceIsNavigable',
        'DestIsNavigable', 'SourceIsAggregate', 'DestIsAggregate', 'SubType')
obj = {r['Object_ID']: (r['Stereotype'] or '', ppath(r['Package_ID'])) for r in c.execute('select Object_ID, Stereotype, Package_ID from t_object')}
for ra, view, ty, old, s, t, new, rev in MAP:
    rows = c.execute('select * from t_connector where Connector_Type=? and ifnull(Stereotype,\'\')=?', (ty, old or '')).fetchall()
    for k in rows:
        a, b = obj.get(k['Start_Object_ID']), obj.get(k['End_Object_ID'])
        if not a or not b or a[0] != F(s) or b[0] != F(t): continue
        top, sub = (a[1].split('/') + [''])[:2]
        if ra != '*' and ('Reference Architecture' not in top or (ra and top != ra) or (view and sub != view)): continue
        S, T = (k['End_Object_ID'], k['Start_Object_ID']) if rev else (k['Start_Object_ID'], k['End_Object_ID'])
        key = (top.replace(' Reference Architecture', ' RA'), f'{ty} «{old or ""}» {s} → {t}', f'{"reverse, " if rev else ""}«{new}»')
        dup = c.execute('select Connector_ID from t_connector where Start_Object_ID=? and End_Object_ID=? and Stereotype=? and Connector_ID<>?', (S, T, new, k['Connector_ID'])).fetchone()
        if dup:
            c.execute('delete from t_diagramlinks where ConnectorID=?', (k['Connector_ID'],)); c.execute('delete from t_xref where Client=?', (k['ea_guid'],))
            c.execute('delete from t_connectortag where ElementID=?', (k['Connector_ID'],)); c.execute('delete from t_connector where Connector_ID=?', (k['Connector_ID'],))
            log.append(key[:2] + ('duplicate of an existing FRAME link – deleted',)); continue
        tp = template(new, F(t) if rev else F(s), F(s) if rev else F(t))
        if not tp: sys.exit(f'no template for «{new}»')
        if rev: reverse(k['Connector_ID'])
        c.execute(f'update t_connector set {", ".join(x + "=?" for x in COLS)} where Connector_ID=?', [tp[x] for x in COLS] + [k['Connector_ID']])
        c.execute('update t_connector set Stereotype=?, Btm_Mid_Label=? where Connector_ID=?',
                  (new, re.sub('«[^»]*»', f'«{new}»', tp['Btm_Mid_Label'] or f'«{new}»'), k['Connector_ID']))
        xd = f'@STEREO;Name={new};FQName=FRAME_Profile::{new};@ENDSTEREO;'
        c.execute("delete from t_xref where Client=? and Name='Stereotypes'", (k['ea_guid'],))
        c.execute("insert into t_xref (XrefID, Name, Type, Visibility, Partition, Client, Supplier, Description) values (?,?,?,?,?,?,?,?)",
                  (guid(), 'Stereotypes', 'connector property', 'Public', '0', k['ea_guid'], '<none>', xd))
        log.append(key)

# links that should not exist (decided 2026-11-06): plain UML links between two elements of the same kind and
# Component → Component / Interface (interfaces are linked through the physical data flow)
DELETE = [('C-ITS Reference Architecture', 'Component', 'Component'), ('C-ITS Reference Architecture', 'Component', 'Interface'),
          ('', 'User_Need', 'User_Need'), ('', 'User_Need', 'User_Need_Service'), ('', 'User_Need_Service', 'User_Need'),
          ('', 'Role', 'Role'), ('', 'Information_Object', 'Information_Object'), ('', 'Data_Object', 'Data_Object'), ('', 'Actor', 'Actor')]
FRAME_ST = {r[0] for r in c.execute("select Name from t_object where Package_ID=(select Package_ID from t_package where Name='FRAME_Profile') and Stereotype='stereotype'")}
for k in c.execute('select * from t_connector').fetchall():
    a, b = obj.get(k['Start_Object_ID']), obj.get(k['End_Object_ID'])
    if not a or not b or (k['Stereotype'] in FRAME_ST): continue
    top = a[1].split('/')[0]
    if 'Reference Architecture' not in top: continue
    for ra, s, t in DELETE:
        if a[0] == F(s) and b[0] == F(t) and (not ra or top == ra):
            c.execute('delete from t_diagramlinks where ConnectorID=?', (k['Connector_ID'],)); c.execute('delete from t_xref where Client=?', (k['ea_guid'],))
            c.execute('delete from t_connectortag where ElementID=?', (k['Connector_ID'],)); c.execute('delete from t_connector where Connector_ID=?', (k['Connector_ID'],))
            log.append((top.replace(' Reference Architecture', ' RA'), f'{k["Connector_Type"]} «{k["Stereotype"] or ""}» {s} → {t}', 'deleted (should not exist)'))
            break
cnt = Counter(log)
md = ['# Reference architectures, second pass: new V1.3 relationships and links that should not exist', '', 'Script: `tools/fixes/2026-11-06_ra_links_2_V1.3.py`; mappings decided by the git maintainer.', '',
      f'{len(log)} changes.', '', '| RA | Link before | After | Count |', '|---|---|---|---|']
md += [f'| {a} | {b} | {d} | {n} |' for (a, b, d), n in sorted(cnt.items())]
open(rep, 'w', encoding='utf-8', newline='\n').write('\n'.join(md) + '\n')
print('\n'.join(md[4:]))
if APPLY:
    c.commit(); print('APPLIED')
