"""Issue #68 – sub-terminators are types of their terminator, not components (decided by the git maintainer 2026-11-08).

The FRAME Meta Model and FRAME_Profile define Sub-terminator «is Type of» Terminator, but the reference architectures drew
the link as «component of» (Aggregation) and once as a plain UML «Instantiate» (Parking Operator → NAP Content Provider).
  - every Terminator → Terminator «component of» and «Instantiate» link outside FRAME Toolsetup becomes an Abstraction
    «is Type of» (FRAME_Profile), same ends and direction (sub-terminator → terminator); diagrams keep the link
  - the FRAME Meta Model self-link Terminator/ Subterminator «component of» (named "Is type of") is removed;
    the «is Type of» self-link stays
  - a link that would duplicate an existing «is Type of» between the same ends is removed instead
The Quick Linker rule «component of» Terminator → Terminator added in V1.3 is dropped in 2026-11-06_mdg_technology_V1.3.py
(V1.2 already offers «is Type of» Terminator → Terminator); 2026-11-06_toolsetup_V1.3.py then removes it from FRAME_Profile.

usage: python tools/fixes/2026-11-08_subterminators_is_type_of.py model.qea report.md [--apply]
"""
import sys, sqlite3, uuid
path, rep = sys.argv[1:3]; APPLY = '--apply' in sys.argv
c = sqlite3.connect(path); c.row_factory = sqlite3.Row
guid = lambda: '{' + str(uuid.uuid4()).upper() + '}'
ins = lambda t, d: f'insert into {t} ({",".join(chr(34) + k + chr(34) for k in d)}) values ({",".join("?" * len(d))})'
log = []
TOOLSETUP = "(select Package_ID from t_package where Name in ('FRAME_Profile','FRAME_Toolbox','FRAME_Diagram','FRAME Toolsetup'))"
META = c.execute("select Package_ID from t_object where Name='Terminator/ Subterminator' and Stereotype='FRAME_Terminator'").fetchone()[0]
def delete(k):
    for t, col in (('t_connectortag', 'ElementID'), ('t_diagramlinks', 'ConnectorID')):
        c.execute(f'delete from {t} where {col}=?', (k['Connector_ID'],))
    c.execute('delete from t_xref where Client=?', (k['ea_guid'],))
    c.execute('delete from t_connector where Connector_ID=?', (k['Connector_ID'],))
Q = f"""select k.*, s.Name sn, t.Name tn, s.Package_ID sp from t_connector k join t_object s on s.Object_ID=k.Start_Object_ID
        join t_object t on t.Object_ID=k.End_Object_ID where s.Stereotype='FRAME_Terminator' and t.Stereotype='FRAME_Terminator'
        and s.Package_ID not in {TOOLSETUP}"""
have = {(k['Start_Object_ID'], k['End_Object_ID']) for k in c.execute(Q + " and k.Stereotype='is Type of'")}
n = 0
for k in c.execute(Q + " and k.Stereotype in ('component of','Instantiate') order by tn, sn").fetchall():
    if k['sp'] == META:
        delete(k); log.append(f'- FRAME Meta Model: «component of» {k["sn"]} → {k["tn"]} (named "{k["Name"]}") removed'); continue
    if k['Direction'] != 'Source -> Destination':
        sys.exit(f'{k["Connector_ID"]}: direction {k["Direction"]} – not expected')
    if (k['Start_Object_ID'], k['End_Object_ID']) in have:
        delete(k); log.append(f'- {k["sn"]} → {k["tn"]}: «{k["Stereotype"]}» removed, «is Type of» exists'); continue
    c.execute("""update t_connector set Connector_Type='Abstraction', Stereotype='is Type of', SubType=NULL, SourceIsAggregate=0, DestIsAggregate=0,
                 Btm_Mid_Label='«abstraction»   «is Type of»', SourceIsNavigable=0, DestIsNavigable=1,
                 SourceStyle='Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Non-Navigable;',
                 DestStyle='Union=0;Derived=0;AllowDuplicates=0;Owned=0;Navigable=Navigable;',
                 Name=case when Name in ('component of','Instantiate') then NULL else Name end where Connector_ID=?""", (k['Connector_ID'],))
    c.execute("delete from t_xref where Client=? and Name='Stereotypes'", (k['ea_guid'],))
    c.execute(ins('t_xref', d := dict(XrefID=guid(), Name='Stereotypes', Type='connector property', Visibility='Public', Partition='0',
              Description='@STEREO;Name=is Type of;FQName=FRAME_Profile::is Type of;@ENDSTEREO;', Client=k['ea_guid'], Supplier='<none>')), list(d.values()))
    have.add((k['Start_Object_ID'], k['End_Object_ID'])); n += 1
    log.append(f'- {k["sn"]} «is Type of» {k["tn"]} (was «{k["Stereotype"]}»)')
left = c.execute(Q + " and k.Stereotype<>'is Type of'").fetchall()
log.append(f'\n{n} links retyped; Terminator → Terminator links other than «is Type of» left: {len(left)} '
           + ', '.join(f'{k["sn"]} «{k["Stereotype"] or k["Connector_Type"]}» {k["tn"]}' for k in left))
open(rep, 'w', encoding='utf-8').write('# Sub-terminators «is Type of» terminator (#68, 2026-11-08)\n\nScript: `tools/fixes/2026-11-08_subterminators_is_type_of.py`.\n\n' + '\n'.join(log) + '\n')
print(log[-1])
if APPLY: c.commit()
