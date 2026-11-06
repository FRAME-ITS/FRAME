"""Restore the four SSTP Role ↔ Role associations that carry agreements through ProxyConnectors.

usage: 2026-11-07_restore_sstp_role_links.py model.qea old_model.qea [--apply]
The second pass of the RA clean-up (2026-11-06) deleted all plain UML links between two Roles. In the SSTP Organisational
View four of them are the classifiers of ProxyConnectors to which agreements are attached (EA Project Integrity:
"proxyconnector dependency – missing classified connector"). They are copied back from the old model with their
stereotype record, tags and diagram links. Kept as they were (Association, no FRAME stereotype).
"""
import sys, sqlite3
path, old = sys.argv[1:3]; APPLY = '--apply' in sys.argv
c = sqlite3.connect(path); o = sqlite3.connect(old); c.row_factory = o.row_factory = sqlite3.Row
ins = lambda tab, d: f'insert into {tab} (' + ','.join('"%s"' % k for k in d) + ') values (' + ','.join('?' * len(d)) + ')'
now = {r[0] for r in c.execute('select ea_guid from t_connector')}
for p in c.execute("select Object_ID, Classifier_guid from t_object where Object_Type='ProxyConnector'").fetchall():
    g = p['Classifier_guid']
    if not g or g in now: continue
    k = o.execute('select * from t_connector where ea_guid=?', (g,)).fetchone()
    if not k: print('not in old model', g); continue
    for end in ('Start_Object_ID', 'End_Object_ID'):
        if not c.execute('select 1 from t_object where Object_ID=?', (k[end],)).fetchone(): sys.exit(f'end {k[end]} missing')
    d = dict(k); oldid = d['Connector_ID']
    if c.execute('select 1 from t_connector where Connector_ID=?', (oldid,)).fetchone(): d.pop('Connector_ID')
    cid = c.execute(ins('t_connector', d), list(d.values())).lastrowid
    for x in o.execute('select * from t_xref where Client=?', (g,)).fetchall(): c.execute(ins('t_xref', dict(x)), list(dict(x).values()))
    for t in o.execute('select * from t_connectortag where ElementID=?', (oldid,)).fetchall():
        t = dict(t); t.pop('PropertyID'); t['ElementID'] = cid; c.execute(ins('t_connectortag', t), list(t.values()))
    for dl in o.execute('select * from t_diagramlinks where ConnectorID=?', (oldid,)).fetchall():
        dl = dict(dl); dl.pop('Instance_ID'); dl['ConnectorID'] = cid
        if c.execute('select 1 from t_diagram where Diagram_ID=?', (dl['DiagramID'],)).fetchone(): c.execute(ins('t_diagramlinks', dl), list(dl.values()))
    a = c.execute('select Name from t_object where Object_ID=?', (k['Start_Object_ID'],)).fetchone()[0]
    b = c.execute('select Name from t_object where Object_ID=?', (k['End_Object_ID'],)).fetchone()[0]
    print(f'restored {k["Connector_Type"]} «{k["Stereotype"] or ""}» {a} → {b}')
if APPLY:
    c.commit(); print('APPLIED')
