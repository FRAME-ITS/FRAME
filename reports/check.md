# Model check – FRAME.qea

**45 errors, 73 warnings**

| Rule | Related issue | Errors | Warnings |
|---|---|---|---|
| componentof | #80, #81 | 8 | 42 |
| context-diagram | #91 | 0 | 1 |
| duplicate |  | 0 | 2 |
| function-flows |  | 0 | 1 |
| function-parent |  | 0 | 5 |
| in-out | #69 | 28 | 0 |
| release-hygiene |  | 0 | 1 |
| self-reference | #62 | 0 | 2 |
| servedby |  | 9 | 5 |
| stereotype-spelling | #86 | 0 | 3 |
| unused-flow | #76 | 0 | 11 |

## Errors

<details><summary><b>componentof</b> (8)</summary>

- «Componentof» Low_Level_Data_Flow **flds-psef_location_data** (Frame Repository) → flds-emergency_call_location (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» Low_Level_Data_Flow **flds-psef_location_data** (Frame Repository) → flds-emergency_vehicle_location (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «component of» Low_Level_Data_Flow **fo.co-PSAP_data_update** (Frame Repository) → fo.co-PSAP_data_inputs (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «componentof» Low_Level_Data_Flow **fo.co-request_PSAP_data_output** (Frame Repository) → fo.co-PSAP_data_inputs (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «componentof» Low_Level_Data_Flow **mt.mffo_current_inter-urban_traffic_data** (Frame Repository) → mt.mffo_current_road_network_data (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «componentof» Low_Level_Data_Flow **mt.mffo_current_urban_traffic_data** (Frame Repository) → mt.mffo_current_road_network_data (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «componentof» Low_Level_Data_Flow **mt.mffo_historic_intre-urban_traffic_data** (Frame Repository) → mt.mffo_historic_road_network_data (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «componentof» Low_Level_Data_Flow **mt.mffo_historic_urban_traffic_data** (Frame Repository) → mt.mffo_historic_road_network_data (Low_Level_Data_Flow) runs whole → part or between low-level flows

</details>

<details><summary><b>in-out</b> (28)</summary>

- «IN» Low_Level_Data_Flow **fft.ftom-incident_responses** (Frame Repository) → F8.6.5 Provide FTOM Interface for FTEP Monitoring: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fft.ftom-prepare_new_FTEP** (Frame Repository) → F8.4.3 Provide Freight Transport Operations Manager Interface: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fft.ftom-request_existing_FTEP** (Frame Repository) → F8.4.3 Provide Freight Transport Operations Manager Interface: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **mpto_current_driver_availability** (Frame Repository) → F4.4 Control PT Fleet: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **mpto_demand_vehicle_repaired** (Frame Repository) → F4.7 Provide On-demand Services: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **mpto_fare_scheme_for_PT_driver** (Frame Repository) → F4.2 Plan PT Service: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **mpto_fare_scheme_for_service** (Frame Repository) → F4.2 Plan PT Service: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **mt_carpark_occupancy_for_inter-urban** (Frame Repository) → F3.1.5 Provide Management of Service Areas: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **mt_inter-urban_strategy_command_response_failure** (Frame Repository) → F3.1.2.13 Manage Inter-urban Traffic Strategies: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **psef_request_emergency_response_statistics** (Frame Repository) → F2.1.2 Manage Emergency Intervention: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **pshvs_instructions_&_warnings_for_other_vehicles** (Frame Repository) → F5.16 Provide Outputs to Host Vehicle Drivers: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **pshvs_load_operational_data** (Frame Repository) → D5.1 Operational Data: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **pshvs_location_from_other_vehicle** (Frame Repository) → F5.13 Provide Vehicle Data and ISA: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **pshvs_other_vehicle_trajectory_for_host_vehicle** (Frame Repository) → F5.15.3 Determine Host Vehicle Situation: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **pshvs_read_operational_data** (Frame Repository) → F5.11.13 Manage Operational Data Store: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **pshvs_request_driver_condition** (Frame Repository) → F5.11.13 Manage Operational Data Store: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **pshvs_request_driver_stored_data** (Frame Repository) → F5.11.13 Manage Operational Data Store: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **pshvs_request_tvd_incident_data** (Frame Repository) → F5.11.13 Manage Operational Data Store: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **pshvs_vehicle_data_for_trip_planning** (Frame Repository) → F5.14 Provide In-vehicle Trip Planning & Implementation: expected «OUT» for this direction (or reverse the connector)
- «OUT» Datastore **D5.1 Operational Data** (Frame Repository) → pshvs_read_operational_data: expected «IN» for this direction (or reverse the connector)
- «OUT» High_Level_Function **F3.6 Operate National Access Point** (Frame Repository) → tnap.cp-registration_response: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F3.6.2 Manage Registrations and Provide Authorisation Service** (Frame Repository) → tnap.cp-registration_response: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F5.11.11 Monitor Status of Driver** (Frame Repository) → pshvs_request_driver_stored_data: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F5.11.13 Manage Operational Data Store** (Frame Repository) → pshvs_load_operational_data: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F5.11.6 Provide Incident Related Data** (Frame Repository) → pshvs_request_tvd_incident_data: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F5.11.7 Provide In-vehicle eCall Facilities** (Frame Repository) → pshvs_request_driver_condition: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F8.4.3 Provide Freight Transport Operations Manager Interface** (Frame Repository) → tft.ftom-prepared_new_FTEP: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F8.4.3 Provide Freight Transport Operations Manager Interface** (Frame Repository) → tft.ftom-requested_existing_FTEP: expected «IN» for this direction (or reverse the connector)

</details>

<details><summary><b>servedby</b> (9)</summary>

- User_Need **11.1.1.6** (C-ITS Reference Architecture) → F3.1.1.5 Provide Urban Traffic Management Facilities is Usage «», expected Association «Servedby»
- User_Need **11.1.1.6** (C-ITS Reference Architecture) → F5.16.1 Manage Communication from Vehicle to Driver is Usage «», expected Association «Servedby»
- User_Need **11.1.1.6** (C-ITS Reference Architecture) → F5.16.2 Output Commands and Dynamic Warnings is Usage «», expected Association «Servedby»
- User_Need **11.1.4.1** (C-ITS Reference Architecture) → F5.16.1 Manage Communication from Vehicle to Driver is Usage «», expected Association «Servedby»
- User_Need **11.1.4.1** (C-ITS Reference Architecture) → F5.16.2 Output Commands and Dynamic Warnings is Usage «», expected Association «Servedby»
- User_Need **11.2.4.1** (C-ITS Reference Architecture) → F3.1 Provide Traffic Control is Usage «», expected Association «Servedby»
- User_Need **11.2.4.1** (C-ITS Reference Architecture) → F5.16.1 Manage Communication from Vehicle to Driver is Usage «», expected Association «Servedby»
- User_Need **11.2.4.1** (C-ITS Reference Architecture) → F5.16.2 Output Commands and Dynamic Warnings is Usage «», expected Association «Servedby»
- User_Need **11.2.4.1** (C-ITS Reference Architecture) → F9.3 Manage Vehicle Access to Sensitive Areas is Usage «», expected Association «Servedby»

</details>

## Warnings

<details><summary><b>componentof</b> (42)</summary>

- «Componentof» High_Level_Data_Flow **fnap-mt_inputs** (NAP Reference Architecture) → fnap.cc-metadata_search_request (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **fnap-mt_inputs** (NAP Reference Architecture) → fnap.cc-support_request (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **fnap-mt_inputs** (NAP Reference Architecture) → fnap.cp-metadata_&_authorisation_credentials (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **fnap-mt_inputs** (NAP Reference Architecture) → fnap.cp-registration_request (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **fnap-mt_inputs** (NAP Reference Architecture) → fnap.cp-support_request (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **fnap-mt_inputs** (NAP Reference Architecture) → fnap.cp-support_request (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **tnap-mt_outputs** (NAP Reference Architecture) → tnap.cc-support_response (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **tnap-mt_outputs** (NAP Reference Architecture) → tnap.cc-support_response (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **tnap-mt_outputs** (NAP Reference Architecture) → tnap.cp-support_response (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **tnap-mt_outputs** (NAP Reference Architecture) → tnap.cp-support_response (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «component of» High_Level_Function **F9.1 Enable Cooperative Roadside Vehicle Interactions** (C-ITS Reference Architecture) → F9.1.1 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.1 Enable Cooperative Roadside Vehicle Interactions** (C-ITS Reference Architecture) → F9.1.2 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.1 Enable Cooperative Roadside Vehicle Interactions** (C-ITS Reference Architecture) → F9.1.3 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.1 Enable Cooperative Roadside Vehicle Interactions** (C-ITS Reference Architecture) → F9.1.4 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.1 Enable Cooperative Roadside Vehicle Interactions** (C-ITS Reference Architecture) → F9.1.5 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.1 Enable Cooperative Roadside Vehicle Interactions** (C-ITS Reference Architecture) → F9.1.6 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.1 Enable Cooperative Roadside Vehicle Interactions** (C-ITS Reference Architecture) → F9.1.7 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.3 Manage Vehicle Access to Sensitive Locations/ Areas** (C-ITS Reference Architecture) → F9.3.1 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.3 Manage Vehicle Access to Sensitive Locations/ Areas** (C-ITS Reference Architecture) → F9.3.10 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.3 Manage Vehicle Access to Sensitive Locations/ Areas** (C-ITS Reference Architecture) → F9.3.11 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.3 Manage Vehicle Access to Sensitive Locations/ Areas** (C-ITS Reference Architecture) → F9.3.12 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.3 Manage Vehicle Access to Sensitive Locations/ Areas** (C-ITS Reference Architecture) → F9.3.13 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.3 Manage Vehicle Access to Sensitive Locations/ Areas** (C-ITS Reference Architecture) → F9.3.14 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.3 Manage Vehicle Access to Sensitive Locations/ Areas** (C-ITS Reference Architecture) → F9.3.15 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.3 Manage Vehicle Access to Sensitive Locations/ Areas** (C-ITS Reference Architecture) → F9.3.2 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.3 Manage Vehicle Access to Sensitive Locations/ Areas** (C-ITS Reference Architecture) → F9.3.3 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.3 Manage Vehicle Access to Sensitive Locations/ Areas** (C-ITS Reference Architecture) → F9.3.4 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.3 Manage Vehicle Access to Sensitive Locations/ Areas** (C-ITS Reference Architecture) → F9.3.5 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.3 Manage Vehicle Access to Sensitive Locations/ Areas** (C-ITS Reference Architecture) → F9.3.6 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.3 Manage Vehicle Access to Sensitive Locations/ Areas** (C-ITS Reference Architecture) → F9.3.7 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.3 Manage Vehicle Access to Sensitive Locations/ Areas** (C-ITS Reference Architecture) → F9.3.8 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.3 Manage Vehicle Access to Sensitive Locations/ Areas** (C-ITS Reference Architecture) → F9.3.9 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.5 Manage Interurban Urban Traffic Zones** (C-ITS Reference Architecture) → F9.5.1 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.5 Manage Interurban Urban Traffic Zones** (C-ITS Reference Architecture) → F9.5.2 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.5 Manage Interurban Urban Traffic Zones** (C-ITS Reference Architecture) → F9.5.3 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.5 Manage Interurban Urban Traffic Zones** (C-ITS Reference Architecture) → F9.5.3 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.5 Manage Interurban Urban Traffic Zones** (C-ITS Reference Architecture) → F9.5.4 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.5 Manage Interurban Urban Traffic Zones** (C-ITS Reference Architecture) → F9.5.5 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.5 Manage Interurban Urban Traffic Zones** (C-ITS Reference Architecture) → F9.5.6 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.5 Manage Interurban Urban Traffic Zones** (C-ITS Reference Architecture) → F9.5.7 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.5 Manage Interurban Urban Traffic Zones** (C-ITS Reference Architecture) → F9.5.8 (Low_Level_Function) runs whole → part
- «component of» High_Level_Function **F9.6 - Future messages and C-ITS services** (C-ITS Reference Architecture) → F9.6.1 (Low_Level_Function) runs whole → part

</details>

<details><summary><b>context-diagram</b> (1)</summary>

- Terminator **Freight Transport** (Frame Repository) has high-level data flows but is not in the FRAME Context Diagram

</details>

<details><summary><b>duplicate</b> (2)</summary>

- 2× User_Need **1.1.4** in the FRAME Repository
- 2× User_Need_Group **11 C-ITS** in the FRAME Repository

</details>

<details><summary><b>function-flows</b> (1)</summary>

- Low_Level_Function **F6.5.8 Enable Final Approval of Trip Plan** (Frame Repository) has no IN and OUT data flows

</details>

<details><summary><b>function-parent</b> (5)</summary>

- Low_Level_Function **F3.1.1.5.11 Monitor Access to Urban Zones** (Frame Repository) is not «Componentof» a high-level function or functional area
- Low_Level_Function **F3.1.1.5.12 Prevent Access to Urban Zones** (Frame Repository) is not «Componentof» a high-level function or functional area
- Low_Level_Function **F3.1.1.5.21 Send Messages to Approaching Urban Vehicles** (Frame Repository) is not «Componentof» a high-level function or functional area
- Low_Level_Function **F3.1.2.14.6 Send Messages to Approaching Inter-urban Vehicles** (Frame Repository) is not «Componentof» a high-level function or functional area
- Low_Level_Function **F6.5.8 Enable Final Approval of Trip Plan** (Frame Repository) is not «Componentof» a high-level function or functional area

</details>

<details><summary><b>release-hygiene</b> (1)</summary>

- top-level package **Test Package** looks like a test package – remove before a release

</details>

<details><summary><b>self-reference</b> (2)</summary>

- High_Level_Data_Flow **FRAME_High_Level_Data_Flow1** (Test Package) has a Aggregation «component of» to itself
- Terminator **FRAME_Terminator1** (Test Package) has a Abstraction «is Type of» to itself

</details>

<details><summary><b>servedby</b> (5)</summary>

- User_Need **6.5.1.1** (NAP Reference Architecture) → F3.6.4 Manage Metadata Retrieval is Aggregation «componentof», expected Association «Servedby»
- User_Need **6.5.1.2** (NAP Reference Architecture) → F3.6.4 Manage Metadata Retrieval is Aggregation «componentof», expected Association «Servedby»
- User_Need **6.5.1.3** (NAP Reference Architecture) → F3.6.4 Manage Metadata Retrieval is Aggregation «componentof», expected Association «Servedby»
- User_Need **6.5.1.6** (NAP Reference Architecture) → F3.6.4 Manage Metadata Retrieval is Aggregation «componentof», expected Association «Servedby»
- User_Need **6.5.1.8** (NAP Reference Architecture) → F3.6.4 Manage Metadata Retrieval is Aggregation «componentof», expected Association «Servedby»

</details>

<details><summary><b>stereotype-spelling</b> (3)</summary>

- connector stereotype written in 2 ways: «Servedby» 1746×, «served by» 137×
- connector stereotype written in 2 ways: «belongsto» 867×, «belongs to» 5×
- connector stereotype written in 3 ways: «Componentof» 1851×, «componentof» 605×, «component of» 157×

</details>

<details><summary><b>unused-flow</b> (11)</summary>

- High_Level_Data_Flow **fes-psef_iputs** (Frame Repository) is not shown in any diagram
- High_Level_Data_Flow **mpto_route_data_for_planning_&_reports** (Frame Repository) is not shown in any diagram
- High_Level_Data_Flow **mpto_service_&_scheduling_data** (Frame Repository) is not shown in any diagram
- High_Level_Data_Flow **tes-psef_outputs** (Frame Repository) is not shown in any diagram
- Low_Level_Data_Flow **fesp.bsp-bookable_service_information** (Frame Repository) is not shown in any diagram
- Low_Level_Data_Flow **mffo_new_FTEP_data** (Frame Repository) is not shown in any diagram
- Low_Level_Data_Flow **pepf_contract_RF** (Frame Repository) is not shown in any diagram
- Low_Level_Data_Flow **pepf_illegal_action_notification_DPV** (Frame Repository) is not shown in any diagram
- Low_Level_Data_Flow **pscs_static_bus_lane_data** (Frame Repository) is not shown in any diagram
- Low_Level_Data_Flow **tesp.bsp-request_bookable_service_information** (Frame Repository) is not shown in any diagram
- Low_Level_Data_Flow **to.tio-current_other_travel_data** (Frame Repository) is not shown in any diagram

</details>

