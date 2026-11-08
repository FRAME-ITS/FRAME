# FRAME Toolsetup aligned with technology V1.3

Script: `tools/fixes/2026-11-06_toolsetup_V1.3.py`.

- stereotype class «Impacts» → «impacts»
- toolbox entry FRAME_Profile::impacts(UML::Association) → impacts
- new stereotype class «performs» (copy of «use») with toolbox entry
- rule added: «defines» FRAME_Business_Expectation → FRAME_ITS_Service
- rule added: «owned by» FRAME_Application → FRAME_Role
- rule added: «performs» FRAME_Actor → FRAME_Role
- rule removed (not in V1.3): «defines» FRAME_Role → FRAME_Actor
- toolbox label FRAME_Component: "Component" → "Sub-system"
- toolbox label FRAME_Application: "Application" → "Module"

Rules in the package and not in V1.3: 4
- «None» FRAME_Datastore → FRAME_Information_Object
- «None» FRAME_Information_Object → FRAME_Information_Object
- «None» FRAME_Requirement → FRAME_Organisation
- «None» FRAME_Stakeholder → FRAME_Requirement

Rules in V1.3 and not in the package: 0
