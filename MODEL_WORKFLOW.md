# Working with the FRAME model (.qea) – SharePoint and git

The FRAME Architecture Tool is one Enterprise Architect model, `model/FRAME.qea` (an SQLite file).
The FRAME Maintainers edit it in **SharePoint**; this repository keeps its **history, change reports and releases**.

| Where | What | Who |
|---|---|---|
| SharePoint `20_Sources/Model/FRAME.qea` | working copy that the Maintainers edit | all Maintainers |
| git `model/FRAME.qea` (Git LFS) | history: one commit per SharePoint check-in, tags = releases | git maintainer |
| `export/` | readable YAML export of the model, regenerated with every model commit | automatic |
| `reports/` | convention check (`check.md`) and change reports between versions | automatic / git maintainer |
| GitHub Releases | published `.qea.zip`, toolbox and release notes for users | release manager |

## 1. Editing the model (all Maintainers – SharePoint)

1. In SharePoint, **Check out** `20_Sources/Model/FRAME.qea`. Only one person can have it checked out; everybody else sees who is working on it.
2. **Download** the file and work on the local copy in Enterprise Architect. Do not open the model directly in a OneDrive-synchronised folder – EA keeps the SQLite file open and synchronisation can corrupt it.
3. **Close Enterprise Architect**, upload the file back (same name) and **Check in** with a comment that says what changed and which issue it solves, e.g. `#91 Freight Transport added to the Context Diagram`.

One check-in should contain one logical change. Large changes are split into several check-ins.

## 2. Synchronising SharePoint → git (git maintainer)

```powershell
cd FRAME
git switch release/5.3.0          # the branch of the next release
python tools/sync_sharepoint.py status "<path to SharePoint FRAME.qea>"
python tools/sync_sharepoint.py import "<path to SharePoint FRAME.qea>" --author "Name <mail>" --message "<check-in comment>" --sp-version <version> --commit
git push
```

`import` copies the file to `model/FRAME.qea`, checks the SQLite integrity, regenerates `export/`, runs `tools/check.py`
and records the state in `model/SYNC.json`. With `--commit` the commit is made in the name of the person who checked the file in.
The script refuses to import when the git model has changes that were never exported to SharePoint.

## 3. Changes made in git (scripts, bulk fixes) → SharePoint

Only while the git maintainer has the file **checked out** in SharePoint:

1. `git lfs lock model/FRAME.qea`, make the change, commit (the pre-commit hook regenerates `export/`).
2. `python tools/sync_sharepoint.py export "<path to SharePoint FRAME.qea>"` – refused if the SharePoint file changed since the last synchronisation.
3. Check the file in on SharePoint, commit `model/SYNC.json`, `git lfs unlock model/FRAME.qea`.

## 4. Tools

| Tool | Purpose |
|---|---|
| `tools/export.py model/FRAME.qea export` | model → YAML, one file per package, plus diagrams, glossary and documentation templates |
| `tools/diff.py OLD.qea NEW.qea report.md` / `tools/diff.py --git v5.2.0 HEAD report.md` | change report by view: new/deleted objects, renames, description changes, connections, diagrams |
| `tools/check.py model/FRAME.qea reports/check.md [--strict]` | convention check (IN/OUT direction, «component of» part → whole, «served by», unused data flows, stereotype spelling, Context Diagram, …); each rule is linked to the related GitHub issue |
| `tools/sync_sharepoint.py` | SharePoint ↔ git synchronisation with conflict protection |
| `tools/hooks/` | pre-commit (re-export) and Git LFS hooks |
| `tools/ci/model-diff.yml` | GitHub Actions workflow: change report and check as a comment on every pull request that changes the model. Copy it to `.github/workflows/` to activate it. |

All tools are plain Python 3 (standard library only).

## 5. One-time setup (Windows)

```powershell
git lfs install                      # once per user
git clone https://github.com/FRAME-ITS/FRAME.git
cd FRAME
git config core.hooksPath tools/hooks
```

## 6. Branches, versions and releases

- `master` holds released versions, tagged `vMAJOR.MINOR.PATCH` (first tag in this scheme: `v5.2.0`).
- `release/<version>` holds the work on the next release; it is merged to `master` by a pull request.
- Levels of the Technical Change Decision Process decide the version step: Level 1–2 → patch, Level 3 → minor, Level 4–5 → major.
- Release: merge the pull request, tag, attach `FRAME_Architecture_Tool_V<version>.qea.zip`, the toolbox (`FRAME_V1_MTS.xml`) and the release notes (based on `tools/diff.py --git <previous tag> <new tag>`) to a GitHub Release, and copy the same files to SharePoint `40_Published`.
- `.qea` files are stored in Git LFS (free quota of the organisation: 10 GiB storage, 10 GiB transfer per month); a model version takes about 33 MB.
