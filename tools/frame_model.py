"""Shared loader for the FRAME Enterprise Architect model (.qea = SQLite).

Adapted from the NAPCORE NRA tooling. Used by export.py, diff.py and check.py.
"""
import sqlite3, re, html, zipfile, io, base64, os, subprocess

MODEL = 'model/FRAME.qea'


def connect(path):
    c = sqlite3.connect(f'file:{path}?mode=ro', uri=True)
    c.row_factory = sqlite3.Row
    return c


def plain(note):
    """EA notes are stored as light HTML; keep text readable and stable."""
    if not note:
        return ''
    t = note.replace('\r\n', '\n')
    t = re.sub(r'<li>', '- ', t)
    t = re.sub(r'<[^>]+>', '', t)
    t = html.unescape(t)
    return '\n'.join(l.rstrip() for l in t.split('\n')).strip()


def package_paths(c):
    pk = {r['Package_ID']: (r['Name'], r['Parent_ID']) for r in c.execute('select Package_ID, Name, Parent_ID from t_package')}
    cache = {}

    def ppath(pid):
        if pid in cache:
            return cache[pid]
        parts, p = [], pid
        while p in pk and pk[p][1] != 0:
            parts.append(pk[p][0]); p = pk[p][1]
        cache[pid] = '/'.join(reversed(parts))
        return cache[pid]
    return pk, ppath


def load(path):
    """Return a dict with packages, elements, connectors, diagrams, glossary, templates."""
    c = connect(path)
    pk, ppath = package_paths(c)
    tags = {}
    for r in c.execute('select Object_ID, Property, Value from t_objectproperties'):
        tags.setdefault(r['Object_ID'], {})[r['Property']] = r['Value'] or ''
    objs = {}
    for r in c.execute('select * from t_object'):
        o = dict(r)
        objs[o['Object_ID']] = {
            'guid': o['ea_guid'], 'name': (o['Name'] or '').strip(), 'type': o['Object_Type'],
            'stereotype': o['Stereotype'] or '', 'alias': o['Alias'] or '', 'keywords': o['PDATA5'] or '',
            'status': o['Status'] or '', 'version': o['Version'] or '', 'tpos': o['TPos'] or 0,
            'package': ppath(o['Package_ID']), 'note': plain(o['Note']),
            'tags': {k: v for k, v in sorted(tags.get(o['Object_ID'], {}).items())},
        }
    cons = {}
    for r in c.execute('select * from t_connector'):
        s, t = objs.get(r['Start_Object_ID']), objs.get(r['End_Object_ID'])
        cons[r['ea_guid']] = {
            'guid': r['ea_guid'], 'type': r['Connector_Type'], 'stereotype': r['Stereotype'] or '',
            'source': s['guid'] if s else None, 'target': t['guid'] if t else None,
            'source_name': s['name'] if s else '?', 'target_name': t['name'] if t else '?',
            'name': r['Name'] or '', 'note': plain(r['Notes']),
        }
    dobj = {}
    for d, o in c.execute('select Diagram_ID, Object_ID from t_diagramobjects'):
        dobj.setdefault(d, []).append(o)
    diags = {}
    for r in c.execute('select * from t_diagram'):
        els = sorted(objs[o]['name'] for o in dobj.get(r['Diagram_ID'], []) if o in objs)
        diags[r['ea_guid']] = {'guid': r['ea_guid'], 'name': r['Name'], 'package': ppath(r['Package_ID']),
                               'type': r['Diagram_Type'], 'note': plain(r['Notes']), 'elements': els}
    gloss = {r['Term']: {'type': r['Type'], 'meaning': plain(r['Meaning'])} for r in c.execute('select * from t_glossary')}
    tmpl = {}
    for r in c.execute("select DocName, DocID, BinContent, Version from t_document where DocType='SSDOCSTYLE'"):
        try:
            s = zipfile.ZipFile(io.BytesIO(r['BinContent'])).read('str.dat').decode('utf-16le')
            m = re.search(r'<SSDocument\.Document[^>]*>(.*?)</SSDocument\.Document>', s, re.S)
            rtf = base64.b64decode(re.sub(r'\s', '', m.group(1))).decode('latin-1') if m else ''
            opts = re.search(r'<SSDocument\.Options ([^>]*)>', s)
            secs = re.findall(r'<SSDocument\.Section name="([^"]*)"[^>]*enabled="1"', s)
            body = rtf[rtf.find('Pkg_Begin}'):] if 'Pkg_Begin}' in rtf else rtf[-4000:]
            body = re.sub(r'\{\\\*\\bkmk(start|end) [^}]*\}', '', body)
            body = re.sub(r"\\'[0-9a-f]{2}", '', body); body = re.sub(r'\\[a-z]+-?\d* ?', '', body); body = re.sub(r'[{}]', '', body)
            tmpl[r['DocName']] = {'id': r['DocID'], 'kind': {2: 'cover', 3: 'stylesheet', 4: 'toc'}.get(r['Version'], 'template/fragment'),
                                  'options': opts.group(1) if opts else '', 'sections': secs, 'content': ' '.join(body.split())}
        except Exception as e:  # templates are optional; never fail the export because of one
            tmpl[r['DocName']] = {'id': r['DocID'], 'error': str(e)}
    return {'packages': {pid: ppath(pid) for pid in pk}, 'elements': {o['guid']: o for o in objs.values()},
            'connectors': cons, 'diagrams': diags, 'glossary': gloss, 'templates': tmpl}


def view_of(package_path):
    """Grouping used in reports: top-level package and its first child,
    e.g. 'Frame Repository / Frame Functional View' or 'NAP Reference Architecture / 03 NAP Organisational View'."""
    parts = [p for p in package_path.split('/') if p]
    return ' / '.join(parts[:2])


def model_from_git(ref, path=MODEL):
    """Return a temporary file with the model as stored at a git ref.
    Works with git-lfs (smudge) and, where git-lfs is not installed, with objects in .git/lfs/objects."""
    import tempfile
    blob = subprocess.run(['git', 'show', f'{ref}:{path}'], capture_output=True, check=True).stdout
    if blob.startswith(b'version https://git-lfs'):
        oid = re.search(rb'oid sha256:([0-9a-f]{64})', blob).group(1).decode()
        gitdir = subprocess.run(['git', 'rev-parse', '--git-dir'], capture_output=True, check=True, text=True).stdout.strip()
        local = os.path.join(gitdir, 'lfs', 'objects', oid[:2], oid[2:4], oid)
        if os.path.exists(local):
            blob = open(local, 'rb').read()
        else:
            blob = subprocess.run(['git', 'lfs', 'smudge'], input=blob, capture_output=True, check=True).stdout
    f = tempfile.NamedTemporaryFile(suffix='.qea', delete=False); f.write(blob); f.close()
    return f.name
