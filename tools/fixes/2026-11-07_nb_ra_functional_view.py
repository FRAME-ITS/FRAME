"""NB Reference Architecture – Functional View, comments of R. Bossom (2026-09) [F1–F12], group C of the review.

1. Diagram "02 National Body Functional View": connector labels hidden (the «IN»/«OUT» labels confused readers; the arrows
   show the direction, and the stereotypes stay in the model) [F1, F2, F8, F10].
2. Data flows with the same name and different content renamed after their content [F3]; flows read from a data store
   named after the data, not after a request.
3. Every data flow note starts with its source and target ("From … to …") [F11, F12].
4. Every function note ends with its inputs and outputs, taken from the «IN»/«OUT» connectors [F6, F9 – a first step;
   the descriptions themselves are for the NB RA authors].
5. "Status of CA" had two «OUT» and no «IN»: the registry is its producer (read by Compliance Assessment).

usage: python tools/fixes/2026-11-07_nb_ra_functional_view.py model.qea report.md [--apply]
"""
import sys, re, sqlite3
path, rep = sys.argv[1:3]; APPLY = '--apply' in sys.argv
c = sqlite3.connect(path); c.row_factory = sqlite3.Row
log = []
fv = c.execute("select Package_ID from t_package where Name='NB Functional View'").fetchone()[0]
pk = [fv] + [r[0] for r in c.execute('select Package_ID from t_package where Parent_ID=?', (fv,))]
P = ','.join(map(str, pk))
name = lambda o: c.execute('select Name from t_object where Object_ID=?', (o,)).fetchone()[0]

# 1
d = c.execute("select Diagram_ID, StyleEx from t_diagram where Name='02 National Body Functional View'").fetchone()
if 'SuppConnectorLabels=0' in d['StyleEx']:
    c.execute('update t_diagram set StyleEx=? where Diagram_ID=?', (d['StyleEx'].replace('SuppConnectorLabels=0', 'SuppConnectorLabels=1'), d['Diagram_ID']))
    log.append('- diagram 02 National Body Functional View: connector labels hidden')

# 5
k = c.execute(f"""select k.Connector_ID, k.ea_guid from t_connector k join t_object f on f.Object_ID=k.Start_Object_ID join t_object t on t.Object_ID=k.End_Object_ID
                 where f.Name='Status of CA' and f.Package_ID in ({P}) and t.Name='Compliance assessment registry' and k.Stereotype='OUT'""").fetchone()
if k:
    c.execute("""update t_connector set Start_Object_ID=End_Object_ID, End_Object_ID=Start_Object_ID, Stereotype='IN', Start_Edge=End_Edge, End_Edge=Start_Edge
                 where Connector_ID=?""", (k['Connector_ID'],))
    c.execute("update t_xref set Description=replace(Description,'Name=OUT;','Name=IN;') where Client=? and Name='Stereotypes'", (k['ea_guid'],))
    for dl in c.execute('select Instance_ID, Style from t_diagramlinks where ConnectorID=?', (k['Connector_ID'],)).fetchall():
        st = dl['Style'] or ''
        so, eo = re.search(r'SOID=([^;]*);', st), re.search(r'EOID=([^;]*);', st)
        if so and eo:
            st = st.replace(f'SOID={so.group(1)};', 'SOID=@@;').replace(f'EOID={eo.group(1)};', f'EOID={so.group(1)};').replace('SOID=@@;', f'SOID={eo.group(1)};')
        c.execute("update t_diagramlinks set Style=?, Geometry='SX=0;SY=0;EX=0;EY=0;' where Instance_ID=?", (st, dl['Instance_ID']))
    log.append('- Status of CA: «OUT» to Compliance assessment registry → «IN» from the registry')

# 2  (flow name, producer, consumer) -> new name
RENAME = {
    ('Request', 'Handling Non-Compliance', 'Managing general requests regarding self-declaration'): 'Request for self-declaration information',
    ('Response', 'Managing general requests regarding self-declaration', 'Handling Non-Compliance'): 'Self-declaration information for non-compliance',
    ('Request', 'Handling Non-Compliance', 'Compliance Assessment'): 'Request for compliance assessment',
    ('Response', 'Compliance Assessment', 'Handling Non-Compliance'): 'Compliance assessment result for non-compliance',
    ('Request self-declaration', 'Self-declaration Storage', 'Compliance Assessment'): 'Self-declaration for compliance assessment',
    ('Request data', 'Stakeholder List', 'Manage Stakeholder List'): 'Stakeholder data',
    ('Request information', 'Stakeholder List', 'Validation of completeness'): 'Stakeholder contact details',
    ('Store CA result', 'Compliance assessment registry', 'Handling Non-Compliance'): 'Compliance assessment result',
    ('Status request on SD', 'Self-declaration Journal', 'Handling Non-Compliance'): 'Self-declaration status for non-compliance',
    ('Provide self-declaration', 'Self-declaration Storage', 'Reporting of self-declaration and compliance assessment results'): 'Self-declarations for reporting',
    ('Provide status of SD', 'Self-declaration Journal', 'Reporting of self-declaration and compliance assessment results'): 'Self-declaration status for reporting',
    ('Status of CA', 'Compliance assessment registry', 'Compliance Assessment'): 'Previous compliance assessment results',
}
def ends(f):
    i = [r[0] for r in c.execute("select s.Name from t_connector k join t_object s on s.Object_ID=k.Start_Object_ID where k.End_Object_ID=? and k.Stereotype='IN'", (f,))]
    o = [r[0] for r in c.execute("select t.Name from t_connector k join t_object t on t.Object_ID=k.End_Object_ID where k.Start_Object_ID=? and k.Stereotype='OUT'", (f,))]
    return i, o
flows = c.execute(f"select Object_ID, Name, Note from t_object where Package_ID in ({P}) and Stereotype='FRAME_Low_Level_Data_Flow'").fetchall()
for f in flows:
    i, o = ends(f['Object_ID'])
    new = RENAME.get((f['Name'], i[0] if i else '', o[0] if o else ''))
    if new:
        c.execute('update t_object set Name=? where Object_ID=?', (new, f['Object_ID'])); log.append(f'- flow "{f["Name"]}" ({i[0]} → {o[0]}) renamed "{new}"')

# 3
for f in c.execute(f"select Object_ID, Name, Note from t_object where Package_ID in ({P}) and Stereotype='FRAME_Low_Level_Data_Flow'").fetchall():
    i, o = ends(f['Object_ID']); note = f['Note'] or ''
    if note.startswith('From: '): continue
    head = f'From: {", ".join(i) or "?"}\r\nTo: {", ".join(o) or "?"}\r\n'
    c.execute('update t_object set Note=? where Object_ID=?', (head + ('\r\n' + note if note.strip() else ''), f['Object_ID']))
    log.append(f'- flow "{f["Name"]}": source and target added to the note' + ('' if note.strip() else ' (note was empty)'))

# 4
for fn in c.execute(f"select Object_ID, Name, Note from t_object where Package_ID in ({P}) and Stereotype in ('FRAME_Low_Level_Function','FRAME_High_Level_Function')").fetchall():
    note = fn['Note'] or ''
    if '\nInputs:' in note: continue
    ins = sorted(r[0] for r in c.execute("select f.Name from t_connector k join t_object f on f.Object_ID=k.Start_Object_ID where k.End_Object_ID=? and k.Stereotype='OUT'", (fn['Object_ID'],)))
    outs = sorted(r[0] for r in c.execute("select f.Name from t_connector k join t_object f on f.Object_ID=k.End_Object_ID where k.Start_Object_ID=? and k.Stereotype='IN'", (fn['Object_ID'],)))
    if not ins and not outs: continue
    tail = '\r\n\r\nInputs: ' + ('; '.join(ins) or '–') + '\r\nOutputs: ' + ('; '.join(outs) or '–')
    c.execute('update t_object set Note=? where Object_ID=?', (note.rstrip() + tail, fn['Object_ID']))
    log.append(f'- function "{fn["Name"]}": {len(ins)} inputs, {len(outs)} outputs listed')

open(rep, 'w', encoding='utf-8', newline='\n').write('# NB Reference Architecture – Functional View (review R. Bossom, group C)\n\n' + '\n'.join(log) + '\n')
print('\n'.join(log))
if APPLY: c.commit(); print('APPLIED')
