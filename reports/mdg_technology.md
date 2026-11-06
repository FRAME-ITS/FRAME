# MDG technology embedded in FRAME.qea compared with FRAME.qea

Technology **FRAME** – FRAME Architecture V1.3; profile FRAME_Profile defines 62 stereotypes.

## Quick Linker rules vs. use in the model

For each rule (source → target) the number of connectors drawn in that direction and in the opposite direction.

| Connector | Source | Target | in the model | opposite direction |
|---|---|---|---|---|
| «IN» | Datastore | Low_Level_Data_Flow | 82 | 0 |
| «IN» | Functional_Area | High_Level_Data_Flow | 196 | 0 |
| «IN» | Functional_Area | Low_Level_Data_Flow | 15 | 0 |
| «IN» | High_Level_Function | High_Level_Data_Flow | 239 | 0 |
| «IN» | High_Level_Function | Low_Level_Data_Flow | 1431 | 0 |
| «IN» | Low_Level_Function | Low_Level_Data_Flow | 1652 | 0 |
| «IN» | System | High_Level_Data_Flow | 44 | 0 |
| «IN» | System | Low_Level_Data_Flow | 1 | 0 |
| «IN» | TDF_HighLevelFunction | Terminator | 0 | 0 |
| «IN» | Terminator | High_Level_Data_Flow | 180 | 0 |
| «IN» | Terminator | Low_Level_Data_Flow | 429 | 0 |
| «OUT» | High_Level_Data_Flow | Functional_Area | 144 | 0 |
| «OUT» | High_Level_Data_Flow | High_Level_Function | 213 | 0 |
| «OUT» | High_Level_Data_Flow | System | 20 | 0 |
| «OUT» | High_Level_Data_Flow | Terminator | 143 | 0 |
| «OUT» | Low_Level_Data_Flow | Datastore | 82 | 0 |
| «OUT» | Low_Level_Data_Flow | Functional_Area | 11 | 0 |
| «OUT» | Low_Level_Data_Flow | High_Level_Function | 461 | 0 |
| «OUT» | Low_Level_Data_Flow | Low_Level_Function | 1741 | 0 |
| «OUT» | Low_Level_Data_Flow | System | 1 | 0 |
| «OUT» | Low_Level_Data_Flow | Terminator | 347 | 0 |
| «OUT» | Terminator | TDF_HighLevelFunction | 0 | 0 |
| «accepted by» | Role | Agreement | 15 | 0 |
| «adheres to» | Agreement | Role | 33 | 0 |
| «adheres to» | Application | Specification | 4 | 0 |
| «adheres to» | Component | Specification | 7 | 0 |
| «adheres to» | Datastore | Specification | 1 | 0 |
| «adheres to» | ITS_Service | Specification | 5 | 0 |
| «adheres to» | ITS_Service_Process | Specification | 10 | 0 |
| «adheres to» | Information_Object | Specification | 16 | 0 |
| «adheres to» | Interface | Specification | 24 | 0 |
| «adheres to» | Low_Level_Data_Flow | Specification | 0 | 0 |
| «adheres to» | Low_Level_Function | Specification | 5 | 0 |
| «adheres to» | Physical_Data_Flow | Specification | 0 | 0 |
| «adheres to» | System | Specification | 1 | 0 |
| «adheres to» | Terminator | Agreement | 2 | 0 |
| «associate» | ITS_Vision | Mission_Statement | 3 | 0 |
| «associate» | Role | Component | 0 | 0 |
| «belongs to» | User_Need | User_Need_Topic | 662 | 39 |
| «belongs to» | User_Need_Service | User_Need_Group | 31 | 3 |
| «belongs to» | User_Need_Topic | User_Need_Service | 122 | 5 |
| «component of» | Functional_Area | System | 9 | 0 |
| «component of» | High_Level_Data_Flow | High_Level_Data_Flow | 448 | 448 |
| «component of» | High_Level_Function | Functional_Area | 62 | 0 |
| «component of» | High_Level_Function | High_Level_Function | 16 | 16 |
| «component of» | Low_Level_Data_Flow | High_Level_Data_Flow | 1530 | 0 |
| «component of» | Low_Level_Function | Functional_Area | 117 | 0 |
| «component of» | Low_Level_Function | High_Level_Function | 347 | 0 |
| «component of» | Terminator | Terminator | 69 | 69 |
| «contains» | Application | Datastore | 8 | 0 |
| «contains» | Application | Low_Level_Function | 39 | 0 |
| «contains» | Application | Physical_Data_Flow | 23 | 0 |
| «contains» | Information_Object | Data_Object | 16 | 0 |
| «contains» | Low_Level_Data_Flow | Data_Object | 4 | 0 |
| «contains» | Low_Level_Data_Flow | Information_Object | 13 | 0 |
| «contains» | Physical_Data_Flow | Information_Object | 26 | 0 |
| «defines» | Actor | Requirement | 0 | 0 |
| «defines» | Agreement | Requirement | 0 | 0 |
| «defines» | Application | Information_Object | 0 | 0 |
| «defines» | Application | Interface | 10 | 0 |
| «defines» | Application | Requirement | 0 | 0 |
| «defines» | Business_Expectation | Mission_Statement | 13 | 0 |
| «defines» | Business_Expectation | Requirement | 0 | 0 |
| «defines» | Component | Requirement | 0 | 0 |
| «defines» | Datastore | Requirement | 0 | 0 |
| «defines» | Desired_Architecture_Goals | Requirement | 0 | 0 |
| «defines» | Functionality | Application | 0 | 0 |
| «defines» | Functionality | Component | 0 | 0 |
| «defines» | ITS_Business_Process | Requirement | 0 | 0 |
| «defines» | ITS_Domain | Requirement | 0 | 0 |
| «defines» | ITS_Service | ITS_Business_Process | 1 | 0 |
| «defines» | ITS_Service | ITS_Service_Process | 10 | 0 |
| «defines» | ITS_Service | Requirement | 1 | 0 |
| «defines» | ITS_Service | User_Need | 75 | 0 |
| «defines» | ITS_Service_Added_Value | Requirement | 0 | 0 |
| «defines» | ITS_Service_Added_Value | User_Need | 1 | 0 |
| «defines» | ITS_Service_Process | Functionality | 0 | 0 |
| «defines» | ITS_Service_Process | Requirement | 0 | 0 |
| «defines» | ITS_Service_Process | Role | 14 | 0 |
| «defines» | ITS_Vision | ITS_Service | 0 | 0 |
| «defines» | ITS_Vision | Requirement | 1 | 0 |
| «defines» | ITS_Vision | User_Need | 0 | 0 |
| «defines» | Information_Object | Requirement | 0 | 0 |
| «defines» | Interface | Requirement | 0 | 0 |
| «defines» | Low_Level_Data_Flow | Functionality | 0 | 0 |
| «defines» | Low_Level_Data_Flow | Requirement | 0 | 0 |
| «defines» | Low_Level_Function | Functionality | 0 | 0 |
| «defines» | Low_Level_Function | Requirement | 0 | 0 |
| «defines» | Mission_Statement | ITS_Service | 16 | 0 |
| «defines» | Mission_Statement | Requirement | 0 | 0 |
| «defines» | Mission_Statement | User_Need | 0 | 0 |
| «defines» | Organisation | Requirement | 0 | 0 |
| «defines» | Physical_Data_Flow | Requirement | 0 | 0 |
| «defines» | Role | Actor | 33 | 0 |
| «defines» | Role | Organisation | 1 | 0 |
| «defines» | Role | Requirement | 0 | 0 |
| «defines» | Role | User_Need | 0 | 0 |
| «defines» | Specification | Agreement | 1 | 0 |
| «defines» | Specification | Requirement | 7 | 0 |
| «defines» | Stakeholder | ITS_Vision | 2 | 0 |
| «defines» | Stakeholder | Requirement | 13 | 0 |
| «defines» | System | Requirement | 0 | 0 |
| «defines» | Terminator | Application | 1 | 0 |
| «defines» | Terminator | Requirement | 0 | 0 |
| «defines» | User_Need | Functionality | 0 | 0 |
| «defines» | User_Need | Requirement | 1 | 0 |
| «defines» | User_Need_Topic | Requirement | 0 | 0 |
| «delivered by» | ITS_Service | ITS_Service_Added_Value | 0 | 0 |
| «delivers value to» | ITS_Service_Added_Value | Stakeholder | 52 | 0 |
| «fulfilled by» | Requirement | Actor | 0 | 0 |
| «fulfilled by» | Requirement | Agreement | 1 | 0 |
| «fulfilled by» | Requirement | Application | 24 | 0 |
| «fulfilled by» | Requirement | Business_Expectation | 0 | 0 |
| «fulfilled by» | Requirement | Component | 9 | 0 |
| «fulfilled by» | Requirement | Datastore | 0 | 0 |
| «fulfilled by» | Requirement | Desired_Architecture_Goals | 0 | 0 |
| «fulfilled by» | Requirement | ITS_Business_Process | 0 | 0 |
| «fulfilled by» | Requirement | ITS_Domain | 0 | 0 |
| «fulfilled by» | Requirement | ITS_Service | 0 | 0 |
| «fulfilled by» | Requirement | ITS_Service_Added_Value | 0 | 0 |
| «fulfilled by» | Requirement | ITS_Service_Process | 0 | 0 |
| «fulfilled by» | Requirement | ITS_Vision | 0 | 0 |
| «fulfilled by» | Requirement | Information_Object | 0 | 0 |
| «fulfilled by» | Requirement | Interface | 9 | 0 |
| «fulfilled by» | Requirement | Low_Level_Data_Flow | 0 | 0 |
| «fulfilled by» | Requirement | Low_Level_Function | 6 | 0 |
| «fulfilled by» | Requirement | Mission_Statement | 0 | 0 |
| «fulfilled by» | Requirement | Organisation | 0 | 0 |
| «fulfilled by» | Requirement | Physical_Data_Flow | 0 | 0 |
| «fulfilled by» | Requirement | Role | 0 | 0 |
| «fulfilled by» | Requirement | System | 1 | 0 |
| «fulfilled by» | Requirement | Terminator | 1 | 0 |
| «fulfilled by» | Requirement | User_Need | 0 | 0 |
| «fulfilled by» | Stakeholder | Requirement | 6 | 0 |
| «has» | ITS_Service | ITS_Domain | 4 | 0 |
| «has» | Organisation | ITS_Business_Process | 1 | 0 |
| «has» | Stakeholder | Business_Expectation | 13 | 0 |
| «has» | Stakeholder | Desired_Architecture_Goals | 14 | 0 |
| «hosted by» | Application | Component | 13 | 0 |
| «impacts» | High_Level_Function | Functional_Area | 0 | 0 |
| «impacts» | Low_Level_Function | Functional_Area | 0 | 0 |
| «impacts» | Low_Level_Function | High_Level_Function | 0 | 0 |
| «implements» | Actor | Desired_Architecture_Goals | 3 | 0 |
| «instants of» | Stakeholder | Organisation | 0 | 0 |
| «is Type of» | Actor | Stakeholder | 29 | 0 |
| «is Type of» | Actor | Terminator | 12 | 0 |
| «is Type of» | Datastore | Component | 1 | 0 |
| «is Type of» | Terminator | Terminator | 1 | 1 |
| «served by» | ITS_Service_Process | Low_Level_Function | 45 | 0 |
| «served by» | Low_Level_Data_Flow | Physical_Data_Flow | 60 | 0 |
| «served by» | User_Need | Low_Level_Function | 1785 | 0 |
| «stored in» | Information_Object | Datastore | 3 | 0 |
| «triggers» | ITS_Business_Process | ITS_Business_Process | 23 | 23 |
| «triggers» | ITS_Service_Process | ITS_Service_Process | 69 | 69 |
| «use» | Agreement | Specification | 4 | 0 |
| «use» | Component | Physical_Data_Flow | 25 | 0 |
| «use» | Interface | Information_Object | 12 | 0 |
| «use» | Physical_Data_Flow | Interface | 22 | 0 |
| «use» | Terminator | Physical_Data_Flow | 12 | 0 |

## Connector stereotypes used in the model but not defined in the technology

none
