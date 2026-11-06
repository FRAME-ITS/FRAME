# FRAME Toolsetup aligned with technology V1.3

Script: `tools/fixes/2026-11-06_toolsetup_V1.3.py`.

- stereotype class «Impacts» → «impacts»
- toolbox entry FRAME_Profile::impacts(UML::Association) → impacts
- new stereotype class «delivers» (copy of «use») with toolbox entry
- stereotype class «delivers»: «stereotype» xref added
- rule reversed: «accepted by» FRAME_Role → FRAME_Agreement  becomes  FRAME_Agreement → FRAME_Role
- rule reversed: «adheres to» FRAME_Agreement → FRAME_Role  becomes  FRAME_Role → FRAME_Agreement
- rule added: «delivers» FRAME_ITS_Service → FRAME_ITS_Service_Added_Value
- rule removed (not in V1.3): «delivered by» FRAME_ITS_Service → FRAME_ITS_Service_Added_Value
- rule removed (not in V1.3): «defines» FRAME_ITS_Service_Added_Value → FRAME_User_Need
- rule removed (not in V1.3): «defines» FRAME_ITS_Vision → FRAME_Requirement
- rule removed (not in V1.3): «defines» FRAME_Business_Expectation → FRAME_Mission_Statement
- 1 rule connectors: name set to the rule stereotype

Rules in the package and not in V1.3: 4
- «None» FRAME_Datastore → FRAME_Information_Object
- «None» FRAME_Information_Object → FRAME_Information_Object
- «None» FRAME_Requirement → FRAME_Organisation
- «None» FRAME_Stakeholder → FRAME_Requirement

Rules in V1.3 and not in the package: 0
