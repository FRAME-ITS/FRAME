# Changes after the NRA article comparison

Script: `tools/fixes/2026-11-06_article_alignment.py`; decided by the git maintainer.

- 33× Role «defines» Actor → Actor «performs» Role (reversed)
- Meta Model: Business_Expectation «defines» ITS_Service added
- Meta Model: ITS_Service «delivered by» ITS_Service_Added_Value added
- Meta Model: Terminator/ Subterminator «use» Physical Dataflow added
- Meta Model: Interface «defines» Requirement added
- Meta Model: Application «owned by» Role added
- NAP RA: Actor "NAP Content Consumer" merged into "Content Consumer" (links moved, duplicates removed, note kept)
- NAP RA: Actor "NAP Content Provider" merged into "Content Provider" (links moved, duplicates removed, note kept)
- NAP RA: Stakeholder "NAP" merged into "NAP Operator" (links moved, duplicates removed, note kept)
- NAP RA: "European Commision (EC)" → "European Commission (EC)"
- NAP RA: "Automatic provision of metadata vie machine to machine interface" → "Automatic provision of metadata via machine to machine interface"
- NAP RA: grouping specification "FRAME_Specification1" → "Content Consumer data retrieval specifications"

Kept: specification "Specification tbd" (NAP RA, marks interfaces whose standard is not yet chosen); empty "FRAME_Specification1" in the eCall motivation layer (eCall RA, not part of this clean-up).
