"""Group C: the IN/OUT connectors and low-level «component of» that groups A/B left open.

usage: 2026-11-06_groupC_open_items.py model.qea proposal.md [--apply]

IN/OUT (#69). For each data flow the role of every endpoint is decided from the flow description and from the
low-level producer/consumer: the high-level function that contains the producer is a producer, the one that contains
the consumer is a consumer. A producer must be  endpoint --«IN»--> flow,  a consumer  flow --«OUT»--> endpoint;
the script relabels and/or reverses the connector to get there.

«component of» between low-level data flows (#80, #81). The part flow is attached to the high-level flow instead:
the LL→LL link is deleted; where either flow is left without a high-level parent, it gets a «component of» to the
high-level parent of the other one.
"""
import sqlite3, sys, re, uuid
path, rep = sys.argv[1:3]; APPLY = '--apply' in sys.argv
c = sqlite3.connect(path); c.row_factory = sqlite3.Row
P, C = 'producer', 'consumer'
ROLES = {  # flow: {endpoint name prefix: role}
    'fft.ftom-incident_responses': {'F8.6.5 ': C},
    'fft.ftom-prepare_new_FTEP': {'F8.4.3 ': C},
    'fft.ftom-request_existing_FTEP': {'F8.4.3 ': C},
    'tft.ftom-prepared_new_FTEP': {'F8.4.3 ': P},
    'tft.ftom-requested_existing_FTEP': {'F8.4.3 ': P},
    'tnap.cp-registration_response': {'F3.6.2 ': P, 'F3.6 ': P},
    'mpto_current_driver_availability': {'F4.4 ': C},
    'mpto_demand_vehicle_repaired': {'F4.7 ': C},
    'mpto_fare_scheme_for_PT_driver': {'F4.2 ': P, 'F4.5 ': C},
    'mpto_fare_scheme_for_service': {'F4.2 ': P, 'F4.5 ': C},
    'mt_carpark_occupancy_for_inter-urban': {'F3.1.5 ': C},
    'mt_inter-urban_strategy_command_response_failure': {'F3.1.2.13 ': C},
    'psef_request_emergency_response_statistics': {'F2.1.2 ': C},
    'pshvs_instructions_&_warnings_for_other_vehicles': {'F5.16 ': P, 'F5.12 ': C},
    'pshvs_location_from_other_vehicle': {'F5.13 ': C},
    'pshvs_other_vehicle_trajectory_for_host_vehicle': {'F5.15.3 ': C},
    'pshvs_vehicle_data_for_trip_planning': {'F5.14 ': C},
    'pshvs_load_operational_data': {'F5.11.13 ': P, 'D5.1 ': C},
    'pshvs_read_operational_data': {'D5.1 ': P, 'F5.11.13 ': C},
    'pshvs_request_driver_condition': {'F5.11.7 ': P, 'F5.11.13 ': C},
    'pshvs_request_driver_stored_data': {'F5.11.11 ': P, 'F5.11.13 ': C},
    'pshvs_request_tvd_incident_data': {'F5.11.6 ': P, 'F5.11.13 ': C},
}
guid = lambda: '{' + str(uuid.uuid4()).upper() + '}'
ins = lambda tab, d: f'insert into {tab} (' + ','.join('"%s"' % k for k in d) + ') values (' + ','.join('?' * len(d)) + ')'


def swap_geom(g):
    if not g: return g
    d = dict(re.findall(r'(SX|SY|EX|EY)=(-?\d+)', g))
    if not d: return g
    r = {'SX': d.get('EX', '0'), 'SY': d.get('EY', '0'), 'EX': d.get('SX', '0'), 'EY': d.get('SY', '0')}
    g = re.sub(r'\b(SX|SY|EX|EY)=(-?\d+)', lambda m: f'{m.group(1)}={r[m.group(1)]}', g)
    return re.sub(r'EDGE=(\d)', lambda m: 'EDGE=' + {'1': '3', '3': '1', '2': '4', '4': '2'}.get(m.group(1), m.group(1)), g, 1)


def reverse(k):
    c.execute('''update t_connector set Start_Object_ID=End_Object_ID, End_Object_ID=Start_Object_ID, Start_Edge=End_Edge,
                 End_Edge=Start_Edge, PtStartX=PtEndX, PtEndX=PtStartX, PtStartY=PtEndY, PtEndY=PtStartY where Connector_ID=?''', (k,))
    for dl in c.execute('select Instance_ID, Geometry, Style, Path from t_diagramlinks where ConnectorID=?', (k,)).fetchall():
        st = dl['Style'] or ''
        so, eo = re.search(r'SOID=([^;]*);', st), re.search(r'EOID=([^;]*);', st)
        if so and eo:
            st = st.replace(f'SOID={so.group(1)};', 'SOID=@@;').replace(f'EOID={eo.group(1)};', f'EOID={so.group(1)};').replace('SOID=@@;', f'SOID={eo.group(1)};')
        p = dl['Path']
        p = ';'.join(reversed([x for x in p.split(';') if x])) + ';' if p else p
        c.execute('update t_diagramlinks set Geometry=?, Style=?, Path=? where Instance_ID=?', (swap_geom(dl['Geometry']), st, p, dl['Instance_ID']))


def relabel(k, new):
    r = c.execute('select ea_guid, Btm_Mid_Label from t_connector where Connector_ID=?', (k,)).fetchone()
    lab = re.sub('«(IN|OUT)»', f'«{new}»', r['Btm_Mid_Label'] or '')
    c.execute('update t_connector set Stereotype=?, Btm_Mid_Label=? where Connector_ID=?', (new, lab or r['Btm_Mid_Label'], k))
    c.execute("update t_xref set Description=? where Client=? and Name='Stereotypes'",
              (f'@STEREO;Name={new};FQName=FRAME_Profile::{new};@ENDSTEREO;', r['ea_guid']))


md = ['# Group C – open IN/OUT and low-level «component of»', '',
      'Convention: producer `endpoint --«IN»--> flow`, consumer `flow --«OUT»--> endpoint`. Role of each endpoint from the',
      'flow description and the low-level producer/consumer (a high-level function takes the role of the low-level function it contains).', '',
      '## IN/OUT (#69)', '', '| Flow | Endpoint | Role | Now | Action |', '|---|---|---|---|---|']
n_io = 0
for flow, roles in ROLES.items():
    f = c.execute("select Object_ID from t_object where trim(Name)=? and Stereotype like 'FRAME_%Data_Flow'", (flow,)).fetchone()[0]
    for pre, role in roles.items():
        rows = c.execute("""select k.Connector_ID, k.Stereotype, k.Start_Object_ID, o.Name from t_connector k join t_object o
                            on o.Object_ID = case when k.Start_Object_ID=? then k.End_Object_ID else k.Start_Object_ID end
                            where ? in (k.Start_Object_ID, k.End_Object_ID) and k.Stereotype in ('IN','OUT') and o.Name like ?""",
                         (f, f, pre + '%')).fetchall()
        if len(rows) != 1:
            sys.exit(f'{flow} / {pre}: {len(rows)} connectors – stop')
        k = rows[0]
        flow_first = k['Start_Object_ID'] == f
        now = f'{"flow → " if flow_first else ""}«{k["Stereotype"]}»{"" if flow_first else " → flow"}'
        want_lab, want_flow_first = ('IN', False) if role == P else ('OUT', True)
        act = []
        if flow_first != want_flow_first:
            act.append('reverse'); APPLY and reverse(k['Connector_ID'])
        if k['Stereotype'] != want_lab:
            act.append(f'relabel «{want_lab}»'); APPLY and relabel(k['Connector_ID'], want_lab)
        if act:
            n_io += 1
        md.append(f'| {flow} | {k["Name"].strip()} | {role} | {now} | {", ".join(act) or "ok"} |')

md += ['', '## «component of» between low-level data flows (#80, #81)', '', '| Part (LL) | Former target (LL) | Action |', '|---|---|---|']
tmpl = c.execute("""select k.Connector_ID from t_connector k join t_object a on a.Object_ID=k.Start_Object_ID join t_object b on b.Object_ID=k.End_Object_ID
                    where k.Stereotype='component of' and a.Stereotype='FRAME_Low_Level_Data_Flow' and b.Stereotype='FRAME_High_Level_Data_Flow' limit 1""").fetchone()[0]
hl_parents = lambda o: c.execute("""select b.Object_ID, trim(b.Name) from t_connector k join t_object b on b.Object_ID=k.End_Object_ID
                                     where k.Start_Object_ID=? and k.Stereotype='component of' and b.Stereotype='FRAME_High_Level_Data_Flow'""", (o,)).fetchall()
ll = c.execute("""select k.Connector_ID, k.ea_guid, a.Object_ID s, trim(a.Name) sn, b.Object_ID t, trim(b.Name) tn from t_connector k
                  join t_object a on a.Object_ID=k.Start_Object_ID join t_object b on b.Object_ID=k.End_Object_ID
                  where k.Stereotype='component of' and a.Stereotype='FRAME_Low_Level_Data_Flow' and b.Stereotype='FRAME_Low_Level_Data_Flow'
                  order by tn, sn""").fetchall()
added = set()
for k in ll:
    act = ['delete LL→LL link (on no diagram)']
    if APPLY:
        c.execute('delete from t_diagramlinks where ConnectorID=?', (k['Connector_ID'],))
        c.execute('delete from t_xref where Client=?', (k['ea_guid'],))
        c.execute('delete from t_connector where Connector_ID=?', (k['Connector_ID'],))
    # both flows must end up with a high-level parent; a flow without one takes the parent(s) of the other
    for me, other, who in ((k['s'], k['t'], 'part'), (k['t'], k['s'], 'former target')):
        have = hl_parents(me)
        if have:
            act.append(f'{who} already part of ' + ', '.join(n for _, n in have)); continue
        for hid, hn in hl_parents(other):
            if (me, hid) in added: continue
            added.add((me, hid)); act.append(f'add «component of» {who} → {hn}')
            if APPLY:
                t = dict(c.execute('select * from t_connector where Connector_ID=?', (tmpl,)).fetchone()); old = t.pop('Connector_ID')
                t.update(Start_Object_ID=me, End_Object_ID=hid, ea_guid=guid(), PDATA5='SX=0;SY=0;EX=0;EY=0;')
                c.execute(ins('t_connector', t), list(t.values()))
                for x in c.execute('select * from t_xref where Client=(select ea_guid from t_connector where Connector_ID=?)', (old,)).fetchall():
                    x = dict(x); x.update(XrefID=guid(), Client=t['ea_guid']); c.execute(ins('t_xref', x), list(x.values()))
    md.append(f'| {k["sn"]} | {k["tn"]} | {"; ".join(act)} |')
md.insert(5, f'{n_io} IN/OUT connectors changed, {len(ll)} low-level «component of» replaced, {len(added)} high-level «component of» added.\n')
open(rep, 'w', encoding='utf-8', newline='\n').write('\n'.join(md) + '\n')
print(md[5])
if APPLY:
    c.commit(); print('APPLIED')
