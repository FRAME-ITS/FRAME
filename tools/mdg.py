"""Extract the MDG technology embedded in the model and report its connector rules (Quick Linker) against the model.

Usage:  python tools/mdg.py [model/FRAME.qea] [report.md] [--xml FRAME_technology.xml]
The model carries the FRAME technology itself (Import to Model, t_document DocType TECHNOLOGY). This is the version
Enterprise Architect uses for the model, independent of any toolbox file imported by the user.
"""
import sys, os, re, io, sqlite3, zipfile
from collections import Counter, defaultdict
sys.path.insert(0, os.path.dirname(__file__))
from frame_model import MODEL

def technology(model):
    c = sqlite3.connect(f'file:{model}?mode=ro', uri=True)
    r = c.execute("select DocName, BinContent from t_document where DocType='TECHNOLOGY'").fetchone()
    raw = zipfile.ZipFile(io.BytesIO(r[1])).read('str.dat')
    return r[0], raw.decode('utf-16le') if raw[1:2] == b'\x00' else raw.decode('utf-8')

def rules(xml):
    prof = xml[xml.find('name="FRAME_Profile"'):]
    prof = prof[:prof.find('</UMLProfile>')]
    out = []
    for m in re.finditer(r'<Stereotype name="([^"]*)"[^>]*>(.*?)</Stereotype>', prof, re.S):
        for st, tg in re.findall(r'<stereotypedrelationship stereotype="([^"]*)" constraint="([^"]*)"', m.group(2)):
            for t in tg.split(';'):
                out.append((st.split('::')[-1], m.group(1), t.split('::')[-1]))
    return sorted(set(out)), set(re.findall(r'<Stereotype name="([^"]*)"', prof))

def main(argv):
    xml_out = argv[argv.index('--xml') + 1] if '--xml' in argv else None
    args = [a for a in argv if a != '--xml' and a != xml_out]
    model = args[0] if args else MODEL
    out = args[1] if len(args) > 1 else None
    name, xml = technology(model)
    if xml_out:
        open(xml_out, 'w', encoding='utf-8', newline='\n').write(xml)
    ver = re.search(r'<Documentation id="[^"]*" name="([^"]*)" version="([^"]*)"', xml)
    rl, defined = rules(xml)
    c = sqlite3.connect(f'file:{model}?mode=ro', uri=True)
    st = {r[0]: r[1] or '' for r in c.execute('select Object_ID, Stereotype from t_object')}
    used = Counter()
    for s, t, cs in c.execute('select Start_Object_ID, End_Object_ID, Stereotype from t_connector where Stereotype is not null'):
        used[(cs, st.get(s, ''), st.get(t, ''))] += 1
    md = [f'# MDG technology embedded in {os.path.basename(model)}', '',
          f'Technology **{name}** – {ver.group(1)} {ver.group(2)}; profile FRAME_Profile defines {len(defined)} stereotypes.', '',
          '## Quick Linker rules vs. use in the model', '',
          'For each rule (source → target) the number of connectors drawn in that direction and in the opposite direction.', '',
          '| Connector | Source | Target | in the model | opposite direction |', '|---|---|---|---|---|']
    for cs, s, t in rl:
        if s.startswith('FRAME_') and t.startswith('FRAME_'):
            same = sum(n for (k, a, b), n in used.items() if k.replace(' ', '').lower() == cs.replace(' ', '').lower() and a == s and b == t)
            opp = sum(n for (k, a, b), n in used.items() if k.replace(' ', '').lower() == cs.replace(' ', '').lower() and a == t and b == s)
            flag = ' ⚠' if opp > same else ''
            md.append(f'| «{cs}» | {s.replace("FRAME_", "")} | {t.replace("FRAME_", "")} | {same} | {opp}{flag} |')
    undefined = Counter(cs for (cs, a, b), n in used.items() for _ in range(n) if a.startswith('FRAME_') and cs not in defined and cs not in ('Instantiate', 'Call', 'stereotyped relationship', 'ArchiMate_Association'))
    md += ['', '## Connector stereotypes used in the model but not defined in the technology', '']
    md += [f'- «{k}» {v}×' for k, v in undefined.most_common()] or ['none']
    text = '\n'.join(md) + '\n'
    if out:
        open(out, 'w', encoding='utf-8', newline='\n').write(text); print('written', out)
    else:
        sys.stdout.write(text)

if __name__ == '__main__':
    main(sys.argv[1:])
