# Group C – open IN/OUT and low-level «component of»

Convention: producer `endpoint --«IN»--> flow`, consumer `flow --«OUT»--> endpoint`. Role of each endpoint from the
flow description and the low-level producer/consumer (a high-level function takes the role of the low-level function it contains).

31 IN/OUT connectors changed, 8 low-level «component of» replaced, 3 high-level «component of» added.

## IN/OUT (#69)

| Flow | Endpoint | Role | Now | Action |
|---|---|---|---|---|
| fft.ftom-incident_responses | F8.6.5 Provide FTOM Interface for FTEP Monitoring | consumer | flow → «IN» | relabel «OUT» |
| fft.ftom-prepare_new_FTEP | F8.4.3 Provide Freight Transport Operations Manager Interface | consumer | flow → «IN» | relabel «OUT» |
| fft.ftom-request_existing_FTEP | F8.4.3 Provide Freight Transport Operations Manager Interface | consumer | flow → «IN» | relabel «OUT» |
| tft.ftom-prepared_new_FTEP | F8.4.3 Provide Freight Transport Operations Manager Interface | producer | «OUT» → flow | relabel «IN» |
| tft.ftom-requested_existing_FTEP | F8.4.3 Provide Freight Transport Operations Manager Interface | producer | «OUT» → flow | relabel «IN» |
| tnap.cp-registration_response | F3.6.2 Manage Registrations and Provide Authorisation Service | producer | «OUT» → flow | relabel «IN» |
| tnap.cp-registration_response | F3.6 Operate National Access Point | producer | «OUT» → flow | relabel «IN» |
| mpto_current_driver_availability | F4.4 Control PT Fleet | consumer | flow → «IN» | relabel «OUT» |
| mpto_demand_vehicle_repaired | F4.7 Provide On-demand Services | consumer | flow → «IN» | relabel «OUT» |
| mpto_fare_scheme_for_PT_driver | F4.2 Plan PT Service | producer | flow → «IN» | reverse |
| mpto_fare_scheme_for_PT_driver | F4.5 Provide PT Fare Facilities | consumer | «IN» → flow | reverse, relabel «OUT» |
| mpto_fare_scheme_for_service | F4.2 Plan PT Service | producer | flow → «IN» | reverse |
| mpto_fare_scheme_for_service | F4.5 Provide PT Fare Facilities | consumer | «IN» → flow | reverse, relabel «OUT» |
| mt_carpark_occupancy_for_inter-urban | F3.1.5 Provide Management of Service Areas | consumer | flow → «IN» | relabel «OUT» |
| mt_inter-urban_strategy_command_response_failure | F3.1.2.13 Manage Inter-urban Traffic Strategies | consumer | flow → «IN» | relabel «OUT» |
| psef_request_emergency_response_statistics | F2.1.2 Manage Emergency Intervention | consumer | flow → «IN» | relabel «OUT» |
| pshvs_instructions_&_warnings_for_other_vehicles | F5.16 Provide Outputs to Host Vehicle Drivers | producer | flow → «IN» | reverse |
| pshvs_instructions_&_warnings_for_other_vehicles | F5.12 Provide Vehicle Communications Interfaces | consumer | «IN» → flow | reverse, relabel «OUT» |
| pshvs_location_from_other_vehicle | F5.13 Provide Vehicle Data and ISA | consumer | flow → «IN» | relabel «OUT» |
| pshvs_other_vehicle_trajectory_for_host_vehicle | F5.15.3 Determine Host Vehicle Situation | consumer | flow → «IN» | relabel «OUT» |
| pshvs_vehicle_data_for_trip_planning | F5.14 Provide In-vehicle Trip Planning & Implementation | consumer | flow → «IN» | relabel «OUT» |
| pshvs_load_operational_data | F5.11.13 Manage Operational Data Store | producer | «OUT» → flow | relabel «IN» |
| pshvs_load_operational_data | D5.1 Operational Data | consumer | flow → «IN» | relabel «OUT» |
| pshvs_read_operational_data | D5.1 Operational Data | producer | «OUT» → flow | relabel «IN» |
| pshvs_read_operational_data | F5.11.13 Manage Operational Data Store | consumer | flow → «IN» | relabel «OUT» |
| pshvs_request_driver_condition | F5.11.7 Provide In-vehicle eCall Facilities | producer | «OUT» → flow | relabel «IN» |
| pshvs_request_driver_condition | F5.11.13 Manage Operational Data Store | consumer | flow → «IN» | relabel «OUT» |
| pshvs_request_driver_stored_data | F5.11.11 Monitor Status of Driver | producer | «OUT» → flow | relabel «IN» |
| pshvs_request_driver_stored_data | F5.11.13 Manage Operational Data Store | consumer | flow → «IN» | relabel «OUT» |
| pshvs_request_tvd_incident_data | F5.11.6 Provide Incident Related Data | producer | «OUT» → flow | relabel «IN» |
| pshvs_request_tvd_incident_data | F5.11.13 Manage Operational Data Store | consumer | flow → «IN» | relabel «OUT» |

## «component of» between low-level data flows (#80, #81)

| Part (LL) | Former target (LL) | Action |
|---|---|---|
| flds-psef_location_data | flds-emergency_call_location | delete LL→LL link (on no diagram); part already part of From Location Data Source; add «component of» former target → From Location Data Source |
| flds-psef_location_data | flds-emergency_vehicle_location | delete LL→LL link (on no diagram); part already part of From Location Data Source; add «component of» former target → From Location Data Source |
| fo.co-PSAP_data_update | fo.co-PSAP_data_inputs | delete LL→LL link (on no diagram); add «component of» part → fo-psef_inputs; former target already part of fo-psef_inputs |
| fo.co-request_PSAP_data_output | fo.co-PSAP_data_inputs | delete LL→LL link (on no diagram); part already part of fo-psef_inputs; former target already part of fo-psef_inputs |
| mt.mffo_current_inter-urban_traffic_data | mt.mffo_current_road_network_data | delete LL→LL link (on no diagram); part already part of mt.mffo_data_for_FTEP_preparation; former target already part of mt.mffo_incident_response_and_data, mt.mffo_data_for_FTEP_preparation |
| mt.mffo_current_urban_traffic_data | mt.mffo_current_road_network_data | delete LL→LL link (on no diagram); part already part of mt.mffo_data_for_FTEP_preparation; former target already part of mt.mffo_incident_response_and_data, mt.mffo_data_for_FTEP_preparation |
| mt.mffo_historic_intre-urban_traffic_data | mt.mffo_historic_road_network_data | delete LL→LL link (on no diagram); part already part of mt.mffo_data_for_FTEP_preparation; former target already part of mt.mffo_incident_response_and_data, mt.mffo_data_for_FTEP_preparation |
| mt.mffo_historic_urban_traffic_data | mt.mffo_historic_road_network_data | delete LL→LL link (on no diagram); part already part of mt.mffo_data_for_FTEP_preparation; former target already part of mt.mffo_incident_response_and_data, mt.mffo_data_for_FTEP_preparation |
