"""Give FRAME diagrams the diagram type of the FRAME technology, so that Enterprise Architect opens the FRAME toolbox
(and with it the FRAME Quick Linker) automatically.

usage: 2026-11-06_diagram_type_FRAME.py model.qea report.md [--apply]
Diagram types of technologies that no longer exist in the model (FrameNext::Data Flow Diagram / Context Diagram /
User Need Diagram, FN_Diagram::FRAME NEXT Diagram) and the misspelt FRAME_Diagram::FRAME Diagram become
FRAME_Diagram::FRAME_Diagram (t_diagram.StyleEx MDGDgm). Other diagram types (requirements, ArchiMate, …) are kept.
"""
import sqlite3, sys, re
from collections import Counter
path, rep = sys.argv[1:3]; APPLY = '--apply' in sys.argv
NEW = 'FRAME_Diagram::FRAME_Diagram'
OLD = ('FrameNext::Data Flow Diagram', 'FrameNext::Context Diagram', 'FrameNext::User Need Diagram',
       'FN_Diagram::FRAME NEXT Diagram', 'FRAME_Diagram::FRAME Diagram')
c = sqlite3.connect(path)
pk = {r[0]: (r[1], r[2]) for r in c.execute('select Package_ID, Name, Parent_ID from t_package')}
def top(p):
    s = []
    while p in pk and pk[p][1] != 0: s.append(pk[p][0]); p = pk[p][1]
    return (list(reversed(s)) + [''])[0]
rows = []
for did, name, pid, st in c.execute('select Diagram_ID, Name, Package_ID, StyleEx from t_diagram').fetchall():
    m = re.search(r'MDGDgm=([^;]*);', st or '')
    if m and m.group(1) in OLD:
        rows.append((top(pid), name, m.group(1)))
        if APPLY:
            c.execute('update t_diagram set StyleEx=? where Diagram_ID=?', (st.replace(f'MDGDgm={m.group(1)};', f'MDGDgm={NEW};'), did))
cnt = Counter(r[2] for r in rows)
md = ['# Diagram type FRAME_Diagram', '', f'{len(rows)} diagrams changed to `{NEW}`: ' + ', '.join(f'{k} {v}×' for k, v in cnt.most_common()), '',
      '| View | Diagram | Former type |', '|---|---|---|'] + [f'| {a} | {b} | {t} |' for a, b, t in sorted(rows)]
open(rep, 'w', encoding='utf-8', newline='\n').write('\n'.join(md) + '\n')
print(md[2])
if APPLY:
    c.commit(); print('APPLIED')
