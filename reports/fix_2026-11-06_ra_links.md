# Reference architectures: UML links → FRAME relationships (V1.3)

Script: `tools/fixes/2026-11-06_ra_links_V1.3.py`; mappings decided by the git maintainer.

221 changes.

| RA | Link before | After | Count |
|---|---|---|---|
| C-ITS RA | Abstraction «» Actor → Stakeholder | «is Type of» | 6 |
| C-ITS RA | Abstraction «» User_Need → User_Need_Topic | «belongs to» | 10 |
| C-ITS RA | Abstraction «» User_Need_Service → User_Need_Topic | reverse, «belongs to» | 3 |
| C-ITS RA | Abstraction «» User_Need_Topic → User_Need | duplicate of an existing FRAME link – deleted | 1 |
| C-ITS RA | Abstraction «» User_Need_Topic → User_Need | reverse, «belongs to» | 44 |
| C-ITS RA | Aggregation «component of» High_Level_Function → Low_Level_Function | duplicate of an existing FRAME link – deleted | 1 |
| C-ITS RA | Aggregation «component of» High_Level_Function → Low_Level_Function | reverse, «component of» | 31 |
| C-ITS RA | Association «» Business_Expectation → Mission_Statement | «defines» | 1 |
| C-ITS RA | Realisation «» Actor → Role | reverse, «defines» | 1 |
| C-ITS RA | Usage «» Actor → Role | reverse, «defines» | 1 |
| C-ITS RA | Usage «» User_Need_Topic → User_Need | reverse, «belongs to» | 1 |
| NAP RA | Aggregation «component of» High_Level_Data_Flow → Low_Level_Data_Flow | duplicate of an existing FRAME link – deleted | 5 |
| NAP RA | Aggregation «component of» High_Level_Data_Flow → Low_Level_Data_Flow | reverse, «component of» | 5 |
| NAP RA | Aggregation «component of» User_Need → Low_Level_Function | «served by» | 5 |
| NAP RA | Association «» ITS_Vision → Mission_Statement | «associate» | 1 |
| NAP RA | Association «» Low_Level_Data_Flow → Data_Object | «contains» | 2 |
| NAP RA | Association «» Specification → Interface | reverse, «adheres to» | 2 |
| NAP RA | Realisation «» Business_Expectation → Mission_Statement | «defines» | 6 |
| NAP RA | Usage «Instantiate» ITS_Domain → ITS_Service | reverse, «has» | 1 |
| NAP RA | Usage «Instantiate» Specification → ITS_Service | reverse, «adheres to» | 3 |
| NAP RA | Usage «Instantiate» Stakeholder → ITS_Vision | «defines» | 1 |
| NAP element | Seamless EU-wide provision of data and services (NAP Reference Architecture/00 NAP Motivation Layer/Other Elements): stereotype FRAME_Vision → FRAME_ITS_Vision | 1 | 1 |
| National Body RA | Realisation «» Business_Expectation → Mission_Statement | «defines» | 5 |
| National Body RA | Usage «Instantiate» ITS_Domain → ITS_Service | reverse, «has» | 1 |
| National Body RA | Usage «Instantiate» Specification → ITS_Service | reverse, «adheres to» | 2 |
| Truckparking RA (SSTP) | Usage «» Actor → Role | reverse, «defines» | 5 |
| Truckparking RA (SSTP) | Usage «» Application → Component | «hosted by» | 1 |
| Truckparking RA (SSTP) | Usage «» Application → Interface | «defines» | 10 |
| Truckparking RA (SSTP) | Usage «» Application → Terminator | reverse, «defines» | 1 |
| Truckparking RA (SSTP) | Usage «» Component → Application | reverse, «hosted by» | 3 |
| eCall RA | Abstraction «» Actor → Terminator | «is Type of» | 6 |
| eCall RA | Abstraction «» Role → ITS_Service_Process | duplicate of an existing FRAME link – deleted | 8 |
| eCall RA | Abstraction «» Role → ITS_Service_Process | reverse, «defines» | 1 |
| eCall RA | Abstraction «» Stakeholder → Desired_Architecture_Goals | «has» | 4 |
| eCall RA | Association «» ITS_Service → User_Need | «defines» | 16 |
| eCall RA | Realisation «» Stakeholder → Requirement | «defines» | 13 |
| eCall RA | Usage «Call» ITS_Service → ITS_Service_Process | duplicate of an existing FRAME link – deleted | 1 |
| eCall RA | Usage «Call» ITS_Service → ITS_Service_Process | «defines» | 3 |
| eCall RA | Usage «Instantiate» Actor → Stakeholder | «is Type of» | 4 |
| eCall RA | Usage «Instantiate» Physical_Data_Flow → Interface | «use» | 4 |
| eCall RA | Usage «Instantiate» Stakeholder → Actor | reverse, «is Type of» | 1 |
