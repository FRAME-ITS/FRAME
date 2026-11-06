# FRAME toolbox (MDG technology)

| File | Version | What it is |
|---|---|---|
| `FRAME_Technology_V1.2_embedded.xml` | V1.2 | The technology **embedded in `model/FRAME.qea`** (the one the model actually uses), extracted with `python tools/mdg.py --xml <file>`. Reference copy: it carries the profile, toolbox, diagram profile, tagged value types and RTF templates, but **not** the stereotype images, four of the five scripts, model views and model searches of the V1.0 file. |
| `FRAME_V1_MTS.xml` | V1.0 | Last published full technology file (with images and scripts). Outdated: uses `componentof` / `belongsto` instead of «component of» / «belongs to» and the V1.0 Quick Linker. |
| `FRAME_V1_MTS.mts`, `FRAME_Profile.xml`, `FRAME_Toolbox.xml`, `FRAME_Diagram.xml` | V1.0 | Sources from which `FRAME_V1_MTS.xml` was generated. |

Users who open `FRAME.qea` do **not** need to import a toolbox: the technology V1.2 is stored in the model.
The toolbox file is needed only for a new or XMI-imported project.

Open point (see the issue on the toolbox): generate a complete V1.2 technology file (Publish → Generate MDG Technology,
from the FRAME Toolsetup package and the `.mts` updated to V1.2, with images and scripts) and publish it with release 5.3;
fix the reversed Quick Linker rules and stereotype names listed in `reports/mdg_technology.md` first.
