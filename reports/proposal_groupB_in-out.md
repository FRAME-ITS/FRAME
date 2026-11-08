# Proposal – IN/OUT connectors against the convention (#69)

Convention (prevailing use in V5.2): **«IN» producer → data flow**, **«OUT» data flow → consumer** – the arrow follows the data.
For every deviating connector the role of the function/terminator is derived from the data flow naming convention
(`f<terminator>-…` from, `t<terminator>-…` to a terminator, `abc.def-…` from area abc to area def) and from the other links of the same flow.

153 connectors. **No change has been made yet** – group B is applied only after review.

| Scope | Confidence | Proposed action | Count |
|---|---|---|---|
| FRAME Repository | conflict | review | 10 |
| FRAME Repository | high | relabel | 12 |
| FRAME Repository | high | reverse | 2 |
| FRAME Repository | medium | relabel | 65 |
| FRAME Repository | medium | reverse | 18 |
| FRAME Repository | unknown | review | 21 |
| Reference architectures | high | relabel | 17 |
| Reference architectures | medium | relabel | 5 |
| Reference architectures | medium | reverse | 1 |
| Reference architectures | unknown | review | 2 |

| Scope | Flow | Endpoint | Now | Proposed | Confidence | Evidence |
|---|---|---|---|---|---|---|
| FRAME Repository | fmms-mpto_control_inputs | F4.4 Control PT Fleet | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | high | flow "fmms-mpto_co…" from a terminator into the system; flow already has a producer |
| FRAME Repository | fnap.cc-support_request | F3.6 Operate National Access Point | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | high | flow "fnap.cc-supp…" from a terminator into the system; flow already has a producer |
| FRAME Repository | fnap.cc-support_request | F3.6.5 Provide NAP User Support | «IN» flow→Low_Level_Function | relabel «IN» → «OUT» | high | flow "fnap.cc-supp…" from a terminator into the system; flow already has a producer |
| FRAME Repository | fnap.cp-metadata_&_authorisation_credentials | F3.6.3 Manage Content Providers Metadata | «IN» flow→Low_Level_Function | relabel «IN» → «OUT» | high | flow "fnap.cp-meta…" from a terminator into the system; flow already has a producer |
| FRAME Repository | fnap.cp-metadata_&_authorisation_credentials | F3.6 Operate National Access Point | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | high | flow "fnap.cp-meta…" from a terminator into the system; flow already has a producer |
| FRAME Repository | fnap.cp-support_request | F3.6 Operate National Access Point | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | high | flow "fnap.cp-supp…" from a terminator into the system; flow already has a producer |
| FRAME Repository | fnap.cp-support_request | F3.6.5 Provide NAP User Support | «IN» flow→Low_Level_Function | relabel «IN» → «OUT» | high | flow "fnap.cp-supp…" from a terminator into the system; flow already has a producer |
| FRAME Repository | tnap-mt_outputs | NAP Actors | «OUT» Terminator→flow | reverse direction (keep label) | high | flow name "tnap-mt_outp…" = to terminator; flow already has a producer |
| FRAME Repository | tnap-mt_outputs | NAP Actors | «OUT» Terminator→flow | reverse direction (keep label) | high | flow name "tnap-mt_outp…" = to terminator; flow already has a producer |
| FRAME Repository | tnap.cc-data_response | NAP Content Consumer | «IN» flow→Terminator | relabel «IN» → «OUT» | high | flow name "tnap.cc-data…" = to terminator; flow already has a producer |
| FRAME Repository | tnap.cc-support_response | F3.6 Operate National Access Point | «OUT» High_Level_Function→flow | relabel «OUT» → «IN» | high | flow "tnap.cc-supp…" from the system to a terminator; flow already has a consumer |
| FRAME Repository | tnap.cc-support_response | F3.6.5 Provide NAP User Support | «OUT» Low_Level_Function→flow | relabel «OUT» → «IN» | high | flow "tnap.cc-supp…" from the system to a terminator; flow already has a consumer |
| FRAME Repository | tnap.cp-support_response | F3.6 Operate National Access Point | «OUT» High_Level_Function→flow | relabel «OUT» → «IN» | high | flow "tnap.cp-supp…" from the system to a terminator; flow already has a consumer |
| FRAME Repository | tnap.cp-support_response | F3.6.5 Provide NAP User Support | «OUT» Low_Level_Function→flow | relabel «OUT» → «IN» | high | flow "tnap.cp-supp…" from the system to a terminator; flow already has a consumer |
| FRAME Repository | From NAP Actors | System | «IN» flow→System | relabel «IN» → «OUT» | medium | flow already has a producer |
| FRAME Repository | To NAP Actors | System | «OUT» System→flow | relabel «OUT» → «IN» | medium | flow already has a consumer |
| FRAME Repository | fae-tunnel_atmospheric_conditions | F3.1.7 Provide Traffic Management for Tunnels | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fae-tunnel_a…" from a terminator into the system |
| FRAME Repository | fbti.tms-tunnel_system_inputs | F3.1.7 Provide Traffic Management for Tunnels | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fbti.tms-tun…" from a terminator into the system |
| FRAME Repository | fd-carpark_space_payment | F3.1.4 Provide Management of Car Parks | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fd-carpark_s…" from a terminator into the system |
| FRAME Repository | fd.ptd-assign_vehicle_to_service | F4.1 Monitor PT fleet | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fd.ptd-assig…" from a terminator into the system |
| FRAME Repository | fd.ptd-driver_status | F4.3 Provide PT Management | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fd.ptd-drive…" from a terminator into the system |
| FRAME Repository | fd.ptd-request_fares | F4.5 Provide PT Fare Facilities | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fd.ptd-reque…" from a terminator into the system |
| FRAME Repository | fesp.b-urban_traffic_information_request | F3.1.1 Provide Urban Traffic Management | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fesp.b-urban…" from a terminator into the system |
| FRAME Repository | fesp.dvip-vehicle_data_for_inter-urban_fcd_check | F3.1.2 Provide Inter-urban Traffic Management | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fesp.dvip-ve…" from a terminator into the system |
| FRAME Repository | fesp.dvip-vehicle_data_for_urban_fcd_check | F3.1.1 Provide Urban Traffic Management | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fesp.dvip-ve…" from a terminator into the system |
| FRAME Repository | fesp.g-map_data_for_vehicle_sensor_data | F5.15 Provide In-vehicle Detection and Analysis | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fesp.g-map_d…" from a terminator into the system |
| FRAME Repository | fesp.g-static_road_information | F5.13 Provide Vehicle Data and ISA | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fesp.g-stati…" from a terminator into the system |
| FRAME Repository | fesp.g-vehicle_trip_plan_implementation_map_data | F5.14 Provide In-vehicle Trip Planning & Implementation | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fesp.g-vehic…" from a terminator into the system |
| FRAME Repository | ffc-carpark_space_payment_response | F3.1.4 Provide Management of Car Parks | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "ffc-carpark_…" from a terminator into the system |
| FRAME Repository | ffc-confirmed_fare_payment | F4.5 Provide PT Fare Facilities | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "ffc-confirme…" from a terminator into the system |
| FRAME Repository | ffc-demand_service_payment_confirmed | F4.7 Provide On-demand Services | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "ffc-demand_s…" from a terminator into the system |
| FRAME Repository | ffc-mt_inputs | F3. Manage Traffic | «IN» flow→Functional_Area | relabel «IN» → «OUT» | medium | flow "ffc-mt_input…" from a terminator into the system |
| FRAME Repository | flds-location_data_for_vehicle_sensor_data | F5.15 Provide In-vehicle Detection and Analysis | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "flds-locatio…" from a terminator into the system |
| FRAME Repository | flds-on-demand_service_vehicle_location | F4.7 Provide On-demand Services | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "flds-on-dema…" from a terminator into the system |
| FRAME Repository | flds-vehicle_location_for_trip_monitoring | F5.14 Provide In-vehicle Trip Planning & Implementation | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "flds-vehicle…" from a terminator into the system |
| FRAME Repository | flds-vehicle_sharer_location | F4.6 Provide Facilities for Vehicle Sharing | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "flds-vehicle…" from a terminator into the system |
| FRAME Repository | fmms.mmc-crossing_request | Multi-Modal Crossing | «IN» flow→Terminator | reverse direction (keep label) | medium | flow name "fmms.mmc-cro…" = from terminator |
| FRAME Repository | fmms.mmc-inter-urban_crossing_request | Multi-Modal Crossing | «IN» flow→Terminator | reverse direction (keep label) | medium | flow name "fmms.mmc-int…" = from terminator |
| FRAME Repository | fmms.mmc-urban_crossing_command | Multi-Modal Crossing | «IN» flow→Terminator | reverse direction (keep label) | medium | flow name "fmms.mmc-urb…" = from terminator |
| FRAME Repository | fmms.mmc-urban_crossing_information | Multi-Modal Crossing | «IN» flow→Terminator | reverse direction (keep label) | medium | flow name "fmms.mmc-urb…" = from terminator |
| FRAME Repository | fmms.mmc-urban_crossing_inputs | Multi-Modal Crossing | «IN» flow→Terminator | reverse direction (keep label) | medium | flow name "fmms.mmc-urb…" = from terminator |
| FRAME Repository | fmms.mms-PT_service_change_request | Multi-Modal Management System | «IN» flow→Terminator | reverse direction (keep label) | medium | flow name "fmms.mms-PT_…" = from terminator |
| FRAME Repository | fmms.mms-accident_information | Multi-Modal Management System | «IN» flow→Terminator | reverse direction (keep label) | medium | flow name "fmms.mms-acc…" = from terminator |
| FRAME Repository | fmms.mms-control_parameters | Multi-Modal Management System | «IN» flow→Terminator | reverse direction (keep label) | medium | flow name "fmms.mms-con…" = from terminator |
| FRAME Repository | fmms.mms-current_service_status | Multi-Modal Management System | «IN» flow→Terminator | reverse direction (keep label) | medium | flow name "fmms.mms-cur…" = from terminator |
| FRAME Repository | fmms.mms-data_for_demand_services | Multi-Modal Management System | «IN» flow→Terminator | reverse direction (keep label) | medium | flow name "fmms.mms-dat…" = from terminator |
| FRAME Repository | fmms.mms-demand_inputs | Multi-Modal Management System | «IN» flow→Terminator | reverse direction (keep label) | medium | flow name "fmms.mms-dem…" = from terminator |
| FRAME Repository | fmms.mms-ferry_service_information | Multi-Modal Management System | «IN» flow→Terminator | reverse direction (keep label) | medium | flow name "fmms.mms-fer…" = from terminator |
| FRAME Repository | fmms.mms-incident_inputs | Multi-Modal Management System | «IN» flow→Terminator | reverse direction (keep label) | medium | flow name "fmms.mms-inc…" = from terminator |
| FRAME Repository | fmms.mms-plannings | Multi-Modal Management System | «IN» flow→Terminator | reverse direction (keep label) | medium | flow name "fmms.mms-pla…" = from terminator |
| FRAME Repository | fmms.mms-rail_service_information | Multi-Modal Management System | «IN» flow→Terminator | reverse direction (keep label) | medium | flow name "fmms.mms-rai…" = from terminator |
| FRAME Repository | fmms.mms-service_change_request_response | Multi-Modal Management System | «IN» flow→Terminator | reverse direction (keep label) | medium | flow name "fmms.mms-ser…" = from terminator |
| FRAME Repository | fmms.mms-service_details_response | Multi-Modal Management System | «IN» flow→Terminator | reverse direction (keep label) | medium | flow name "fmms.mms-ser…" = from terminator |
| FRAME Repository | fmms.mms-strike_details | Multi-Modal Management System | «IN» flow→Terminator | reverse direction (keep label) | medium | flow name "fmms.mms-str…" = from terminator |
| FRAME Repository | fnap.cc-data_request | NAP Content Consumer | «OUT» Terminator→flow | relabel «OUT» → «IN» | medium | flow name "fnap.cc-data…" = from terminator |
| FRAME Repository | fnap.cc-metadata_search_request | F3.6 Operate National Access Point | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fnap.cc-meta…" from a terminator into the system |
| FRAME Repository | fnap.cp-registration_request | F3.6.2 Manage Registrations and Provide Authorisation Service | «IN» flow→Low_Level_Function | relabel «IN» → «OUT» | medium | flow "fnap.cp-regi…" from a terminator into the system |
| FRAME Repository | fnap.cp-registration_request | F3.6 Operate National Access Point | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fnap.cp-regi…" from a terminator into the system |
| FRAME Repository | fo.co-PSAP_data_inputs | F2.1.11 Manage eCall Messages | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fo.co-PSAP_d…" from a terminator into the system |
| FRAME Repository | fo.co-request_PSAP_data_output | F2.1.11 Manage eCall Messages | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fo.co-reques…" from a terminator into the system |
| FRAME Repository | fo.eo-request_statistical_report | F2.1 Manage Emergencies | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fo.eo-reques…" from a terminator into the system |
| FRAME Repository | fo.eo-stop_stolen_vehicle | F2.2 Manage Stolen Vehicle Notification | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fo.eo-stop_s…" from a terminator into the system |
| FRAME Repository | fo.rno-inter-urban_road_static_network_data | F3.1.2.13 Manage Inter-urban Traffic Strategies | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fo.rno-inter…" from a terminator into the system |
| FRAME Repository | fors.pts-arrival_prediction_data | F4.1 Monitor PT fleet | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fors.pts-arr…" from a terminator into the system |
| FRAME Repository | fors.tsc-local_priority_request_details | F3.1.1.5 Provide Urban Traffic Management Facilities | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fors.tsc-loc…" from a terminator into the system |
| FRAME Repository | fors.tss-traffic_prediction_results | F3.1.6 Provide Traffic Predictions | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fors.tss-tra…" from a terminator into the system |
| FRAME Repository | fre-roadside_speed_indication_details | F5.13 Provide Vehicle Data and ISA | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fre-roadside…" from a terminator into the system |
| FRAME Repository | frp-guidance_data | F5.12.12 Collect Road Network Information | «IN» flow→Low_Level_Function | relabel «IN» → «OUT» | medium | flow "frp-guidance…" from a terminator into the system |
| FRAME Repository | frp-local_vehicle_road_surface_conditions | F5.15 Provide In-vehicle Detection and Analysis | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "frp-local_ve…" from a terminator into the system |
| FRAME Repository | ft.p-presence_indication | F5.15 Provide In-vehicle Detection and Analysis | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "ft.p-presenc…" from a terminator into the system |
| FRAME Repository | ftrfc-freight_vehicle_identity_for_rest_area | F3.1.5 Provide Management of Service Areas | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "ftrfc-freigh…" from a terminator into the system |
| FRAME Repository | ftrfc-inter-urban_local_data_for_ramp_metering | F3.1.2.13 Manage Inter-urban Traffic Strategies | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "ftrfc-inter-…" from a terminator into the system |
| FRAME Repository | ftrfc-inter-urban_vehicle_presence_for_messages | F3.1.2.14 Implement Inter-urban Management Traffic Strategy | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "ftrfc-inter-…" from a terminator into the system |
| FRAME Repository | ftrfc-traffic_conditions_in_tunnel | F3.1.7 Provide Traffic Management for Tunnels | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "ftrfc-traffi…" from a terminator into the system |
| FRAME Repository | fv-identity_for_inter-urban_zone_access | F3.1.2.13 Manage Inter-urban Traffic Strategies | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fv-identity_…" from a terminator into the system |
| FRAME Repository | fv-identity_for_urban_zone_access | F3.1.1.5 Provide Urban Traffic Management Facilities | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fv-identity_…" from a terminator into the system |
| FRAME Repository | fv.fv-freight_vehicle_identity_for_rest_area | F3.1.5 Provide Management of Service Areas | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fv.fv-freigh…" from a terminator into the system |
| FRAME Repository | fve.onv-vehicle_presence_indication | F5.15 Provide In-vehicle Detection and Analysis | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fve.onv-vehi…" from a terminator into the system |
| FRAME Repository | fve.oru-presence_indication | F5.15 Provide In-vehicle Detection and Analysis | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fve.oru-pres…" from a terminator into the system |
| FRAME Repository | fve.so-object_presence_indication | F5.15 Provide In-vehicle Detection and Analysis | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fve.so-objec…" from a terminator into the system |
| FRAME Repository | fws-mpto_inputs | F4. Manage Public Transport Operations | «IN» flow→Functional_Area | relabel «IN» → «OUT» | medium | flow "fws-mpto_inp…" from a terminator into the system |
| FRAME Repository | fws-weather_conditions_for_ISA | F5.13 Provide Vehicle Data and ISA | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fws-weather_…" from a terminator into the system |
| FRAME Repository | mt.pshvs_service_area_information | F5.16.1 Manage Communication from Vehicle to Driver | «IN» flow→Low_Level_Function | relabel «IN» → «OUT» | medium | flow mt→pshvs, function in pshvs |
| FRAME Repository | mt.pshvs_service_area_information | F3.1.5.3 Output Service Area Messages | «OUT» Low_Level_Function→flow | relabel «OUT» → «IN» | medium | flow mt→pshvs, function in mt |
| FRAME Repository | mt.pshvs_service_area_information | F3.1.5 Provide Management of Service Areas | «OUT» High_Level_Function→flow | relabel «OUT» → «IN» | medium | flow mt→pshvs, function in mt |
| FRAME Repository | mt_load_NAP_user_data | D3.17 NAP Users | «IN» flow→Datastore | relabel «IN» → «OUT» | medium | flow already has a producer |
| FRAME Repository | mt_read_NAP_user_data | D3.17 NAP Users | «OUT» Datastore→flow | relabel «OUT» → «IN» | medium | flow already has a consumer |
| FRAME Repository | psef.mpto_alarm_acknowledgements | F4. Manage Public Transport Operations | «IN» flow→Functional_Area | relabel «IN» → «OUT» | medium | flow psef→mpto, function in mpto |
| FRAME Repository | pshvs.mt_inter-urban_xfcd | F3.1.2 Provide Inter-urban Traffic Management | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow pshvs→mt, function in mt |
| FRAME Repository | pshvs.mt_outputs_to_driver_via_roadside | F3.1 Provide Traffic Control | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow pshvs→mt, function in mt |
| FRAME Repository | pshvs.psef_eCall_message | F2.1.11 Manage eCall Messages | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow pshvs→psef, function in psef |
| FRAME Repository | pshvs_driver_condition | F5.11.13 Manage Operational Data Store | «OUT» Low_Level_Function→flow | relabel «OUT» → «IN» | medium | flow already has a consumer |
| FRAME Repository | pshvs_tvd_incident_data | F5.11.13 Manage Operational Data Store | «OUT» Low_Level_Function→flow | relabel «OUT» → «IN» | medium | flow already has a consumer |
| FRAME Repository | pshvs_tvd_scenario | F5.11.13 Manage Operational Data Store | «IN» flow→Low_Level_Function | relabel «IN» → «OUT» | medium | flow already has a producer |
| FRAME Repository | tnap.cc-metadata_search_result | F3.6 Operate National Access Point | «OUT» High_Level_Function→flow | relabel «OUT» → «IN» | medium | flow "tnap.cc-meta…" from the system to a terminator |
| FRAME Repository | tnap.cp-metadata_&_success_report | F3.6.3 Manage Content Providers Metadata | «OUT» Low_Level_Function→flow | relabel «OUT» → «IN» | medium | flow "tnap.cp-meta…" from the system to a terminator |
| FRAME Repository | tnap.cp-metadata_&_success_report | F3.6 Operate National Access Point | «OUT» High_Level_Function→flow | relabel «OUT» → «IN» | medium | flow "tnap.cp-meta…" from the system to a terminator |
| FRAME Repository | fft.ftom-incident_responses | F8.6.5 Provide FTOM Interface for FTEP Monitoring | «IN» flow→Low_Level_Function | review in EA | conflict | flow "fft.ftom-inc…" from a terminator into the system; flow already has a consumer |
| FRAME Repository | fft.ftom-prepare_new_FTEP | F8.4.3 Provide Freight Transport Operations Manager Interface | «IN» flow→Low_Level_Function | review in EA | conflict | flow "fft.ftom-pre…" from a terminator into the system; flow already has a consumer |
| FRAME Repository | fft.ftom-request_existing_FTEP | F8.4.3 Provide Freight Transport Operations Manager Interface | «IN» flow→Low_Level_Function | review in EA | conflict | flow "fft.ftom-req…" from a terminator into the system; flow already has a consumer |
| FRAME Repository | fmms.mmc-inter-urban_crossing_request | F3.1.2.14 Implement Inter-urban Management Traffic Strategy | «IN» flow→High_Level_Function | review in EA | conflict | flow "fmms.mmc-int…" from a terminator into the system; flow already has a consumer |
| FRAME Repository | fmms.mms-data_for_demand_services | F4.7 Provide On-demand Services | «IN» flow→High_Level_Function | review in EA | conflict | flow "fmms.mms-dat…" from a terminator into the system; flow already has a consumer |
| FRAME Repository | fmms.mms-service_details_response | F4.6 Provide Facilities for Vehicle Sharing | «IN» flow→High_Level_Function | review in EA | conflict | flow "fmms.mms-ser…" from a terminator into the system; flow already has a consumer |
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
| NAP Reference Architecture | fnap.cc-support_request | F3.6.5 Provide NAP User Support | «IN» flow→Low_Level_Function | relabel «IN» → «OUT» | high | flow "fnap.cc-supp…" from a terminator into the system; flow already has a producer |
| NAP Reference Architecture | fnap.cc-support_request | F3.6 Operate National Access Point | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | high | flow "fnap.cc-supp…" from a terminator into the system; flow already has a producer |
| NAP Reference Architecture | fnap.cp-metadata_&_authorisation_credentials | F3.6.3 Manage Content Providers Metadata | «IN» flow→Low_Level_Function | relabel «IN» → «OUT» | high | flow "fnap.cp-meta…" from a terminator into the system; flow already has a producer |
| NAP Reference Architecture | fnap.cp-metadata_&_authorisation_credentials | F3.6 Operate National Access Point | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | high | flow "fnap.cp-meta…" from a terminator into the system; flow already has a producer |
| NAP Reference Architecture | fnap.cp-registration_request | F3.6.2 Manage Registrations and Provide Authorisation Service | «IN» flow→Low_Level_Function | relabel «IN» → «OUT» | high | flow "fnap.cp-regi…" from a terminator into the system; flow already has a producer |
| NAP Reference Architecture | fnap.cp-registration_request | F3.6 Operate National Access Point | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | high | flow "fnap.cp-regi…" from a terminator into the system; flow already has a producer |
| NAP Reference Architecture | fnap.cp-support_request | F3.6.5 Provide NAP User Support | «IN» flow→Low_Level_Function | relabel «IN» → «OUT» | high | flow "fnap.cp-supp…" from a terminator into the system; flow already has a producer |
| NAP Reference Architecture | fnap.cp-support_request | F3.6 Operate National Access Point | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | high | flow "fnap.cp-supp…" from a terminator into the system; flow already has a producer |
| NAP Reference Architecture | tnap.cc-data_response | NAP Content Consumer | «IN» flow→Terminator | relabel «IN» → «OUT» | high | flow name "tnap.cc-data…" = to terminator; flow already has a producer |
| NAP Reference Architecture | tnap.cc-support_response | F3.6.5 Provide NAP User Support | «OUT» Low_Level_Function→flow | relabel «OUT» → «IN» | high | flow "tnap.cc-supp…" from the system to a terminator; flow already has a consumer |
| NAP Reference Architecture | tnap.cc-support_response | F3.6 Operate National Access Point | «OUT» High_Level_Function→flow | relabel «OUT» → «IN» | high | flow "tnap.cc-supp…" from the system to a terminator; flow already has a consumer |
| NAP Reference Architecture | tnap.cp-metadata_&_success_report | F3.6.3 Manage Content Providers Metadata | «OUT» Low_Level_Function→flow | relabel «OUT» → «IN» | high | flow "tnap.cp-meta…" from the system to a terminator; flow already has a consumer |
| NAP Reference Architecture | tnap.cp-metadata_&_success_report | F3.6 Operate National Access Point | «OUT» High_Level_Function→flow | relabel «OUT» → «IN» | high | flow "tnap.cp-meta…" from the system to a terminator; flow already has a consumer |
| NAP Reference Architecture | tnap.cp-registration_response | F3.6.2 Manage Registrations and Provide Authorisation Service | «OUT» Low_Level_Function→flow | relabel «OUT» → «IN» | high | flow "tnap.cp-regi…" from the system to a terminator; flow already has a consumer |
| NAP Reference Architecture | tnap.cp-registration_response | F3.6 Operate National Access Point | «OUT» High_Level_Function→flow | relabel «OUT» → «IN» | high | flow "tnap.cp-regi…" from the system to a terminator; flow already has a consumer |
| NAP Reference Architecture | tnap.cp-support_response | F3.6.5 Provide NAP User Support | «OUT» Low_Level_Function→flow | relabel «OUT» → «IN» | high | flow "tnap.cp-supp…" from the system to a terminator; flow already has a consumer |
| NAP Reference Architecture | tnap.cp-support_response | F3.6 Operate National Access Point | «OUT» High_Level_Function→flow | relabel «OUT» → «IN» | high | flow "tnap.cp-supp…" from the system to a terminator; flow already has a consumer |
| NAP Reference Architecture | fnap.cc-data_request | NAP Content Consumer | «OUT» Terminator→flow | relabel «OUT» → «IN» | medium | flow name "fnap.cc-data…" = from terminator |
| NAP Reference Architecture | fnap.cc-metadata_search_request | F3.6 Operate National Access Point | «IN» flow→High_Level_Function | relabel «IN» → «OUT» | medium | flow "fnap.cc-meta…" from a terminator into the system |
| NAP Reference Architecture | mt_load_NAP_user_data | D3.17 NAP Users | «IN» flow→Datastore | relabel «IN» → «OUT» | medium | flow already has a producer |
| NAP Reference Architecture | mt_read_NAP_user_data | D3.17 NAP Users | «OUT» Datastore→flow | relabel «OUT» → «IN» | medium | flow already has a consumer |
| NAP Reference Architecture | tnap-mt_outputs | NAP Actors | «OUT» Terminator→flow | reverse direction (keep label) | medium | flow name "tnap-mt_outp…" = to terminator |
| NAP Reference Architecture | tnap.cc-metadata_search_result | F3.6 Operate National Access Point | «OUT» High_Level_Function→flow | relabel «OUT» → «IN» | medium | flow "tnap.cc-meta…" from the system to a terminator |
| FRAME Meta Model | FRAME_Low_Level_Data_Flow | Terminator/ Subterminator | «IN» flow→Terminator | review in EA | unknown |  |
| FRAME Meta Model | FRAME_Low_Level_Data_Flow | Terminator/ Subterminator | «OUT» Terminator→flow | review in EA | unknown |  |

## Other group B items (review, no automatic fix proposed)

### «componentof» still against the convention (#80, #81)

Links between two low-level data flows or other combinations where the whole and the part cannot be derived from the names.

- «Componentof» Low_Level_Data_Flow **flds-psef_location_data** (Frame Repository) → flds-emergency_call_location (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «Componentof» Low_Level_Data_Flow **flds-psef_location_data** (Frame Repository) → flds-emergency_vehicle_location (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «component of» Low_Level_Data_Flow **fo.co-PSAP_data_update** (Frame Repository) → fo.co-PSAP_data_inputs (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «componentof» Low_Level_Data_Flow **fo.co-request_PSAP_data_output** (Frame Repository) → fo.co-PSAP_data_inputs (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «componentof» Low_Level_Data_Flow **mt.mffo_current_inter-urban_traffic_data** (Frame Repository) → mt.mffo_current_road_network_data (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «componentof» Low_Level_Data_Flow **mt.mffo_current_urban_traffic_data** (Frame Repository) → mt.mffo_current_road_network_data (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «componentof» Low_Level_Data_Flow **mt.mffo_historic_intre-urban_traffic_data** (Frame Repository) → mt.mffo_historic_road_network_data (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «componentof» Low_Level_Data_Flow **mt.mffo_historic_urban_traffic_data** (Frame Repository) → mt.mffo_historic_road_network_data (Low_Level_Data_Flow) runs whole → part or between low-level flows

### User Need → function links of type Usage (C-ITS user needs 11.x, #87/#93)

The C-ITS user needs in the FRAME Repository use Usage links, partly to high-level functions. This may be intentional for the C-ITS reference architecture; decide whether they become «served by» links to low-level functions.

- User_Need **11.1.1.6** (C-ITS Reference Architecture) → F3.1.1.5 Provide Urban Traffic Management Facilities is Usage «», expected Association «Servedby»
- User_Need **11.1.1.6** (C-ITS Reference Architecture) → F5.16.1 Manage Communication from Vehicle to Driver is Usage «», expected Association «Servedby»
- User_Need **11.1.1.6** (C-ITS Reference Architecture) → F5.16.2 Output Commands and Dynamic Warnings is Usage «», expected Association «Servedby»
- User_Need **11.1.4.1** (C-ITS Reference Architecture) → F5.16.1 Manage Communication from Vehicle to Driver is Usage «», expected Association «Servedby»
- User_Need **11.1.4.1** (C-ITS Reference Architecture) → F5.16.2 Output Commands and Dynamic Warnings is Usage «», expected Association «Servedby»
- User_Need **11.2.4.1** (C-ITS Reference Architecture) → F3.1 Provide Traffic Control is Usage «», expected Association «Servedby»
- User_Need **11.2.4.1** (C-ITS Reference Architecture) → F5.16.1 Manage Communication from Vehicle to Driver is Usage «», expected Association «Servedby»
- User_Need **11.2.4.1** (C-ITS Reference Architecture) → F5.16.2 Output Commands and Dynamic Warnings is Usage «», expected Association «Servedby»
- User_Need **11.2.4.1** (C-ITS Reference Architecture) → F9.3 Manage Vehicle Access to Sensitive Areas is Usage «», expected Association «Servedby»
