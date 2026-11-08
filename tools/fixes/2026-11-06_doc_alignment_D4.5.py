"""Corrections from the comparison with FRAME NEXT D4.5 Theory of Operations (2021) – reports/compare_D4.2_D4.5_vs_model.md.

usage: 2026-11-06_doc_alignment_D4.5.py model.qea report.md [--apply]
  1. the 8 low-level functions of F3.4 get the prefix 'F' in their names
  2. F3.1.2.14 → 'Implement Inter-urban Traffic Management Strategy'
  3. the second User Need '1.1.4' is 1.2.4 (D4.5 Part 12) – renamed and moved under topic 1.2 Data Exchange
  4. topic names 1.3 Adaptability, 1.4 Constraints, 1.9 Quality of Data Content
  5. requirement type Functionality / Function / Fuctional → Functional
  7. data-flow prefixes fft.fton → fft.ftom, tmmms- → tmms-
  8. terminator mnemonics from D4.5 as element alias (only where the alias is empty; not for terminators shown on
     diagrams that display aliases – NAP Content Provider / Consumer)
"""
import sys, sqlite3
path, rep = sys.argv[1:3]; APPLY = '--apply' in sys.argv
c = sqlite3.connect(path); c.row_factory = sqlite3.Row
log = []
def rename(oid, new, why):
    old = c.execute('select Name from t_object where Object_ID=?', (oid,)).fetchone()[0]
    if old != new:
        c.execute('update t_object set Name=? where Object_ID=?', (new, oid)); log.append(f'{why}: `{old}` → `{new}`')
def one(sql, *a):
    r = c.execute(sql, a).fetchall()
    if len(r) != 1: sys.exit(f'expected one row for {a}: {len(r)}')
    return r[0]
REPO = one("select Package_ID from t_package where Name='Frame Repository'")[0]

# 1
for o in c.execute("select Object_ID, Name from t_object where Stereotype='FRAME_Low_Level_Function' and Name like '3.4.%'").fetchall():
    rename(o['Object_ID'], 'F' + o['Name'], 'function name prefix')
# 2
o = one("select Object_ID from t_object where Name='F3.1.2.14 Implement Inter-urban Management Traffic Strategy'")
rename(o[0], 'F3.1.2.14 Implement Inter-urban Traffic Management Strategy', 'function name (D4.5)')
# 3
un = one("select Object_ID from t_object where Name='1.1.4' and Stereotype='FRAME_User_Need' and Note like 'Systems that conform to the Framework Architecture shall exchange information%'")[0]
topic = one("select Object_ID from t_object where Name='1.2 Data Exchange' and Stereotype='FRAME_User_Need_Topic'")[0]
rename(un, '1.2.4', 'User Need number (D4.5 Part 12)')
c.execute('update t_object set ParentID=? where Object_ID=?', (topic, un)); log.append('User Need 1.2.4 moved under topic 1.2 Data Exchange')
# 4
for old, new in (('1.3 Adapability', '1.3 Adaptability'), ('1.4 Constrains', '1.4 Constraints'), ('1.9 Quality of Data', '1.9 Quality of Data Content')):
    o = one("select Object_ID from t_object where Name=? and Stereotype='FRAME_User_Need_Topic'", old)
    rename(o[0], new, 'User Need topic name (D4.5)')
# 5
for r in c.execute("select r.ReqID, r.Requirement, o.Name from t_objectrequires r join t_object o on o.Object_ID=r.Object_ID where r.Requirement in ('Functionality','Function','Fuctional') and o.Stereotype='FRAME_Low_Level_Function'").fetchall():
    c.execute("update t_objectrequires set Requirement='Functional' where ReqID=?", (r['ReqID'],))
    log.append(f'requirement type `{r["Requirement"]}` → `Functional`: {r["Name"]}')
# 7
for old, new in (('fft.fton-', 'fft.ftom-'), ('tmmms-', 'tmms-')):
    for o in c.execute("select Object_ID, Name, Alias from t_object where Name like ? and Stereotype like 'FRAME_%Data_Flow'", (old + '%',)).fetchall():
        rename(o['Object_ID'], new + o['Name'][len(old):], 'data-flow prefix')
        if o['Alias'] and o['Alias'].startswith(old):
            c.execute('update t_object set Alias=? where Object_ID=?', (new + o['Alias'][len(old):], o['Object_ID']))
# 8
MN = {'Bookable Service Provider': 'esp.bsp', 'Bridge Operator': 'o.bo', 'Bridge Structures': 'bti.bs', 'Broadcaster': 'esp.b',
      'Communications Operator': 'o.co', 'Cyclist': 't.c', 'Driver and Vehicle Information Provider': 'esp.dvip',
      'Electronic Payments Operator': 'o.epo', 'Emergency Management System': 'ors.ems', 'Emergency Operator': 'o.eo',
      'Emergency Vehicle Driver': 'd.e', 'Environmental Traffic Management System': 'ors.etms', 'Freight Terminal Area': 'ft.fta',
      'Freight Transport': 'ft', 'Freight Transport Operations Manager': 'ft.ftom', 'Freight Transport User': 'ft.ftu',
      'Freight Vehicle': 'v.fv', 'Freight Vehicle Driver': 'd.fvd', 'General Information Provider': 'esp.gip',
      'Geographic Information Provider': 'esp.g', 'Hazardous Goods Vehicle Driver': 'd.hgvd', 'Human Machine Interface': 'v.hmi',
      'Incident Traffic Management System': 'ors.itms', 'Inter-urban Traffic Management System': 'ors.iutms',
      'Mobile Communications Provider': 'esp.mcp', 'Multi-Modal Crossing': 'mms.mmc', 'Multi-Modal Management System': 'mms.mms',
      'Multi-Modal Travel Information Provider': 'esp.mmtip', 'On-Demand Service Driver': 'd.odsd', 'On-Demand Service Operator': 'o.odso',
      'On-Demand Service Passenger': 't.odsp', 'On-Demand Service Vehicle': 'v.odsv', 'Other Mode Freight System': 'mms.omfs',
      'Other Navigation Device': 'ors.ond', 'Other Road Users': 've.oru', 'Other Vehicle': 'v.ov', 'Parking Operator': 'o.po',
      'Pedestrian': 't.p', 'Planned Event Organiser': 'esp.peo', 'Pre-Trip Traveller': 't.ptt', 'Public Transport Driver': 'd.ptd',
      'Public Transport Maintenance Organisation': 'mo.ptmo', 'Public Transport Management System': 'ors.ptms',
      'Public Transport Operator': 'o.pto', 'Public Transport Passenger': 't.ptp', 'Public Transport Stop': 'ors.pts',
      'Public Transport Vehicle': 'v.ptv', 'Road Maintenance Operator': 'o.rmo', 'Road Maintenance Organisation': 'mo.rmo',
      'Road Network Operator': 'o.rno', 'Static Traveller': 't.st', 'Stationary Object': 've.so', 'Traffic Signal Controller': 'ors.tsc',
      'Traffic Simulation System': 'ors.tss', 'Traffic and Travel Information Provider': 'esp.ttip', 'Traveller Information Operator': 'o.tio',
      'Trip Planning Driver': 'd.tpd', 'Tunnel Management System': 'bti.tms', 'Tunnel Operator': 'o.tnlo', 'Un/Loading Zone Operator': 'o.ulzo',
      'Urban Traffic Management System': 'ors.utms', 'Vehicle Sharer': 't.vs', 'Vehicle Systems': 'v.vs', 'Vehicle eCall Activation': 'v.vea'}
alias_dgm = {r[0] for r in c.execute("""select x.Object_ID from t_diagram d join t_diagramobjects x on x.Diagram_ID=d.Diagram_ID
                                        where d.StyleEx like '%UseAlias=1%' or d.PDATA like '%UseAlias=1%'""")}
skipped = []
for o in c.execute("select Object_ID, Name, Alias from t_object where Stereotype='FRAME_Terminator'").fetchall():
    n = (o['Name'] or '').strip()
    if n not in MN or o['Alias']: continue
    if o['Object_ID'] in alias_dgm: skipped.append(n); continue
    c.execute('update t_object set Alias=? where Object_ID=?', (MN[n], o['Object_ID'])); log.append(f'terminator alias: {n} = `{MN[n]}`')
if skipped: log.append('alias not set (terminator shown on a diagram that displays aliases): ' + ', '.join(sorted(set(skipped))))
md = ['# Corrections from D4.5 (2021)', '', 'Script: `tools/fixes/2026-11-06_doc_alignment_D4.5.py`; see `reports/compare_D4.2_D4.5_vs_model.md`.', ''] + [f'- {l}' for l in log]
open(rep, 'w', encoding='utf-8', newline='\n').write('\n'.join(md) + '\n')
print('\n'.join(md[4:]))
if APPLY:
    c.commit(); print('APPLIED')
