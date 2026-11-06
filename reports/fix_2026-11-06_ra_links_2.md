# Reference architectures, second pass: new V1.3 relationships and links that should not exist

Script: `tools/fixes/2026-11-06_ra_links_2_V1.3.py`; mappings decided by the git maintainer.

318 changes.

| RA | Link before | After | Count |
|---|---|---|---|
| C-ITS RA | Abstraction «» User_Need → User_Need | deleted (should not exist) | 5 |
| C-ITS RA | Abstraction «» User_Need → User_Need_Service | deleted (should not exist) | 1 |
| C-ITS RA | Abstraction «» User_Need_Service → User_Need | deleted (should not exist) | 1 |
| C-ITS RA | Association «defines» ITS_Service_Added_Value → Stakeholder | «delivers value to» | 14 |
| C-ITS RA | Dependency «» Role → Role | deleted (should not exist) | 1 |
| C-ITS RA | Realisation «» Actor → Actor | deleted (should not exist) | 5 |
| C-ITS RA | Realisation «» Component → Component | deleted (should not exist) | 1 |
| C-ITS RA | Realisation «» Component → Interface | deleted (should not exist) | 1 |
| C-ITS RA | Realisation «» Data_Object → Data_Object | deleted (should not exist) | 5 |
| C-ITS RA | Realisation «» Role → Role | deleted (should not exist) | 3 |
| C-ITS RA | Usage «» Component → Component | deleted (should not exist) | 8 |
| C-ITS RA | Usage «» Component → Interface | deleted (should not exist) | 7 |
| C-ITS RA | Usage «» Component → Physical_Data_Flow | «use» | 2 |
| C-ITS RA | Usage «» Physical_Data_Flow → Component | reverse, «use» | 2 |
| FRAME Meta Model | Association «defines» ITS_Service_Added_Value → Stakeholder | «delivers value to» | 1 |
| NAP RA | Association «defines» ITS_Service_Added_Value → Stakeholder | «delivers value to» | 24 |
| NAP RA | Dependency «» Application → Low_Level_Function | «contains» | 4 |
| NAP RA | Realisation «» Information_Object → Information_Object | deleted (should not exist) | 4 |
| NAP RA | Usage «» Application → Datastore | «contains» | 3 |
| NAP RA | Usage «» Application → Low_Level_Function | «contains» | 6 |
| NAP RA | Usage «» Application → Physical_Data_Flow | «contains» | 19 |
| NAP RA | Usage «» Information_Object → Low_Level_Data_Flow | reverse, «contains» | 1 |
| NAP RA | Usage «» Low_Level_Data_Flow → Information_Object | «contains» | 11 |
| NAP RA | Usage «» Physical_Data_Flow → Application | reverse, «contains» | 3 |
| NAP RA | Usage «» Physical_Data_Flow → Terminator | reverse, «use» | 1 |
| NAP RA | Usage «» Terminator → Physical_Data_Flow | «use» | 11 |
| National Body RA | Association «defines» ITS_Service_Added_Value → Stakeholder | «delivers value to» | 11 |
| National Body RA | Association «» Stakeholder → ITS_Service_Added_Value | reverse, «delivers value to» | 1 |
| National Body RA | Dependency «» ITS_Business_Process → ITS_Business_Process | «triggers» | 23 |
| National Body RA | Dependency «» ITS_Service_Process → ITS_Service_Process | «triggers» | 32 |
| National Body RA | Usage «Call» ITS_Service_Process → ITS_Service_Process | «triggers» | 14 |
| National Body RA | Usage «Instantiate» ITS_Service_Process → ITS_Service_Process | «triggers» | 9 |
| Truckparking RA (SSTP) | Association «ArchiMate_Association» Role → Role | deleted (should not exist) | 2 |
| Truckparking RA (SSTP) | Association «IN» Component → Physical_Data_Flow | «use» | 10 |
| Truckparking RA (SSTP) | Association «OUT» Physical_Data_Flow → Component | reverse, «use» | 10 |
| Truckparking RA (SSTP) | Association «» Role → Role | deleted (should not exist) | 6 |
| Truckparking RA (SSTP) | Usage «» Application → Datastore | «contains» | 5 |
| Truckparking RA (SSTP) | Usage «» Application → Low_Level_Function | duplicate of an existing FRAME link – deleted | 2 |
| Truckparking RA (SSTP) | Usage «» Application → Low_Level_Function | «contains» | 28 |
| eCall RA | Abstraction «» Information_Object → Low_Level_Data_Flow | reverse, «contains» | 1 |
| eCall RA | Association «» Requirement → Specification | reverse, «defines» | 6 |
| eCall RA | Association «» Role → Role | deleted (should not exist) | 2 |
| eCall RA | Usage «Instantiate» ITS_Service_Added_Value → Stakeholder | «delivers value to» | 1 |
| eCall RA | Usage «» Information_Object → Information_Object | deleted (should not exist) | 11 |
