"""Move connector stereotypes from the legacy FrameNext profile (and names not defined in the toolbox) to FRAME_Profile.
Updates t_connector.Stereotype, the stereotype record in t_xref and the stereotype text in the connector label.
usage: convert_profile.py model.qea [--apply]"""
import sqlite3, sys
APPLY = '--apply' in sys.argv
c = sqlite3.connect(sys.argv[1])
MAP = {'FrameNext::Componentof': 'componentof', 'FRAME_Profile::component of': 'componentof',
       'FrameNext::Servedby': 'served by', 'FRAME_Profile::belongs to': 'belongsto',
       'FrameNext::IN': 'IN', 'FrameNext::OUT': 'OUT'}
total = 0
for fq, new in MAP.items():
    old = fq.split('::')[1]
    rows = c.execute("""select k.Connector_ID, k.Stereotype, k.Btm_Mid_Label, x.XrefID from t_connector k join t_xref x on x.Client = k.ea_guid
                        where x.Name='Stereotypes' and x.Description = ?""", (f'@STEREO;Name={old};FQName={fq};@ENDSTEREO;',)).fetchall()
    print(f'{fq:32} → FRAME_Profile::{new:12} {len(rows)}')
    total += len(rows)
    if APPLY:
        for cid, st, lab, xid in rows:
            lab2 = lab.replace(f'«{old}»', f'«{new}»') if lab else lab
            c.execute('update t_connector set Stereotype=?, Btm_Mid_Label=? where Connector_ID=?', (new, lab2, cid))
            c.execute('update t_xref set Description=? where XrefID=?', (f'@STEREO;Name={new};FQName=FRAME_Profile::{new};@ENDSTEREO;', xid))
print('total', total)
if APPLY:
    c.commit(); print('APPLIED')
