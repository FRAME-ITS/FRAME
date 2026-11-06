# Model check – FRAME.qea

**3 errors, 14 warnings**

| Rule | Related issue | Errors | Warnings |
|---|---|---|---|
| duplicate |  | 0 | 2 |
| function-flows |  | 0 | 1 |
| servedby |  | 3 | 0 |
| unused-flow | #76 | 0 | 11 |

## Errors

<details><summary><b>servedby</b> (3)</summary>

- User_Need **11.1.1.6** (C-ITS Reference Architecture) → F3.1.1.5 Provide Urban Traffic Management Facilities is Usage «», expected Association «served by»
- User_Need **11.2.4.1** (C-ITS Reference Architecture) → F3.1 Provide Traffic Control is Usage «», expected Association «served by»
- User_Need **11.2.4.1** (C-ITS Reference Architecture) → F9.3 Manage Vehicle Access to Sensitive Areas is Usage «», expected Association «served by»

</details>

## Warnings

<details><summary><b>duplicate</b> (2)</summary>

- 2× User_Need **1.1.4** in the FRAME Repository
- 2× User_Need_Group **11 C-ITS** in the FRAME Repository

</details>

<details><summary><b>function-flows</b> (1)</summary>

- Low_Level_Function **F6.5.8 Enable Final Approval of Trip Plan** (Frame Repository) has no IN and OUT data flows

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

