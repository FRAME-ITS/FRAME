# FRAME toolbox (MDG technology)

| File | Version | What it is |
|---|---|---|
| `FRAME_Technology_V1.3.xml` | **V1.3** | **Corrected technology for release 5.3** – built from V1.2 by `tools/fixes/2026-11-06_mdg_technology_V1.3.py`; changes in `FRAME_Technology_V1.3_changes.md`. Import: *Specialize → Manage Technology* / *Import MDG Technology*, or into a model. |
| `FRAME_Technology_V1.2_embedded.xml` | V1.2 | The technology embedded in `model/FRAME.qea` before 5.3 (now replaced by V1.3) (extracted with `python tools/mdg.py --xml <file>`). Base of V1.3. |
| `FRAME_V1_MTS.xml` | V1.0 | Last published technology file. Outdated: `componentof` / `belongsto` instead of «component of» / «belongs to», V1.0 Quick Linker, four stereotype-migration scripts (FrameNext → FRAME_Profile) that are no longer needed. |
| `FRAME_V1_MTS.mts`, `FRAME_Profile.xml`, `FRAME_Toolbox.xml`, `FRAME_Diagram.xml` | V1.0 | Sources from which `FRAME_V1_MTS.xml` was generated in EA. |

What V1.3 changes against V1.2 (details in the changes file):
- Quick Linker rules of the function hierarchy («component of» LL function → HL function → functional area) and of the user-need
  hierarchy («belongs to» user need → topic → service → group) now point the same way as the model (part → whole).
- Rules added for patterns used throughout the FRAME Repository (sub-terminator, HL function in HL function, functional area in system,
  IN/OUT of System and functional areas).
- Motivation layer: Business Expectation «defines» Mission Statement (as in the FRAME Meta Model) and ITS Service «adheres to»
  Specification added – the NAP, National Body and C-ITS reference architectures had to draw these as plain UML links.
- Physical, functional and communication views (decided 2026-11-06): Application «contains» LL function / data store / physical
  data flow; LL data flow «contains» Information Object; Component / Terminator «use» Physical Data Flow (one link for both
  directions); new stereotype «triggers» for ITS Service Process → Process and ITS Business Process → Process;
  Specification «defines» Requirement; new stereotype «delivers value to» for ITS Service Added Value → Stakeholder (was «defines»).
- NRA article (decided 2026-11-06): Business Expectation «defines» ITS Service; Application «owned by» Role; new stereotype
  «performs» – Actor «performs» Role replaces Role «defines» Actor; toolbox labels *Sub-system* (FRAME_Component) and
  *Module* (FRAME_Application), as in D4.2 and the documentation (stereotype names unchanged).
- Quick Linker references to undefined names fixed (Component of, Defines, instant of, associated); «Impacts» → «impacts»,
  «deliverd by» → «delivered by» (neither is used by a connector in the model).
- For the core FRAME Repository stereotypes (functional area, functions, data flows, terminator, data store, system, user needs)
  the Quick Linker offers only the FRAME relationships (`_HideUmlLinks`); plain UML links can still be drawn from the toolbox.
  The FRAME relationships appear when the FRAME toolbox is active (Quick Linker option *Filter to Toolbox*). Diagrams of type
  `FRAME_Diagram` open the FRAME toolbox automatically – the diagram type now refers to it as `FRAME::FRAME_Toolbox`; all FRAME
  diagrams of the model have this type (`tools/fixes/2026-11-06_diagram_type_FRAME.py`).
- The start-page images of V1.0 included, so a new project gets them too.

`python tools/mdg.py model/FRAME.qea reports/mdg_technology_V1.3.md --tech drafts/latest/toolbox/FRAME_Technology_V1.3.xml`
compares the rules with the model: no rule points against the model.

Users who open `FRAME.qea` do not need to import a toolbox – V1.3 is stored in the model. The file is needed for a
new or XMI-imported project.
