# eCall and Broadcaster data-flow links «instants of» / «owned by» → IN / OUT (#96 point 4, 2026-11-09)

Script: `tools/fixes/2026-11-09_ecall_flow_links_instance_of.py`.

- D2.4 PSAP eCall Sessions Data → psef_eCall_data_from_store: «instants of» → «IN»
- F2.1.11 Manage eCall Messages → psef_PSAP_status_request: «instants of» → «IN»
- F2.1.11.1 Manage eCall Message Transmission → psef.pshvs_eCall_message_failure: «instants of» → «IN»
- F2.1.11.1 Manage eCall Message Transmission → psef_PSAP_status_request: «instants of» → «IN»
- F2.1.11.1 Manage eCall Message Transmission → psef_available_PSAP_list: «instants of» → «IN»
- F2.1.11.1 Manage eCall Message Transmission → psef_eCall_message_status: «instants of» → «IN»
- F2.1.11.2 Manage PSAP Data Stores → psef_load_eCall_data: «instants of» → «IN»
- F2.1.2 Manage Emergency Intervention → psef_PSAP_status_response: «instants of» → «IN»
- F2.1.2.1 Identify and Classify Emergencies → psef_PSAP_status_response: «instants of» → «IN»
- fv.vea-eCall_activation_status → F5.12 Provide Vehicle Communications Interfaces: «owned by» → «OUT»
- fv.vea-eCall_activation_status → F5.12.7 Communicate with In-vehicle Systems: «owned by» → «OUT»
- psef.pshvs_eCall_message_failure → F5.11.7 Provide In-vehicle eCall Facilities: «owned by» → «OUT»
- psef_PSAP_status_request → F2.1.2 Manage Emergency Intervention: «owned by» → «OUT»
- psef_PSAP_status_request → F2.1.2.1 Identify and Classify Emergencies: «owned by» → «OUT»
- psef_PSAP_status_response → F2.1.11 Manage eCall Messages: «owned by» → «OUT»
- psef_PSAP_status_response → F2.1.11.1 Manage eCall Message Transmission: «owned by» → «OUT»
- psef_available_PSAP_list → F2.1.11.2 Manage PSAP Data Stores: «owned by» → «OUT»
- psef_eCall_data_from_store → F2.1.11.2 Manage PSAP Data Stores: «owned by» → «OUT»
- psef_eCall_message_status → F2.1.11.2 Manage PSAP Data Stores: «owned by» → «OUT»
- psef_load_eCall_data → D2.4 PSAP eCall Sessions Data: «owned by» → «OUT»
- tesp.b-demand_data → Broadcaster: «owned by» → «OUT»
- tesp.b-incident_strategy_information  → Broadcaster: «owned by» → «OUT»
- tesp.b-inter-urban_traffic_data  → Broadcaster: «owned by» → «OUT»

23 links retyped; model connectors still «instants of»: 0
