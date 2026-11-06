"""Align the FRAME Toolsetup package (the profile from which the MDG technology is generated) with technology V1.3.

usage: 2026-11-06_toolsetup_V1.3.py model.qea report.md [--apply]
After this, generating the technology from FRAME Toolsetup in EA (Publish Technology) gives the same Quick Linker as
drafts/latest/toolbox/FRAME_Technology_V1.3.xml. Changes in FRAME_Profile / FRAME_Diagram / FRAME_Toolbox:
  - stereotypes «Impacts» → «impacts», «deliverd by» → «delivered by» (class name, _metatype, toolbox entries)
  - «stereotyped relationship» connectors: tag 'stereotype' normalised (Component of, Defines, Impacts, instant of,
    associated, deliverd by), reversed where V1.3 has the opposite direction, added where V1.3 has a rule the package
    lacks, duplicates removed
  - _HideUmlLinks = True on the metaclass of the core FRAME Repository stereotypes
  - diagram type FRAME_Diagram: toolbox = FRAME::FRAME_Toolbox
"""
import sys, os, re, sqlite3, uuid
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from mdg import rules
path, rep = sys.argv[1:3]; APPLY = '--apply' in sys.argv
V13 = 'drafts/latest/toolbox/FRAME_Technology_V1.3.xml'
want = {(a, b, c) for a, b, c in rules(open(V13, 'rb').read().decode('cp1252'))[0]}
c = sqlite3.connect(path); c.row_factory = sqlite3.Row
guid = lambda: '{' + str(uuid.uuid4()).upper() + '}'
ins = lambda tab, d: f'insert into {tab} (' + ','.join('"%s"' % k for k in d) + ') values (' + ','.join('?' * len(d)) + ')'
P = c.execute("select Package_ID from t_package where Name='FRAME_Profile'").fetchone()[0]
PD = c.execute("select Package_ID from t_package where Name='FRAME_Diagram'").fetchone()[0]
PT = c.execute("select Package_ID from t_package where Name='FRAME_Toolbox' and Package_ID<>(select Parent_ID from t_package where Name='FRAME_Profile')").fetchone()[0]
log = []
RENAME_ST = {'Impacts': 'impacts', 'deliverd by': 'delivered by'}
RENAME_TAG = {'Component of': 'component of', 'Defines': 'defines', 'Impacts': 'impacts', 'instant of': 'instants of',
              'associated': 'associate', 'deliverd by': 'delivered by'}

# stereotype classes
for old, new in RENAME_ST.items():
    for o in c.execute("select Object_ID from t_object where Package_ID=? and Name=?", (P, old)).fetchall():
        c.execute('update t_object set Name=? where Object_ID=?', (new, o[0]))
        c.execute("update t_attribute set \"Default\"=? where Object_ID=? and Name='_metatype' and \"Default\"=?", (new, o[0], old))
        log.append(f'stereotype class «{old}» → «{new}»')
    for a in c.execute(f"select ID, Name, \"Default\" from t_attribute where Object_ID in (select Object_ID from t_object where Package_ID={PT}) and Name like ?",
                       (f'FRAME_Profile::{old}(%',)).fetchall():
        c.execute('update t_attribute set Name=?, "Default"=? where ID=?', (a['Name'].replace(f'::{old}(', f'::{new}('), new if a['Default'].lower() == old.lower() else a['Default'], a['ID']))
        log.append(f'toolbox entry {a["Name"]} → {new}')

name = {r[0]: r[1] for r in c.execute('select Object_ID, Name from t_object where Package_ID=?', (P,))}
oid = {v: k for k, v in name.items()}
def rels():
    out = []
    for k in c.execute(f"select Connector_ID, Start_Object_ID s, End_Object_ID t, ea_guid from t_connector where Stereotype='stereotyped relationship' and Start_Object_ID in (select Object_ID from t_object where Package_ID={P})").fetchall():
        tag = c.execute("select PropertyID, VALUE from t_connectortag where ElementID=? and Property='stereotype'", (k['Connector_ID'],)).fetchone()
        out.append((k, tag))
    return out

# normalise tags, reverse
for k, tag in rels():
    if not tag: continue
    v = tag['VALUE']
    if v in RENAME_TAG:
        c.execute('update t_connectortag set VALUE=? where PropertyID=?', (RENAME_TAG[v], tag['PropertyID']))
        log.append(f'rule «{v}» → «{RENAME_TAG[v]}»: {name[k["s"]]} → {name[k["t"]]}'); v = RENAME_TAG[v]
    if (v, name[k['s']], name[k['t']]) not in want and (v, name[k['t']], name[k['s']]) in want:
        c.execute('update t_connector set Start_Object_ID=End_Object_ID, End_Object_ID=Start_Object_ID where Connector_ID=?', (k['Connector_ID'],))
        for dl in c.execute('select Instance_ID, Geometry, Style from t_diagramlinks where ConnectorID=?', (k['Connector_ID'],)).fetchall():
            st = dl['Style'] or ''
            so, eo = re.search(r'SOID=([^;]*);', st), re.search(r'EOID=([^;]*);', st)
            if so and eo:
                st = st.replace(f'SOID={so.group(1)};', 'SOID=@@;').replace(f'EOID={eo.group(1)};', f'EOID={so.group(1)};').replace('SOID=@@;', f'SOID={eo.group(1)};')
            c.execute('update t_diagramlinks set Style=?, Geometry=? where Instance_ID=?', (st, 'SX=0;SY=0;EX=0;EY=0;', dl['Instance_ID']))
        flip_direction(k['Connector_ID'])
        log.append(f'rule reversed: «{v}» {name[k["s"]]} → {name[k["t"]]}  becomes  {name[k["t"]]} → {name[k["s"]]}')

def flip_direction(k):
    # a connector drawn 'Destination -> Source' shows its arrow at the start; after swapping the ends the arrow must stay at the
    # (new) end, so direction and end styles are swapped as well
    r = c.execute('select Direction, SourceStyle, DestStyle, SourceIsNavigable, DestIsNavigable from t_connector where Connector_ID=?', (k,)).fetchone()
    if r[0] == 'Destination -> Source':
        c.execute('update t_connector set Direction=?, SourceStyle=?, DestStyle=?, SourceIsNavigable=?, DestIsNavigable=? where Connector_ID=?',
                  ('Source -> Destination', r[2], r[1], r[4], r[3], k))

# duplicates
seen = set()
for k, tag in rels():
    key = (tag['VALUE'] if tag else None, k['s'], k['t'])
    if tag and key in seen:
        c.execute('delete from t_connectortag where ElementID=?', (k['Connector_ID'],))
        c.execute('delete from t_diagramlinks where ConnectorID=?', (k['Connector_ID'],))
        c.execute('delete from t_xref where Client=?', (k['ea_guid'],))
        c.execute('delete from t_connector where Connector_ID=?', (k['Connector_ID'],))
        log.append(f'duplicate rule removed: «{key[0]}» {name[k["s"]]} → {name[k["t"]]}')
    seen.add(key)

# missing rules
have = {(tag['VALUE'], name[k['s']], name[k['t']]) for k, tag in rels() if tag}
tmpl, ttag = next((k, tag) for k, tag in rels() if tag)
for st, s, t in sorted(want - have):
    if s not in oid or t not in oid:
        log.append(f'NOT ADDED (stereotype class missing): «{st}» {s} → {t}'); continue
    k = dict(c.execute('select * from t_connector where Connector_ID=?', (tmpl['Connector_ID'],)).fetchone()); old = k.pop('Connector_ID')
    k.update(Start_Object_ID=oid[s], End_Object_ID=oid[t], ea_guid=guid(), PDATA5='SX=0;SY=0;EX=0;EY=0;')
    new = c.execute(ins('t_connector', k), list(k.values())).lastrowid
    for x in c.execute('select * from t_xref where Client=?', (tmpl['ea_guid'],)).fetchall():
        x = dict(x); x.update(XrefID=guid(), Client=k['ea_guid']); c.execute(ins('t_xref', x), list(x.values()))
    tg = dict(c.execute('select * from t_connectortag where PropertyID=?', (ttag['PropertyID'],)).fetchone()); tg.pop('PropertyID')
    tg.update(ElementID=new, VALUE=st, ea_guid=guid()); c.execute(ins('t_connectortag', tg), list(tg.values()))
    log.append(f'rule added: «{st}» {s} → {t}')
have = {(tag['VALUE'], name[k['s']], name[k['t']]) for k, tag in rels() if tag}
extra = sorted(have - want)

# _HideUmlLinks
CORE = ('FRAME_Functional_Area', 'FRAME_High_Level_Function', 'FRAME_Low_Level_Function', 'FRAME_High_Level_Data_Flow',
        'FRAME_Low_Level_Data_Flow', 'FRAME_Terminator', 'FRAME_Datastore', 'FRAME_System', 'FRAME_User_Need',
        'FRAME_User_Need_Topic', 'FRAME_User_Need_Service', 'FRAME_User_Need_Group')
ta = dict(c.execute("select * from t_attribute where Object_ID=(select Object_ID from t_object where Package_ID=? and Name='Diagram_Logical') and Name='toolbox'", (PD,)).fetchone())
for st in CORE:
    for (mid,) in c.execute("select End_Object_ID from t_connector where Connector_Type='Extension' and Start_Object_ID=?", (oid[st],)).fetchall():
        if c.execute("select 1 from t_attribute where Object_ID=? and Name='_HideUmlLinks'", (mid,)).fetchone(): continue
        a = dict(ta); a.pop('ID'); a.update(Object_ID=mid, Name='_HideUmlLinks', Default='True', ea_guid=guid(), Pos=99)
        c.execute(ins('t_attribute', a), list(a.values()))
        log.append(f'_HideUmlLinks = True on the metaclass of {st}')
n = c.execute("update t_attribute set \"Default\"='FRAME::FRAME_Toolbox' where ID=? and \"Default\"='FRAME_Toolbox'", (ta['ID'],)).rowcount
if n: log.append('diagram type FRAME_Diagram: toolbox = FRAME::FRAME_Toolbox')

md = ['# FRAME Toolsetup aligned with technology V1.3', '', 'Script: `tools/fixes/2026-11-06_toolsetup_V1.3.py`.', '']
md += [f'- {l}' for l in log]
md += ['', f'Rules in the package and not in V1.3: {len(extra)}'] + [f'- «{a}» {b} → {cc}' for a, b, cc in extra]
md += ['', f'Rules in V1.3 and not in the package: {len(want - have)}'] + [f'- «{a}» {b} → {cc}' for a, b, cc in sorted(want - have)]
open(rep, 'w', encoding='utf-8', newline='\n').write('\n'.join(md) + '\n')
print('\n'.join(md[4:]))
if APPLY:
    c.commit(); print('APPLIED')
