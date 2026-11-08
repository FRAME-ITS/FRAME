"""Changes decided after comparing the NRA article with the model (reports/compare_article_NRA_vs_model.md).

usage: 2026-11-06_article_alignment.py model.qea report.md [--apply]
  - Role «defines» Actor becomes Actor «performs» Role everywhere (reversed, new stereotype of V1.3)
  - FRAME Meta Model: new links Business Expectation «defines» ITS Service, ITS Service «delivered by» Added Value,
    Terminator «use» Physical Data Flow, Interface «defines» Requirement, Application «owned by» Role
  - NAP RA clean-up: actors 'NAP Content Consumer' / 'NAP Content Provider' (on no diagram) merged into 'Content Consumer' /
    'Content Provider'; stakeholder 'NAP' (on no diagram) merged into stakeholder 'NAP Operator'; typos; the grouping
    specification 'FRAME_Specification1' renamed
"""
import sys, re, sqlite3, uuid
path, rep = sys.argv[1:3]; APPLY = '--apply' in sys.argv
c = sqlite3.connect(path); c.row_factory = sqlite3.Row
guid = lambda: '{' + str(uuid.uuid4()).upper() + '}'
ins = lambda tab, d: f'insert into {tab} (' + ','.join('"%s"' % k for k in d) + ') values (' + ','.join('?' * len(d)) + ')'
log = []
COLS = ('Connector_Type', 'Direction', 'SourceStyle', 'DestStyle', 'SourceIsNavigable', 'DestIsNavigable', 'SourceIsAggregate', 'DestIsAggregate', 'SubType')
def template(st):
    return c.execute("""select k.* from t_connector k join t_xref x on x.Client=k.ea_guid and x.Name='Stereotypes'
                        where k.Stereotype=? and x.Description like ? limit 1""", (st, f'%FQName=FRAME_Profile::{st};%')).fetchone() \
        or c.execute("select k.* from t_connector k where k.Stereotype='use' and Connector_Type='Association' limit 1").fetchone()
def set_st(cid, guid_, new):
    tp = template(new)
    c.execute(f'update t_connector set {", ".join(x + "=?" for x in COLS)}, Stereotype=?, Btm_Mid_Label=? where Connector_ID=?',
              [tp[x] for x in COLS] + [new, f'«{new}»', cid])
    c.execute("delete from t_xref where Client=? and Name='Stereotypes'", (guid_,))
    c.execute("insert into t_xref (XrefID, Name, Type, Visibility, Partition, Client, Supplier, Description) values (?,?,?,?,?,?,?,?)",
              (guid(), 'Stereotypes', 'connector property', 'Public', '0', guid_, '<none>', f'@STEREO;Name={new};FQName=FRAME_Profile::{new};@ENDSTEREO;'))
def reverse(cid):
    c.execute('update t_connector set Start_Object_ID=End_Object_ID, End_Object_ID=Start_Object_ID where Connector_ID=?', (cid,))
    for dl in c.execute('select Instance_ID, Style from t_diagramlinks where ConnectorID=?', (cid,)).fetchall():
        st = dl['Style'] or ''; so, eo = re.search(r'SOID=([^;]*);', st), re.search(r'EOID=([^;]*);', st)
        if so and eo:
            st = st.replace(f'SOID={so.group(1)};', 'SOID=@@;').replace(f'EOID={eo.group(1)};', f'EOID={so.group(1)};').replace('SOID=@@;', f'SOID={eo.group(1)};')
        c.execute("update t_diagramlinks set Style=?, Geometry='SX=0;SY=0;EX=0;EY=0;' where Instance_ID=?", (st, dl['Instance_ID']))
def delete_conn(cid, g):
    c.execute('delete from t_diagramlinks where ConnectorID=?', (cid,)); c.execute('delete from t_xref where Client=?', (g,))
    c.execute('delete from t_connectortag where ElementID=?', (cid,)); c.execute('delete from t_connector where Connector_ID=?', (cid,))
def new_conn(s, t, st):
    tp = dict(template(st)); tp.pop('Connector_ID')
    tp.update(Start_Object_ID=s, End_Object_ID=t, ea_guid=guid(), PDATA5='SX=0;SY=0;EX=0;EY=0;')
    cid = c.execute(ins('t_connector', tp), list(tp.values())).lastrowid
    set_st(cid, tp['ea_guid'], st)

# Actor «performs» Role
n = 0
for k in c.execute("""select k.Connector_ID, k.ea_guid, a.Name an, b.Name bn from t_connector k join t_object a on a.Object_ID=k.Start_Object_ID
                      join t_object b on b.Object_ID=k.End_Object_ID where k.Stereotype='defines' and a.Stereotype='FRAME_Role' and b.Stereotype='FRAME_Actor'""").fetchall():
    reverse(k['Connector_ID']); set_st(k['Connector_ID'], k['ea_guid'], 'performs'); n += 1
log.append(f'{n}× Role «defines» Actor → Actor «performs» Role (reversed)')

# FRAME Meta Model links
M = ','.join(str(r[0]) for r in c.execute("select Package_ID from t_package where Name in ('FRAME_Metamodel', 'FRAME Meta Model')"))
mobj = lambda st: c.execute(f"select Object_ID, Name from t_object where Package_ID in ({M}) and Stereotype=?", (st,)).fetchone()
for st, s, t in (('defines', 'Business_Expectation', 'ITS_Service'), ('delivered by', 'ITS_Service', 'ITS_Service_Added_Value'),
                 ('use', 'Terminator', 'Physical_Data_Flow'), ('defines', 'Interface', 'Requirement'), ('owned by', 'Application', 'Role')):
    a, b = mobj('FRAME_' + s), mobj('FRAME_' + t)
    if not a or not b: log.append(f'Meta Model: element missing for {s} → {t}'); continue
    if c.execute('select 1 from t_connector where Start_Object_ID=? and End_Object_ID=? and Stereotype=?', (a[0], b[0], st)).fetchone(): continue
    new_conn(a[0], b[0], st); log.append(f'Meta Model: {a[1]} «{st}» {b[1]} added')

# NAP RA clean-up
def merge(keep, drop):
    K = c.execute('select * from t_object where Object_ID=?', (keep,)).fetchone(); D = c.execute('select * from t_object where Object_ID=?', (drop,)).fetchone()
    for k in c.execute('select * from t_connector where ? in (Start_Object_ID, End_Object_ID)', (drop,)).fetchall():
        s = keep if k['Start_Object_ID'] == drop else k['Start_Object_ID']; t = keep if k['End_Object_ID'] == drop else k['End_Object_ID']
        if s == t or c.execute("select 1 from t_connector where Start_Object_ID=? and End_Object_ID=? and ifnull(Stereotype,'')=ifnull(?,'') and Connector_ID<>?",
                               (s, t, k['Stereotype'], k['Connector_ID'])).fetchone():
            delete_conn(k['Connector_ID'], k['ea_guid'])
        else:
            c.execute('update t_connector set Start_Object_ID=?, End_Object_ID=? where Connector_ID=?', (s, t, k['Connector_ID']))
    dn, kn = re.sub(r'<[^>]+>', ' ', D['Note'] or '').strip(), re.sub(r'<[^>]+>', ' ', K['Note'] or '').strip()
    if dn and dn[:60] not in kn:
        c.execute('update t_object set Note=? where Object_ID=?', ((K['Note'] or '') + '\r\n\r\n' + D['Note'], keep))
    for tb in ('t_objectproperties', 't_attribute', 't_operation', 't_objectrequires', 't_diagramobjects'):
        c.execute(f'delete from {tb} where Object_ID=?', (drop,))
    c.execute('delete from t_xref where Client=?', (D['ea_guid'],)); c.execute('delete from t_object where Object_ID=?', (drop,))
    log.append(f'NAP RA: {D["Stereotype"][6:]} "{D["Name"]}" merged into "{K["Name"]}" (links moved, duplicates removed, note kept)')
NAP = [r[0] for r in c.execute("select Package_ID from t_package")]
def nap_obj(name, st):
    rows = c.execute("select o.Object_ID, o.Package_ID from t_object o where trim(o.Name)=? and o.Stereotype=?", (name, st)).fetchall()
    def top(p):
        while True:
            r = c.execute('select Name, Parent_ID from t_package where Package_ID=?', (p,)).fetchone()
            if not r or r[1] == 0 or c.execute('select Parent_ID from t_package where Package_ID=?', (r[1],)).fetchone()[0] == 0: return r[0] if r else ''
            p = r[1]
    rows = [r for r in rows if top(r[1]) == 'NAP Reference Architecture']
    if len(rows) != 1: sys.exit(f'{name}: {len(rows)}')
    return rows[0][0]
merge(nap_obj('Content Consumer', 'FRAME_Actor'), nap_obj('NAP Content Consumer', 'FRAME_Actor'))
merge(nap_obj('Content Provider', 'FRAME_Actor'), nap_obj('NAP Content Provider', 'FRAME_Actor'))
merge(nap_obj('NAP Operator', 'FRAME_Stakeholder'), nap_obj('NAP', 'FRAME_Stakeholder'))
for old, new in (('European Commision (EC)', 'European Commission (EC)'),
                 ('Automatic provision of metadata vie machine to machine interface', 'Automatic provision of metadata via machine to machine interface')):
    if c.execute('update t_object set Name=? where trim(Name)=?', (new, old)).rowcount: log.append(f'NAP RA: "{old}" → "{new}"')
o = c.execute("select Object_ID from t_object where Name='FRAME_Specification1' and Note like 'There are several specifications%'").fetchone()
if o:
    c.execute("update t_object set Name='Content Consumer data retrieval specifications' where Object_ID=?", (o[0],))
    log.append('NAP RA: grouping specification "FRAME_Specification1" → "Content Consumer data retrieval specifications"')
md = ['# Changes after the NRA article comparison', '', 'Script: `tools/fixes/2026-11-06_article_alignment.py`; decided by the git maintainer.', ''] + [f'- {l}' for l in log]
md += ['', 'Kept: specification "Specification tbd" (NAP RA, marks interfaces whose standard is not yet chosen); empty "FRAME_Specification1" in the eCall motivation layer (eCall RA, not part of this clean-up).']
open(rep, 'w', encoding='utf-8', newline='\n').write('\n'.join(md) + '\n')
print('\n'.join(md[4:]))
if APPLY:
    c.commit(); print('APPLIED')
