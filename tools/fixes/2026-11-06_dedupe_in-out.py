"""Remove duplicate IN/OUT connectors (same ends, same stereotype); diagram links of a removed duplicate are moved to the
kept connector on diagrams where the kept one is not shown yet. usage: dedupe.py model.qea report.txt"""
import sqlite3, sys
c = sqlite3.connect(sys.argv[1]); out = []
pairs = c.execute("select Start_Object_ID,End_Object_ID,upper(Stereotype) from t_connector where upper(Stereotype) in ('IN','OUT') group by 1,2,3 having count(*)>1").fetchall()
for s, e, st in pairs:
    ks = c.execute("""select k.Connector_ID, k.ea_guid, (select count(*) from t_diagramlinks d where d.ConnectorID=k.Connector_ID) n
                      from t_connector k where Start_Object_ID=? and End_Object_ID=? and upper(Stereotype)=? order by n desc, k.Connector_ID""", (s, e, st)).fetchall()
    keep = ks[0][0]
    name = lambda i: c.execute('select trim(Name) from t_object where Object_ID=?', (i,)).fetchone()[0]
    for cid, g, n in ks[1:]:
        moved = 0
        for iid, did in c.execute('select Instance_ID, DiagramID from t_diagramlinks where ConnectorID=?', (cid,)).fetchall():
            if c.execute('select count(*) from t_diagramlinks where ConnectorID=? and DiagramID=?', (keep, did)).fetchone()[0]:
                c.execute('delete from t_diagramlinks where Instance_ID=?', (iid,))
            else:
                c.execute('update t_diagramlinks set ConnectorID=? where Instance_ID=?', (keep, iid)); moved += 1
        c.execute('delete from t_connectortag where ElementID=?', (cid,)); c.execute('delete from t_xref where Client=?', (g,))
        c.execute('delete from t_connector where Connector_ID=?', (cid,))
        out.append(f'- «{st}» {name(s)} → {name(e)} `{g}` removed (diagram links moved to kept connector: {moved})')
c.commit()
open(sys.argv[2], 'w', encoding='utf-8').write('\n'.join(out) + '\n'); print('\n'.join(out)); print(c.execute('pragma integrity_check').fetchone())
