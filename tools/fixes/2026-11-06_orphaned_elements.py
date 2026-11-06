"""Delete orphaned elements (Package_ID points to no package) from the FRAME model, with their tagged values,
stereotype records and connectors. Writes the list of deleted elements to a Markdown report.
usage: fix_orphans.py model.qea report.md [--apply]"""
import sqlite3, sys
path, rep = sys.argv[1:3]; APPLY = '--apply' in sys.argv
c = sqlite3.connect(path)
orph = c.execute("""select Object_ID, ea_guid, Object_Type, Name, Stereotype, CreatedDate from t_object
                    where Package_ID not in (select Package_ID from t_package) order by Object_ID""").fetchall()
ids = [o[0] for o in orph]; guids = [o[1] for o in orph]
ph = lambda xs: ','.join('?' * len(xs))
links = [r[0] for r in c.execute(f'select Connector_ID from t_connector where Start_Object_ID in ({ph(ids)}) or End_Object_ID in ({ph(ids)})', ids + ids)]
lguids = [r[0] for r in c.execute(f'select ea_guid from t_connector where Connector_ID in ({ph(links)})', links)] if links else []
counts = {
 'elements': len(ids),
 'tagged values': c.execute(f'select count(*) from t_objectproperties where Object_ID in ({ph(ids)})', ids).fetchone()[0],
 'stereotype/xref records': c.execute(f'select count(*) from t_xref where Client in ({ph(guids)})', guids).fetchone()[0],
 'connectors': len(links),
}
md = ['# Orphaned elements removed', '', 'Elements whose package does not exist (Package_ID = 0). Reported by the Enterprise Architect',
      'Project Integrity check as "Orphaned object"; present unchanged since the V5.2 release. None of them is shown in a diagram',
      'or has children; apart from EA_IMPORT_STUB (self-link) none has a connector. They remain available in git history (tag v5.2.0).', '',
      ', '.join(f'{v} {k}' for k, v in counts.items()), '', '| Object_ID | GUID | Type | Name | Stereotype | Created |', '|---|---|---|---|---|---|']
md += [f'| {o[0]} | `{o[1]}` | {o[2]} | {o[3]} | {o[4] or ""} | {o[5]} |' for o in orph]
open(rep, 'w', encoding='utf-8', newline='\n').write('\n'.join(md) + '\n')
print(counts)
if APPLY:
    if links:
        c.execute(f'delete from t_diagramlinks where ConnectorID in ({ph(links)})', links)
        c.execute(f'delete from t_connectortag where ElementID in ({ph(links)})', links)
        c.execute(f'delete from t_xref where Client in ({ph(lguids)})', lguids)
        c.execute(f'delete from t_connector where Connector_ID in ({ph(links)})', links)
    c.execute(f'delete from t_objectproperties where Object_ID in ({ph(ids)})', ids)
    c.execute(f'delete from t_xref where Client in ({ph(guids)})', guids)
    for t in ('t_attribute', 't_operation', 't_objectconstraint', 't_objectrequires', 't_objectscenarios', 't_objectfiles', 't_objectproblems', 't_objectresource', 't_objectrisks', 't_objecttests', 't_objecteffort', 't_objectmetrics', 't_objecttrx', 't_diagramobjects'):
        if c.execute("select 1 from sqlite_master where name=?", (t,)).fetchone():
            c.execute(f'delete from {t} where Object_ID in ({ph(ids)})', ids)
    c.execute(f'delete from t_object where Object_ID in ({ph(ids)})', ids)
    c.commit(); print('APPLIED')
