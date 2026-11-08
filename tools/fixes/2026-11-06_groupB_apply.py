"""Apply group B (IN/OUT) fixes with confidence high or medium from reports/proposal_groupB_in-out.csv.
usage: fixB.py model.qea proposal.csv [--apply]"""
import sqlite3, sys, csv, re
path, prop = sys.argv[1:3]; APPLY = '--apply' in sys.argv
c = sqlite3.connect(path); c.row_factory = sqlite3.Row
rows = [r for r in csv.DictReader(open(prop, encoding='utf-8-sig'), delimiter=';') if r['confidence'] in ('high', 'medium')]
def swap_geom(g):
    if not g: return g
    d = dict(re.findall(r'(SX|SY|EX|EY)=(-?\d+)', g))
    if d:
        rep = {'SX': d.get('EX', '0'), 'SY': d.get('EY', '0'), 'EX': d.get('SX', '0'), 'EY': d.get('SY', '0')}
        g = re.sub(r'\b(SX|SY|EX|EY)=(-?\d+)', lambda m: f'{m.group(1)}={rep[m.group(1)]}', g)
    return re.sub(r'EDGE=(\d)', lambda m: 'EDGE=' + {'1': '3', '3': '1', '2': '4', '4': '2'}.get(m.group(1), m.group(1)), g, 1)
def reverse(cid):
    c.execute('''update t_connector set Start_Object_ID=End_Object_ID, End_Object_ID=Start_Object_ID, Start_Edge=End_Edge, End_Edge=Start_Edge,
                 PtStartX=PtEndX, PtEndX=PtStartX, PtStartY=PtEndY, PtEndY=PtStartY where Connector_ID=?''', (cid,))
    for dl in c.execute('select Instance_ID, Geometry, Style, Path from t_diagramlinks where ConnectorID=?', (cid,)).fetchall():
        st = dl['Style'] or ''
        so, eo = re.search(r'SOID=([^;]*);', st), re.search(r'EOID=([^;]*);', st)
        if so and eo:
            st = st.replace(f'SOID={so.group(1)};', 'SOID=@@;').replace(f'EOID={eo.group(1)};', f'EOID={so.group(1)};').replace('SOID=@@;', f'SOID={eo.group(1)};')
        path_ = (';'.join(reversed([p for p in dl['Path'].split(';') if p])) + ';') if dl['Path'] else dl['Path']
        c.execute('update t_diagramlinks set Geometry=?, Style=?, Path=? where Instance_ID=?', (swap_geom(dl['Geometry']), st, path_, dl['Instance_ID']))
def delete(cid, guid):
    c.execute('delete from t_diagramlinks where ConnectorID=?', (cid,)); c.execute('delete from t_connectortag where ElementID=?', (cid,))
    c.execute('delete from t_xref where Client=?', (guid,)); c.execute('delete from t_connector where Connector_ID=?', (cid,))
def relabel(k, new):
    lab = (k['Btm_Mid_Label'] or '').replace(f'«{k["Stereotype"]}»', f'«{new}»')
    c.execute('update t_connector set Stereotype=?, Btm_Mid_Label=? where Connector_ID=?', (new, lab or None, k['Connector_ID']))
    c.execute("update t_xref set Description=? where Client=? and Name='Stereotypes'", (f'@STEREO;Name={new};FQName=FRAME_Profile::{new};@ENDSTEREO;', k['ea_guid']))
done = {'relabel': 0, 'reverse': 0, 'duplicate deleted': 0, 'missing': 0}
for r in rows:
    k = c.execute('select * from t_connector where ea_guid=?', (r['guid'],)).fetchone()
    if not k: done['missing'] += 1; continue
    if r['action'].startswith('relabel'):
        new = 'OUT' if k['Stereotype'].upper() == 'IN' else 'IN'
        if APPLY: relabel(k, new)
        done['relabel'] += 1
    elif r['action'].startswith('reverse'):
        dup = c.execute('select count(*) from t_connector where Start_Object_ID=? and End_Object_ID=? and upper(Stereotype)=upper(?) and Connector_ID<>?',
                        (k['End_Object_ID'], k['Start_Object_ID'], k['Stereotype'], k['Connector_ID'])).fetchone()[0]
        if dup:
            if APPLY: delete(k['Connector_ID'], k['ea_guid'])
            done['duplicate deleted'] += 1
        else:
            if APPLY: reverse(k['Connector_ID'])
            done['reverse'] += 1
print(len(rows), 'rows', done)
if APPLY: c.commit(); print('APPLIED')
