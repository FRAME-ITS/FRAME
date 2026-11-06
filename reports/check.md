# Model check – FRAME.qea

**184 errors, 96 warnings**

| Rule | Related issue | Errors | Warnings |
|---|---|---|---|
| componentof | #80, #81 | 33 | 42 |
| context-diagram | #91 | 0 | 1 |
| dangling |  | 3 | 0 |
| duplicate |  | 0 | 2 |
| function-flows |  | 0 | 1 |
| function-parent |  | 0 | 5 |
| generalization | #79 | 1 | 0 |
| in-out | #69 | 128 | 23 |
| release-hygiene |  | 0 | 1 |
| self-reference | #62 | 1 | 2 |
| servedby |  | 18 | 5 |
| stereotype-spelling | #86 | 0 | 3 |
| unused-flow | #76 | 0 | 11 |

## Errors

<details><summary><b>componentof</b> (33)</summary>

- «Componentof» High_Level_Data_Flow **fnap-mt_inputs** (Frame Repository) → fnap.cc-metadata_search_request (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **fnap-mt_inputs** (Frame Repository) → fnap.cc-support_request (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **fnap-mt_inputs** (Frame Repository) → fnap.cc-support_request (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **fnap-mt_inputs** (Frame Repository) → fnap.cp-metadata_&_authorisation_credentials (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **fnap-mt_inputs** (Frame Repository) → fnap.cp-metadata_&_authorisation_credentials (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **fnap-mt_inputs** (Frame Repository) → fnap.cp-registration_request (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **fnap-mt_inputs** (Frame Repository) → fnap.cp-registration_request (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **fnap-mt_inputs** (Frame Repository) → fnap.cp-support_request (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **fnap-mt_inputs** (Frame Repository) → fnap.cp-support_request (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **fnap-mt_inputs** (Frame Repository) → fnap.cp-support_request (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **fnap-mt_inputs** (Frame Repository) → fnap.cp-support_request (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **mt.mpto_data_from_road_network_predictions** (Frame Repository) → mt.mpto_data_transfer (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **mt.mpto_inter-urban_data_transfer** (Frame Repository) → mt.mpto_data_transfer (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **mt.mpto_urban_data_transfer** (Frame Repository) → mt.mpto_data_transfer (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **mt.pscs_data_for_coop_sys** (Frame Repository) → mt.pscs_rest_area_space_response (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **tnap-mt_outputs** (Frame Repository) → tnap.cc-support_response (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **tnap-mt_outputs** (Frame Repository) → tnap.cp-support_response (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **tnap-mt_outputs** (Frame Repository) → tnap.cp-support_response (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» High_Level_Data_Flow **tors-pscs_outputs** (Frame Repository) → tors.hgvm-hazardous_goods_vehicle_route_implementation (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» Low_Level_Data_Flow **flds-psef_location_data** (Frame Repository) → flds-emergency_call_location (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» Low_Level_Data_Flow **flds-psef_location_data** (Frame Repository) → flds-emergency_vehicle_location (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «component of» Functional_Area **F9. Provide Support for Cooperative Systems** (Frame Repository) → F9.1 Enable Cooperative Roadside Vehicle Interactions (High_Level_Function) runs whole → part
- «component of» Functional_Area **F9. Provide Support for Cooperative Systems** (Frame Repository) → F9.2 Provide Access to Specific Lanes (High_Level_Function) runs whole → part
- «component of» Functional_Area **F9. Provide Support for Cooperative Systems** (Frame Repository) → F9.3 Manage Vehicle Access to Sensitive Locations/ Areas (High_Level_Function) runs whole → part
- «component of» Functional_Area **F9. Provide Support for Cooperative Systems** (Frame Repository) → F9.4 Provide Hazardous Goods Management (High_Level_Function) runs whole → part
- «component of» Functional_Area **F9. Provide Support for Cooperative Systems** (Frame Repository) → F9.5 Manage Interurban Urban Traffic Zones (High_Level_Function) runs whole → part
- «component of» Functional_Area **F9. Provide Support for Cooperative Systems** (Frame Repository) → F9.6 - Future messages and C-ITS services (High_Level_Function) runs whole → part
- «component of» Low_Level_Data_Flow **fo.co-PSAP_data_update** (Frame Repository) → fo.co-PSAP_data_inputs (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «componentof» Low_Level_Data_Flow **fo.co-request_PSAP_data_output** (Frame Repository) → fo.co-PSAP_data_inputs (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «componentof» Low_Level_Data_Flow **mt.mffo_current_inter-urban_traffic_data** (Frame Repository) → mt.mffo_current_road_network_data (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «componentof» Low_Level_Data_Flow **mt.mffo_current_urban_traffic_data** (Frame Repository) → mt.mffo_current_road_network_data (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «componentof» Low_Level_Data_Flow **mt.mffo_historic_intre-urban_traffic_data** (Frame Repository) → mt.mffo_historic_road_network_data (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «componentof» Low_Level_Data_Flow **mt.mffo_historic_urban_traffic_data** (Frame Repository) → mt.mffo_historic_road_network_data (Low_Level_Data_Flow) runs whole → part or between low-level flows

</details>

<details><summary><b>dangling</b> (3)</summary>

- Association «IN» {2B186A93-BA1E-4a1a-B115-BEEDEA3C87BA} has a missing end
- Association «OUT» {AAADCD3B-84C1-466f-B8D4-983F4D943536} has a missing end
- Usage «» {5101F0F4-2B49-4b1c-8801-63B52F4B7493} has a missing end

</details>

<details><summary><b>generalization</b> (1)</summary>

- Generalization Low_Level_Data_Flow **fws-environment_data_for_PT** (Frame Repository) → fws-mpto_inputs: data flows are linked by «Componentof»

</details>

<details><summary><b>in-out</b> (128)</summary>

- «IN» High_Level_Data_Flow **From NAP Actors** (Frame Repository) → System: expected «OUT» for this direction (or reverse the connector)
- «IN» High_Level_Data_Flow **ffc-mt_inputs** (Frame Repository) → F3. Manage Traffic: expected «OUT» for this direction (or reverse the connector)
- «IN» High_Level_Data_Flow **fmms-mpto_control_inputs** (Frame Repository) → F4.4 Control PT Fleet: expected «OUT» for this direction (or reverse the connector)
- «IN» High_Level_Data_Flow **fmms.mmc-crossing_request** (Frame Repository) → Multi-Modal Crossing: expected «OUT» for this direction (or reverse the connector)
- «IN» High_Level_Data_Flow **fmms.mmc-urban_crossing_inputs** (Frame Repository) → Multi-Modal Crossing: expected «OUT» for this direction (or reverse the connector)
- «IN» High_Level_Data_Flow **fmms.mms-demand_inputs** (Frame Repository) → Multi-Modal Management System: expected «OUT» for this direction (or reverse the connector)
- «IN» High_Level_Data_Flow **fmms.mms-incident_inputs** (Frame Repository) → Multi-Modal Management System: expected «OUT» for this direction (or reverse the connector)
- «IN» High_Level_Data_Flow **fws-mpto_inputs** (Frame Repository) → F4. Manage Public Transport Operations: expected «OUT» for this direction (or reverse the connector)
- «IN» High_Level_Data_Flow **psef.mpto_alarm_acknowledgements** (Frame Repository) → F4. Manage Public Transport Operations: expected «OUT» for this direction (or reverse the connector)
- «IN» High_Level_Data_Flow **pshvs.mt_outputs_to_driver_via_roadside** (Frame Repository) → F3.1 Provide Traffic Control: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fae-tunnel_atmospheric_conditions** (Frame Repository) → F3.1.7 Provide Traffic Management for Tunnels: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fbti.tms-tunnel_system_inputs** (Frame Repository) → F3.1.7 Provide Traffic Management for Tunnels: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fd-carpark_space_payment** (Frame Repository) → F3.1.4 Provide Management of Car Parks: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fd.ptd-assign_vehicle_to_service** (Frame Repository) → F4.1 Monitor PT fleet: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fd.ptd-driver_status** (Frame Repository) → F4.3 Provide PT Management: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fd.ptd-request_fares** (Frame Repository) → F4.5 Provide PT Fare Facilities: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fesp.b-urban_traffic_information_request** (Frame Repository) → F3.1.1 Provide Urban Traffic Management: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fesp.dvip-vehicle_data_for_inter-urban_fcd_check** (Frame Repository) → F3.1.2 Provide Inter-urban Traffic Management: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fesp.dvip-vehicle_data_for_urban_fcd_check** (Frame Repository) → F3.1.1 Provide Urban Traffic Management: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fesp.g-map_data_for_vehicle_sensor_data** (Frame Repository) → F5.15 Provide In-vehicle Detection and Analysis: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fesp.g-static_road_information** (Frame Repository) → F5.13 Provide Vehicle Data and ISA: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fesp.g-vehicle_trip_plan_implementation_map_data** (Frame Repository) → F5.14 Provide In-vehicle Trip Planning & Implementation: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **ffc-carpark_space_payment_response** (Frame Repository) → F3.1.4 Provide Management of Car Parks: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **ffc-confirmed_fare_payment** (Frame Repository) → F4.5 Provide PT Fare Facilities: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **ffc-demand_service_payment_confirmed** (Frame Repository) → F4.7 Provide On-demand Services: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fft.ftom-incident_responses** (Frame Repository) → F8.6.5 Provide FTOM Interface for FTEP Monitoring: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fft.ftom-prepare_new_FTEP** (Frame Repository) → F8.4.3 Provide Freight Transport Operations Manager Interface: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fft.ftom-request_existing_FTEP** (Frame Repository) → F8.4.3 Provide Freight Transport Operations Manager Interface: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **flds-location_data_for_vehicle_sensor_data** (Frame Repository) → F5.15 Provide In-vehicle Detection and Analysis: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **flds-on-demand_service_vehicle_location** (Frame Repository) → F4.7 Provide On-demand Services: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **flds-vehicle_location_for_trip_monitoring** (Frame Repository) → F5.14 Provide In-vehicle Trip Planning & Implementation: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **flds-vehicle_sharer_location** (Frame Repository) → F4.6 Provide Facilities for Vehicle Sharing: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fmms.mmc-inter-urban_crossing_request** (Frame Repository) → F3.1.2.14 Implement Inter-urban Management Traffic Strategy: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fmms.mmc-inter-urban_crossing_request** (Frame Repository) → Multi-Modal Crossing: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fmms.mmc-urban_crossing_command** (Frame Repository) → Multi-Modal Crossing: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fmms.mmc-urban_crossing_information** (Frame Repository) → Multi-Modal Crossing: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fmms.mms-PT_service_change_request** (Frame Repository) → Multi-Modal Management System: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fmms.mms-accident_information** (Frame Repository) → Multi-Modal Management System: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fmms.mms-control_parameters** (Frame Repository) → Multi-Modal Management System: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fmms.mms-current_service_status** (Frame Repository) → Multi-Modal Management System: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fmms.mms-data_for_demand_services** (Frame Repository) → F4.7 Provide On-demand Services: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fmms.mms-data_for_demand_services** (Frame Repository) → Multi-Modal Management System: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fmms.mms-ferry_service_information** (Frame Repository) → Multi-Modal Management System: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fmms.mms-plannings** (Frame Repository) → Multi-Modal Management System: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fmms.mms-rail_service_information** (Frame Repository) → Multi-Modal Management System: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fmms.mms-service_change_request_response** (Frame Repository) → Multi-Modal Management System: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fmms.mms-service_details_response** (Frame Repository) → F4.6 Provide Facilities for Vehicle Sharing: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fmms.mms-service_details_response** (Frame Repository) → Multi-Modal Management System: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fmms.mms-strike_details** (Frame Repository) → Multi-Modal Management System: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fnap.cc-metadata_search_request** (Frame Repository) → F3.6 Operate National Access Point: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fnap.cc-support_request** (Frame Repository) → F3.6 Operate National Access Point: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fnap.cc-support_request** (Frame Repository) → F3.6.5 Provide NAP User Support: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fnap.cp-metadata_&_authorisation_credentials** (Frame Repository) → F3.6 Operate National Access Point: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fnap.cp-metadata_&_authorisation_credentials** (Frame Repository) → F3.6.3 Manage Content Providers Metadata: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fnap.cp-registration_request** (Frame Repository) → F3.6 Operate National Access Point: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fnap.cp-registration_request** (Frame Repository) → F3.6.2 Manage Registrations and Provide Authorisation Service: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fnap.cp-support_request** (Frame Repository) → F3.6 Operate National Access Point: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fnap.cp-support_request** (Frame Repository) → F3.6.5 Provide NAP User Support: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fo.co-PSAP_data_inputs** (Frame Repository) → F2.1.11 Manage eCall Messages: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fo.co-request_PSAP_data_output** (Frame Repository) → F2.1.11 Manage eCall Messages: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fo.eo-request_statistical_report** (Frame Repository) → F2.1 Manage Emergencies: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fo.eo-stop_stolen_vehicle** (Frame Repository) → F2.2 Manage Stolen Vehicle Notification: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fo.rno-inter-urban_road_static_network_data** (Frame Repository) → F3.1.2.13 Manage Inter-urban Traffic Strategies: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fors.pts-arrival_prediction_data** (Frame Repository) → F4.1 Monitor PT fleet: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fors.tsc-local_priority_request_details** (Frame Repository) → F3.1.1.5 Provide Urban Traffic Management Facilities: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fors.tss-traffic_prediction_results** (Frame Repository) → F3.1.6 Provide Traffic Predictions: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fre-roadside_speed_indication_details** (Frame Repository) → F5.13 Provide Vehicle Data and ISA: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **frp-guidance_data** (Frame Repository) → F5.12.12 Collect Road Network Information: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **frp-local_vehicle_road_surface_conditions** (Frame Repository) → F5.15 Provide In-vehicle Detection and Analysis: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **ft.p-presence_indication** (Frame Repository) → F5.15 Provide In-vehicle Detection and Analysis: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **ftrfc-freight_vehicle_identity_for_rest_area** (Frame Repository) → F3.1.5 Provide Management of Service Areas: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **ftrfc-inter-urban_local_data_for_ramp_metering** (Frame Repository) → F3.1.2.13 Manage Inter-urban Traffic Strategies: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **ftrfc-inter-urban_vehicle_presence_for_messages** (Frame Repository) → F3.1.2.14 Implement Inter-urban Management Traffic Strategy: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **ftrfc-traffic_conditions_in_tunnel** (Frame Repository) → F3.1.7 Provide Traffic Management for Tunnels: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fv-identity_for_inter-urban_zone_access** (Frame Repository) → F3.1.2.13 Manage Inter-urban Traffic Strategies: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fv-identity_for_urban_zone_access** (Frame Repository) → F3.1.1.5 Provide Urban Traffic Management Facilities: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fv.fv-freight_vehicle_identity_for_rest_area** (Frame Repository) → F3.1.5 Provide Management of Service Areas: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fve.onv-vehicle_presence_indication** (Frame Repository) → F5.15 Provide In-vehicle Detection and Analysis: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fve.oru-presence_indication** (Frame Repository) → F5.15 Provide In-vehicle Detection and Analysis: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fve.so-object_presence_indication** (Frame Repository) → F5.15 Provide In-vehicle Detection and Analysis: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fws-weather_conditions_for_ISA** (Frame Repository) → F5.13 Provide Vehicle Data and ISA: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **mpto_current_driver_availability** (Frame Repository) → F4.4 Control PT Fleet: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **mpto_demand_vehicle_repaired** (Frame Repository) → F4.7 Provide On-demand Services: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **mpto_fare_scheme_for_PT_driver** (Frame Repository) → F4.2 Plan PT Service: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **mpto_fare_scheme_for_service** (Frame Repository) → F4.2 Plan PT Service: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **mt.pshvs_service_area_information** (Frame Repository) → F5.16.1 Manage Communication from Vehicle to Driver: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **mt_carpark_occupancy_for_inter-urban** (Frame Repository) → F3.1.5 Provide Management of Service Areas: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **mt_inter-urban_strategy_command_response_failure** (Frame Repository) → F3.1.2.13 Manage Inter-urban Traffic Strategies: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **mt_load_NAP_user_data** (Frame Repository) → D3.17 NAP Users: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **psef_request_emergency_response_statistics** (Frame Repository) → F2.1.2 Manage Emergency Intervention: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **pshvs.mt_inter-urban_xfcd** (Frame Repository) → F3.1.2 Provide Inter-urban Traffic Management: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **pshvs.psef_eCall_message** (Frame Repository) → F2.1.11 Manage eCall Messages: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **pshvs_instructions_&_warnings_for_other_vehicles** (Frame Repository) → F5.16 Provide Outputs to Host Vehicle Drivers: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **pshvs_load_operational_data** (Frame Repository) → D5.1 Operational Data: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **pshvs_location_from_other_vehicle** (Frame Repository) → F5.13 Provide Vehicle Data and ISA: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **pshvs_other_vehicle_trajectory_for_host_vehicle** (Frame Repository) → F5.15.3 Determine Host Vehicle Situation: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **pshvs_read_operational_data** (Frame Repository) → F5.11.13 Manage Operational Data Store: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **pshvs_request_driver_condition** (Frame Repository) → F5.11.13 Manage Operational Data Store: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **pshvs_request_driver_stored_data** (Frame Repository) → F5.11.13 Manage Operational Data Store: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **pshvs_request_tvd_incident_data** (Frame Repository) → F5.11.13 Manage Operational Data Store: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **pshvs_tvd_scenario** (Frame Repository) → F5.11.13 Manage Operational Data Store: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **pshvs_vehicle_data_for_trip_planning** (Frame Repository) → F5.14 Provide In-vehicle Trip Planning & Implementation: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **tnap.cc-data_response** (NAP Reference Architecture) → NAP Content Consumer: expected «OUT» for this direction (or reverse the connector)
- «OUT» Datastore **D3.17 NAP Users** (Frame Repository) → mt_read_NAP_user_data: expected «IN» for this direction (or reverse the connector)
- «OUT» Datastore **D5.1 Operational Data** (Frame Repository) → pshvs_read_operational_data: expected «IN» for this direction (or reverse the connector)
- «OUT» High_Level_Function **F3.1.5 Provide Management of Service Areas** (Frame Repository) → mt.pshvs_service_area_information: expected «IN» for this direction (or reverse the connector)
- «OUT» High_Level_Function **F3.6 Operate National Access Point** (Frame Repository) → tnap.cc-metadata_search_result: expected «IN» for this direction (or reverse the connector)
- «OUT» High_Level_Function **F3.6 Operate National Access Point** (Frame Repository) → tnap.cc-support_response: expected «IN» for this direction (or reverse the connector)
- «OUT» High_Level_Function **F3.6 Operate National Access Point** (Frame Repository) → tnap.cp-metadata_&_success_report: expected «IN» for this direction (or reverse the connector)
- «OUT» High_Level_Function **F3.6 Operate National Access Point** (Frame Repository) → tnap.cp-registration_response: expected «IN» for this direction (or reverse the connector)
- «OUT» High_Level_Function **F3.6 Operate National Access Point** (Frame Repository) → tnap.cp-support_response: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F3.1.5.3 Output Service Area Messages** (Frame Repository) → mt.pshvs_service_area_information: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F3.6.2 Manage Registrations and Provide Authorisation Service** (Frame Repository) → tnap.cp-registration_response: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F3.6.3 Manage Content Providers Metadata** (Frame Repository) → tnap.cp-metadata_&_success_report: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F3.6.5 Provide NAP User Support** (Frame Repository) → tnap.cc-support_response: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F3.6.5 Provide NAP User Support** (Frame Repository) → tnap.cp-support_response: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F5.11.11 Monitor Status of Driver** (Frame Repository) → pshvs_request_driver_stored_data: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F5.11.13 Manage Operational Data Store** (Frame Repository) → pshvs_driver_condition: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F5.11.13 Manage Operational Data Store** (Frame Repository) → pshvs_load_operational_data: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F5.11.13 Manage Operational Data Store** (Frame Repository) → pshvs_tvd_incident_data: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F5.11.6 Provide Incident Related Data** (Frame Repository) → pshvs_request_tvd_incident_data: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F5.11.7 Provide In-vehicle eCall Facilities** (Frame Repository) → pshvs_request_driver_condition: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F8.4.3 Provide Freight Transport Operations Manager Interface** (Frame Repository) → tft.ftom-prepared_new_FTEP: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F8.4.3 Provide Freight Transport Operations Manager Interface** (Frame Repository) → tft.ftom-requested_existing_FTEP: expected «IN» for this direction (or reverse the connector)
- «OUT» System **System** (Frame Repository) → To NAP Actors: expected «IN» for this direction (or reverse the connector)
- «OUT» Terminator **NAP Actors** (Frame Repository) → tnap-mt_outputs: expected «IN» for this direction (or reverse the connector)
- «OUT» Terminator **NAP Actors** (NAP Reference Architecture) → tnap-mt_outputs: expected «IN» for this direction (or reverse the connector)
- «OUT» Terminator **NAP Content Consumer** (Frame Repository) → fnap.cc-data_request: expected «IN» for this direction (or reverse the connector)

</details>

<details><summary><b>self-reference</b> (1)</summary>

- Low_Level_Function **F8.4.1 Provide Freight Transport User Interface** (Frame Repository) has a Association «belongsto» to itself

</details>

<details><summary><b>servedby</b> (18)</summary>

- User_Need **11.1.1.6** (C-ITS Reference Architecture) → F3.1.1.5 Provide Urban Traffic Management Facilities is Usage «», expected Association «Servedby»
- User_Need **11.1.1.6** (C-ITS Reference Architecture) → F5.16.1 Manage Communication from Vehicle to Driver is Usage «», expected Association «Servedby»
- User_Need **11.1.1.6** (C-ITS Reference Architecture) → F5.16.2 Output Commands and Dynamic Warnings is Usage «», expected Association «Servedby»
- User_Need **11.1.4.1** (C-ITS Reference Architecture) → F5.16.1 Manage Communication from Vehicle to Driver is Usage «», expected Association «Servedby»
- User_Need **11.1.4.1** (C-ITS Reference Architecture) → F5.16.2 Output Commands and Dynamic Warnings is Usage «», expected Association «Servedby»
- User_Need **11.2.4.1** (C-ITS Reference Architecture) → F3.1 Provide Traffic Control is Usage «», expected Association «Servedby»
- User_Need **11.2.4.1** (C-ITS Reference Architecture) → F5.16.1 Manage Communication from Vehicle to Driver is Usage «», expected Association «Servedby»
- User_Need **11.2.4.1** (C-ITS Reference Architecture) → F5.16.2 Output Commands and Dynamic Warnings is Usage «», expected Association «Servedby»
- User_Need **11.2.4.1** (C-ITS Reference Architecture) → F9.3 Manage Vehicle Access to Sensitive Areas is Usage «», expected Association «Servedby»
- User_Need **6.5.1.1** (Frame Repository) → F3.6.4 Manage Metadata Retrieval is Aggregation «componentof», expected Association «Servedby»
- User_Need **6.5.1.2** (Frame Repository) → F3.6.4 Manage Metadata Retrieval is Aggregation «componentof», expected Association «Servedby»
- User_Need **6.5.1.3** (Frame Repository) → F3.6.4 Manage Metadata Retrieval is Aggregation «componentof», expected Association «Servedby»
- User_Need **6.5.1.6** (Frame Repository) → F3.6.4 Manage Metadata Retrieval is Aggregation «componentof», expected Association «Servedby»
- User_Need **6.5.1.8** (Frame Repository) → F3.6.4 Manage Metadata Retrieval is Aggregation «componentof», expected Association «Servedby»
- User_Need **9.10.1.3** (Frame Repository) → F8.6.4 Provide Interface to Other Transport Modes is Association «belongsto», expected Association «Servedby»
- User_Need **9.11.1.14** (Frame Repository) → F8.6.6 Manage Incident Response Data Store is Association «belongsto», expected Association «Servedby»
- User_Need **9.11.1.15** (Frame Repository) → F8.6.5 Provide FTOM Interface for FTEP Monitoring is Association «belongsto», expected Association «Servedby»
- User_Need **9.11.1.9** (Frame Repository) → F8.6.1 Implement FTEP is Association «belongsto», expected Association «Servedby»

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

<details><summary><b>in-out</b> (23)</summary>

- «IN» Low_Level_Data_Flow **fnap.cc-metadata_search_request** (NAP Reference Architecture) → F3.6 Operate National Access Point: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fnap.cc-support_request** (NAP Reference Architecture) → F3.6 Operate National Access Point: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fnap.cc-support_request** (NAP Reference Architecture) → F3.6.5 Provide NAP User Support: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fnap.cp-metadata_&_authorisation_credentials** (NAP Reference Architecture) → F3.6 Operate National Access Point: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fnap.cp-metadata_&_authorisation_credentials** (NAP Reference Architecture) → F3.6.3 Manage Content Providers Metadata: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fnap.cp-registration_request** (NAP Reference Architecture) → F3.6 Operate National Access Point: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fnap.cp-registration_request** (NAP Reference Architecture) → F3.6.2 Manage Registrations and Provide Authorisation Service: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fnap.cp-support_request** (NAP Reference Architecture) → F3.6 Operate National Access Point: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **fnap.cp-support_request** (NAP Reference Architecture) → F3.6.5 Provide NAP User Support: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **mt_load_NAP_user_data** (NAP Reference Architecture) → D3.17 NAP Users: expected «OUT» for this direction (or reverse the connector)
- «IN» Low_Level_Data_Flow **tnap.cc-data_response** (NAP Reference Architecture) → NAP Content Consumer: expected «OUT» for this direction (or reverse the connector)
- «OUT» Datastore **D3.17 NAP Users** (NAP Reference Architecture) → mt_read_NAP_user_data: expected «IN» for this direction (or reverse the connector)
- «OUT» High_Level_Function **F3.6 Operate National Access Point** (NAP Reference Architecture) → tnap.cc-metadata_search_result: expected «IN» for this direction (or reverse the connector)
- «OUT» High_Level_Function **F3.6 Operate National Access Point** (NAP Reference Architecture) → tnap.cc-support_response: expected «IN» for this direction (or reverse the connector)
- «OUT» High_Level_Function **F3.6 Operate National Access Point** (NAP Reference Architecture) → tnap.cp-metadata_&_success_report: expected «IN» for this direction (or reverse the connector)
- «OUT» High_Level_Function **F3.6 Operate National Access Point** (NAP Reference Architecture) → tnap.cp-registration_response: expected «IN» for this direction (or reverse the connector)
- «OUT» High_Level_Function **F3.6 Operate National Access Point** (NAP Reference Architecture) → tnap.cp-support_response: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F3.6.2 Manage Registrations and Provide Authorisation Service** (NAP Reference Architecture) → tnap.cp-registration_response: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F3.6.3 Manage Content Providers Metadata** (NAP Reference Architecture) → tnap.cp-metadata_&_success_report: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F3.6.5 Provide NAP User Support** (NAP Reference Architecture) → tnap.cc-support_response: expected «IN» for this direction (or reverse the connector)
- «OUT» Low_Level_Function **F3.6.5 Provide NAP User Support** (NAP Reference Architecture) → tnap.cp-support_response: expected «IN» for this direction (or reverse the connector)
- «OUT» Terminator **NAP Actors** (NAP Reference Architecture) → tnap-mt_outputs: expected «IN» for this direction (or reverse the connector)
- «OUT» Terminator **NAP Content Consumer** (NAP Reference Architecture) → fnap.cc-data_request: expected «IN» for this direction (or reverse the connector)

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

- connector stereotype written in 2 ways: «Servedby» 1746×, «served by» 128×
- connector stereotype written in 2 ways: «belongsto» 872×, «belongs to» 5×
- connector stereotype written in 3 ways: «Componentof» 1857×, «componentof» 609×, «component of» 157×

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

