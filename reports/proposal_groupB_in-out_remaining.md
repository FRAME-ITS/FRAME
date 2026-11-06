# Proposal – IN/OUT connectors against the convention (#69)

Convention (prevailing use in V5.2): **«IN» producer → data flow**, **«OUT» data flow → consumer** – the arrow follows the data.
For every deviating connector the role of the function/terminator is derived from the data flow naming convention
(`f<terminator>-…` from, `t<terminator>-…` to a terminator, `abc.def-…` from area abc to area def) and from the other links of the same flow.

33 connectors. **No change has been made yet** – group B is applied only after review.

| Scope | Confidence | Proposed action | Count |
|---|---|---|---|
| FRAME Repository | conflict | review | 7 |
| FRAME Repository | medium | relabel | 3 |
| FRAME Repository | unknown | review | 21 |
| Reference architectures | unknown | review | 2 |

| Scope | Flow | Endpoint | Now | Proposed | Confidence | Evidence |
|---|---|---|---|---|---|---|
| FRAME Repository | fmms.mmc-inter-urban_crossing_request | F3.1.2.14 Implement Inter-urban Management Traffic Strategy | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fmms.mmc-int…" from a terminator into the system |
| FRAME Repository | fmms.mms-data_for_demand_services | F4.7 Provide On-demand Services | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fmms.mms-dat…" from a terminator into the system |
| FRAME Repository | fmms.mms-service_details_response | F4.6 Provide Facilities for Vehicle Sharing | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fmms.mms-ser…" from a terminator into the system |
| FRAME Repository | fft.ftom-incident_responses | F8.6.5 Provide FTOM Interface for FTEP Monitoring | «IN» flow→Low_Level_Function | review in EA | conflict | flow "fft.ftom-inc…" from a terminator into the system; flow already has a consumer |
| FRAME Repository | fft.ftom-prepare_new_FTEP | F8.4.3 Provide Freight Transport Operations Manager Interface | «IN» flow→Low_Level_Function | review in EA | conflict | flow "fft.ftom-pre…" from a terminator into the system; flow already has a consumer |
| FRAME Repository | fft.ftom-request_existing_FTEP | F8.4.3 Provide Freight Transport Operations Manager Interface | «IN» flow→Low_Level_Function | review in EA | conflict | flow "fft.ftom-req…" from a terminator into the system; flow already has a consumer |
| FRAME Repository | tft.ftom-prepared_new_FTEP | F8.4.3 Provide Freight Transport Operations Manager Interface | «OUT» Low_Level_Function→flow | review in EA | conflict | flow "tft.ftom-pre…" from the system to a terminator; flow already has a producer |
| FRAME Repository | tft.ftom-requested_existing_FTEP | F8.4.3 Provide Freight Transport Operations Manager Interface | «OUT» Low_Level_Function→flow | review in EA | conflict | flow "tft.ftom-req…" from the system to a terminator; flow already has a producer |
| FRAME Repository | tnap.cp-registration_response | F3.6.2 Manage Registrations and Provide Authorisation Service | «OUT» Low_Level_Function→flow | review in EA | conflict | flow "tnap.cp-regi…" from the system to a terminator; flow already has a producer |
| FRAME Repository | tnap.cp-registration_response | F3.6 Operate National Access Point | «OUT» High_Level_Function→flow | review in EA | conflict | flow "tnap.cp-regi…" from the system to a terminator; flow already has a producer |
| FRAME Repository | mpto_current_driver_availability | F4.4 Control PT Fleet | «IN» flow→High_Level_Function | review in EA | unknown |  |
| FRAME Repository | mpto_demand_vehicle_repaired | F4.7 Provide On-demand Services | «IN» flow→High_Level_Function | review in EA | unknown |  |
| FRAME Repository | mpto_fare_scheme_for_PT_driver | F4.2 Plan PT Service | «IN» flow→High_Level_Function | review in EA | unknown |  |
| FRAME Repository | mpto_fare_scheme_for_service | F4.2 Plan PT Service | «IN» flow→High_Level_Function | review in EA | unknown |  |
| FRAME Repository | mt_carpark_occupancy_for_inter-urban | F3.1.5 Provide Management of Service Areas | «IN» flow→High_Level_Function | review in EA | unknown |  |
| FRAME Repository | mt_inter-urban_strategy_command_response_failure | F3.1.2.13 Manage Inter-urban Traffic Strategies | «IN» flow→High_Level_Function | review in EA | unknown |  |
| FRAME Repository | psef_request_emergency_response_statistics | F2.1.2 Manage Emergency Intervention | «IN» flow→High_Level_Function | review in EA | unknown |  |
| FRAME Repository | pshvs_instructions_&_warnings_for_other_vehicles | F5.16 Provide Outputs to Host Vehicle Drivers | «IN» flow→High_Level_Function | review in EA | unknown |  |
| FRAME Repository | pshvs_load_operational_data | F5.11.13 Manage Operational Data Store | «OUT» Low_Level_Function→flow | review in EA | unknown |  |
| FRAME Repository | pshvs_load_operational_data | D5.1 Operational Data | «IN» flow→Datastore | review in EA | unknown |  |
| FRAME Repository | pshvs_location_from_other_vehicle | F5.13 Provide Vehicle Data and ISA | «IN» flow→High_Level_Function | review in EA | unknown |  |
| FRAME Repository | pshvs_other_vehicle_trajectory_for_host_vehicle | F5.15.3 Determine Host Vehicle Situation | «IN» flow→High_Level_Function | review in EA | unknown |  |
| FRAME Repository | pshvs_read_operational_data | F5.11.13 Manage Operational Data Store | «IN» flow→Low_Level_Function | review in EA | unknown |  |
| FRAME Repository | pshvs_read_operational_data | D5.1 Operational Data | «OUT» Datastore→flow | review in EA | unknown |  |
| FRAME Repository | pshvs_request_driver_condition | F5.11.13 Manage Operational Data Store | «IN» flow→Low_Level_Function | review in EA | unknown |  |
| FRAME Repository | pshvs_request_driver_condition | F5.11.7 Provide In-vehicle eCall Facilities | «OUT» Low_Level_Function→flow | review in EA | unknown |  |
| FRAME Repository | pshvs_request_driver_stored_data | F5.11.13 Manage Operational Data Store | «IN» flow→Low_Level_Function | review in EA | unknown |  |
| FRAME Repository | pshvs_request_driver_stored_data | F5.11.11 Monitor Status of Driver | «OUT» Low_Level_Function→flow | review in EA | unknown |  |
| FRAME Repository | pshvs_request_tvd_incident_data | F5.11.6 Provide Incident Related Data | «OUT» Low_Level_Function→flow | review in EA | unknown |  |
| FRAME Repository | pshvs_request_tvd_incident_data | F5.11.13 Manage Operational Data Store | «IN» flow→Low_Level_Function | review in EA | unknown |  |
| FRAME Repository | pshvs_vehicle_data_for_trip_planning | F5.14 Provide In-vehicle Trip Planning & Implementation | «IN» flow→High_Level_Function | review in EA | unknown |  |
| FRAME Meta Model | FRAME_Low_Level_Data_Flow | Terminator/ Subterminator | «IN» flow→Terminator | review in EA | unknown |  |
| FRAME Meta Model | FRAME_Low_Level_Data_Flow | Terminator/ Subterminator | «OUT» Terminator→flow | review in EA | unknown |  |
