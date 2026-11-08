"""Follow-up of the check of closed issues (reports/check_closed_issues_2026-11-08.md, findings 1 and 2).

#16  42 «belongs to» links of the user-need hierarchy still ran whole → part (User Need Topic → User Need,
     User Need Group → User Need Service), all in the FRAME Repository (groups 9.10, 9.11, "9 Freight", "1 General").
     They are reversed (ends, diagram geometry, direction) to part → whole like the other 2,600 links.
#32/#70  the last element with an old FrameNext stereotype, "PSAP - eCall Mamagement Application"
     (eCall Physical View, FrameNext::HighLevelFunction, on no diagram, no links) becomes FRAME_Application and
     its name is corrected to "PSAP - eCall Management Application".

usage: python tools/fixes/2026-11-08_belongsto_direction_psap.py model.qea report.md [--apply]
"""
import sys, re, sqlite3
path, rep = sys.argv[1:3]; APPLY = '--apply' in sys.argv
c = sqlite3.connect(path); c.row_factory = sqlite3.Row
log = []
def swap_geom(g):
    d = dict(re.findall(r'(SX|SY|EX|EY)=(-?\d+)', g or ''))
    if not d: return g
    r = {'SX': d.get('EX', '0'), 'SY': d.get('EY', '0'), 'EX': d.get('SX', '0'), 'EY': d.get('SY', '0')}
    g = re.sub(r'\b(SX|SY|EX|EY)=(-?\d+)', lambda m: f'{m.group(1)}={r[m.group(1)]}', g)
    return re.sub(r'EDGE=(\d)', lambda m: 'EDGE=' + {'1': '3', '3': '1', '2': '4', '4': '2'}.get(m.group(1), m.group(1)), g, 1)
def reverse(k):
    c.execute('''update t_connector set Start_Object_ID=End_Object_ID, End_Object_ID=Start_Object_ID, Start_Edge=End_Edge, End_Edge=Start_Edge,
                 PtStartX=PtEndX, PtEndX=PtStartX, PtStartY=PtEndY, PtEndY=PtStartY, SourceRole=DestRole, DestRole=SourceRole,
                 SourceCard=DestCard, DestCard=SourceCard where Connector_ID=?''', (k,))
    r = c.execute('select Direction, SourceStyle, DestStyle, SourceIsNavigable, DestIsNavigable from t_connector where Connector_ID=?', (k,)).fetchone()
    if r[0] == 'Destination -> Source':
        c.execute('update t_connector set Direction=?, SourceStyle=?, DestStyle=?, SourceIsNavigable=?, DestIsNavigable=? where Connector_ID=?',
                  ('Source -> Destination', r[2], r[1], r[4], r[3], k))
    for dl in c.execute('select Instance_ID, Geometry, Style, Path from t_diagramlinks where ConnectorID=?', (k,)).fetchall():
        st = dl['Style'] or ''
        so, eo = re.search(r'SOID=([^;]*);', st), re.search(r'EOID=([^;]*);', st)
        if so and eo:
            st = st.replace(f'SOID={so.group(1)};', 'SOID=@@;').replace(f'EOID={eo.group(1)};', f'EOID={so.group(1)};').replace('SOID=@@;', f'SOID={eo.group(1)};')
        p = dl['Path']; p = ';'.join(reversed([x for x in p.split(';') if x])) + ';' if p else p
        c.execute('update t_diagramlinks set Geometry=?, Style=?, Path=? where Instance_ID=?', (swap_geom(dl['Geometry']), st, p, dl['Instance_ID']))

log.append('## #16 «belongs to» part → whole\n')
for k in c.execute("""select k.Connector_ID, s.Name sn, t.Name tn from t_connector k join t_object s on s.Object_ID=k.Start_Object_ID join t_object t on t.Object_ID=k.End_Object_ID
                      where k.Stereotype='belongs to' and ((s.Stereotype='FRAME_User_Need_Group' and t.Stereotype='FRAME_User_Need_Service')
                      or (s.Stereotype='FRAME_User_Need_Service' and t.Stereotype='FRAME_User_Need_Topic')
                      or (s.Stereotype='FRAME_User_Need_Topic' and t.Stereotype='FRAME_User_Need'))""").fetchall():
    reverse(k['Connector_ID']); log.append(f'- {k["tn"].strip()} «belongs to» {k["sn"].strip()} (was reversed)')

log.append('\n## #32/#70 last FrameNext stereotype\n')
for o in c.execute("select Object_ID, Name, ea_guid from t_object where Stereotype='HighLevelFunction' and Name like 'PSAP - eCall Mam%'").fetchall():
    c.execute("update t_object set Stereotype='FRAME_Application', Object_Type='Object', Name='PSAP - eCall Management Application' where Object_ID=?", (o['Object_ID'],))
    c.execute("update t_xref set Description='@STEREO;Name=FRAME_Application;FQName=FRAME_Profile::FRAME_Application;@ENDSTEREO;' where Client=? and Name='Stereotypes'", (o['ea_guid'],))
    log.append(f'- "{o["Name"]}": FrameNext::HighLevelFunction → FRAME_Application, name → "PSAP - eCall Management Application"')
left = c.execute("select count(*) from t_xref where Description like '%FrameNext::%'").fetchone()[0]
log.append(f'\nFrameNext stereotypes left in the model: {left}')
open(rep, 'w', encoding='utf-8', newline='\n').write('# User-need hierarchy direction and the last FrameNext stereotype (2026-11-08)\n\n' + '\n'.join(log) + '\n')
print('\n'.join(log[-4:])); print(sum(1 for l in log if 'was reversed' in l), 'reversed')
if APPLY: c.commit(); print('APPLIED')
