"""Issue #92 – bugs reported by the Serbian ITS National Architecture team (2023, with answers by R. Bossom), 2026-11-09.

point 2  "Broken links in the Functional Trees": 51 high-level functions and functional areas of the FRAME Repository are composite
         elements (or should be) but their composite diagram was lost (NType 8 with PDATA1 = 0, or not composite at all), so
         double-clicking them on a Functional Tree opens nothing. Each has exactly one data flow diagram "DFD <number> ...";
         it becomes the composite diagram (NType 8, PDATA1, DefaultDiagram reference).
point 6b "two associate connectors in the FRAME toolbox": the second one is the plain UML Association (no stereotype, no arrow,
         no label). It is removed from the toolbox page "FRAME Connectors" (FRAME Toolsetup); the MDG technology V1.3 builder
         drops it as well.

usage: python tools/fixes/2026-11-09_issue92_composite_links_toolbox.py model.qea report.md [--apply]
"""
import sys, re, sqlite3, uuid
path, rep = sys.argv[1:3]; APPLY = '--apply' in sys.argv
c = sqlite3.connect(path); c.row_factory = sqlite3.Row
guid = lambda: '{' + str(uuid.uuid4()).upper() + '}'
log = ['## Point 2 – composite diagrams of high-level functions / functional areas\n']
def path_of(pid):
    out = []
    while pid:
        r = c.execute('select Name, Parent_ID from t_package where Package_ID=?', (pid,)).fetchone()
        if not r: break
        out.append(r[0]); pid = r[1]
    return '/'.join(reversed(out))
num = lambda s, pre: (m.group(1) if (m := re.match(pre + r'(F[\d.]+?)\.?[\s-]', s + ' ')) else None)
dfd = {}
for d in c.execute('select Diagram_ID, Name, ea_guid from t_diagram').fetchall():
    n = num(d['Name'], r'\s*DFD\s+')
    if n: dfd.setdefault(n, []).append(d)
dids = {r[0] for r in c.execute('select Diagram_ID from t_diagram')}
n_fix = 0
for o in c.execute("""select Object_ID, Name, NType, PDATA1, Package_ID, ea_guid from t_object
                      where Stereotype in ('FRAME_High_Level_Function','FRAME_Functional_Area') order by Name""").fetchall():
    if 'Frame Repository' not in path_of(o['Package_ID']): continue
    if o['NType'] == 8 and (o['PDATA1'] or '0').isdigit() and int(o['PDATA1'] or 0) in dids: continue
    cand = dfd.get(num(o['Name'], r'(?:Functional Area\s+)?'), [])
    if len(cand) != 1:
        log.append(f'- NOT FIXED {o["Name"]}: {len(cand)} candidate diagrams'); continue
    d = cand[0]
    c.execute("update t_object set NType=8, PDATA1=? where Object_ID=?", (str(d['Diagram_ID']), o['Object_ID']))
    x = c.execute("select XrefID from t_xref where Client=? and Name='DefaultDiagram'", (o['ea_guid'],)).fetchone()
    if x: c.execute('update t_xref set Supplier=? where XrefID=?', (d['ea_guid'], x[0]))
    else: c.execute("""insert into t_xref (XrefID, Name, Type, Visibility, Partition, Client, Supplier)
                       values (?, 'DefaultDiagram', 'element property', 'Public', '0', ?, ?)""", (guid(), o['ea_guid'], d['ea_guid']))
    n_fix += 1
    log.append(f'- {o["Name"].strip()} → "{d["Name"].strip()}"' + ('' if o['NType'] == 8 else ' (was not composite)'))
log.append(f'\n{n_fix} composite links set.\n\n## Point 6b – plain UML Association removed from the toolbox\n')
for a in c.execute("""select a.ID, o.Name from t_attribute a join t_object o on o.Object_ID=a.Object_ID
                      where a.Name='UML::Association' and o.Package_ID in (select Package_ID from t_package where Name='FRAME_Toolbox')""").fetchall():
    c.execute('delete from t_attribute where ID=?', (a['ID'],))
    log.append(f'- toolbox page "{a["Name"]}": entry UML::Association ("associate", no stereotype) removed')
open(rep, 'w', encoding='utf-8').write('# Issue #92 – composite diagrams and toolbox (2026-11-09)\n\nScript: `tools/fixes/2026-11-09_issue92_composite_links_toolbox.py`.\n\n' + '\n'.join(log) + '\n')
print('\n'.join(l for l in log if 'NOT' in l or 'set' in l or 'removed' in l))
if APPLY: c.commit()
