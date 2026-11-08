"""Issues decided by the git maintainer on 2026-11-07 (model part; the MDG part is in 2026-11-06_mdg_technology_V1.3.py).

#82  Role ↔ Agreement: the names were the opposite of the direction. Role → Agreement is «adheres to», Agreement → Role is
     «accepted by». Links drawn 'Destination -> Source' (arrow at the stored source) get their ends swapped first, so the
     arrow on the diagrams stays where it was and only the label changes where it was wrong.
#85  motivation layer of the Meta Model:
     connector 1 Business Expectation «defines» Mission Statement removed; replaced (connector 2) by Business Expectation
       «defines» ITS Service for each ITS Service the Mission Statement defines in the same architecture;
     connector 3 ITS Service «delivered by» Added Value → ITS Service «delivers» Added Value;
     connectors 4 (ITS Vision «defines» Requirement) and 5 (Added Value «defines» User Need) removed.
#87  User Needs 6.5.1.1 and 6.5.1.2 (NAP): data and discovery are for all users, not only authorised users.
#84  definitions of Stakeholder, ITS Vision, ITS Mission Statement and ITS Service in the FRAME Meta Model (texts voted in #84).

usage: python tools/fixes/2026-11-07_issues_82_84_85_87.py model.qea report.md [--apply]
"""
import sys, re, sqlite3, uuid
path, rep = sys.argv[1:3]; APPLY = '--apply' in sys.argv
c = sqlite3.connect(path); c.row_factory = sqlite3.Row
guid = lambda: '{' + str(uuid.uuid4()).upper() + '}'
ins = lambda t, d: f'insert into {t} ({",".join(chr(34) + k + chr(34) for k in d)}) values ({",".join("?" * len(d))})'
log = []
TOOLSETUP = "(select Package_ID from t_package where Name in ('FRAME_Profile','FRAME_Toolbox','FRAME Toolsetup'))"
def ends(k):
    return [c.execute('select Name, Stereotype, Package_ID from t_object where Object_ID=?', (o,)).fetchone() for o in (k['Start_Object_ID'], k['End_Object_ID'])]
def set_stereo(k, st):
    c.execute('update t_connector set Stereotype=?, Name=case when Name=? then ? else Name end where Connector_ID=?', (st, k['Stereotype'], st, k['Connector_ID']))
    c.execute("delete from t_xref where Client=? and Name='Stereotypes'", (k['ea_guid'],))
    c.execute(ins('t_xref', d := dict(XrefID=guid(), Name='Stereotypes', Type='connector property', Visibility='Public', Partition='0',
              Description=f'@STEREO;Name={st};FQName=FRAME_Profile::{st};@ENDSTEREO;', Client=k['ea_guid'], Supplier='<none>')), list(d.values()))
def delete(k):
    if c.execute('select 1 from t_object where Object_Type=\'ProxyConnector\' and Classifier_guid=?', (k['ea_guid'],)).fetchone():
        sys.exit(f'connector {k["Connector_ID"]} is referenced by a ProxyConnector')
    for t, col in (('t_diagramlinks', 'ConnectorID'), ('t_connectortag', 'ElementID'), ('t_connector', 'Connector_ID')):
        c.execute(f'delete from {t} where {col}=?', (k['Connector_ID'],))
    c.execute('delete from t_xref where Client=?', (k['ea_guid'],))
def top(pid):
    while True:
        r = c.execute('select Parent_ID from t_package where Package_ID=?', (pid,)).fetchone()
        if not r or r[0] in (0, 1) or c.execute('select Parent_ID from t_package where Package_ID=?', (r[0],)).fetchone()[0] == 0: return pid
        pid = r[0]

# #82  (idempotent: the name follows the ends; links drawn 'Destination -> Source' get their ends swapped first, so that
#       the stored source is where the arrow starts and the arrow on the diagrams stays as it was)
def swap_geom(g):
    d = dict(re.findall(r'(SX|SY|EX|EY)=(-?\d+)', g or ''))
    if not d: return g
    r = {'SX': d.get('EX', '0'), 'SY': d.get('EY', '0'), 'EX': d.get('SX', '0'), 'EY': d.get('SY', '0')}
    g = re.sub(r'\b(SX|SY|EX|EY)=(-?\d+)', lambda m: f'{m.group(1)}={r[m.group(1)]}', g)
    return re.sub(r'EDGE=(\d)', lambda m: 'EDGE=' + {'1': '3', '3': '1', '2': '4', '4': '2'}.get(m.group(1), m.group(1)), g, 1)
def reverse(k):
    c.execute('''update t_connector set Start_Object_ID=End_Object_ID, End_Object_ID=Start_Object_ID, Start_Edge=End_Edge, End_Edge=Start_Edge,
                 PtStartX=PtEndX, PtEndX=PtStartX, PtStartY=PtEndY, PtEndY=PtStartY, SourceStyle=DestStyle, DestStyle=SourceStyle,
                 SourceIsNavigable=DestIsNavigable, DestIsNavigable=SourceIsNavigable, SourceRole=DestRole, DestRole=SourceRole,
                 SourceCard=DestCard, DestCard=SourceCard, Direction='Source -> Destination' where Connector_ID=?''', (k,))
    for dl in c.execute('select Instance_ID, Geometry, Style, Path from t_diagramlinks where ConnectorID=?', (k,)).fetchall():
        st = dl['Style'] or ''
        so, eo = re.search(r'SOID=([^;]*);', st), re.search(r'EOID=([^;]*);', st)
        if so and eo:
            st = st.replace(f'SOID={so.group(1)};', 'SOID=@@;').replace(f'EOID={eo.group(1)};', f'EOID={so.group(1)};').replace('SOID=@@;', f'SOID={eo.group(1)};')
        p = dl['Path']; p = ';'.join(reversed([x for x in p.split(';') if x])) + ';' if p else p
        c.execute('update t_diagramlinks set Geometry=?, Style=?, Path=? where Instance_ID=?', (swap_geom(dl['Geometry']), st, p, dl['Instance_ID']))
log.append('## #82 Role ↔ Agreement\n')
ROLE, AGR = ('FRAME_Role',), ('FRAME_Agreement', 'Agreement')
for k in c.execute(f"select * from t_connector where Stereotype in ('adheres to','accepted by') and Start_Object_ID not in (select Object_ID from t_object where Package_ID in {TOOLSETUP})").fetchall():
    s, t = ends(k)
    if not ({s['Stereotype'], t['Stereotype']} & set(ROLE) and {s['Stereotype'], t['Stereotype']} & set(AGR)): continue
    note = ''
    if k['Direction'] == 'Destination -> Source':
        reverse(k['Connector_ID']); s, t = t, s; note = ' (ends swapped, was drawn Destination -> Source)'
    new = 'adheres to' if s['Stereotype'] in ROLE else 'accepted by'
    if new != k['Stereotype'] or note:
        set_stereo(k, new); log.append(f'- {s["Name"]} «{new}» {t["Name"]} (was «{k["Stereotype"]}»){note}')

# #85
log.append('\n## #85 motivation layer\n')
for k in c.execute("select k.* from t_connector k join t_object s on s.Object_ID=k.Start_Object_ID join t_object t on t.Object_ID=k.End_Object_ID "
                   "where k.Stereotype='delivered by' and s.Stereotype='FRAME_ITS_Service' and t.Stereotype='FRAME_ITS_Service_Added_Value'").fetchall():
    set_stereo(k, 'delivers'); log.append(f'- ITS Service «delivered by» Added Value → «delivers» (connector {k["Connector_ID"]})')
for k in c.execute("select k.* from t_connector k join t_object s on s.Object_ID=k.Start_Object_ID join t_object t on t.Object_ID=k.End_Object_ID "
                   "where k.Stereotype='defines' and s.Stereotype='FRAME_Business_Expectation' and t.Stereotype='FRAME_Mission_Statement'").fetchall():
    s, t = ends(k); ra = top(s['Package_ID'])
    for sv in c.execute("select t.Object_ID, t.Name, t.Package_ID from t_connector m join t_object t on t.Object_ID=m.End_Object_ID "
                        "where m.Start_Object_ID=? and m.Stereotype='defines' and t.Stereotype='FRAME_ITS_Service'", (k['End_Object_ID'],)).fetchall():
        if top(sv['Package_ID']) != ra: continue
        if c.execute("select 1 from t_connector where Start_Object_ID=? and End_Object_ID=? and Stereotype='defines'", (k['Start_Object_ID'], sv['Object_ID'])).fetchone():
            log.append(f'- {s["Name"]} «defines» {sv["Name"]}: exists'); continue
        n = dict(k); n.pop('Connector_ID'); n.update(End_Object_ID=sv['Object_ID'], ea_guid=guid())
        nk = c.execute(ins('t_connector', n), list(n.values())).lastrowid
        set_stereo(c.execute('select * from t_connector where Connector_ID=?', (nk,)).fetchone(), 'defines')
        log.append(f'- {s["Name"]} «defines» {sv["Name"]}: added')
    delete(k); log.append(f'- {s["Name"]} «defines» {t["Name"]}: removed')
for st, ss, ts in (('defines', 'FRAME_ITS_Vision', 'FRAME_Requirement'), ('defines', 'FRAME_ITS_Service_Added_Value', 'FRAME_User_Need')):
    for k in c.execute("select k.* from t_connector k join t_object s on s.Object_ID=k.Start_Object_ID join t_object t on t.Object_ID=k.End_Object_ID "
                       "where k.Stereotype=? and s.Stereotype=? and t.Stereotype=?", (st, ss, ts)).fetchall():
        s, t = ends(k); delete(k); log.append(f'- {s["Name"]} «{st}» {t["Name"]}: removed')

# #87
log.append('\n## #87 User Needs 6.5.1.1, 6.5.1.2\n')
for name, old, new in (('6.5.1.1', 'accessible to authorised users,', 'accessible to all users,'),
                       ('6.5.1.2', 'for authorised users,', 'for all users,')):
    for o in c.execute("select Object_ID, Note from t_object where Stereotype='FRAME_User_Need' and Name=?", (name,)).fetchall():
        if old in (o['Note'] or ''):
            c.execute('update t_object set Note=? where Object_ID=?', (o['Note'].replace(old, new), o['Object_ID'])); log.append(f'- {name} (object {o["Object_ID"]}): "{old}" → "{new}"')

# #84
log.append('\n## #84 definitions (FRAME Meta Model)\n')
DEF = {
 'FRAME_Stakeholder': 'ITS Stakeholders are organizations or individuals interested in the deployment, operation, or outcomes of ITS services. They can be directly or indirectly affected by the decisions made during the entire lifecycle of ITS Services. They are usually decision-makers such as politicians, high-level managers, and others e.g., the general public or user groups; who typically have little or no knowledge of systems design and implementation beyond what they have acquired as end users.',
 'FRAME_ITS_Vision': 'ITS Vision is the long-term objective and an aspirational goal for the future. The ITS Vision is shared by all ITS Stakeholders. It is a source of inspiration for the ITS Services and provides a clear goal to be adhered to by the ITS Services.',
 'FRAME_Mission_Statement': 'ITS Mission Statement is a short statement that describes what is needed to be done by the ITS Stakeholders in the present to achieve the ITS Vision. It summarizes the purpose of the existence of the ITS Services and guides their use by the ITS Actors and/or the end users. It formulates a clearly structured, overarching policy objective of the ITS service, considering the interests of stakeholders and end-users.',
 'FRAME_ITS_Service': 'The ITS service describes the idea and functional elements of the ITS service as well as framework conditions. The ITS Service is an architectural artifact that describes a value-added service provided by ITS actors to end-users. The added value is created by combining technologies, organizations, processes, and people. The service can be delivered by a single actor or in cooperation with others, and it creates added value that may consist of individual benefits for end users, collective benefits for end-user groups or society, or a mixture of both.'}
MM = "(select Package_ID from t_package where Name='FRAME_Metamodel' or Name='FRAME Meta Model')"
for st, txt in DEF.items():
    for o in c.execute(f'select Object_ID, Name from t_object where Stereotype=? and Package_ID in {MM}', (st,)).fetchall():
        c.execute('update t_object set Note=? where Object_ID=?', (txt, o['Object_ID'])); log.append(f'- {o["Name"]}: definition from #84')

open(rep, 'w', encoding='utf-8', newline='\n').write('# Issues #82, #84, #85, #87 (decided 2026-11-07)\n\n' + '\n'.join(log) + '\n')
print('\n'.join(log))
if APPLY: c.commit(); print('APPLIED')
