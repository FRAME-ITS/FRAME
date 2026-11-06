# FRAME model changes HEAD → working copy

123 changes

| View | Changes |
|---|---|
| Frame Repository / Frame Functional View | 99 |
| NAP Reference Architecture / 02 NAP Functional View | 24 |

## Frame Repository / Frame Functional View

### Frame Repository/Frame Functional View/Data Flows/High Level Data Flows
- connection changed: ~~From NAP Actors → System (Association «IN»)~~ → **From NAP Actors → System (Association «OUT»)**
- connection changed: ~~ffc-mt_inputs → F3. Manage Traffic (Association «IN»)~~ → **ffc-mt_inputs → F3. Manage Traffic (Association «OUT»)**
- connection changed: ~~fmms-mpto_control_inputs → F4.4 Control PT Fleet (Association «IN»)~~ → **fmms-mpto_control_inputs → F4.4 Control PT Fleet (Association «OUT»)**
- connection changed: ~~fo.co-PSAP_data_inputs → F2.1.11 Manage eCall Messages (Association «IN»)~~ → **fo.co-PSAP_data_inputs → F2.1.11 Manage eCall Messages (Association «OUT»)**
- connection changed: ~~fws-mpto_inputs → F4. Manage Public Transport Operations (Association «IN»)~~ → **fws-mpto_inputs → F4. Manage Public Transport Operations (Association «OUT»)**
- connection changed: ~~psef.mpto_alarm_acknowledgements → F4. Manage Public Transport Operations (Association «IN»)~~ → **psef.mpto_alarm_acknowledgements → F4. Manage Public Transport Operations (Association «OUT»)**
- connection changed: ~~pshvs.mt_outputs_to_driver_via_roadside → F3.1 Provide Traffic Control (Association «IN»)~~ → **pshvs.mt_outputs_to_driver_via_roadside → F3.1 Provide Traffic Control (Association «OUT»)**
- connection changed: ~~NAP Actors → tnap-mt_outputs (Association «OUT»)~~ → **tnap-mt_outputs → NAP Actors (Association «OUT»)**
- connection changed: ~~NAP Actors → tnap-mt_outputs (Association «OUT»)~~ → **tnap-mt_outputs → NAP Actors (Association «OUT»)**

### Frame Repository/Frame Functional View/Data Flows/Low Level Data Flows
- connection changed: ~~fae-tunnel_atmospheric_conditions → F3.1.7 Provide Traffic Management for Tunnels (Association «IN»)~~ → **fae-tunnel_atmospheric_conditions → F3.1.7 Provide Traffic Management for Tunnels (Association «OUT»)**
- connection changed: ~~fbti.tms-tunnel_system_inputs → F3.1.7 Provide Traffic Management for Tunnels (Association «IN»)~~ → **fbti.tms-tunnel_system_inputs → F3.1.7 Provide Traffic Management for Tunnels (Association «OUT»)**
- connection changed: ~~fd-carpark_space_payment → F3.1.4 Provide Management of Car Parks (Association «IN»)~~ → **fd-carpark_space_payment → F3.1.4 Provide Management of Car Parks (Association «OUT»)**
- connection changed: ~~fd.ptd-assign_vehicle_to_service → F4.1 Monitor PT fleet (Association «IN»)~~ → **fd.ptd-assign_vehicle_to_service → F4.1 Monitor PT fleet (Association «OUT»)**
- connection changed: ~~fd.ptd-driver_status → F4.3 Provide PT Management (Association «IN»)~~ → **fd.ptd-driver_status → F4.3 Provide PT Management (Association «OUT»)**
- connection changed: ~~fd.ptd-request_fares → F4.5 Provide PT Fare Facilities (Association «IN»)~~ → **fd.ptd-request_fares → F4.5 Provide PT Fare Facilities (Association «OUT»)**
- connection changed: ~~fesp.b-urban_traffic_information_request → F3.1.1 Provide Urban Traffic Management (Association «IN»)~~ → **fesp.b-urban_traffic_information_request → F3.1.1 Provide Urban Traffic Management (Association «OUT»)**
- connection changed: ~~fesp.dvip-vehicle_data_for_inter-urban_fcd_check → F3.1.2 Provide Inter-urban Traffic Management (Association «IN»)~~ → **fesp.dvip-vehicle_data_for_inter-urban_fcd_check → F3.1.2 Provide Inter-urban Traffic Management (Association «OUT»)**
- connection changed: ~~fesp.dvip-vehicle_data_for_urban_fcd_check → F3.1.1 Provide Urban Traffic Management (Association «IN»)~~ → **fesp.dvip-vehicle_data_for_urban_fcd_check → F3.1.1 Provide Urban Traffic Management (Association «OUT»)**
- connection changed: ~~fesp.g-map_data_for_vehicle_sensor_data → F5.15 Provide In-vehicle Detection and Analysis (Association «IN»)~~ → **fesp.g-map_data_for_vehicle_sensor_data → F5.15 Provide In-vehicle Detection and Analysis (Association «OUT»)**
- connection changed: ~~fesp.g-static_road_information → F5.13 Provide Vehicle Data and ISA (Association «IN»)~~ → **fesp.g-static_road_information → F5.13 Provide Vehicle Data and ISA (Association «OUT»)**
- connection changed: ~~fesp.g-vehicle_trip_plan_implementation_map_data → F5.14 Provide In-vehicle Trip Planning & Implementation (Association «IN»)~~ → **fesp.g-vehicle_trip_plan_implementation_map_data → F5.14 Provide In-vehicle Trip Planning & Implementation (Association «OUT»)**
- connection changed: ~~ffc-carpark_space_payment_response → F3.1.4 Provide Management of Car Parks (Association «IN»)~~ → **ffc-carpark_space_payment_response → F3.1.4 Provide Management of Car Parks (Association «OUT»)**
- connection changed: ~~ffc-confirmed_fare_payment → F4.5 Provide PT Fare Facilities (Association «IN»)~~ → **ffc-confirmed_fare_payment → F4.5 Provide PT Fare Facilities (Association «OUT»)**
- connection changed: ~~ffc-demand_service_payment_confirmed → F4.7 Provide On-demand Services (Association «IN»)~~ → **ffc-demand_service_payment_confirmed → F4.7 Provide On-demand Services (Association «OUT»)**
- connection changed: ~~flds-location_data_for_vehicle_sensor_data → F5.15 Provide In-vehicle Detection and Analysis (Association «IN»)~~ → **flds-location_data_for_vehicle_sensor_data → F5.15 Provide In-vehicle Detection and Analysis (Association «OUT»)**
- connection changed: ~~flds-on-demand_service_vehicle_location → F4.7 Provide On-demand Services (Association «IN»)~~ → **flds-on-demand_service_vehicle_location → F4.7 Provide On-demand Services (Association «OUT»)**
- connection changed: ~~flds-vehicle_location_for_trip_monitoring → F5.14 Provide In-vehicle Trip Planning & Implementation (Association «IN»)~~ → **flds-vehicle_location_for_trip_monitoring → F5.14 Provide In-vehicle Trip Planning & Implementation (Association «OUT»)**
- connection changed: ~~flds-vehicle_sharer_location → F4.6 Provide Facilities for Vehicle Sharing (Association «IN»)~~ → **flds-vehicle_sharer_location → F4.6 Provide Facilities for Vehicle Sharing (Association «OUT»)**
- connection changed: ~~fnap.cc-metadata_search_request → F3.6 Operate National Access Point (Association «IN»)~~ → **fnap.cc-metadata_search_request → F3.6 Operate National Access Point (Association «OUT»)**
- connection changed: ~~fnap.cc-support_request → F3.6.5 Provide NAP User Support (Association «IN»)~~ → **fnap.cc-support_request → F3.6.5 Provide NAP User Support (Association «OUT»)**
- connection changed: ~~fnap.cc-support_request → F3.6 Operate National Access Point (Association «IN»)~~ → **fnap.cc-support_request → F3.6 Operate National Access Point (Association «OUT»)**
- connection changed: ~~fnap.cp-metadata_&_authorisation_credentials → F3.6 Operate National Access Point (Association «IN»)~~ → **fnap.cp-metadata_&_authorisation_credentials → F3.6 Operate National Access Point (Association «OUT»)**
- connection changed: ~~fnap.cp-metadata_&_authorisation_credentials → F3.6.3 Manage Content Providers Metadata (Association «IN»)~~ → **fnap.cp-metadata_&_authorisation_credentials → F3.6.3 Manage Content Providers Metadata (Association «OUT»)**
- connection changed: ~~fnap.cp-registration_request → F3.6 Operate National Access Point (Association «IN»)~~ → **fnap.cp-registration_request → F3.6 Operate National Access Point (Association «OUT»)**
- connection changed: ~~fnap.cp-registration_request → F3.6.2 Manage Registrations and Provide Authorisation Service (Association «IN»)~~ → **fnap.cp-registration_request → F3.6.2 Manage Registrations and Provide Authorisation Service (Association «OUT»)**
- connection changed: ~~fnap.cp-support_request → F3.6.5 Provide NAP User Support (Association «IN»)~~ → **fnap.cp-support_request → F3.6.5 Provide NAP User Support (Association «OUT»)**
- connection changed: ~~fnap.cp-support_request → F3.6 Operate National Access Point (Association «IN»)~~ → **fnap.cp-support_request → F3.6 Operate National Access Point (Association «OUT»)**
- connection changed: ~~fo.co-request_PSAP_data_output → F2.1.11 Manage eCall Messages (Association «IN»)~~ → **fo.co-request_PSAP_data_output → F2.1.11 Manage eCall Messages (Association «OUT»)**
- connection changed: ~~fo.eo-request_statistical_report → F2.1 Manage Emergencies (Association «IN»)~~ → **fo.eo-request_statistical_report → F2.1 Manage Emergencies (Association «OUT»)**
- connection changed: ~~fo.eo-stop_stolen_vehicle → F2.2 Manage Stolen Vehicle Notification (Association «IN»)~~ → **fo.eo-stop_stolen_vehicle → F2.2 Manage Stolen Vehicle Notification (Association «OUT»)**
- connection changed: ~~fo.rno-inter-urban_road_static_network_data → F3.1.2.13 Manage Inter-urban Traffic Strategies (Association «IN»)~~ → **fo.rno-inter-urban_road_static_network_data → F3.1.2.13 Manage Inter-urban Traffic Strategies (Association «OUT»)**
- connection changed: ~~fors.pts-arrival_prediction_data → F4.1 Monitor PT fleet (Association «IN»)~~ → **fors.pts-arrival_prediction_data → F4.1 Monitor PT fleet (Association «OUT»)**
- connection changed: ~~fors.tsc-local_priority_request_details → F3.1.1.5 Provide Urban Traffic Management Facilities (Association «IN»)~~ → **fors.tsc-local_priority_request_details → F3.1.1.5 Provide Urban Traffic Management Facilities (Association «OUT»)**
- connection changed: ~~fors.tss-traffic_prediction_results → F3.1.6 Provide Traffic Predictions (Association «IN»)~~ → **fors.tss-traffic_prediction_results → F3.1.6 Provide Traffic Predictions (Association «OUT»)**
- connection changed: ~~fre-roadside_speed_indication_details → F5.13 Provide Vehicle Data and ISA (Association «IN»)~~ → **fre-roadside_speed_indication_details → F5.13 Provide Vehicle Data and ISA (Association «OUT»)**
- connection removed: frp-guidance_data → F5.12.12 Collect Road Network Information (Association «IN»)
- connection changed: ~~frp-local_vehicle_road_surface_conditions → F5.15 Provide In-vehicle Detection and Analysis (Association «IN»)~~ → **frp-local_vehicle_road_surface_conditions → F5.15 Provide In-vehicle Detection and Analysis (Association «OUT»)**
- connection changed: ~~ft.p-presence_indication → F5.15 Provide In-vehicle Detection and Analysis (Association «IN»)~~ → **ft.p-presence_indication → F5.15 Provide In-vehicle Detection and Analysis (Association «OUT»)**
- connection changed: ~~ftrfc-freight_vehicle_identity_for_rest_area → F3.1.5 Provide Management of Service Areas (Association «IN»)~~ → **ftrfc-freight_vehicle_identity_for_rest_area → F3.1.5 Provide Management of Service Areas (Association «OUT»)**
- connection changed: ~~ftrfc-inter-urban_local_data_for_ramp_metering → F3.1.2.13 Manage Inter-urban Traffic Strategies (Association «IN»)~~ → **ftrfc-inter-urban_local_data_for_ramp_metering → F3.1.2.13 Manage Inter-urban Traffic Strategies (Association «OUT»)**
- connection changed: ~~ftrfc-inter-urban_vehicle_presence_for_messages → F3.1.2.14 Implement Inter-urban Management Traffic Strategy (Association «IN»)~~ → **ftrfc-inter-urban_vehicle_presence_for_messages → F3.1.2.14 Implement Inter-urban Management Traffic Strategy (Association «OUT»)**
- connection changed: ~~ftrfc-traffic_conditions_in_tunnel → F3.1.7 Provide Traffic Management for Tunnels (Association «IN»)~~ → **ftrfc-traffic_conditions_in_tunnel → F3.1.7 Provide Traffic Management for Tunnels (Association «OUT»)**
- connection changed: ~~fv-identity_for_inter-urban_zone_access → F3.1.2.13 Manage Inter-urban Traffic Strategies (Association «IN»)~~ → **fv-identity_for_inter-urban_zone_access → F3.1.2.13 Manage Inter-urban Traffic Strategies (Association «OUT»)**
- connection changed: ~~fv-identity_for_urban_zone_access → F3.1.1.5 Provide Urban Traffic Management Facilities (Association «IN»)~~ → **fv-identity_for_urban_zone_access → F3.1.1.5 Provide Urban Traffic Management Facilities (Association «OUT»)**
- connection changed: ~~fv.fv-freight_vehicle_identity_for_rest_area → F3.1.5 Provide Management of Service Areas (Association «IN»)~~ → **fv.fv-freight_vehicle_identity_for_rest_area → F3.1.5 Provide Management of Service Areas (Association «OUT»)**
- connection changed: ~~fve.onv-vehicle_presence_indication → F5.15 Provide In-vehicle Detection and Analysis (Association «IN»)~~ → **fve.onv-vehicle_presence_indication → F5.15 Provide In-vehicle Detection and Analysis (Association «OUT»)**
- connection changed: ~~fve.oru-presence_indication → F5.15 Provide In-vehicle Detection and Analysis (Association «IN»)~~ → **fve.oru-presence_indication → F5.15 Provide In-vehicle Detection and Analysis (Association «OUT»)**
- connection changed: ~~fve.so-object_presence_indication → F5.15 Provide In-vehicle Detection and Analysis (Association «IN»)~~ → **fve.so-object_presence_indication → F5.15 Provide In-vehicle Detection and Analysis (Association «OUT»)**
- connection changed: ~~fws-weather_conditions_for_ISA → F5.13 Provide Vehicle Data and ISA (Association «IN»)~~ → **fws-weather_conditions_for_ISA → F5.13 Provide Vehicle Data and ISA (Association «OUT»)**
- connection changed: ~~mt.pshvs_service_area_information → F5.16.1 Manage Communication from Vehicle to Driver (Association «IN»)~~ → **mt.pshvs_service_area_information → F5.16.1 Manage Communication from Vehicle to Driver (Association «OUT»)**
- connection changed: ~~mt_load_NAP_user_data → D3.17 NAP Users (Association «IN»)~~ → **mt_load_NAP_user_data → D3.17 NAP Users (Association «OUT»)**
- connection changed: ~~pshvs.mt_inter-urban_xfcd → F3.1.2 Provide Inter-urban Traffic Management (Association «IN»)~~ → **pshvs.mt_inter-urban_xfcd → F3.1.2 Provide Inter-urban Traffic Management (Association «OUT»)**
- connection removed: pshvs.mt_rest_area_parking_request → F3.1.5.10 Manage Rest Area Usage (Association «OUT»)
- connection changed: ~~pshvs.psef_eCall_message → F2.1.11 Manage eCall Messages (Association «IN»)~~ → **pshvs.psef_eCall_message → F2.1.11 Manage eCall Messages (Association «OUT»)**
- connection changed: ~~pshvs_tvd_scenario → F5.11.13 Manage Operational Data Store (Association «IN»)~~ → **pshvs_tvd_scenario → F5.11.13 Manage Operational Data Store (Association «OUT»)**

### Frame Repository/Frame Functional View/Data Store
- connection changed: ~~D3.17 NAP Users → mt_read_NAP_user_data (Association «OUT»)~~ → **D3.17 NAP Users → mt_read_NAP_user_data (Association «IN»)**

### Frame Repository/Frame Functional View/Functionality/Functional Area F3 - Manage Traffic
- connection changed: ~~F3.1.5 Provide Management of Service Areas → mt.pshvs_service_area_information (Association «OUT»)~~ → **F3.1.5 Provide Management of Service Areas → mt.pshvs_service_area_information (Association «IN»)**
- connection removed: F3.1.5.10 Manage Rest Area Usage → mt.pshvs_rest_area_parking_response (Association «IN»)
- connection changed: ~~F3.1.5.3 Output Service Area Messages → mt.pshvs_service_area_information (Association «OUT»)~~ → **F3.1.5.3 Output Service Area Messages → mt.pshvs_service_area_information (Association «IN»)**
- connection changed: ~~F3.6 Operate National Access Point → tnap.cp-metadata_&_success_report (Association «OUT»)~~ → **F3.6 Operate National Access Point → tnap.cp-metadata_&_success_report (Association «IN»)**
- connection changed: ~~F3.6 Operate National Access Point → tnap.cp-support_response (Association «OUT»)~~ → **F3.6 Operate National Access Point → tnap.cp-support_response (Association «IN»)**
- connection changed: ~~F3.6 Operate National Access Point → tnap.cc-support_response (Association «OUT»)~~ → **F3.6 Operate National Access Point → tnap.cc-support_response (Association «IN»)**
- connection changed: ~~F3.6 Operate National Access Point → tnap.cc-metadata_search_result (Association «OUT»)~~ → **F3.6 Operate National Access Point → tnap.cc-metadata_search_result (Association «IN»)**
- connection changed: ~~F3.6.3 Manage Content Providers Metadata → tnap.cp-metadata_&_success_report (Association «OUT»)~~ → **F3.6.3 Manage Content Providers Metadata → tnap.cp-metadata_&_success_report (Association «IN»)**
- connection changed: ~~F3.6.5 Provide NAP User Support → tnap.cc-support_response (Association «OUT»)~~ → **F3.6.5 Provide NAP User Support → tnap.cc-support_response (Association «IN»)**
- connection changed: ~~F3.6.5 Provide NAP User Support → tnap.cp-support_response (Association «OUT»)~~ → **F3.6.5 Provide NAP User Support → tnap.cp-support_response (Association «IN»)**

### Frame Repository/Frame Functional View/Functionality/Functional Area F5 - Provide Support for Host Vehicle Systems
- connection changed: ~~F5.11.13 Manage Operational Data Store → pshvs_driver_condition (Association «OUT»)~~ → **F5.11.13 Manage Operational Data Store → pshvs_driver_condition (Association «IN»)**
- connection changed: ~~F5.11.13 Manage Operational Data Store → pshvs_tvd_incident_data (Association «OUT»)~~ → **F5.11.13 Manage Operational Data Store → pshvs_tvd_incident_data (Association «IN»)**

### Frame Repository/Frame Functional View/System
- connection changed: ~~System → To NAP Actors (Association «OUT»)~~ → **System → To NAP Actors (Association «IN»)**

### Frame Repository/Frame Functional View/Terminators & Terminator Diagrams/Terminators
- connection changed: ~~fmms.mmc-urban_crossing_information → Multi-Modal Crossing (Association «IN»)~~ → **Multi-Modal Crossing → fmms.mmc-urban_crossing_information (Association «IN»)**
- connection changed: ~~fmms.mmc-urban_crossing_inputs → Multi-Modal Crossing (Association «IN»)~~ → **Multi-Modal Crossing → fmms.mmc-urban_crossing_inputs (Association «IN»)**
- connection changed: ~~fmms.mmc-inter-urban_crossing_request → Multi-Modal Crossing (Association «IN»)~~ → **Multi-Modal Crossing → fmms.mmc-inter-urban_crossing_request (Association «IN»)**
- connection changed: ~~fmms.mmc-urban_crossing_command → Multi-Modal Crossing (Association «IN»)~~ → **Multi-Modal Crossing → fmms.mmc-urban_crossing_command (Association «IN»)**
- connection changed: ~~fmms.mmc-crossing_request → Multi-Modal Crossing (Association «IN»)~~ → **Multi-Modal Crossing → fmms.mmc-crossing_request (Association «IN»)**
- connection changed: ~~fmms.mms-service_change_request_response → Multi-Modal Management System (Association «IN»)~~ → **Multi-Modal Management System → fmms.mms-service_change_request_response (Association «IN»)**
- connection changed: ~~fmms.mms-control_parameters → Multi-Modal Management System (Association «IN»)~~ → **Multi-Modal Management System → fmms.mms-control_parameters (Association «IN»)**
- connection changed: ~~fmms.mms-PT_service_change_request → Multi-Modal Management System (Association «IN»)~~ → **Multi-Modal Management System → fmms.mms-PT_service_change_request (Association «IN»)**
- connection changed: ~~fmms.mms-current_service_status → Multi-Modal Management System (Association «IN»)~~ → **Multi-Modal Management System → fmms.mms-current_service_status (Association «IN»)**
- connection changed: ~~fmms.mms-service_details_response → Multi-Modal Management System (Association «IN»)~~ → **Multi-Modal Management System → fmms.mms-service_details_response (Association «IN»)**
- connection changed: ~~fmms.mms-accident_information → Multi-Modal Management System (Association «IN»)~~ → **Multi-Modal Management System → fmms.mms-accident_information (Association «IN»)**
- connection changed: ~~fmms.mms-rail_service_information → Multi-Modal Management System (Association «IN»)~~ → **Multi-Modal Management System → fmms.mms-rail_service_information (Association «IN»)**
- connection changed: ~~fmms.mms-incident_inputs → Multi-Modal Management System (Association «IN»)~~ → **Multi-Modal Management System → fmms.mms-incident_inputs (Association «IN»)**
- connection changed: ~~fmms.mms-strike_details → Multi-Modal Management System (Association «IN»)~~ → **Multi-Modal Management System → fmms.mms-strike_details (Association «IN»)**
- connection changed: ~~fmms.mms-plannings → Multi-Modal Management System (Association «IN»)~~ → **Multi-Modal Management System → fmms.mms-plannings (Association «IN»)**
- connection changed: ~~fmms.mms-data_for_demand_services → Multi-Modal Management System (Association «IN»)~~ → **Multi-Modal Management System → fmms.mms-data_for_demand_services (Association «IN»)**
- connection changed: ~~fmms.mms-demand_inputs → Multi-Modal Management System (Association «IN»)~~ → **Multi-Modal Management System → fmms.mms-demand_inputs (Association «IN»)**
- connection changed: ~~fmms.mms-ferry_service_information → Multi-Modal Management System (Association «IN»)~~ → **Multi-Modal Management System → fmms.mms-ferry_service_information (Association «IN»)**
- connection changed: ~~NAP Content Consumer → fnap.cc-data_request (Association «OUT»)~~ → **NAP Content Consumer → fnap.cc-data_request (Association «IN»)**
- connection removed: Road Network Operator → fo.rno-demand_management_inputs (Association «IN»)

## NAP Reference Architecture / 02 NAP Functional View

### NAP Reference Architecture/02 NAP Functional View/Data Stores
- connection changed: ~~D3.17 NAP Users → mt_read_NAP_user_data (Association «OUT»)~~ → **D3.17 NAP Users → mt_read_NAP_user_data (Association «IN»)**

### NAP Reference Architecture/02 NAP Functional View/Functional Data Flow
- connection changed: ~~fnap.cc-metadata_search_request → F3.6 Operate National Access Point (Association «IN»)~~ → **fnap.cc-metadata_search_request → F3.6 Operate National Access Point (Association «OUT»)**
- connection changed: ~~fnap.cc-support_request → F3.6.5 Provide NAP User Support (Association «IN»)~~ → **fnap.cc-support_request → F3.6.5 Provide NAP User Support (Association «OUT»)**
- connection changed: ~~fnap.cc-support_request → F3.6 Operate National Access Point (Association «IN»)~~ → **fnap.cc-support_request → F3.6 Operate National Access Point (Association «OUT»)**
- connection changed: ~~fnap.cp-metadata_&_authorisation_credentials → F3.6.3 Manage Content Providers Metadata (Association «IN»)~~ → **fnap.cp-metadata_&_authorisation_credentials → F3.6.3 Manage Content Providers Metadata (Association «OUT»)**
- connection changed: ~~fnap.cp-metadata_&_authorisation_credentials → F3.6 Operate National Access Point (Association «IN»)~~ → **fnap.cp-metadata_&_authorisation_credentials → F3.6 Operate National Access Point (Association «OUT»)**
- connection changed: ~~fnap.cp-registration_request → F3.6.2 Manage Registrations and Provide Authorisation Service (Association «IN»)~~ → **fnap.cp-registration_request → F3.6.2 Manage Registrations and Provide Authorisation Service (Association «OUT»)**
- connection changed: ~~fnap.cp-registration_request → F3.6 Operate National Access Point (Association «IN»)~~ → **fnap.cp-registration_request → F3.6 Operate National Access Point (Association «OUT»)**
- connection changed: ~~fnap.cp-support_request → F3.6 Operate National Access Point (Association «IN»)~~ → **fnap.cp-support_request → F3.6 Operate National Access Point (Association «OUT»)**
- connection changed: ~~fnap.cp-support_request → F3.6.5 Provide NAP User Support (Association «IN»)~~ → **fnap.cp-support_request → F3.6.5 Provide NAP User Support (Association «OUT»)**
- connection changed: ~~mt_load_NAP_user_data → D3.17 NAP Users (Association «IN»)~~ → **mt_load_NAP_user_data → D3.17 NAP Users (Association «OUT»)**
- connection changed: ~~tnap.cc-data_response → NAP Content Consumer (Association «IN»)~~ → **tnap.cc-data_response → NAP Content Consumer (Association «OUT»)**
- connection changed: ~~tnap.cc-data_response → NAP Content Consumer (Association «IN»)~~ → **tnap.cc-data_response → NAP Content Consumer (Association «OUT»)**

### NAP Reference Architecture/02 NAP Functional View/Functional Data Flow/high level FDFs
- connection changed: ~~NAP Actors → tnap-mt_outputs (Association «OUT»)~~ → **tnap-mt_outputs → NAP Actors (Association «OUT»)**

### NAP Reference Architecture/02 NAP Functional View/Functions
- connection changed: ~~F3.6.2 Manage Registrations and Provide Authorisation Service → tnap.cp-registration_response (Association «OUT»)~~ → **F3.6.2 Manage Registrations and Provide Authorisation Service → tnap.cp-registration_response (Association «IN»)**
- connection changed: ~~F3.6.3 Manage Content Providers Metadata → tnap.cp-metadata_&_success_report (Association «OUT»)~~ → **F3.6.3 Manage Content Providers Metadata → tnap.cp-metadata_&_success_report (Association «IN»)**
- connection changed: ~~F3.6.5 Provide NAP User Support → tnap.cc-support_response (Association «OUT»)~~ → **F3.6.5 Provide NAP User Support → tnap.cc-support_response (Association «IN»)**
- connection changed: ~~F3.6.5 Provide NAP User Support → tnap.cp-support_response (Association «OUT»)~~ → **F3.6.5 Provide NAP User Support → tnap.cp-support_response (Association «IN»)**

### NAP Reference Architecture/02 NAP Functional View/Functions/high level functions
- connection changed: ~~F3.6 Operate National Access Point → tnap.cp-metadata_&_success_report (Association «OUT»)~~ → **F3.6 Operate National Access Point → tnap.cp-metadata_&_success_report (Association «IN»)**
- connection changed: ~~F3.6 Operate National Access Point → tnap.cp-registration_response (Association «OUT»)~~ → **F3.6 Operate National Access Point → tnap.cp-registration_response (Association «IN»)**
- connection changed: ~~F3.6 Operate National Access Point → tnap.cp-support_response (Association «OUT»)~~ → **F3.6 Operate National Access Point → tnap.cp-support_response (Association «IN»)**
- connection changed: ~~F3.6 Operate National Access Point → tnap.cc-support_response (Association «OUT»)~~ → **F3.6 Operate National Access Point → tnap.cc-support_response (Association «IN»)**
- connection changed: ~~F3.6 Operate National Access Point → tnap.cc-metadata_search_result (Association «OUT»)~~ → **F3.6 Operate National Access Point → tnap.cc-metadata_search_result (Association «IN»)**

### NAP Reference Architecture/02 NAP Functional View/Terminators
- connection changed: ~~NAP Content Consumer → fnap.cc-data_request (Association «OUT»)~~ → **NAP Content Consumer → fnap.cc-data_request (Association «IN»)**

## Duplicate IN/OUT connectors removed

- «IN» F3.1.5.10 Manage Rest Area Usage → mt.pshvs_rest_area_parking_response `{10B2B83F-90F5-4e06-BC37-0D5B0E47A2D4}` removed (diagram links moved to kept connector: 0)
- «OUT» pshvs.mt_rest_area_parking_request → F3.1.5.10 Manage Rest Area Usage `{E3AD8B34-87F8-44a1-B78E-B197013162EF}` removed (diagram links moved to kept connector: 0)
- «OUT» frp-guidance_data → F5.12.12 Collect Road Network Information `{3AE92658-B8CF-457f-8290-C6DFADB593E8}` removed (diagram links moved to kept connector: 0)
- «IN» Road Network Operator → fo.rno-demand_management_inputs `{1818A7C7-842F-40de-B7EC-AC13D56A2DFF}` removed (diagram links moved to kept connector: 0)
