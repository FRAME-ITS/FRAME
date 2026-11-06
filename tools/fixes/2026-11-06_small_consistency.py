"""Small consistency fixes. usage: 2026-11-06_small_consistency.py model.qea [--apply]
- the last «belongsto» (Abstraction, local stereotype) 7.6 → 7 Traffic Management becomes Association «belongs to»
  (FRAME_Profile), like the other User_Need_Service → User_Need_Group links
- typo: data flow 'fes-psef_iputs' renamed 'fes-psef_inputs' (#76)
"""
import sqlite3, sys
path = sys.argv[1]; APPLY = '--apply' in sys.argv
c = sqlite3.connect(path); c.row_factory = sqlite3.Row
t = c.execute("""select k.* from t_connector k join t_object a on a.Object_ID=k.Start_Object_ID join t_object b on b.Object_ID=k.End_Object_ID
                 where k.Stereotype='belongs to' and a.Stereotype='FRAME_User_Need_Service' and b.Stereotype='FRAME_User_Need_Group'
                 and k.Connector_Type='Association' limit 1""").fetchone()
xd = c.execute("select Description from t_xref where Client=? and Name='Stereotypes'", (t['ea_guid'],)).fetchone()[0]
cols = ('Connector_Type', 'Stereotype', 'Direction', 'Btm_Mid_Label', 'SourceStyle', 'DestStyle', 'SourceContainment',
        'DestContainment', 'SubType', 'SourceIsAggregate', 'DestIsAggregate', 'SourceIsNavigable', 'DestIsNavigable')
for k in c.execute("select * from t_connector where Stereotype='belongsto'").fetchall():
    print(f'«belongsto» {k["Connector_Type"]} → Association «belongs to»: connector {k["ea_guid"]}')
    c.execute(f'update t_connector set {", ".join(x + "=?" for x in cols)} where Connector_ID=?', [t[x] for x in cols] + [k['Connector_ID']])
    c.execute("update t_xref set Description=? where Client=? and Name='Stereotypes'", (xd, k['ea_guid']))
for o in c.execute("select Object_ID, Name from t_object where trim(Name)='fes-psef_iputs'").fetchall():
    print(f"rename '{o['Name'].strip()}' → 'fes-psef_inputs'")
    c.execute('update t_object set Name=? where Object_ID=?', (o['Name'].replace('iputs', 'inputs'), o['Object_ID']))
if APPLY:
    c.commit(); print('APPLIED')
