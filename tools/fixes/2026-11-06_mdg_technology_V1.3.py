"""Build the corrected FRAME MDG technology V1.3 from the V1.2 embedded in the model.

usage: python tools/fixes/2026-11-06_mdg_technology_V1.3.py [model/FRAME.qea] [out.xml] [changes.md] [--embed model-copy.qea]
Base: technology V1.2 as it was stored in the model (drafts/latest/toolbox/FRAME_Technology_V1.2_embedded.xml). Changes:
  1. Quick Linker rules (stereotypedrelationship) that point the opposite way to the model are reversed
     (function hierarchy «component of», user-need hierarchy «belongs to», «associate» Mission Statement – ITS Vision).
     Rules added for patterns the FRAME Repository uses throughout (HL function in HL function,
     functional area in system, IN/OUT of System and functional areas in the Context / functional-area diagrams) and, in the
     motivation layer, Business Expectation «defines» Mission Statement (FRAME Meta Model) and ITS Service «adheres to» Specification;
     physical/functional/communication views: Application «contains» LL function / data store / physical data flow,
     LL data flow «contains» Information Object, Component/Terminator «use» Physical Data Flow, process «triggers» process,
     Specification «defines» Requirement, Agreement «use» Specification, Specification «defines» Agreement,
     Actor «implements» Desired Architecture Goals (new stereotype), Terminator «adheres to» Agreement, Component «owned by» Role, Data Object «adheres to» Specification;
     ITS Service Added Value «delivers value to» Stakeholder replaces «defines».
  2. Quick Linker references to stereotypes that the profile does not define are mapped to the defined name
     (Component of, Defines, instant of, associated).
  3. Stereotype names unified (not used by any connector in the model): «Impacts» → «impacts», «deliverd by» → «delivered by».
  4. Model images of the published V1.0 file (start-page images) added, so that a new project gets them too.
  6. Quick Linker shows only the FRAME relationships for the core FRAME Repository stereotypes (_HideUmlLinks).
  7. Diagram type FRAME_Diagram refers to its toolbox as FRAME::FRAME_Toolbox (opens with the diagram).
  8. Toolbox labels Sub-system (FRAME_Component) and Module (FRAME_Application); Actor «performs» Role replaces Role «defines» Actor.
  5. Version V1.3 (technology, FRAME_Profile, FRAME_Toolbox, FRAME_Diagram).
"""
import sys, os, re, sqlite3
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
from mdg import technology
argv = [a for i, a in enumerate(sys.argv) if a != '--embed' and (i == 0 or sys.argv[i - 1] != '--embed')]
model = argv[1] if len(argv) > 1 else 'model/FRAME.qea'
out = argv[2] if len(argv) > 2 else 'drafts/latest/toolbox/FRAME_Technology_V1.3.xml'
rep = argv[3] if len(argv) > 3 else 'drafts/latest/toolbox/FRAME_Technology_V1.3_changes.md'
V10 = 'drafts/latest/toolbox/FRAME_V1_MTS.xml'
BASE = 'drafts/latest/toolbox/FRAME_Technology_V1.2_embedded.xml'   # V1.2 as it was embedded in the model
x = open(BASE, encoding='utf-8').read()
log = []
P = 'FRAME_Profile::'

# 3. stereotype names (everywhere: definition, metatype, Quick Linker, toolbox)
for old, new in (('Impacts', 'impacts'), ('deliverd by', 'delivered by')):
    n = len(re.findall(re.escape(old) + r'(?=["(])', x)) + len(re.findall(re.escape(P + old) + r'(?=["(;])', x))
    x = re.sub(r'(?<=["])' + re.escape(old) + r'(?=")', new, x)
    x = x.replace(P + old + '"', P + new + '"').replace(P + old + '(', P + new + '(').replace(P + old + ';', P + new + ';')
    log.append(f'stereotype «{old}» renamed «{new}» ({n} occurrences)')
# 3b. new connector stereotypes (decided 2026-11-06): «delivers value to» (ITS Service Added Value → Stakeholder, was «defines»)
#     and «triggers» (process → process); defined like «use» (Association, Source -> Destination) and added to the toolbox page
for st in ('delivers value to', 'triggers', 'implements', 'performs', 'delivers'):
    if f'<Stereotype name="{st}"' in x: continue
    use = re.search(r'<Stereotype name="use" metatype="use".*?</Stereotype>', x, re.S).group(0)
    x = x.replace(use, use + '\n\t\t\t\t\t' + use.replace('name="use" metatype="use"', f'name="{st}" metatype="{st}"'), 1)
    tag = '<Tag name="FRAME_Profile::use(UML::Association)" type="" description="" unit="" values="" default="use"/>'
    x = x.replace(tag, tag + '\n\t\t\t\t\t\t\t' + tag.replace('::use(', f'::{st}(').replace('default="use"', f'default="{st}"'), 1)
    log.append(f'new stereotype «{st}» (Association) with toolbox entry')

# 2. Quick Linker references to undefined names
for old, new in (('Component of', 'component of'), ('Defines', 'defines'), ('instant of', 'instants of'), ('associated', 'associate')):
    n = x.count(f'stereotype="{P}{old}"')
    x = x.replace(f'stereotype="{P}{old}"', f'stereotype="{P}{new}"')
    log.append(f'Quick Linker: «{old}» → «{new}» ({n} rules)')

# 1. reverse rules that point the opposite way to the model
REVERSE = [('component of', 'FRAME_Functional_Area', 'FRAME_Low_Level_Function'),
           ('component of', 'FRAME_Functional_Area', 'FRAME_High_Level_Function'),
           ('component of', 'FRAME_High_Level_Function', 'FRAME_Low_Level_Function'),
           ('belongs to', 'FRAME_User_Need_Group', 'FRAME_User_Need_Service'),
           ('belongs to', 'FRAME_User_Need_Service', 'FRAME_User_Need_Topic'),
           ('belongs to', 'FRAME_User_Need_Topic', 'FRAME_User_Need'),
           ('associate', 'FRAME_Mission_Statement', 'FRAME_ITS_Vision')]
s0, s1 = x.find('name="FRAME_Profile"'), None
s1 = x.find('</UMLProfile>', s0)
prof = x[s0:s1]
def block(p, name):
    m = re.search(r'<Stereotype name="' + re.escape(name) + r'"[^>]*>.*?</Stereotype>', p, re.S)
    if not m: sys.exit(f'stereotype {name} not found')
    return m
REL = re.compile(r'(\s*)<stereotypedrelationship stereotype="([^"]*)" constraint="([^"]*)"/>')
def edit_rules(name, st, fn):
    """apply fn(list of constraint targets) to the rule «st» of stereotype `name`; [] removes the rule"""
    global prof
    m = block(prof, name); b = m.group(0); found = False
    def sub(r):
        nonlocal found
        if r.group(2) != P + st: return r.group(0)
        found = True
        t = fn(list(dict.fromkeys(r.group(3).split(';'))))
        return f'{r.group(1)}<stereotypedrelationship stereotype="{r.group(2)}" constraint="{";".join(t)}"/>' if t else ''
    b = REL.sub(sub, b)
    if not found:
        t = fn([])
        if t:
            rule = f'<stereotypedrelationship stereotype="{P}{st}" constraint="{";".join(t)}"/>'
            if '<stereotypedrelationships>' in b:
                b = b.replace('<stereotypedrelationships>', '<stereotypedrelationships>\n\t\t\t\t\t\t\t' + rule, 1)
            else:
                h = re.match(r'<Stereotype name="[^"]*"[^>]*>', b).group(0)
                b = h + '\n\t\t\t\t\t\t<stereotypedrelationships>\n\t\t\t\t\t\t\t' + rule + '\n\t\t\t\t\t\t</stereotypedrelationships>' + b[len(h):]
    b = re.sub(r'\s*<stereotypedrelationships>\s*</stereotypedrelationships>', '', b)
    prof = prof[:m.start()] + b + prof[m.end():]
    return found
for st, src, tgt in REVERSE:
    had = []
    edit_rules(src, st, lambda t: (had.append(P + tgt in t), [c for c in t if c != P + tgt])[1])
    if not any(had): sys.exit(f'rule {st} {src} -> {tgt} not found')
    edit_rules(tgt, st, lambda t: t + [P + src] if P + src not in t else t)
    log.append(f'Quick Linker reversed: «{st}» {src[6:]} → {tgt[6:]}  becomes  {tgt[6:]} → {src[6:]}')
# 1b. rules for patterns the FRAME Repository uses throughout but the Quick Linker does not offer
# sub-terminator → terminator is «is Type of» (already in V1.2; issue #68, decided 2026-11-08), not «component of»
ADD = [('component of', 'FRAME_High_Level_Function', 'FRAME_High_Level_Function'),
       ('component of', 'FRAME_Functional_Area', 'FRAME_System'),
       ('IN', 'FRAME_System', 'FRAME_High_Level_Data_Flow'), ('OUT', 'FRAME_High_Level_Data_Flow', 'FRAME_System'),   # Context Diagram
       ('IN', 'FRAME_Functional_Area', 'FRAME_Low_Level_Data_Flow'), ('OUT', 'FRAME_Low_Level_Data_Flow', 'FRAME_Functional_Area'),
       # motivation layer: relationships of the FRAME Meta Model that the reference architectures (NAP, NB, C-ITS) had to draw as
       # plain UML Realisation/Instantiate links because the technology did not offer them
       ('adheres to', 'FRAME_ITS_Service', 'FRAME_Specification'),
       # decided 2026-11-06 from the reference architectures (physical, functional, communication views)
       ('contains', 'FRAME_Application', 'FRAME_Low_Level_Function'), ('contains', 'FRAME_Application', 'FRAME_Datastore'),
       ('contains', 'FRAME_Application', 'FRAME_Physical_Data_Flow'), ('contains', 'FRAME_Low_Level_Data_Flow', 'FRAME_Information_Object'),
       ('use', 'FRAME_Component', 'FRAME_Physical_Data_Flow'), ('use', 'FRAME_Terminator', 'FRAME_Physical_Data_Flow'),
       ('triggers', 'FRAME_ITS_Service_Process', 'FRAME_ITS_Service_Process'),
       ('triggers', 'FRAME_ITS_Business_Process', 'FRAME_ITS_Business_Process'),
       ('delivers value to', 'FRAME_ITS_Service_Added_Value', 'FRAME_Stakeholder'),
       ('defines', 'FRAME_Specification', 'FRAME_Requirement'),
       # decided 2026-11-06 (second round)
       ('use', 'FRAME_Agreement', 'FRAME_Specification'), ('defines', 'FRAME_Specification', 'FRAME_Agreement'),
       ('implements', 'FRAME_Actor', 'FRAME_Desired_Architecture_Goals'), ('adheres to', 'FRAME_Terminator', 'FRAME_Agreement'),
       # FRAME Meta Model (decided 2026-11-06)
       ('owned by', 'FRAME_Component', 'FRAME_Role'), ('adheres to', 'FRAME_Data_Object', 'FRAME_Specification'),
       # NRA article (decided 2026-11-06)
       ('defines', 'FRAME_Business_Expectation', 'FRAME_ITS_Service'), ('owned by', 'FRAME_Application', 'FRAME_Role'),
       ('performs', 'FRAME_Actor', 'FRAME_Role'),
       # issues #82 (Role «adheres to» Agreement, Agreement «accepted by» Role) and #85 (ITS Service «delivers» Added Value), decided 2026-11-07
       ('adheres to', 'FRAME_Role', 'FRAME_Agreement'), ('accepted by', 'FRAME_Agreement', 'FRAME_Role'),
       ('delivers', 'FRAME_ITS_Service', 'FRAME_ITS_Service_Added_Value')]
# rules replaced by the above
DROP = [('defines', 'FRAME_ITS_Service_Added_Value', 'FRAME_Stakeholder'), ('defines', 'FRAME_Role', 'FRAME_Actor'),
        # issue #82: names were swapped against the direction
        ('adheres to', 'FRAME_Agreement', 'FRAME_Role'), ('accepted by', 'FRAME_Role', 'FRAME_Agreement'),
        # issue #85: connector 3 replaced by «delivers»; connectors 1, 4, 5 removed
        ('delivered by', 'FRAME_ITS_Service', 'FRAME_ITS_Service_Added_Value'),
        ('defines', 'FRAME_ITS_Vision', 'FRAME_Requirement'), ('defines', 'FRAME_ITS_Service_Added_Value', 'FRAME_User_Need')]
for st, src, tgt in DROP:
    edit_rules(src, st, lambda t: [c for c in t if c != P + tgt])
    log.append(f'Quick Linker removed: «{st}» {src[6:]} → {tgt[6:]}')
for st, src, tgt in ADD:
    edit_rules(src, st, lambda t: t + [P + tgt] if P + tgt not in t else t)
    log.append(f'Quick Linker added: «{st}» {src[6:]} → {tgt[6:]}')
# merge rules of the same stereotype within one stereotype (after renaming: Defines/defines, Impacts/impacts)
def merge(m):
    b = m.group(0); seen = {}; order = []
    for r in REL.finditer(b):
        if r.group(2) not in seen: seen[r.group(2)] = []; order.append(r.group(2))
        seen[r.group(2)] += [c for c in r.group(3).split(';') if c not in seen[r.group(2)]]
    n = len(REL.findall(b))
    if n == len(order): return b
    log.append(f'Quick Linker: {m.group(1).replace("FRAME_", "")} – {n} rules merged into {len(order)}')
    first = True
    def sub(r):
        nonlocal first
        if not first: return ''
        first = False
        return ''.join(f'{r.group(1)}<stereotypedrelationship stereotype="{k}" constraint="{";".join(seen[k])}"/>' for k in order)
    return REL.sub(sub, b)
prof = re.sub(r'<Stereotype name="([^"]*)"[^>]*>.*?</Stereotype>', merge, prof, flags=re.S)
# 6. Quick Linker offers only the FRAME relationships for the core FRAME Repository stereotypes (_HideUmlLinks on the metaclass)
CORE = ('FRAME_Functional_Area', 'FRAME_High_Level_Function', 'FRAME_Low_Level_Function', 'FRAME_High_Level_Data_Flow',
        'FRAME_Low_Level_Data_Flow', 'FRAME_Terminator', 'FRAME_Datastore', 'FRAME_System', 'FRAME_User_Need',
        'FRAME_User_Need_Topic', 'FRAME_User_Need_Service', 'FRAME_User_Need_Group')
for name in CORE:
    m = block(prof, name); b = m.group(0)
    if '_HideUmlLinks' in b: continue
    b2, n = re.subn(r'<Apply type="([^"]+)"\s*/>', r'<Apply type="\1"><Property name="_HideUmlLinks" value="True"/></Apply>', b)
    if not n: sys.exit(f'{name}: no metaclass (Apply) found')
    prof = prof[:m.start()] + b2 + prof[m.end():]
log.append('Quick Linker: UML links hidden (_HideUmlLinks) for ' + ', '.join(n[6:] for n in CORE))
x = x[:s0] + prof + x[s1:]

# 7. FRAME diagrams open the FRAME toolbox: the diagram type needs the qualified toolbox name <technology>::<toolbox profile>
n = x.count('<Property name="toolbox" value="FRAME_Toolbox"/>')
x = x.replace('<Property name="toolbox" value="FRAME_Toolbox"/>', '<Property name="toolbox" value="FRAME::FRAME_Toolbox"/>')
log.append(f'diagram type FRAME_Diagram: toolbox "FRAME_Toolbox" → "FRAME::FRAME_Toolbox" ({n}), so the FRAME toolbox opens with the diagram')

# 8. toolbox labels as in D4.2 and the documentation: Component → Sub-system, Application → Module (stereotype names unchanged)
for st, old, new in (('FRAME_Component', 'Component', 'Sub-system'), ('FRAME_Application', 'Application', 'Module')):
    t = f'<Tag name="FRAME_Profile::{st}(UML::'
    n = len(re.findall(re.escape(t) + r'[^)]*\)" type="" description="" unit="" values="" default="' + old + '"', x))
    x = re.sub('(' + re.escape(t) + r'[^)]*\)" type="" description="" unit="" values="" default=")' + old + '"', r'\g<1>' + new + '"', x)
    log.append(f'toolbox label {st}: "{old}" → "{new}" ({n})')

# 4. model images from V1.0
v10 = open(V10, encoding='cp1252').read()
imgs = v10[v10.find('<Images>'):v10.find('</Images>') + len('</Images>')]
if '<Images>' not in x and imgs:
    x = x.replace('<DiagramProfile>', imgs + '<DiagramProfile>', 1)
    log.append(f'model images added from V1.0: {len(re.findall(r"<DataRow>", imgs))} (start-page images)')

# 5. versions
x = x.replace('name="FRAME Architecture" version="V1.2"', 'name="FRAME Architecture" version="V1.3"')
x = re.sub(r'(<Documentation id="[^"]*" name="FRAME_(?:Profile|Toolbox|Diagram)" version=")[^"]*"', r'\g<1>1.3"', x)
x = x.replace('<?xml version="1.0"?>', '<?xml version="1.0" encoding="windows-1252"?>', 1)
import xml.dom.minidom
xml.dom.minidom.parseString(x.encode('cp1252'))   # well-formed
open(out, 'w', encoding='cp1252', newline='\r\n').write(x)
open(rep, 'w', encoding='utf-8', newline='\n').write('# FRAME MDG technology V1.3 – changes against V1.2 (embedded in FRAME.qea)\n\n'
    + f'Built by `tools/fixes/2026-11-06_mdg_technology_V1.3.py`.\n\n' + '\n'.join('- ' + l for l in log) + '\n')
print('\n'.join(log)); print('written', out)


def embed(model_path, xml_text):
    """store the technology in the model (t_document TECHNOLOGY), as Enterprise Architect does on 'Import to model':
    zip with str.dat in UTF-16LE; model images are not included (they are in t_image already)."""
    import io, zipfile, time
    t = re.sub(r'<Images>.*?</Images>', '', xml_text, flags=re.S).replace('<?xml version="1.0" encoding="windows-1252"?>', '<?xml version="1.0"?>', 1)
    buf = io.BytesIO()
    with zipfile.ZipFile(buf, 'w', zipfile.ZIP_DEFLATED) as z:
        z.writestr(zipfile.ZipInfo('str.dat', time.localtime()[:6]), t.encode('utf-16le'), zipfile.ZIP_DEFLATED)
    c = sqlite3.connect(model_path)
    n = c.execute("update t_document set BinContent=? where DocType='TECHNOLOGY' and DocName='FRAME'", (buf.getvalue(),)).rowcount
    c.commit()
    if n != 1: sys.exit('embedded technology FRAME not found')
    print('embedded in', model_path)


if '--embed' in sys.argv:
    embed(sys.argv[sys.argv.index('--embed') + 1], x)
