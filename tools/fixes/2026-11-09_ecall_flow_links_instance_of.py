"""Issue #96 point 4 – the stereotype «instants of» (2026-11-09).

In V5.2, 23 data-flow links did not use IN/OUT (eCall functions F2.1.2, F2.1.11, F5.11, F5.12, D2.4, and 3 flows to Broadcaster):
  producer → low-level data flow was drawn as «instants of» (9 links),
  low-level data flow → consumer as «owned by» (14 links).
These flows had no other producer/consumer links, so the links are the IN/OUT of the flows. They become Association «IN» / «OUT»
(FRAME_Profile); ends and diagrams unchanged; links drawn without an arrow (Unspecified) get Source -> Destination.
After that no model connector uses «instants of»; the stereotype is renamed «instance of» in the MDG technology V1.3
(2026-11-06_mdg_technology_V1.3.py) and in FRAME_Profile (2026-11-06_toolsetup_V1.3.py). Its only Quick Linker rule,
Stakeholder → Organisation, is part of #14.

usage: python tools/fixes/2026-11-09_ecall_flow_links_instance_of.py model.qea report.md [--apply]
"""
import sys, sqlite3, uuid
path, rep = sys.argv[1:3]; APPLY = '--apply' in sys.argv
c = sqlite3.connect(path); c.row_factory = sqlite3.Row
guid = lambda: '{' + str(uuid.uuid4()).upper() + '}'
ins = lambda t, d: f'insert into {t} ({",".join(chr(34) + k + chr(34) for k in d)}) values ({",".join("?" * len(d))})'
FLOW = ('FRAME_Low_Level_Data_Flow', 'FRAME_High_Level_Data_Flow')
END = ('FRAME_Low_Level_Function', 'FRAME_High_Level_Function', 'FRAME_Functional_Area', 'FRAME_System', 'FRAME_Terminator', 'FRAME_Datastore')
log = []
Q = """select k.*, s.Name sn, s.Stereotype ss, t.Name tn, t.Stereotype ts from t_connector k join t_object s on s.Object_ID=k.Start_Object_ID
       join t_object t on t.Object_ID=k.End_Object_ID where k.Connector_Type='Association' and k.Stereotype=?"""
todo = [(k, 'IN') for k in c.execute(Q, ('instants of',)).fetchall() if k['ss'] in END and k['ts'] in FLOW] + \
       [(k, 'OUT') for k in c.execute(Q, ('owned by',)).fetchall() if k['ss'] in FLOW and k['ts'] in END]
for k, st in sorted(todo, key=lambda x: (x[1], x[0]['sn'], x[0]['tn'])):
    if k['Direction'] == 'Unspecified':   # drawn without an arrow: give it the direction of all IN/OUT links
        c.execute("""update t_connector set Direction='Source -> Destination', SourceIsNavigable=0, DestIsNavigable=1,
                     SourceStyle='Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Non-Navigable;',
                     DestStyle='Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Navigable;' where Connector_ID=?""", (k['Connector_ID'],))
    elif k['Direction'] != 'Source -> Destination': sys.exit(f'{k["Connector_ID"]}: direction {k["Direction"]}')
    c.execute('update t_connector set Stereotype=?, Btm_Mid_Label=?, Name=case when Name=? then NULL else Name end where Connector_ID=?',
              (st, f'  «{st}»', k['Stereotype'], k['Connector_ID']))
    c.execute("delete from t_xref where Client=? and Name='Stereotypes'", (k['ea_guid'],))
    c.execute(ins('t_xref', d := dict(XrefID=guid(), Name='Stereotypes', Type='connector property', Visibility='Public', Partition='0',
              Description=f'@STEREO;Name={st};FQName=FRAME_Profile::{st};@ENDSTEREO;', Client=k['ea_guid'], Supplier='<none>')), list(d.values()))
    log.append(f'- {k["sn"]} → {k["tn"]}: «{k["Stereotype"]}» → «{st}»')
left = c.execute("""select count(*) from t_connector k join t_object s on s.Object_ID=k.Start_Object_ID where k.Stereotype='instants of'
                    and s.Package_ID not in (select Package_ID from t_package where Name in ('FRAME_Profile','FRAME_Toolbox','FRAME_Diagram'))""").fetchone()[0]
log.append(f'\n{len(todo)} links retyped; model connectors still «instants of»: {left}')
open(rep, 'w', encoding='utf-8').write('# eCall and Broadcaster data-flow links «instants of» / «owned by» → IN / OUT (#96 point 4, 2026-11-09)\n\n'
    'Script: `tools/fixes/2026-11-09_ecall_flow_links_instance_of.py`.\n\n' + '\n'.join(log) + '\n')
print(log[-1])
if APPLY: c.commit()
