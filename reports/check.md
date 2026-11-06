# Model check – FRAME.qea

**3 errors, 61 warnings**

| Rule | Related issue | Errors | Warnings |
|---|---|---|---|
| componentof | #80, #81 | 0 | 42 |
| duplicate |  | 0 | 2 |
| function-flows |  | 0 | 1 |
| servedby |  | 3 | 5 |
| unused-flow | #76 | 0 | 11 |

## Errors

<details><summary><b>servedby</b> (3)</summary>

- User_Need **11.1.1.6** (C-ITS Reference Architecture) → F3.1.1.5 Provide Urban Traffic Management Facilities is Usage «», expected Association «Servedby»
- User_Need **11.2.4.1** (C-ITS Reference Architecture) → F3.1 Provide Traffic Control is Usage «», expected Association «Servedby»
- User_Need **11.2.4.1** (C-ITS Reference Architecture) → F9.3 Manage Vehicle Access to Sensitive Areas is Usage «», expected Association «Servedby»

</details>

## Warnings

<details><summary><b>componentof</b> (42)</summary>

- «component of» High_Level_Data_Flow **fnap-mt_inputs** (NAP Reference Architecture) → fnap.cc-metadata_search_request (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «component of» High_Level_Data_Flow **fnap-mt_inputs** (NAP Reference Architecture) → fnap.cc-support_request (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «component of» High_Level_Data_Flow **fnap-mt_inputs** (NAP Reference Architecture) → fnap.cp-metadata_&_authorisation_credentials (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «component of» High_Level_Data_Flow **fnap-mt_inputs** (NAP Reference Architecture) → fnap.cp-registration_request (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «component of» High_Level_Data_Flow **fnap-mt_inputs** (NAP Reference Architecture) → fnap.cp-support_request (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «component of» High_Level_Data_Flow **fnap-mt_inputs** (NAP Reference Architecture) → fnap.cp-support_request (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «component of» High_Level_Data_Flow **tnap-mt_outputs** (NAP Reference Architecture) → tnap.cc-support_response (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «component of» High_Level_Data_Flow **tnap-mt_outputs** (NAP Reference Architecture) → tnap.cc-support_response (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «component of» High_Level_Data_Flow **tnap-mt_outputs** (NAP Reference Architecture) → tnap.cp-support_response (Low_Level_Data_Flow) runs whole → part or between low-level flows
- «component of» High_Level_Data_Flow **tnap-mt_outputs** (NAP Reference Architecture) → tnap.cp-support_response (Low_Level_Data_Flow) runs whole → part or between low-level flows
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

<details><summary><b>duplicate</b> (2)</summary>

- 2× User_Need **1.1.4** in the FRAME Repository
- 2× User_Need_Group **11 C-ITS** in the FRAME Repository

</details>

<details><summary><b>function-flows</b> (1)</summary>

- Low_Level_Function **F6.5.8 Enable Final Approval of Trip Plan** (Frame Repository) has no IN and OUT data flows

</details>

<details><summary><b>servedby</b> (5)</summary>

- User_Need **6.5.1.1** (NAP Reference Architecture) → F3.6.4 Manage Metadata Retrieval is Aggregation «component of», expected Association «Servedby»
- User_Need **6.5.1.2** (NAP Reference Architecture) → F3.6.4 Manage Metadata Retrieval is Aggregation «component of», expected Association «Servedby»
- User_Need **6.5.1.3** (NAP Reference Architecture) → F3.6.4 Manage Metadata Retrieval is Aggregation «component of», expected Association «Servedby»
- User_Need **6.5.1.6** (NAP Reference Architecture) → F3.6.4 Manage Metadata Retrieval is Aggregation «component of», expected Association «Servedby»
- User_Need **6.5.1.8** (NAP Reference Architecture) → F3.6.4 Manage Metadata Retrieval is Aggregation «component of», expected Association «Servedby»

</details>

<details><summary><b>unused-flow</b> (11)</summary>

- High_Level_Data_Flow **fes-psef_inputs** (Frame Repository) is not shown in any diagram
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

