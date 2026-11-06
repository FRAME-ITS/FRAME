# MDG technology embedded in FRAME.qea

Technology **FRAME** – FRAME Architecture V1.2; profile FRAME_Profile defines 59 stereotypes.

## Quick Linker rules vs. use in the model

For each rule (source → target) the number of connectors drawn in that direction and in the opposite direction.

| Connector | Source | Target | in the model | opposite direction |
|---|---|---|---|---|
| «Component of» | Functional_Area | Low_Level_Function | 1 | 116 ⚠ |
| «Defines» | Application | Information_Object | 0 | 0 |
| «Defines» | Application | Interface | 0 | 0 |
| «Defines» | Functionality | Application | 0 | 0 |
| «Defines» | Functionality | Component | 0 | 0 |
| «Defines» | ITS_Service | ITS_Business_Process | 1 | 0 |
| «Defines» | ITS_Service | ITS_Service_Process | 7 | 0 |
| «Defines» | ITS_Service | User_Need | 59 | 0 |
| «Defines» | ITS_Service_Added_Value | User_Need | 1 | 0 |
| «Defines» | ITS_Service_Process | Functionality | 0 | 0 |
| «Defines» | ITS_Service_Process | Role | 13 | 0 |
| «Defines» | ITS_Vision | ITS_Service | 0 | 0 |
| «Defines» | ITS_Vision | User_Need | 0 | 0 |
| «Defines» | Low_Level_Data_Flow | Functionality | 0 | 0 |
| «Defines» | Low_Level_Function | Functionality | 0 | 0 |
| «Defines» | Mission_Statement | ITS_Service | 16 | 0 |
| «Defines» | Mission_Statement | User_Need | 0 | 0 |
| «Defines» | Role | Actor | 26 | 0 |
| «Defines» | Role | Organisation | 1 | 0 |
| «Defines» | Role | User_Need | 0 | 0 |
| «Defines» | Terminator | Application | 0 | 0 |
| «Defines» | User_Need | Functionality | 0 | 0 |
| «IN» | Datastore | Low_Level_Data_Flow | 81 | 1 |
| «IN» | Functional_Area | High_Level_Data_Flow | 196 | 0 |
| «IN» | High_Level_Function | High_Level_Data_Flow | 239 | 0 |
| «IN» | High_Level_Function | Low_Level_Data_Flow | 1430 | 11 |
| «IN» | Low_Level_Function | Low_Level_Data_Flow | 1645 | 7 |
| «IN» | System | Low_Level_Data_Flow | 1 | 0 |
| «IN» | TDF_HighLevelFunction | Terminator | 0 | 0 |
| «IN» | Terminator | High_Level_Data_Flow | 180 | 0 |
| «IN» | Terminator | Low_Level_Data_Flow | 428 | 1 |
| «Impacts» | High_Level_Function | Functional_Area | 0 | 0 |
| «Impacts» | Low_Level_Function | Functional_Area | 0 | 0 |
| «OUT» | High_Level_Data_Flow | Functional_Area | 144 | 0 |
| «OUT» | High_Level_Data_Flow | High_Level_Function | 213 | 0 |
| «OUT» | High_Level_Data_Flow | Terminator | 143 | 0 |
| «OUT» | Low_Level_Data_Flow | Datastore | 81 | 1 |
| «OUT» | Low_Level_Data_Flow | High_Level_Function | 450 | 1 |
| «OUT» | Low_Level_Data_Flow | Low_Level_Function | 1734 | 7 |
| «OUT» | Low_Level_Data_Flow | System | 1 | 0 |
| «OUT» | Low_Level_Data_Flow | Terminator | 346 | 1 |
| «OUT» | Terminator | TDF_HighLevelFunction | 0 | 0 |
| «accepted by» | Role | Agreement | 15 | 0 |
| «adheres to» | Agreement | Role | 33 | 0 |
| «adheres to» | Application | Specification | 4 | 0 |
| «adheres to» | Component | Specification | 7 | 0 |
| «adheres to» | Datastore | Specification | 1 | 0 |
| «adheres to» | ITS_Service_Process | Specification | 10 | 0 |
| «adheres to» | Information_Object | Specification | 16 | 0 |
| «adheres to» | Interface | Specification | 22 | 0 |
| «adheres to» | Low_Level_Data_Flow | Specification | 0 | 0 |
| «adheres to» | Low_Level_Function | Specification | 5 | 0 |
| «adheres to» | Physical_Data_Flow | Specification | 0 | 0 |
| «adheres to» | System | Specification | 1 | 0 |
| «associate» | ITS_Vision | Mission_Statement | 2 | 0 |
| «associate» | Mission_Statement | ITS_Vision | 0 | 2 ⚠ |
| «associated» | Role | Component | 0 | 0 |
| «belongs to» | User_Need_Group | User_Need_Service | 4 | 30 ⚠ |
| «belongs to» | User_Need_Service | User_Need_Topic | 6 | 118 ⚠ |
| «belongs to» | User_Need_Topic | User_Need | 39 | 606 ⚠ |
| «component of» | Functional_Area | High_Level_Function | 1 | 61 ⚠ |
| «component of» | High_Level_Data_Flow | High_Level_Data_Flow | 448 | 448 |
| «component of» | High_Level_Function | Low_Level_Function | 33 | 315 ⚠ |
| «component of» | Low_Level_Data_Flow | High_Level_Data_Flow | 1522 | 10 |
| «contains» | Information_Object | Data_Object | 16 | 0 |
| «contains» | Low_Level_Data_Flow | Data_Object | 1 | 0 |
| «contains» | Physical_Data_Flow | Information_Object | 26 | 0 |
| «defines» | Actor | Requirement | 0 | 0 |
| «defines» | Agreement | Requirement | 0 | 0 |
| «defines» | Application | Requirement | 0 | 0 |
| «defines» | Business_Expectation | Requirement | 0 | 0 |
| «defines» | Component | Requirement | 0 | 0 |
| «defines» | Datastore | Requirement | 0 | 0 |
| «defines» | Desired_Architecture_Goals | Requirement | 0 | 0 |
| «defines» | ITS_Business_Process | Requirement | 0 | 0 |
| «defines» | ITS_Domain | Requirement | 0 | 0 |
| «defines» | ITS_Service | Requirement | 0 | 0 |
| «defines» | ITS_Service_Added_Value | Requirement | 0 | 0 |
| «defines» | ITS_Service_Added_Value | Stakeholder | 50 | 0 |
| «defines» | ITS_Service_Process | Requirement | 0 | 0 |
| «defines» | ITS_Vision | Requirement | 0 | 0 |
| «defines» | Information_Object | Requirement | 0 | 0 |
| «defines» | Interface | Requirement | 0 | 0 |
| «defines» | Low_Level_Data_Flow | Requirement | 0 | 0 |
| «defines» | Low_Level_Function | Requirement | 0 | 0 |
| «defines» | Mission_Statement | Requirement | 0 | 0 |
| «defines» | Organisation | Requirement | 0 | 0 |
| «defines» | Physical_Data_Flow | Requirement | 0 | 0 |
| «defines» | Role | Requirement | 0 | 0 |
| «defines» | Stakeholder | ITS_Vision | 1 | 0 |
| «defines» | Stakeholder | Requirement | 0 | 0 |
| «defines» | System | Requirement | 0 | 0 |
| «defines» | Terminator | Requirement | 0 | 0 |
| «defines» | User_Need | Requirement | 0 | 0 |
| «defines» | User_Need_Topic | Requirement | 0 | 0 |
| «deliverd by» | ITS_Service | ITS_Service_Added_Value | 0 | 0 |
| «fulfilled by» | Requirement | Actor | 0 | 0 |
| «fulfilled by» | Requirement | Agreement | 1 | 0 |
| «fulfilled by» | Requirement | Application | 23 | 0 |
| «fulfilled by» | Requirement | Business_Expectation | 0 | 0 |
| «fulfilled by» | Requirement | Component | 8 | 0 |
| «fulfilled by» | Requirement | Datastore | 0 | 0 |
| «fulfilled by» | Requirement | Desired_Architecture_Goals | 0 | 0 |
| «fulfilled by» | Requirement | ITS_Business_Process | 0 | 0 |
| «fulfilled by» | Requirement | ITS_Domain | 0 | 0 |
| «fulfilled by» | Requirement | ITS_Service | 0 | 0 |
| «fulfilled by» | Requirement | ITS_Service_Added_Value | 0 | 0 |
| «fulfilled by» | Requirement | ITS_Service_Process | 0 | 0 |
| «fulfilled by» | Requirement | ITS_Vision | 0 | 0 |
| «fulfilled by» | Requirement | Information_Object | 0 | 0 |
| «fulfilled by» | Requirement | Interface | 8 | 0 |
| «fulfilled by» | Requirement | Low_Level_Data_Flow | 0 | 0 |
| «fulfilled by» | Requirement | Low_Level_Function | 5 | 0 |
| «fulfilled by» | Requirement | Mission_Statement | 0 | 0 |
| «fulfilled by» | Requirement | Organisation | 0 | 0 |
| «fulfilled by» | Requirement | Physical_Data_Flow | 0 | 0 |
| «fulfilled by» | Requirement | Role | 0 | 0 |
| «fulfilled by» | Requirement | System | 0 | 0 |
| «fulfilled by» | Requirement | Terminator | 0 | 0 |
| «fulfilled by» | Requirement | User_Need | 0 | 0 |
| «fulfilled by» | Stakeholder | Requirement | 6 | 0 |
| «has» | ITS_Service | ITS_Domain | 2 | 0 |
| «has» | Organisation | ITS_Business_Process | 1 | 0 |
| «has» | Stakeholder | Business_Expectation | 13 | 0 |
| «has» | Stakeholder | Desired_Architecture_Goals | 10 | 0 |
| «hosted by» | Application | Component | 9 | 0 |
| «impacts» | Low_Level_Function | High_Level_Function | 0 | 0 |
| «instant of» | Stakeholder | Organisation | 0 | 0 |
| «is Type of» | Actor | Stakeholder | 18 | 0 |
| «is Type of» | Actor | Terminator | 6 | 0 |
| «is Type of» | Datastore | Component | 1 | 0 |
| «is Type of» | Terminator | Terminator | 1 | 1 |
| «served by» | ITS_Service_Process | Low_Level_Function | 45 | 0 |
| «served by» | Low_Level_Data_Flow | Physical_Data_Flow | 60 | 0 |
| «served by» | User_Need | Low_Level_Function | 1780 | 0 |
| «stored in» | Information_Object | Datastore | 3 | 0 |
| «use» | Interface | Information_Object | 12 | 0 |
| «use» | Physical_Data_Flow | Interface | 18 | 0 |

## Connector stereotypes used in the model but not defined in the technology

- «belongsto» 1×
