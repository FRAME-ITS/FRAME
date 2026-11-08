"""Align connector stereotypes with the FRAME technology V1.2 that is embedded in the model (t_document TECHNOLOGY).
V1.2 defines «component of» and «belongs to» (with a space); the older toolbox V1.0 in the repository used «componentof» and «belongsto».
usage: convert_v12.py model.qea [--apply]"""
import sqlite3, sys
APPLY = '--apply' in sys.argv
c = sqlite3.connect(sys.argv[1])
MAP = {'componentof': 'component of', 'belongsto': 'belongs to'}
for old, new in MAP.items():
    rows = c.execute("""select k.Connector_ID, k.Btm_Mid_Label, x.XrefID from t_connector k join t_xref x on x.Client=k.ea_guid
                        where x.Name='Stereotypes' and x.Description=?""", (f'@STEREO;Name={old};FQName=FRAME_Profile::{old};@ENDSTEREO;',)).fetchall()
    print(f'FRAME_Profile::{old:12} → FRAME_Profile::{new:13} {len(rows)}')
    if APPLY:
        for cid, lab, xid in rows:
            c.execute('update t_connector set Stereotype=?, Btm_Mid_Label=? where Connector_ID=?', (new, lab.replace(f'«{old}»', f'«{new}»') if lab else lab, cid))
            c.execute('update t_xref set Description=? where XrefID=?', (f'@STEREO;Name={new};FQName=FRAME_Profile::{new};@ENDSTEREO;', xid))
if APPLY:
    c.commit(); print('APPLIED', c.execute('pragma integrity_check').fetchone())
