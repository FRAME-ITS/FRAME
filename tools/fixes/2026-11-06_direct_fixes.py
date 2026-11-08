"""Direct fixes agreed by the git maintainer before the 5.3 pull request (one step per commit).

usage: 2026-11-06_direct_fixes.py model.qea STEP [--apply]
  parents  add the missing «component of» of five low-level functions to their high-level function (by numbering)
  cits     C-ITS user needs: plain Usage links to low-level functions -> Association «served by»
  testpkg  remove the top-level 'Test Package' (metamodel test elements, self-contained)
  context  #91 Freight Transport in the FRAME Context Diagram, with its IN/OUT links to the context-level flows
New connectors are cloned from an existing connector of the same kind (all EA columns, stereotype record).
"""
import sqlite3, sys, uuid
path, step = sys.argv[1:3]; APPLY = '--apply' in sys.argv
c = sqlite3.connect(path); c.row_factory = sqlite3.Row
guid = lambda: '{' + str(uuid.uuid4()).upper() + '}'
oid = lambda name: c.execute("select Object_ID from t_object where trim(Name)=?", (name,)).fetchone()[0]
nm = lambda i: c.execute('select Name from t_object where Object_ID=?', (i,)).fetchone()[0].strip()
log = []
ins = lambda tab, d: f'insert into {tab} (' + ','.join('"%s"' % k for k in d) + ') values (' + ','.join('?' * len(d)) + ')'


def clone(tmpl_id, start, end):
    """copy connector tmpl_id (all columns, stereotype record) between start and end; returns the new Connector_ID"""
    t = dict(c.execute('select * from t_connector where Connector_ID=?', (tmpl_id,)).fetchone())
    old = t['ea_guid']; t.pop('Connector_ID'); t.update(Start_Object_ID=start, End_Object_ID=end, ea_guid=guid(),
                                                       PDATA5='SX=0;SY=0;EX=0;EY=0;')
    cur = c.execute(ins('t_connector', t), list(t.values()))
    for x in c.execute('select * from t_xref where Client=?', (old,)).fetchall():
        x = dict(x); x.update(XrefID=guid(), Client=t['ea_guid'])
        c.execute(ins('t_xref', x), list(x.values()))
    return cur.lastrowid


if step == 'parents':
    tmpl = c.execute("""select k.Connector_ID from t_connector k join t_object a on a.Object_ID=k.Start_Object_ID
                        join t_object b on b.Object_ID=k.End_Object_ID where k.Stereotype='component of'
                        and a.Stereotype='FRAME_Low_Level_Function' and b.Stereotype='FRAME_High_Level_Function' limit 1""").fetchone()[0]
    for child, parent in (('F3.1.1.5.11', 'F3.1.1.5'), ('F3.1.1.5.12', 'F3.1.1.5'), ('F3.1.1.5.21', 'F3.1.1.5'),
                          ('F3.1.2.14.6', 'F3.1.2.14'), ('F6.5.8', 'F6.5')):
        a = c.execute("select Object_ID from t_object where Name like ? and Stereotype='FRAME_Low_Level_Function'", (child + ' %',)).fetchone()[0]
        b = c.execute("select Object_ID from t_object where Name like ? and Stereotype='FRAME_High_Level_Function'", (parent + ' %',)).fetchone()[0]
        if c.execute("select 1 from t_connector where Start_Object_ID=? and End_Object_ID=? and Stereotype='component of'", (a, b)).fetchone():
            continue
        log.append(f'«component of» {nm(a)} → {nm(b)}')
        clone(tmpl, a, b)

elif step == 'cits':
    tmpl = c.execute("""select k.Connector_ID from t_connector k join t_object a on a.Object_ID=k.Start_Object_ID
                        where k.Stereotype='served by' and a.Stereotype='FRAME_User_Need'
                        and exists(select 1 from t_xref x where x.Client=k.ea_guid) limit 1""").fetchone()[0]
    t = c.execute('select * from t_connector where Connector_ID=?', (tmpl,)).fetchone()
    xdesc = c.execute("select Description from t_xref where Client=? and Name='Stereotypes'", (t['ea_guid'],)).fetchone()[0]
    for k in c.execute("""select k.* from t_connector k join t_object a on a.Object_ID=k.Start_Object_ID join t_object b on b.Object_ID=k.End_Object_ID
                          where a.Stereotype='FRAME_User_Need' and b.Stereotype='FRAME_Low_Level_Function' and k.Connector_Type='Usage'
                          and k.Stereotype is null""").fetchall():
        log.append(f'Usage → «served by»: {nm(k["Start_Object_ID"])} → {nm(k["End_Object_ID"])}')
        c.execute("""update t_connector set Connector_Type='Association', Stereotype='served by', Btm_Mid_Label=?, Direction=?,
                     SourceStyle=?, DestStyle=?, SourceContainment=?, DestContainment=?, SourceChangeable=?, DestChangeable=?,
                     SourceTS=?, DestTS=? where Connector_ID=?""",
                  (t['Btm_Mid_Label'], t['Direction'], t['SourceStyle'], t['DestStyle'], t['SourceContainment'], t['DestContainment'],
                   t['SourceChangeable'], t['DestChangeable'], t['SourceTS'], t['DestTS'], k['Connector_ID']))
        c.execute("delete from t_xref where Client=? and Name='Stereotypes'", (k['ea_guid'],))
        c.execute("insert into t_xref (XrefID, Name, Type, Visibility, Partition, Client, Supplier, Description) values (?,?,?,?,?,?,?,?)",
                  (guid(), 'Stereotypes', 'connector property', 'Public', '0', k['ea_guid'], '<none>', xdesc))

elif step == 'testpkg':
    pid, pguid = c.execute("select Package_ID, ea_guid from t_package where Name='Test Package' and Parent_ID in (select Package_ID from t_package where Parent_ID=0)").fetchone()
    ids = [r[0] for r in c.execute('select Object_ID from t_object where Package_ID=?', (pid,))]
    q = ','.join(map(str, ids))
    outside = c.execute(f'select count(*) from t_connector where (Start_Object_ID in ({q})) <> (End_Object_ID in ({q}))').fetchone()[0]
    if outside or c.execute('select count(*) from t_package where Parent_ID=?', (pid,)).fetchone()[0]:
        sys.exit('Test Package is not self-contained – stop')
    ks = c.execute(f'select Connector_ID, ea_guid from t_connector where Start_Object_ID in ({q})').fetchall()
    dg = c.execute('select Diagram_ID, ea_guid from t_diagram where Package_ID=?', (pid,)).fetchall()
    pobj = c.execute("select Object_ID, ea_guid from t_object where Object_Type='Package' and PDATA1=?", (str(pid),)).fetchone()
    log.append(f'package Test Package: {len(ids)} elements, {len(ks)} connectors, {len(dg)} diagram')
    for i in ids:
        log.append(f'- {nm(i)}')
    kq = ','.join(str(k[0]) for k in ks); dq = ','.join(str(d[0]) for d in dg)
    gl = [k[1] for k in ks] + [d[1] for d in dg] + [r[0] for r in c.execute(f'select ea_guid from t_object where Object_ID in ({q})')] + [pguid, pobj[1]]
    c.execute(f'delete from t_diagramlinks where ConnectorID in ({kq}) or DiagramID in ({dq})')
    c.execute(f'delete from t_connectortag where ElementID in ({kq})')
    c.execute(f'delete from t_connector where Connector_ID in ({kq})')
    c.execute(f'delete from t_diagramobjects where Diagram_ID in ({dq}) or Object_ID in ({q},{pobj[0]})')
    c.execute(f'delete from t_diagram where Diagram_ID in ({dq})')
    for t in ('t_objectproperties', 't_attribute', 't_operation', 't_objectconstraint', 't_objectrequires', 't_objectscenarios',
              't_objectfiles', 't_objectproblems', 't_objectresource', 't_objectrisks', 't_objecttests', 't_objecteffort',
              't_objectmetrics', 't_objecttrx'):
        if c.execute('select 1 from sqlite_master where name=?', (t,)).fetchone():
            c.execute(f'delete from {t} where Object_ID in ({q},{pobj[0]})')
    c.executemany('delete from t_xref where Client=?', [(g,) for g in gl])
    c.execute(f'delete from t_object where Object_ID in ({q},{pobj[0]})')
    c.execute('delete from t_package where Package_ID=?', (pid,))

elif step == 'context':
    D = c.execute("select Diagram_ID from t_diagram where Name='FRAME Context Diagram'").fetchone()[0]
    ft, op = oid('Freight Transport'), oid('Operator')
    frm, to = oid('From Freight Transport'), oid('To Freight Transport')
    t_in = c.execute("select Connector_ID from t_connector where Start_Object_ID=? and End_Object_ID=? and Stereotype='IN'", (op, oid('From Operator'))).fetchone()[0]
    t_out = c.execute("select Connector_ID from t_connector where Start_Object_ID=? and End_Object_ID=? and Stereotype='OUT'", (oid('To Operator'), op)).fetchone()[0]
    new = []
    for tmpl, s, e, lab in ((t_in, ft, frm, 'IN'), (t_out, to, ft, 'OUT')):
        if not c.execute("select 1 from t_connector where Start_Object_ID=? and End_Object_ID=? and Stereotype=?", (s, e, lab)).fetchone():
            new.append(clone(tmpl, s, e)); log.append(f'«{lab}» {nm(s)} → {nm(e)}')
    if not c.execute('select 1 from t_diagramobjects where Diagram_ID=? and Object_ID=?', (D, ft)).fetchone():
        style = c.execute('select ObjectStyle from t_diagramobjects where Diagram_ID=? and Object_ID=?', (D, op)).fetchone()[0]
        style = style.replace(style.split('DUID=')[1][:8], uuid.uuid4().hex[:8].upper())
        seq = c.execute('select max(Sequence)+1 from t_diagramobjects where Diagram_ID=?', (D,)).fetchone()[0]
        # free space right of the flows, between External Service Provider and Vehicle Environment
        c.execute('insert into t_diagramobjects (Diagram_ID, Object_ID, RectTop, RectLeft, RectRight, RectBottom, Sequence, ObjectStyle) values (?,?,?,?,?,?,?,?)',
                  (D, ft, -655, 731, 789, -715, seq, style))
        log.append('Freight Transport placed in the FRAME Context Diagram')
    duid = lambda i: c.execute('select ObjectStyle from t_diagramobjects where Diagram_ID=? and Object_ID=?', (D, i)).fetchone()[0].split('DUID=')[1][:8]
    for k in new:
        s, e = c.execute('select Start_Object_ID, End_Object_ID from t_connector where Connector_ID=?', (k,)).fetchone()
        c.execute('insert into t_diagramlinks (DiagramID, ConnectorID, Geometry, Style, Hidden) values (?,?,?,?,0)',
                  (D, k, 'SX=0;SY=0;EX=0;EY=0;EDGE=2;$LLB=;LLT=;LMT=;LMB=;LRT=;LRB=;IRHS=;ILHS=;',
                   f'Mode=1;EOID={duid(e)};SOID={duid(s)};Color=-1;LWidth=0;'))
else:
    sys.exit(__doc__)

print('\n'.join(log))
if APPLY:
    c.commit(); print('APPLIED')
else:
    c.rollback(); print('(dry run)')
