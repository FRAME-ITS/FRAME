# Reference architectures, third pass (decided 2026-11-06)

Script: `tools/fixes/2026-11-06_ra_links_3_V1.3.py`; mappings decided by the git maintainer.

32 changes.

| RA | Link before | After | Count |
|---|---|---|---|
| C-ITS RA | Abstraction «» Actor → Desired_Architecture_Goals | «implements» | 2 |
| C-ITS RA | Realisation «» Actor → Desired_Architecture_Goals | «implements» | 1 |
| C-ITS RA | Usage «» User_Need → High_Level_Function | deleted (should not exist) | 3 |
| NAP RA | Dependency «» Low_Level_Function → Role | deleted (should not exist) | 1 |
| NAP RA | Dependency «» Terminator → Agreement | «adheres to» | 2 |
| National Body RA | Association «» Agreement → Specification | «use» | 3 |
| National Body RA | Association «» Specification → Agreement | «defines» | 1 |
| National Body RA | Usage «» Agreement → Specification | «use» | 1 |
| Truckparking RA (SSTP) | Usage «» Component → Terminator | deleted (should not exist) | 2 |
| eCall RA | Association «» ITS_Service_Process → ITS_Service_Process | «triggers» | 1 |
| eCall RA | Usage «Instantiate» ITS_Service_Process → ITS_Service_Process | duplicate of an existing FRAME link – deleted | 1 |
| eCall RA | Usage «Instantiate» ITS_Service_Process → ITS_Service_Process | «triggers» | 13 |
| eCall RA | Usage «» Datastore → Terminator | deleted (should not exist) | 1 |
