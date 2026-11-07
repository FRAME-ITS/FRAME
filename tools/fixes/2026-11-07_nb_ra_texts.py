"""NB Reference Architecture – texts on the landing page and in the motivation view, comments of R. Bossom (2026-09),
groups A and B of the review (only what lives in the model; the web export itself is done from EA).

[G1] landing page: the NB RA is a live document that expands on the FRAME Repository
[G6] landing page: how to navigate the published architecture
[G2–G4] landing page: problems are reported as GitHub issues (the link pointed to the repository start page)
[S2] glossary: abbreviations used in the architecture added
[M1] motivation view: "Link to other Views" → "Link to Views of Stakeholders"
[S3] change history: entry for the next version (draft, version number to be confirmed)

usage: python tools/fixes/2026-11-07_nb_ra_texts.py model.qea report.md [--apply]
"""
import sys, sqlite3
path, rep = sys.argv[1:3]; APPLY = '--apply' in sys.argv
c = sqlite3.connect(path); c.row_factory = sqlite3.Row
log = []
N = '\r\n'
def obj(where, *a):
    r = c.execute(f'select Object_ID, Name, Note from t_object where {where}', a).fetchall()
    if len(r) != 1: sys.exit(f'{len(r)} objects for {where} {a}')
    return r[0]

land = obj("Note like 'Welcome to the Landing Page of National Body Reference Architecture%'")
note = land['Note']
if 'live document' not in note:
    note = note.replace('The Architecture will show common functionalities and processes of National Bodies in Europe.',
        'The Architecture will show common functionalities and processes of National Bodies in Europe.' + N + N +
        'The NB Reference Architecture is a live document: it expands on what is in the FRAME Repository by providing much greater detail.' + N + N +
        'How to navigate: the index on the left lists the packages and elements of the architecture; the boxes in the diagrams '
        '(e.g. the views on this page) open the diagram of the view, and each element page lists its connections to other elements.')
    note = note.replace('please report it under:' + N + '<a href="$inet://https://github.com/NAPCORE/NB-Reference-Architecture"><font color="#0000ff"><u>https://github.com/NAPCORE/NB-Reference-Architecture</u></font></a>',
        'please report it as an issue under:' + N + '<a href="$inet://https://github.com/NAPCORE/NB-Reference-Architecture/issues"><font color="#0000ff"><u>https://github.com/NAPCORE/NB-Reference-Architecture/issues</u></font></a>')
    if '/issues' not in note: sys.exit('landing page: issue link not found')
    c.execute('update t_object set Note=? where Object_ID=?', (note, land['Object_ID'])); log.append('- landing page: live-document note, navigation hint, issue link [G1, G6, G2–G4]')

g = obj("Name='NB Glossary' and Stereotype='GlossaryEntry'")
ADD = [('EC', 'European Commission'), ('EU', 'European Union'), ('ITS', 'Intelligent Transport Systems'), ('MS', 'Member State'),
       ('NAP', 'National Access Point'), ('NAPCORE', 'National Access Point Coordination Organisation for Europe'),
       ('SD', 'Self-declaration'), ('Compliance assessment', 'written in full in this architecture; "CA" stands for Competent Authority')]
note = g['Note']; added = []
for a, t in ADD:
    if f'{N}{a}\t' not in note and not note.startswith(a + '\t'):
        note = note.rstrip() + N + N + f'{a}\t\t{t}'; added.append(a)
if added:
    c.execute('update t_object set Note=? where Object_ID=?', (note, g['Object_ID'])); log.append(f'- glossary: {", ".join(added)} added [S2]')

for b in c.execute("select Object_ID, Name from t_object where Object_Type='Boundary' and lower(Name)='link to other views' and Package_ID in "
                   "(select Package_ID from t_package where Name='NB Motivational Layer')").fetchall():
    c.execute("update t_object set Name='Link to Views of Stakeholders' where Object_ID=?", (b['Object_ID'],)); log.append(f'- motivation view: "{b["Name"]}" → "Link to Views of Stakeholders" [M1]')

h = obj("Name='Change History' and Stereotype='model document' and Note like '%Change History V0.1 to 0.2%'")
if 'V1.1.0' not in h['Note']:
    entry = N.join(['07.11.2026 Change History V1.0.0 to V1.1.0 (draft; review of R. Bossom, 09/2026):', '',
        'Landing Page:', 'Note that the NB Reference Architecture is a live document; navigation hint; link to GitHub issues', 'Glossary: abbreviations added', '',
        'Motivational Layer:', 'Boxes "Link to other Views" renamed "Link to Views of Stakeholders"', '',
        'Functional View:', 'Connector labels (IN/OUT) hidden in the diagram', 'Data flows renamed after their content (Request/Response pairs, flows read from data stores)',
        'Source and target in every data-flow description; inputs and outputs in every function description', 'Status of CA: produced by the Compliance assessment registry', '',
        'FRAME relationships (FRAME 5.3, MDG technology V1.3):', 'Role «adheres to» Agreement, Agreement «accepted by» Role; Actor «performs» Role; Business Expectation «defines» ITS Service', '', ''])
    c.execute('update t_object set Note=? where Object_ID=?', (entry + h['Note'], h['Object_ID'])); log.append('- change history: entry V1.0.0 → V1.1.0 (draft) [S3]')

open(rep, 'w', encoding='utf-8', newline='\n').write('# NB Reference Architecture – texts (review R. Bossom, groups A and B)\n\n' + '\n'.join(log) + '\n')
print('\n'.join(log))
if APPLY: c.commit(); print('APPLIED')
