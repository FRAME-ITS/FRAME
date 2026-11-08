# FRAME model changes HEAD → working copy

39 changes

| View | Changes |
|---|---|
| (root) | 3 |
| C-ITS Reference Architecture / 02 C-ITS Functional View | 6 |
| Frame Repository / FRAME User Needs | 9 |
| Frame Repository / Frame Functional View | 16 |
| NAP Reference Architecture / 02 NAP Functional View | 5 |

## (root)
- connection removed: ? → ? (Association «IN»)
- connection removed: ? → ? (Usage)
- connection removed: ? → ? (Association «OUT»)

## C-ITS Reference Architecture / 02 C-ITS Functional View

### C-ITS Reference Architecture/02 C-ITS Functional View/F9.1 Enable Cooperative Roadside Vehicle Interactions
- connection changed: ~~F9. Provide Support for Cooperative Systems → F9.1 Enable Cooperative Roadside Vehicle Interactions (Aggregation «component of»)~~ → **F9.1 Enable Cooperative Roadside Vehicle Interactions → F9. Provide Support for Cooperative Systems (Aggregation «component of»)**

### C-ITS Reference Architecture/02 C-ITS Functional View/F9.2 Provide Access to Specific Lanes
- connection changed: ~~F9. Provide Support for Cooperative Systems → F9.2 Provide Access to Specific Lanes (Aggregation «component of»)~~ → **F9.2 Provide Access to Specific Lanes → F9. Provide Support for Cooperative Systems (Aggregation «component of»)**

### C-ITS Reference Architecture/02 C-ITS Functional View/F9.3 Manage Vehicle Access to Sensitive Locations/Areas (DENM Messages)
- connection changed: ~~F9. Provide Support for Cooperative Systems → F9.3 Manage Vehicle Access to Sensitive Locations/ Areas (Aggregation «component of»)~~ → **F9.3 Manage Vehicle Access to Sensitive Locations/ Areas → F9. Provide Support for Cooperative Systems (Aggregation «component of»)**

### C-ITS Reference Architecture/02 C-ITS Functional View/F9.4 Provide Hazardous Goods Management
- connection changed: ~~F9. Provide Support for Cooperative Systems → F9.4 Provide Hazardous Goods Management (Aggregation «component of»)~~ → **F9.4 Provide Hazardous Goods Management → F9. Provide Support for Cooperative Systems (Aggregation «component of»)**

### C-ITS Reference Architecture/02 C-ITS Functional View/F9.5 Manage Interurban Urban Traffic Zones (IVIM Messages)
- connection changed: ~~F9. Provide Support for Cooperative Systems → F9.5 Manage Interurban Urban Traffic Zones (Aggregation «component of»)~~ → **F9.5 Manage Interurban Urban Traffic Zones → F9. Provide Support for Cooperative Systems (Aggregation «component of»)**

### C-ITS Reference Architecture/02 C-ITS Functional View/F9.6 Provide C-ITS services based on future message formats
- connection changed: ~~F9. Provide Support for Cooperative Systems → F9.6 - Future messages and C-ITS services (Aggregation «component of»)~~ → **F9.6 - Future messages and C-ITS services → F9. Provide Support for Cooperative Systems (Aggregation «component of»)**

## Frame Repository / FRAME User Needs

### Frame Repository/FRAME User Needs
- connection changed: ~~6.5.1.1 → F3.6.4 Manage Metadata Retrieval (Aggregation «componentof»)~~ → **6.5.1.1 → F3.6.4 Manage Metadata Retrieval (Association «served by»)**
- connection changed: ~~6.5.1.2 → F3.6.4 Manage Metadata Retrieval (Aggregation «componentof»)~~ → **6.5.1.2 → F3.6.4 Manage Metadata Retrieval (Association «served by»)**
- connection changed: ~~6.5.1.3 → F3.6.4 Manage Metadata Retrieval (Aggregation «componentof»)~~ → **6.5.1.3 → F3.6.4 Manage Metadata Retrieval (Association «served by»)**
- connection changed: ~~6.5.1.6 → F3.6.4 Manage Metadata Retrieval (Aggregation «componentof»)~~ → **6.5.1.6 → F3.6.4 Manage Metadata Retrieval (Association «served by»)**
- connection changed: ~~6.5.1.8 → F3.6.4 Manage Metadata Retrieval (Aggregation «componentof»)~~ → **6.5.1.8 → F3.6.4 Manage Metadata Retrieval (Association «served by»)**
- connection changed: ~~9.10.1.3 → F8.6.4 Provide Interface to Other Transport Modes (Association «belongsto»)~~ → **9.10.1.3 → F8.6.4 Provide Interface to Other Transport Modes (Association «served by»)**
- connection changed: ~~9.11.1.14 → F8.6.6 Manage Incident Response Data Store (Association «belongsto»)~~ → **9.11.1.14 → F8.6.6 Manage Incident Response Data Store (Association «served by»)**
- connection changed: ~~9.11.1.15 → F8.6.5 Provide FTOM Interface for FTEP Monitoring (Association «belongsto»)~~ → **9.11.1.15 → F8.6.5 Provide FTOM Interface for FTEP Monitoring (Association «served by»)**
- connection changed: ~~9.11.1.9 → F8.6.1 Implement FTEP (Association «belongsto»)~~ → **9.11.1.9 → F8.6.1 Implement FTEP (Association «served by»)**

## Frame Repository / Frame Functional View

### Frame Repository/Frame Functional View/Data Flows/High Level Data Flows
- connection removed: fnap-mt_inputs → fnap.cp-support_request (Aggregation «Componentof»)
- connection removed: fnap-mt_inputs → fnap.cc-support_request (Aggregation «Componentof»)
- connection removed: fnap-mt_inputs → fnap.cp-support_request (Aggregation «Componentof»)
- connection removed: tnap-mt_outputs → tnap.cp-support_response (Aggregation «Componentof»)
- connection removed: tnap-mt_outputs → tnap.cp-support_response (Aggregation «Componentof»)
- connection removed: tnap-mt_outputs → tnap.cc-support_response (Aggregation «Componentof»)

### Frame Repository/Frame Functional View/Data Flows/Low Level Data Flows
- connection changed: ~~fnap-mt_inputs → fnap.cp-metadata_&_authorisation_credentials (Aggregation «Componentof»)~~ → **fnap.cp-metadata_&_authorisation_credentials → fnap-mt_inputs (Aggregation «Componentof»)**
- connection changed: ~~fnap-mt_inputs → fnap.cp-registration_request (Aggregation «Componentof»)~~ → **fnap.cp-registration_request → fnap-mt_inputs (Aggregation «Componentof»)**
- connection changed: ~~fnap-mt_inputs → fnap.cp-support_request (Aggregation «Componentof»)~~ → **fnap.cp-support_request → fnap-mt_inputs (Aggregation «Componentof»)**
- connection changed: ~~fws-environment_data_for_PT → fws-mpto_inputs (Generalization)~~ → **fws-environment_data_for_PT → fws-mpto_inputs (Aggregation «componentof»)**
- connection changed: ~~mt.mpto_urban_data_transfer → mt.mpto_data_transfer (Aggregation «Componentof»)~~ → **mt.mpto_data_transfer → mt.mpto_urban_data_transfer (Aggregation «Componentof»)**
- connection changed: ~~mt.mpto_inter-urban_data_transfer → mt.mpto_data_transfer (Aggregation «Componentof»)~~ → **mt.mpto_data_transfer → mt.mpto_inter-urban_data_transfer (Aggregation «Componentof»)**
- connection changed: ~~mt.mpto_data_from_road_network_predictions → mt.mpto_data_transfer (Aggregation «Componentof»)~~ → **mt.mpto_data_transfer → mt.mpto_data_from_road_network_predictions (Aggregation «Componentof»)**
- connection changed: ~~mt.pscs_data_for_coop_sys → mt.pscs_rest_area_space_response (Aggregation «Componentof»)~~ → **mt.pscs_rest_area_space_response → mt.pscs_data_for_coop_sys (Aggregation «Componentof»)**
- connection changed: ~~tors-pscs_outputs → tors.hgvm-hazardous_goods_vehicle_route_implementation (Aggregation «Componentof»)~~ → **tors.hgvm-hazardous_goods_vehicle_route_implementation → tors-pscs_outputs (Aggregation «Componentof»)**

### Frame Repository/Frame Functional View/Functionality/Functional Area F8 - Manage Freight and Fleet Operations
- connection removed: F8.4.1 Provide Freight Transport User Interface → F8.4.1 Provide Freight Transport User Interface (Association «belongsto»)

## NAP Reference Architecture / 02 NAP Functional View

### NAP Reference Architecture/02 NAP Functional View/Functional Data Flow
- connection changed: ~~fnap-mt_inputs → fnap.cc-metadata_search_request (Aggregation «Componentof»)~~ → **fnap.cc-metadata_search_request → fnap-mt_inputs (Aggregation «Componentof»)**
- connection changed: ~~fnap-mt_inputs → fnap.cc-support_request (Aggregation «Componentof»)~~ → **fnap.cc-support_request → fnap-mt_inputs (Aggregation «Componentof»)**
- connection changed: ~~fnap-mt_inputs → fnap.cp-metadata_&_authorisation_credentials (Aggregation «Componentof»)~~ → **fnap.cp-metadata_&_authorisation_credentials → fnap-mt_inputs (Aggregation «Componentof»)**
- connection changed: ~~fnap-mt_inputs → fnap.cp-registration_request (Aggregation «Componentof»)~~ → **fnap.cp-registration_request → fnap-mt_inputs (Aggregation «Componentof»)**
- connection changed: ~~fnap-mt_inputs → fnap.cp-support_request (Aggregation «Componentof»)~~ → **fnap.cp-support_request → fnap-mt_inputs (Aggregation «Componentof»)**
