# FRAME Toolsetup aligned with technology V1.3

Script: `tools/fixes/2026-11-06_toolsetup_V1.3.py`.

- stereotype class «Impacts» → «impacts»
- toolbox entry FRAME_Profile::impacts(UML::Association) → impacts
- new stereotype class «implements» (copy of «use») with toolbox entry
- rule added: «adheres to» FRAME_Terminator → FRAME_Agreement
- rule added: «defines» FRAME_Specification → FRAME_Agreement
- rule added: «implements» FRAME_Actor → FRAME_Desired_Architecture_Goals
- rule added: «use» FRAME_Agreement → FRAME_Specification

Rules in the package and not in V1.3: 4
- «None» FRAME_Datastore → FRAME_Information_Object
- «None» FRAME_Information_Object → FRAME_Information_Object
- «None» FRAME_Requirement → FRAME_Organisation
- «None» FRAME_Stakeholder → FRAME_Requirement

Rules in V1.3 and not in the package: 0
