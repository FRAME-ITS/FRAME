# FRAME Toolsetup aligned with technology V1.3

Script: `tools/fixes/2026-11-06_toolsetup_V1.3.py`.

- stereotype class «Impacts» → «impacts»
- toolbox entry FRAME_Profile::impacts(UML::Association) → impacts
- new stereotype class «delivers value to» (copy of «use») with toolbox entry
- new stereotype class «triggers» (copy of «use») with toolbox entry
- rule added: «contains» FRAME_Application → FRAME_Datastore
- rule added: «contains» FRAME_Application → FRAME_Low_Level_Function
- rule added: «contains» FRAME_Application → FRAME_Physical_Data_Flow
- rule added: «contains» FRAME_Low_Level_Data_Flow → FRAME_Information_Object
- rule added: «defines» FRAME_Specification → FRAME_Requirement
- rule added: «delivers value to» FRAME_ITS_Service_Added_Value → FRAME_Stakeholder
- rule added: «triggers» FRAME_ITS_Business_Process → FRAME_ITS_Business_Process
- rule added: «triggers» FRAME_ITS_Service_Process → FRAME_ITS_Service_Process
- rule added: «use» FRAME_Component → FRAME_Physical_Data_Flow
- rule added: «use» FRAME_Terminator → FRAME_Physical_Data_Flow
- rule removed (not in V1.3): «defines» FRAME_ITS_Service_Added_Value → FRAME_Stakeholder

Rules in the package and not in V1.3: 4
- «None» FRAME_Datastore → FRAME_Information_Object
- «None» FRAME_Information_Object → FRAME_Information_Object
- «None» FRAME_Requirement → FRAME_Organisation
- «None» FRAME_Stakeholder → FRAME_Requirement

Rules in V1.3 and not in the package: 0
