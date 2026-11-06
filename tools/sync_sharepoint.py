"""Keep the SharePoint working copy of the FRAME model and the git repository in step.

The FRAME Maintainers edit the model in SharePoint (20_Sources/Model/FRAME.qea, locked with Check out).
The git repository keeps the history. This script moves the model between the two and records the
state of the last synchronisation in model/SYNC.json, so that a change made on one side is never
overwritten by the other.

Usage (run in the repository root):
  python tools/sync_sharepoint.py status  <SharePoint FRAME.qea>
  python tools/sync_sharepoint.py import  <SharePoint FRAME.qea> --author "Name <mail>" --message "check-in comment"
                                          [--sp-version 12.0] [--commit]
  python tools/sync_sharepoint.py export  <SharePoint FRAME.qea> [--sp-version 13.0]

import  SharePoint -> git. Copies the file to model/FRAME.qea, re-exports export/, runs the check and
        updates SYNC.json. With --commit it also commits (author = the person who checked the file in).
        Refused if model/FRAME.qea has commits that were never exported to SharePoint.
export  git -> SharePoint. Only when you have the file checked out in SharePoint. Refused if the
        SharePoint file changed since the last synchronisation (import it first).
<SharePoint FRAME.qea> is the file in your OneDrive-synchronised copy of the library, or a downloaded copy.
"""
import sys, os, json, hashlib, shutil, sqlite3, subprocess, datetime, argparse

MODEL = 'model/FRAME.qea'
SYNC = 'model/SYNC.json'


def sha(path):
    h = hashlib.sha256()
    with open(path, 'rb') as f:
        for b in iter(lambda: f.read(1 << 20), b''):
            h.update(b)
    return h.hexdigest()


def integrity(path):
    c = sqlite3.connect(f'file:{path}?mode=ro', uri=True)
    res = c.execute('pragma quick_check').fetchone()[0]
    n = c.execute('select count(*) from t_object').fetchone()[0]
    c.close()
    if res != 'ok':
        sys.exit(f'{path}: SQLite integrity check failed ({res}) – do not synchronise, ask the last editor')
    return n


def load_sync():
    return json.load(open(SYNC, encoding='utf-8')) if os.path.exists(SYNC) else {}


def save_sync(d):
    with open(SYNC, 'w', encoding='utf-8', newline='\n') as f:
        json.dump(d, f, indent=2, ensure_ascii=False); f.write('\n')


def now():
    return datetime.datetime.now().astimezone().isoformat(timespec='seconds')


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('action', choices=['status', 'import', 'export'])
    ap.add_argument('sharepoint')
    ap.add_argument('--author'); ap.add_argument('--message'); ap.add_argument('--sp-version')
    ap.add_argument('--commit', action='store_true')
    a = ap.parse_args()
    if not os.path.isdir('model') or not os.path.isdir('tools'):
        sys.exit('run in the repository root')
    s = load_sync()
    sp_hash = sha(a.sharepoint) if os.path.exists(a.sharepoint) else None
    git_hash = sha(MODEL) if os.path.exists(MODEL) else None
    last = s.get('sha256')
    sp_changed = sp_hash != last
    git_changed = git_hash != last
    if a.action == 'status':
        if not last:
            print('no synchronisation recorded yet (model/SYNC.json missing) – the first import starts the record'); return
        print(f'last sync      : {s.get("synced_at", "never")} ({s.get("direction", "-")}, SharePoint version {s.get("sharepoint_version", "?")})')
        print(f'SharePoint file: {"CHANGED since last sync" if sp_changed else "unchanged"}')
        print(f'git model      : {"CHANGED since last sync" if git_changed else "unchanged"}')
        if sp_changed and git_changed and sp_hash != git_hash:
            print('!! both sides changed – resolve manually (compare with tools/diff.py) before synchronising')
        return
    if a.action == 'import':
        if not sp_changed:
            print('SharePoint file unchanged since the last synchronisation – nothing to import'); return
        if last and git_changed:
            sys.exit('model/FRAME.qea has changes that were not exported to SharePoint – export them first or reconcile with tools/diff.py')
        n = integrity(a.sharepoint)
        shutil.copyfile(a.sharepoint, MODEL)
        subprocess.run([sys.executable, 'tools/export.py', MODEL, 'export'], check=True)
        subprocess.run([sys.executable, 'tools/check.py', MODEL, 'reports/check.md'], check=False)
        s.update(sha256=sp_hash, size=os.path.getsize(MODEL), elements=n, direction='SharePoint -> git', synced_at=now(),
                 sharepoint_version=a.sp_version or s.get('sharepoint_version'), author=a.author, message=a.message)
        save_sync(s)
        print(f'imported {a.sharepoint} ({n} elements)')
        if a.commit:
            if not (a.author and a.message):
                sys.exit('--commit needs --author and --message (take them from the SharePoint check-in)')
            subprocess.run(['git', 'add', MODEL, SYNC, 'export', 'reports/check.md'], check=True)
            subprocess.run(['git', 'commit', '--author', a.author, '-m', a.message,
                            '-m', f'Imported from SharePoint (version {a.sp_version or "?"}).'], check=True)
        else:
            print('next: git add model export reports && git commit --author "<editor>" -m "<check-in comment>"')
        return
    if a.action == 'export':
        if sp_changed:
            sys.exit('the SharePoint file changed since the last synchronisation – import it first (someone else worked on it)')
        if not git_changed:
            print('git model unchanged since the last synchronisation – nothing to export'); return
        integrity(MODEL)
        shutil.copyfile(MODEL, a.sharepoint)
        s.update(sha256=git_hash, size=os.path.getsize(MODEL), direction='git -> SharePoint', synced_at=now(),
                 sharepoint_version=a.sp_version or s.get('sharepoint_version'))
        save_sync(s)
        print(f'exported to {a.sharepoint} – check the file in on SharePoint, then commit model/SYNC.json')


if __name__ == '__main__':
    main()
