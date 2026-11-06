"""FRAME Meta Model, third pass (decided by the git maintainer 2026-11-06): the last meta-model links without a V1.3 rule.

usage: 2026-11-06_metamodel_3_V1.3.py model.qea report.md [--apply]
  deleted (the relationship is given by a path through other elements):
    Role → ITS Service (via ITS Service «defines» ITS Service Process «defines» Role)
    LL Function «Call» Component (via Application «contains» LL Function, Application «hosted by» Component)
    Interface «Instantiate» LL Data Flow, LL Data Flow → Interface (via LL Data Flow «served by» Physical Data Flow «use» Interface)
  retyped: Role → Component  →  Component «owned by» Role;  Terminator «Instantiate» Terminator  →  «component of» (sub-terminator);
           Terminator → Application  →  Terminator «defines» Application
  merged: element 'DataObject' (not on the diagram) into 'Data_Object'; its «adheres to» Specification moves over, its other
          links duplicate links of Data_Object and are deleted
"""
import sys, re, sqlite3, uuid
path, rep = sys.argv[1:3]; APPLY = '--apply' in sys.argv
c = sqlite3.connect(path); c.row_factory = sqlite3.Row
guid = lambda: '{' + str(uuid.uuid4()).upper() + '}'
M = [r[0] for r in c.execute("select Package_ID from t_package where Name in ('FRAME_Metamodel', 'FRAME Meta Model')")]
q = ','.join(map(str, M)); log = []
def links():
    return c.execute(f"""select k.*, a.Name an, a.Stereotype ast, b.Name bn, b.Stereotype bst from t_connector k
                         join t_object a on a.Object_ID=k.Start_Object_ID join t_object b on b.Object_ID=k.End_Object_ID
                         where a.Package_ID in ({q}) and b.Package_ID in ({q})""").fetchall()
def delete(k, why):
    c.execute('delete from t_diagramlinks where ConnectorID=?', (k['Connector_ID'],)); c.execute('delete from t_xref where Client=?', (k['ea_guid'],))
    c.execute('delete from t_connectortag where ElementID=?', (k['Connector_ID'],)); c.execute('delete from t_connector where Connector_ID=?', (k['Connector_ID'],))
    log.append(f'deleted: {k["Connector_Type"]} «{k["Stereotype"] or ""}» {k["an"]} → {k["bn"]} ({why})')
def template(st):
    return c.execute("""select k.* from t_connector k join t_xref x on x.Client=k.ea_guid and x.Name='Stereotypes'
                        where k.Stereotype=? and x.Description like ? limit 1""", (st, f'%FQName=FRAME_Profile::{st};%')).fetchone() \
        or c.execute("select k.* from t_connector k where k.Stereotype='use' limit 1").fetchone()
COLS = ('Connector_Type', 'Direction', 'SourceStyle', 'DestStyle', 'SourceIsNavigable', 'DestIsNavigable', 'SourceIsAggregate', 'DestIsAggregate', 'SubType')
def retype(k, new, rev=False):
    tp = template(new)
    if rev:
        c.execute('update t_connector set Start_Object_ID=End_Object_ID, End_Object_ID=Start_Object_ID where Connector_ID=?', (k['Connector_ID'],))
        for dl in c.execute('select Instance_ID, Style from t_diagramlinks where ConnectorID=?', (k['Connector_ID'],)).fetchall():
            st = dl['Style'] or ''; so, eo = re.search(r'SOID=([^;]*);', st), re.search(r'EOID=([^;]*);', st)
            if so and eo:
                st = st.replace(f'SOID={so.group(1)};', 'SOID=@@;').replace(f'EOID={eo.group(1)};', f'EOID={so.group(1)};').replace('SOID=@@;', f'SOID={eo.group(1)};')
            c.execute("update t_diagramlinks set Style=?, Geometry='SX=0;SY=0;EX=0;EY=0;' where Instance_ID=?", (st, dl['Instance_ID']))
    c.execute(f'update t_connector set {", ".join(x + "=?" for x in COLS)}, Stereotype=?, Btm_Mid_Label=? where Connector_ID=?',
              [tp[x] for x in COLS] + [new, f'«{new}»', k['Connector_ID']])
    c.execute("delete from t_xref where Client=? and Name='Stereotypes'", (k['ea_guid'],))
    c.execute("insert into t_xref (XrefID, Name, Type, Visibility, Partition, Client, Supplier, Description) values (?,?,?,?,?,?,?,?)",
              (guid(), 'Stereotypes', 'connector property', 'Public', '0', k['ea_guid'], '<none>', f'@STEREO;Name={new};FQName=FRAME_Profile::{new};@ENDSTEREO;'))
    log.append(f'{k["Connector_Type"]} «{k["Stereotype"] or ""}» {k["an"]} → {k["bn"]}  becomes  ' + (f'{k["bn"]} «{new}» {k["an"]}' if rev else f'«{new}»'))

F = lambda s: 'FRAME_' + s
for k in links():
    pair, ty, st = (k['ast'], k['bst']), k['Connector_Type'], k['Stereotype']
    if pair == (F('Role'), F('ITS_Service')) and ty == 'Abstraction' and not st: delete(k, 'path via ITS Service Process')
    elif pair == (F('Low_Level_Function'), F('Component')) and st == 'Call': delete(k, 'path via Application')
    elif pair == (F('Interface'), F('Low_Level_Data_Flow')) and st == 'Instantiate': delete(k, 'path via Physical Data Flow')
    elif pair == (F('Low_Level_Data_Flow'), F('Interface')) and ty == 'Usage' and not st: delete(k, 'path via Physical Data Flow')
    elif pair == (F('Role'), F('Component')) and ty == 'Usage' and not st: retype(k, 'owned by', rev=True)
    elif pair == (F('Terminator'), F('Terminator')) and st == 'Instantiate': retype(k, 'component of')
    elif pair == (F('Terminator'), F('Application')) and ty == 'Usage' and not st: retype(k, 'defines')

# merge DataObject into Data_Object
keep = c.execute(f"select Object_ID from t_object where Package_ID in ({q}) and Name='Data_Object' and Stereotype='FRAME_Data_Object'").fetchone()
drop = c.execute(f"select Object_ID, ea_guid from t_object where Package_ID in ({q}) and Name='DataObject' and Stereotype='FRAME_Data_Object'").fetchone()
if keep and drop:
    K, D = keep[0], drop[0]
    for k in links():
        if D not in (k['Start_Object_ID'], k['End_Object_ID']): continue
        s, t = (K if k['Start_Object_ID'] == D else k['Start_Object_ID']), (K if k['End_Object_ID'] == D else k['End_Object_ID'])
        same = c.execute('select 1 from t_connector where Start_Object_ID=? and End_Object_ID=? and ifnull(Stereotype,\'\')=ifnull(?,\'\') and Connector_ID<>?', (s, t, k['Stereotype'], k['Connector_ID'])).fetchone()
        rev_contains = (k['Connector_Type'] == 'Usage' and not k['Stereotype'] and
                        c.execute("select 1 from t_connector where Start_Object_ID=? and End_Object_ID=? and Stereotype='contains'", (t, s)).fetchone())
        if same or rev_contains:
            delete(k, 'duplicate after merging DataObject into Data_Object')
        else:
            c.execute('update t_connector set Start_Object_ID=?, End_Object_ID=? where Connector_ID=?', (s, t, k['Connector_ID']))
            log.append(f'moved to Data_Object: «{k["Stereotype"] or ""}» {k["an"]} → {k["bn"]}')
    for t in ('t_objectproperties', 't_attribute', 't_operation', 't_diagramobjects'):
        c.execute(f'delete from {t} where Object_ID=?', (D,))
    c.execute('delete from t_xref where Client=?', (drop[1],)); c.execute('delete from t_object where Object_ID=?', (D,))
    log.append('element DataObject merged into Data_Object and deleted')
md = ['# FRAME Meta Model, third pass', '', 'Script: `tools/fixes/2026-11-06_metamodel_3_V1.3.py` (decided by the git maintainer).', ''] + [f'- {l}' for l in log]
open(rep, 'w', encoding='utf-8', newline='\n').write('\n'.join(md) + '\n')
print('\n'.join(md[4:]))
if APPLY:
    c.commit(); print('APPLIED')
