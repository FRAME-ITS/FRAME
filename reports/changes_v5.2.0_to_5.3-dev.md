# FRAME model changes v5.2.0 → working copy

286 changes

| View | Changes |
|---|---|
| (root) | 1 |
| National Body Reference Architecture | 9 |
| National Body Reference Architecture / 00 NB Motivational Layer | 2 |
| National Body Reference Architecture / 02 NB Functional View | 3 |
| National Body Reference Architecture / 05 NB Communication View | 5 |
| National Body Reference Architecture / NB Communication View | 87 |
| National Body Reference Architecture / NB Functional View | 109 |
| National Body Reference Architecture / NB Motivational Layer | 36 |
| National Body Reference Architecture / NB Organisational View | 15 |
| National Body Reference Architecture / Supplements | 19 |

## (root)
- **Package** National Body Reference Architecture `{83F96735-FCA0-4453-90B4-7156D421D49D}` — *substantive description change*
  - **The main objective of this architecture is the harmonisation of National Bodies activities on the European level as well as increasing their effectiveness. From the perspective of the National Body, the architecture defines its roles, functions, and processes. From a governance and compliance assessment point of view, it defines the minimum requirements to be met at the national level in aim to achieve the harmonisation of National Bodies activities as well as their interoperability at European level. The National Body Reference Architecture aims to support the National Bodies by providing g …

## National Body Reference Architecture

### National Body Reference Architecture
- **Package** 01 NB User Needs `{3850AE83-83B5-4848-BF4D-108F0F8111C5}` — *object deleted*
- **Package** 06 NB Security View `{70756C99-EEB3-4ab0-93D5-066EC159B491}` — *object deleted*
- **Package** NB Communication View `{DF3898D8-D408-4513-883C-F2244B8D329C}` — *title change*
  - name: ~~05 NB Communication View~~ → **NB Communication View**
- **Package** NB Functional View `{A2CCC6DC-AA6F-43ee-963D-F21FE59D4039}` — *title change; substantive description change*
  - name: ~~02 NB Functional View~~ → **NB Functional View**
  - ~~/ Competent Authority Reference Architecture~~ **reference architecture** … **they** … ~~delegated acts.~~ **Delegated Regulations.** … ~~Competent Authority~~ **authority** … ~~Terminators~~ **Terminators, the entities who start or end processes or functionalities,** … ~~neighbor~~ **related**
- **Package** NB Motivational Layer `{5BB11B5F-DD5A-4750-B3D2-F3EDD1ECDEA3}` — *title change; editorial description change*
  - name: ~~00 NB Motivational Layer~~ → **NB Motivational Layer**
  - ~~Body or Competent Authority (NB/CA). However, national bodies~~ **Body. National Bodies** … ~~recognised~~ **recognized** … ~~regulate,~~ **regulate**
- **Package** NB Organisational View `{6F98105C-8282-4fc9-B746-5317AF661808}` — *title change*
  - name: ~~03 NB Organisational View~~ → **NB Organisational View**
- **Package** NB Physical View `{918FDB86-8032-47aa-9179-32E2242AC14B}` — *title change*
  - name: ~~04 NB Physical View~~ → **NB Physical View**
- diagram **National Body Landing Page** — elements added: Change History, Issues Tracking and Wiki, NB Glossary
- diagram **Todos** — diagram deleted

## National Body Reference Architecture / 00 NB Motivational Layer

### National Body Reference Architecture/00 NB Motivational Layer/Further Elements
- **FRAME_ITS_Vision** NB _Vision `{80F8D22D-6FA7-4d3c-BA96-439708D36890}` — *object deleted*
- connection removed: NB _Vision → Increased findability and visibility of data and services EU-wide (Realisation)

## National Body Reference Architecture / 02 NB Functional View

### National Body Reference Architecture/02 NB Functional View
- **Package** HL Function `{954794E9-288B-4627-96E0-CC56924A7E36}` — *object deleted*

### National Body Reference Architecture/02 NB Functional View/LL DataFlows
- **FRAME_Low_Level_Data_Flow** Request stakeholder `{71D1CB99-EEFE-42b2-9884-A46F29131B61}` — *object deleted*
- connection removed: Request stakeholder → Reporting of self declaration and compliance assessment results (Association «OUT»)

## National Body Reference Architecture / 05 NB Communication View

### National Body Reference Architecture/05 NB Communication View/Service Processes
- **FRAME_ITS_Service_Process** Check completness of the handed in self declaration `{F9F6C0EC-2BA7-45d2-BFF9-E69247BD2E3A}` — *object deleted*
- connection removed: Check completness of the handed in self declaration → Receiving feedback about the status, correctness and time line (Usage «Instantiate»)
- **FRAME_ITS_Service_Process** Correction of Self declaration `{0F719F39-347C-4582-98E3-76232B1D8FB8}` — *object deleted*
- connection removed: Correction of Self declaration → Receiving updated self declaration (Usage «Instantiate»)
- **FRAME_ITS_Service_Process** has to maybe correct contact details `{B2D8D198-92ED-44c5-AE64-663405FBAFBF}` — *object deleted*

## National Body Reference Architecture / NB Communication View

### National Body Reference Architecture/NB Communication View
- diagram **05 NB Communication View** — elements added: Compliance assessment, Handling non-compliance process; elements removed: Procedure for dealing with non-compliance
- **Package** Compliance assessment `{C4D62817-B564-4fbd-BD40-E5AAAABB07FC}` — *title change; metadata change*
  - name: ~~Compliance assesment~~ → **Compliance assessment**
  - package: `National Body Reference Architecture/05 NB Communication View` → `National Body Reference Architecture/NB Communication View`
- **Package** Non Compliance Process `{5A8740A1-F800-4b3b-8CFE-7F11F4156620}` — *metadata change*
  - package: `National Body Reference Architecture/05 NB Communication View` → `National Body Reference Architecture/NB Communication View`
- **Package** Self-declaration Reception Process `{58364AC4-6F20-4129-8FC7-D428DB8B8F4E}` — *title change; metadata change*
  - name: ~~Self Declaration Receiving Process~~ → **Self-declaration Reception Process**
  - package: `National Body Reference Architecture/05 NB Communication View` → `National Body Reference Architecture/NB Communication View`

### National Body Reference Architecture/NB Communication View/Compliance assessment
- diagram **Compliance assessment** — renamed ~~Compliance assesment~~ → **Compliance assessment**; elements added: National Body determines the verdict of compliance assessment, National Body indicates non-compliance, National Body informs the service or data provider, National Body may receive feedback from the service or data provider, National Body performing content assessment, National Body performing theoretical inspection, National Body reacting on feedback, National Body updates documentation and registration of assessment results and carried out random inspections, Provision of relevant information, Random selection process, Reception of updated and necessary information, Requesting necessary information from data and service provider, Select set of self-declaration for random selection, Service or data provider may appeal the decision according to national laws, regulations and/or procedures, Service or data provider receives assessment results; elements removed: NB Updates documentation and registration of assessment results and carried out random inspections, NB determines the verdict of compliance assement, NB indicates non-compliance, NB informs the Service or Data provider, NB may recieves feedback from the Service or Data provider, NB performing content assesment, NB performing theoretical inspection, NB reacting on feedback, Provission of relevant information, Random Selection Process, Reception of actualised and necessary information, Requesting necessary information from Data and Service Provider, Select set of Self-Declaration for random selection, Service or Data provider may appeal the decision according to national laws, regulations and/or procedures, Service or Data provider receives assessment results
- **Package** Service Processes `{0185B279-5D3B-4e62-8F32-B14B61417EF5}` — *new object*

### National Body Reference Architecture/NB Communication View/Compliance assessment/Service Processes
- **FRAME_ITS_Service_Process** National Body determines the verdict of compliance assessment `{A6EAA190-A9C2-400e-B625-2608F1B7CA01}` — *title change; substantive description change; metadata change*
  - name: ~~NB determines the verdict of compliance assement~~ → **National Body determines the verdict of compliance assessment**
  - **The national body determines the verdict of the compliance assessment based on the results of the theoretical assessment and the content assessment. Determining the verdict of the compliance assessment is explained in NAPCORE milestone report M5.3: "The verdict of the compliance assessment is determined based on the results of theoretical and content assessments. A 'pass' verdict will be assigned if neither the results of the theoretical assessment nor the results of the content assessment indicate non-compliance to the delegated regulation. Otherwise, a 'fail' verdict will be issued. The ve …
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Compliance assessment/Service Processes`
- **FRAME_ITS_Service_Process** National Body indicates non-compliance `{1235A3AD-9772-47a0-A8E7-96CD366C65C9}` — *title change; substantive description change; metadata change*
  - name: ~~NB indicates non-compliance~~ → **National Body indicates non-compliance**
  - **The results of the compliance assessment process and documentation related to compliance assessment are the basis of the potential non-compliance process. These include the verdict of the compliance assessment, the compliance assessment form, the self-declaration selected for random inspection and the accompanying documents supplementing the self-declaration.**
  - package: `National Body Reference Architecture/05 NB Communication View/Compliance assesment` → `National Body Reference Architecture/NB Communication View/Compliance assessment/Service Processes`
- **FRAME_ITS_Service_Process** National Body informs the service or data provider `{4D68A761-475F-419b-A694-674A57AD7A68}` — *title change; substantive description change; metadata change*
  - name: ~~NB informs the Service or Data provider~~ → **National Body informs the service or data provider**
  - **national body informs the service or data provider of the** … ~~should include a instructions~~ **of the compliance assessment. If the assessment results indicate non-compliance, the national body shall provide information on the characteristics of the service** … ~~procedures to fix~~ **data publication identified as non-compliant and** … ~~incorrect parts?~~ **corresponding articles of the applicable delegated act, e.g. by providing the compliance assessment forms documenting the results of compliance assessment.**
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Compliance assessment/Service Processes`
- **FRAME_ITS_Service_Process** National Body may receive feedback from the service or data provider `{5D80C3AA-191A-4be9-AE0B-0359B3961855}` — *title change; substantive description change; metadata change*
  - name: ~~NB may recieves feedback from the Service or Data provider~~ → **National Body may receive feedback from the service or data provider**
  - **The national body shall be capable of receiving feedback from a service or data provider for which a compliance assessment was carried out.**
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Compliance assessment/Service Processes`
- **FRAME_ITS_Service_Process** National Body performing content assessment `{809F8DCF-09A1-4a35-8E23-582A648708D7}` — *title change; substantive description change; metadata change*
  - name: ~~NB performing content assesment~~ → **National Body performing content assessment**
  - **The national body performs a content assessment according to the requirements of applicable delegated act and national regulations. It is recommended to use the document templates provided by NAPCORE for content assessment applicable to the delegated act and the stakeholder group. Latest versions of document templates for content assessment are available on the NAPCORE web site: https://napcore.eu/activity-wg5-national-bodies-and-compliance-assessment/ The** … ~~https://rupprechtconsultde.sharepoint.com/sites/NAPCOREallpartners/Shared%20Documents/Forms/AllItems.aspx?id=%2Fsites%2FNAPCOREallp …
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Compliance assessment/Service Processes`
- **FRAME_ITS_Service_Process** National Body performing theoretical inspection `{7D2FE5AA-F34C-4b2e-891C-12CDB95CB854}` — *title change; substantive description change; metadata change*
  - name: ~~NB performing theoretical inspection~~ → **National Body performing theoretical inspection**
  - ~~In case of~~ **"In short, the theoretical assessment is a compliance review in which the content of the self-declaration is compared against the compliance requirements derived from the applicable delegated regulation." "-- 'Theoretical assessment', deals with the question of whether formal criteria have been met. Requirements of the delegated regulations can be covered, for example, by indications in the self-declaration forms, by descriptions in the accompanying documents, by entries on the NAP or metadata entries or by provided terms and conditions of the respective entity. The crucial qu …
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Compliance assessment/Service Processes`
- **FRAME_ITS_Service_Process** National Body reacting on feedback `{B91A8A84-862E-4e4e-901F-49CED3D4A47F}` — *title change; substantive description change; metadata change*
  - name: ~~NB reacting on feedback~~ → **National Body reacting on feedback**
  - ~~Needs~~ **Feedback received by the national body from stakeholders may be related** … **the compliance assessment process established by the national body or the interpretation of the delegated acts, e.g. to results of compliance assessments. Feedback from stakeholders may** … ~~defined~~ **used to improve the operations of the national body and to develop improvements to regulation. If the feedback provided** … ~~WG5!!~~ **the stakeholder includes a claim that a mistake has occurred in the process of random selection and compliance assessment, the national body shall act according to nation …
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Compliance assessment/Service Processes`
- **FRAME_ITS_Service_Process** National Body updates documentation and registration of assessment results and carried out random inspections `{6E63A273-E997-4476-85F0-B1B3F0D41948}` — *title change; substantive description change; metadata change*
  - name: ~~NB Updates documentation and registration of assessment results and carried out random inspections~~ → **National Body updates documentation and registration of assessment results and carried out random inspections**
  - **After the compliance assessment has been carried out, the national body will document and register the details of the compliance assessment, the verdict of the assessment and the documentation related to the assessment. Relevant documentation includes e.g. the compliance assessment form, the self-declaration selected for random inspection and compliance assessment and the accompanying documents related to the self-declaration. The National Body will update the details of the compliance assessment if the stakeholder appeals the result.**
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Compliance assessment/Service Processes`
- **FRAME_ITS_Service_Process** Provision of relevant information `{E4F0051F-C913-4413-8AF6-46712CCE0E29}` — *title change; substantive description change; metadata change*
  - name: ~~Provission of relevant information~~ → **Provision of relevant information**
  - ~~Body / Competent Authority.~~ **Body.**
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Compliance assessment/Service Processes`
- **FRAME_ITS_Service_Process** Random selection process `{C6B07CCB-F05A-4574-88E8-2D721FA1CC0F}` — *title change; substantive description change; metadata change*
  - name: ~~Random Selection Process~~ → **Random selection process**
  - **The random selection process starts with a pre-selected set of self-declarations. When the number of self-declarations available for selection is known, the national body shall determine the number of self-declarations for which a compliance assessment will be carried out. When selecting the number of compliance assessments to be carried out, the national body usually needs to consider several factors such as the expected impact of compliance assessments and the resources available to the national body. When the random selection is carried out, each self-declaration in the pre-selected set o …
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Compliance assessment/Service Processes`
- **FRAME_ITS_Service_Process** Reception of updated and necessary information `{9AF2F00D-7E33-4491-84C7-D4B0E1E62235}` — *title change; substantive description change; metadata change*
  - name: ~~Reception of actualised and necessary information~~ → **Reception of updated and necessary information**
  - ~~/ Competent Authority~~ … ~~actualized and~~ **updated or additional information, necessary** … ~~the compliance,~~ **compliance** … ~~necessary information~~
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Compliance assessment/Service Processes`
- **FRAME_ITS_Service_Process** Requesting necessary information from data and service provider `{7F23CFE4-500A-4271-9B84-3CA47D3D0129}` — *title change; metadata change*
  - name: ~~Requesting necessary information from Data and Service Provider~~ → **Requesting necessary information from data and service provider**
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Compliance assessment/Service Processes`
- **FRAME_ITS_Service_Process** Select set of self-declaration for random selection `{E45FA344-8B3C-4004-A1C5-10DB1D60987A}` — *title change; substantive description change; metadata change*
  - name: ~~Select set of Self-Declaration for random selection~~ → **Select set of self-declaration for random selection**
  - ~~of Self-declarations~~ **process starts with listing all the self-declarations submitted to the national body. First, self-declarations which have been withdrawn by the stakeholder or moved to inactive state by the national body will be deselected. Second, the national body may deselect also self-declarations** … ~~the~~ **which a** … ~~could be based on relevant Delegated Regulations. Optional but recommended by NAPCORE Recommendation Startified random selection~~ **has been carried out during the previous year or the year before that.**
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Compliance assessment/Service Processes`
- **FRAME_ITS_Service_Process** Service or data provider may appeal the decision according to national laws, regulations and/or procedures `{49B7A4CB-3650-45aa-AC5A-DA84600747B5}` — *title change; metadata change*
  - name: ~~Service or Data provider may appeal the decision according to national laws, regulations and/or procedures~~ → **Service or data provider may appeal the decision according to national laws, regulations and/or procedures**
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Compliance assessment/Service Processes`
- **FRAME_ITS_Service_Process** Service or data provider receives assessment results `{70D2E98B-A46D-41ef-918C-821C6149B02E}` — *title change; metadata change*
  - name: ~~Service or Data provider receives assessment results~~ → **Service or data provider receives assessment results**
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Compliance assessment/Service Processes`

### National Body Reference Architecture/NB Communication View/Non Compliance Process
- diagram **Non Compliance Process** — elements added: Collect possible other information related to identified non-compliance., Detects a non-compliance and request a investigation, Document the decision on non-compliance and the consequences of non-compliance, General Public, Identify non-compliance to individual articles of the applicable delegated act, Identify objectives of the applicable delegated act of the ITS directive by non-compliance, Identify possible actions which are proportional to the objectives when applied individually or as a package, Identify relevant stakeholder characteristics and cintextual factors related to non-complaint., Information on potential non-compliance has been identifyed, Initiate the actions prescribed in the decision on non-compliance and consequences of non-compliance, Investigate whether non-compliance has likely occurred, No reason to expect non-compliance, Optional: request further information from the stakeholder, Process appeals made by the stakeholder, Random inspection of the self-declaration or the accompanying documents indicates non-compliance …; elements removed: Administrative decision on non-compliance and the consequences of non-compliance, Identify actions available for the national body to address non-compliance, Identify non-compliance to individual articles of, Identify objectives of the applicable delegated act or the ITS directive affected by non-compliance, Initiate the Actions prescribed in the decision on non-compliance and consequences of non-compliance, Process appeals made by, Select actions which are proportional to the objectives when applied individually or as a package, Select the action or a combination of Actions which best corresponds to the objectives of the delegated act and the ITS directive
- **Package** Service Processes `{6B723CBD-DC06-49cd-83F3-3FBB735C17FE}` — *new object*

### National Body Reference Architecture/NB Communication View/Non Compliance Process/Service Processes
- connection removed:  → Select actions which are proportional to the objectives when applied individually or as a package (Dependency)
- connection removed: Administrative decision on non-compliance and the consequences of non-compliance → Initiate the Actions prescribed in the decision on non-compliance and consequences of non-compliance (Dependency)
- **FRAME_ITS_Service_Process** Collect possible other information related to identified non-compliance. `{30A34EAE-AB95-4169-900E-BCE47DE46558}` — *new object*
- connection added: Collect possible other information related to identified non-compliance. → Identify possible actions which are proportional to the objectives when applied individually or as a package (Dependency)
- **FRAME_ITS_Service_Process** Detects a non-compliance and request a investigation `{BFBE5607-B5E9-467c-B966-ED0BBD6200CF}` — *new object*
- connection added: Detects a non-compliance and request a investigation → Information on potential non-compliance has been identifyed (Dependency)
- **FRAME_ITS_Service_Process** Document the decision on non-compliance and the consequences of non-compliance `{6B336EE1-25C0-4087-9D25-CE72AF9D5730}` — *title change; metadata change*
  - name: ~~Administrative decision on non-compliance and the consequences of non-compliance~~ → **Document the decision on non-compliance and the consequences of non-compliance**
  - package: `National Body Reference Architecture/05 NB Communication View/Non Compliance Process` → `National Body Reference Architecture/NB Communication View/Non Compliance Process/Service Processes`
- connection added: Document the decision on non-compliance and the consequences of non-compliance → Initiate the actions prescribed in the decision on non-compliance and consequences of non-compliance (Dependency)
- connection removed: Identify actions available for the national body to address non-compliance → Select actions which are proportional to the objectives when applied individually or as a package (Dependency)
- connection removed: Identify non-compliance to individual articles of → Identify objectives of the applicable delegated act or the ITS directive affected by non-compliance (Dependency)
- **FRAME_ITS_Service_Process** Identify non-compliance to individual articles of the applicable delegated act `{3C58CE28-9384-47b8-AC17-414A0B505D90}` — *title change; substantive description change; metadata change*
  - name: ~~Identify actions available for the national body to address non-compliance~~ → **Identify non-compliance to individual articles of the applicable delegated act**
  - **All reported types of non-compliance should be recorded by the NB so as other data sets or services by the same or a different provider can also be checked against similar non-compliance issues. Non-provision of data The Delegated Regulations enacted under the European ITS Directive define obligations for several stakeholder groups to register data or services on the National Access Point, otherwise make it available and establish other obligations related to services and data (e.g. to provide data in a standardised format). It is possible that the National Body encounters situations in whic …
  - package: `National Body Reference Architecture/05 NB Communication View/Non Compliance Process` → `National Body Reference Architecture/NB Communication View/Non Compliance Process/Service Processes`
- connection added: Identify non-compliance to individual articles of the applicable delegated act → Collect possible other information related to identified non-compliance. (Dependency)
- connection added: Identify non-compliance to individual articles of the applicable delegated act → Optional: request further information from the stakeholder (Dependency)
- connection added: Identify non-compliance to individual articles of the applicable delegated act → Identify relevant stakeholder characteristics and cintextual factors related to non-complaint. (Dependency)
- connection added: Identify non-compliance to individual articles of the applicable delegated act → Receives administrative decision on compliance (Dependency)
- connection added: Identify non-compliance to individual articles of the applicable delegated act → Identify objectives of the applicable delegated act of the ITS directive by non-compliance (Dependency)
- **FRAME_ITS_Service_Process** Identify objectives of the applicable delegated act of the ITS directive by non-compliance `{51BC8E5A-6E2C-4209-8131-7AF457A731E9}` — *new object*
- connection added: Identify objectives of the applicable delegated act of the ITS directive by non-compliance → Identify possible actions which are proportional to the objectives when applied individually or as a package (Dependency)
- **FRAME_ITS_Service_Process** Identify possible actions which are proportional to the objectives when applied individually or as a package `{7615DF18-80CE-44f4-A8A0-6AC788682D66}` — *title change; substantive description change; metadata change*
  - name: ~~Select actions which are proportional to the objectives when applied individually or as a package~~ → **Identify possible actions which are proportional to the objectives when applied individually or as a package**
  - **In its current form, the Delegated Regulations or the ITS Directive define no administrative powers for the NB to address non-compliance. Moreover, the Delegated Regulations or the ITS Directive define no procedure for a situation in which the results of compliance assessment (based on random inspections) indicate non-compliance in a service or a data set. The options available to the NB are therefore subject to national regulations. The extent to which the NB is legally authorized to intervene in case of non-compliance and the type of actions it can take (e.g. rejection of submitted self-de …
  - package: `National Body Reference Architecture/05 NB Communication View/Non Compliance Process` → `National Body Reference Architecture/NB Communication View/Non Compliance Process/Service Processes`
- **FRAME_ITS_Service_Process** Identify relevant stakeholder characteristics and cintextual factors related to non-complaint. `{F6C45D87-E8EA-4ada-B52C-10DF47119321}` — *new object*
- connection added: Identify relevant stakeholder characteristics and cintextual factors related to non-complaint. → Identify possible actions which are proportional to the objectives when applied individually or as a package (Dependency)
- **FRAME_ITS_Service_Process** Information on potential non-compliance has been identifyed `{17EBAC7E-E847-47d1-9515-E747B015C202}` — *title change; substantive description change; metadata change*
  - name: ~~Identify objectives of the applicable delegated act or the ITS directive affected by non-compliance~~ → **Information on potential non-compliance has been identifyed**
  - ~~Identify objectives~~ **When reporting a non-compliance, the data users should be urged to provide a clear description** … ~~applicable delegated act~~ **non-compliance case they have identified, providing as much information as possible. Their own contact details should also be available to the NAP operator so that they can be reached if additional information is needed** … **even for a follow-up communication about** … ~~ITS directive affected~~ **treatment of the non-compliance case, depending on the communication policy of each NAP. The NB should support the data users for reporting comp …
  - package: `National Body Reference Architecture/05 NB Communication View/Non Compliance Process` → `National Body Reference Architecture/NB Communication View/Non Compliance Process/Service Processes`
- **FRAME_ITS_Service_Process** Initiate the actions prescribed in the decision on non-compliance and consequences of non-compliance `{77E39EED-5D44-4837-86A7-1D4FE22A5348}` — *title change; substantive description change; metadata change*
  - name: ~~Initiate the Actions prescribed in the decision on non-compliance and consequences of non-compliance~~ → **Initiate the actions prescribed in the decision on non-compliance and consequences of non-compliance**
  - **The actions of the NB should be proportional to the objective and the expected benefit to be achieved with the action. Therefore, increasing consequences should be clearly justified. The societal acceptance of serious consequences such as penalties will likely depend on the expected consequences of violating the applicable Delegated Regulation. It is also important that the consequences of non-compliance are applied in a transparent way, taking into account equal treatment of stakeholders. Penalties or other consequences could be justified e.g. in situations in which the infringement of the  …
  - package: `National Body Reference Architecture/05 NB Communication View/Non Compliance Process` → `National Body Reference Architecture/NB Communication View/Non Compliance Process/Service Processes`
- **FRAME_ITS_Service_Process** Investigate whether non-compliance has likely occurred `{A7F694D0-3401-4f76-937D-CBB2750B11BF}` — *title change; substantive description change; metadata change*
  - name: ~~~~ → **Investigate whether non-compliance has likely occurred**
  - ~~(e.g. severity and likelihood~~ **After a first investigation** … ~~impact)~~ **complaint by the NB depending on the resources available, the complaint could be further reported to the national authorities. All reported types of non-compliance should be recorded by the NB so as other data sets or services by the same or a different provider can also be checked against similar non-compliance issues.**
  - package: `National Body Reference Architecture/05 NB Communication View/Non Compliance Process` → `National Body Reference Architecture/NB Communication View/Non Compliance Process/Service Processes`
- connection added: Investigate whether non-compliance has likely occurred → No reason to expect non-compliance (Dependency)
- **FRAME_ITS_Service_Process** May appeals result `{0F014357-0944-4afd-BF33-3432540FEC30}` — *substantive description change; metadata change*
  - **The data or service provider may appeal the decision of the national body regarding the outcome of the random inspection according to procedures specified in national legislation.**
  - package: `National Body Reference Architecture/05 NB Communication View/Non Compliance Process` → `National Body Reference Architecture/NB Communication View/Non Compliance Process/Service Processes`
- **FRAME_ITS_Service_Process** No reason to expect non-compliance `{325F0B4B-A215-4be2-958B-FE3ABFFDEF1A}` — *new object*
- **FRAME_ITS_Service_Process** Optional: request further information from the stakeholder `{72D6074D-100F-45cc-967D-B8D5A4B6F924}` — *new object*
- connection added: Optional: request further information from the stakeholder → Identify possible actions which are proportional to the objectives when applied individually or as a package (Dependency)
- **FRAME_ITS_Service_Process** Process appeals made by the stakeholder `{9F4D540F-34D7-418e-B561-42E8C5D180F4}` — *title change; substantive description change; metadata change*
  - name: ~~Process appeals made by~~ → **Process appeals made by the stakeholder**
  - **Persisting non-compliance may be less possible to be identified through random inspections as the possibility to inspect again the same data set is rather low. However, it could be identified through repetitive complaints by data users or through the combination or random inspections and complaints. In their current form, the Delegated Regulations require Member States to assess compliance by receiving self-declarations and performing random inspections of the self-declarations. By definition, the selection of self-declarations for inspection is a random selection. Random inspections are the …
  - package: `National Body Reference Architecture/05 NB Communication View/Non Compliance Process` → `National Body Reference Architecture/NB Communication View/Non Compliance Process/Service Processes`
- connection added: Process appeals made by the stakeholder → Initiate the actions prescribed in the decision on non-compliance and consequences of non-compliance (Dependency)
- **FRAME_ITS_Service_Process** Random inspection of the self-declaration or the accompanying documents indicates non-compliance `{0B142C7E-8FB3-4b74-B4FA-E7FE2D238380}` — *title change; substantive description change; metadata change*
  - name: ~~Identify non-compliance to individual articles of~~ → **Random inspection of the self-declaration or the accompanying documents indicates non-compliance**
  - **Based on the compliance assessment process as defined in Milestone M5.3, it is clear that the non-compliance process is a follow-up process to the Compliance Assessment rather than an independent process. Specifically, random inspections of submitted self-declarations and the accompanying documents may result in the identification of non-compliance, which is documented through the compliance assessment results form. Based on the defined compliance assessment process, the identification of non-compliance based on random inspections might be the result of the: - Theoretical assessment (accordi …
  - package: `National Body Reference Architecture/05 NB Communication View/Non Compliance Process` → `National Body Reference Architecture/NB Communication View/Non Compliance Process/Service Processes`
- **FRAME_ITS_Service_Process** Receives administrative decision on compliance `{8C585B95-F1E0-488d-8095-B8C9D04ADE68}` — *new object*
- **FRAME_ITS_Service_Process** Receives administrative decision on non-compliance `{2D10B3DF-27FC-434a-B27C-1DBEC025DFA4}` — *substantive description change; metadata change*
  - **The service or data provider will receive an administrative decision on non-compliance.**
  - package: `National Body Reference Architecture/05 NB Communication View/Non Compliance Process` → `National Body Reference Architecture/NB Communication View/Non Compliance Process/Service Processes`
- connection added: Receives administrative decision on non-compliance → change documents, data or services according to  requested actions (Dependency)
- **FRAME_ITS_Service_Process** Select the action or a combination of actions which corresponds best to the objectives of national laws, the delegated acts and the ITS directive. `{24A1FBF5-07C2-46c6-BA46-73BC353DA4ED}` — *title change; metadata change*
  - name: ~~Select the action or a combination of Actions which best corresponds to the objectives of the delegated act and the ITS directive~~ → **Select the action or a combination of actions which corresponds best to the objectives of national laws, the delegated acts and the ITS directive.**
  - package: `National Body Reference Architecture/05 NB Communication View/Non Compliance Process` → `National Body Reference Architecture/NB Communication View/Non Compliance Process/Service Processes`
- **FRAME_ITS_Service_Process** change documents, data or services according to  requested actions `{0D6C06EB-41CC-48c1-86E9-5288373F3611}` — *new object*
- connection added: change documents, data or services according to  requested actions → Identify non-compliance to individual articles of the applicable delegated act (Dependency)

### National Body Reference Architecture/NB Communication View/Self-declaration Reception Process
- diagram **Self Declaration reception process** — elements added: Fill in harmonized NAPCORE self-declaration form, Hosting metadata of service or data set, Optional: Generate digital self-declaration, Processing feedback and correction of self-declaration, Receiving information about a DR relevant service or data set, Receiving updated self-declaration, Submit NAPCORE self-declaration form, The NB is receiving the self-declaration, The NB performs initial check of the self-declaration; elements removed: Check completness of the handed in self declaration, Correction of Self declaration, Fill in harmonized NAPCORE self declaration form, Fulfilling National Body activities and reliabilities according to ITS directive 2010/EU/40, Hosting Meta Data of service or data set, Processing feedback of self declaration, Receiving updated self declaration, Submit NAPCORE self declaration form, The NB is checking contact details of service and data provider, The NB is receiving the Self declaration, has to maybe correct contact details, is receiving information about a DR relevant service or data set
- **Package** Service Processes `{7F011F05-0E99-41ca-B3FB-AD27993F8E14}` — *metadata change*
  - package: `National Body Reference Architecture/05 NB Communication View` → `National Body Reference Architecture/NB Communication View/Self-declaration Reception Process`

### National Body Reference Architecture/NB Communication View/Self-declaration Reception Process/Service Processes
- **FRAME_ITS_Service_Process** Fill in harmonized NAPCORE self-declaration form `{AFAD8CA3-653B-40c4-8DA4-3FA1210DC161}` — *title change; metadata change*
  - name: ~~Fill in harmonized NAPCORE self declaration form~~ → **Fill in harmonized NAPCORE self-declaration form**
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Self-declaration Reception Process/Service Processes`
- **FRAME_ITS_Service_Process** Hosting metadata of service or data set `{37633241-ECB4-4e36-B8CE-1A367B786FA9}` — *title change; substantive description change; metadata change*
  - name: ~~Hosting Meta Data of service or data set~~ → **Hosting metadata of service or data set**
  - **In the case that the NAP is a meta data directory, the stakeholder publishes meta data on the data or service at the NAP according to the delegated regulations. In the case that the NAP is a data platform, the stakeholder describe and upload there data to the NAP. The NAP has to made the description and/or data accessible to the NB/CA.**
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Self-declaration Reception Process/Service Processes`
- connection added: Hosting metadata of service or data set → Publish information about service and data set (Dependency)
- **FRAME_ITS_Service_Process** Optional: Generate digital self-declaration `{1CBCF3DF-D807-4382-B235-54BC9911CEC5}` — *new object*
- connection added: Optional: Generate digital self-declaration → The NB is receiving the self-declaration (Dependency)
- **FRAME_ITS_Service_Process** Processing feedback and correction of self-declaration `{F3FAC284-6AB7-4dff-91BF-30E676B4F449}` — *title change; substantive description change; metadata change*
  - name: ~~Processing feedback of self declaration~~ → **Processing feedback and correction of self-declaration**
  - **If the stakeholder has to correct the self-declaration, the necessary changes are figured out and corrected.**
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Self-declaration Reception Process/Service Processes`
- connection added: Processing feedback and correction of self-declaration → Receiving updated self-declaration (Dependency)
- connection removed: Processing feedback of self declaration → Correction of Self declaration (Usage «Call»)
- **FRAME_ITS_Service_Process** Provides information for potential applicants `{511629E8-2B64-44be-AD7E-5B0D536AF7E0}` — *substantive description change; metadata change*
  - ~~body~~ **Body** … ~~(incl.~~ **including** … ~~)~~
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Self-declaration Reception Process/Service Processes`
- **FRAME_ITS_Service_Process** Publish information about service and data set `{EEEAD142-5CAF-4c12-BD1F-F23BAC12B31F}` — *metadata change*
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Self-declaration Reception Process/Service Processes`
- connection added: Publish information about service and data set → Optional: Generate digital self-declaration (Dependency)
- **FRAME_ITS_Service_Process** Receiving feedback about the status, correctness and time line `{857D8A5A-25DE-4a3b-B540-111B66E86B0A}` — *substantive description change; metadata change*
  - **The stakeholder will receive feedback on the status of the self-declaration. If there is a lack of completeness or any other obvious issue, the stakeholder will be asked for a correction of the self-declaration. If there is no issue found, the stakeholder will be informed that the self-declaration is accepted and that the self-declaration is in the pool for compliance assessments.**
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Self-declaration Reception Process/Service Processes`
- **FRAME_ITS_Service_Process** Receiving information about a DR relevant service or data set `{AD70904D-2757-48d6-8694-EB8A81FF4B5C}` — *title change; metadata change*
  - name: ~~is receiving information about a DR relevant service or data set~~ → **Receiving information about a DR relevant service or data set**
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Self-declaration Reception Process/Service Processes`
- connection removed: Receiving updated self declaration → Check completness of the handed in self declaration (Usage «Call»)
- **FRAME_ITS_Service_Process** Receiving updated self-declaration `{52A1D0E9-18F4-447f-9FAE-D82C183E31AC}` — *title change; substantive description change; metadata change*
  - name: ~~Receiving updated self declaration~~ → **Receiving updated self-declaration**
  - **The corrected self-declaration is sent to the National Body for a new approval.**
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Self-declaration Reception Process/Service Processes`
- connection added: Receiving updated self-declaration → The NB performs initial check of the self-declaration (Dependency)
- **FRAME_ITS_Service_Process** Submit NAPCORE self-declaration form `{1C797A58-9B2E-4a26-91AA-118A6AD4BE65}` — *title change; substantive description change; metadata change*
  - name: ~~Submit NAPCORE self declaration form~~ → **Submit NAPCORE self-declaration form**
  - ~~Self-declaration~~ **self-declaration**
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Self-declaration Reception Process/Service Processes`
- **FRAME_ITS_Service_Process** Submits service or data set description to national access point `{7B02B177-D0AC-4386-992A-752FF35B1A89}` — *substantive description change; metadata change*
  - **the** … ~~Todo: add types of stakeholder for necessary NAP description~~
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Self-declaration Reception Process/Service Processes`
- connection removed: Submits service or data set description to national access point → Publish information about service and data set (Usage «Call»)
- connection removed: The NB is checking contact details of service and data provider → has to maybe correct contact details (Association)
- connection removed: The NB is checking contact details of service and data provider → Check completness of the handed in self declaration (Usage «Call»)
- **FRAME_ITS_Service_Process** The NB is receiving the self-declaration `{EBF2FCE9-7013-4b62-8356-BF4F38EFC1DD}` — *title change; substantive description change; metadata change*
  - name: ~~The NB is receiving the Self declaration~~ → **The NB is receiving the self-declaration**
  - **The National Body receives the self-declaration in a harmonised format from the stakeholder or through the NAP.**
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Self-declaration Reception Process/Service Processes`
- **FRAME_ITS_Service_Process** The NB performs initial check of the self-declaration `{C786EAA8-695A-4db8-8B91-A185468C996F}` — *title change; substantive description change; metadata change*
  - name: ~~The NB is checking contact details of service and data provider~~ → **The NB performs initial check of the self-declaration**
  - **Within an initial check the completeness of the SD and the correctness of the contact information are proven.**
  - package: `National Body Reference Architecture/05 NB Communication View/Service Processes` → `National Body Reference Architecture/NB Communication View/Self-declaration Reception Process/Service Processes`
- connection added: The NB performs initial check of the self-declaration → Receiving feedback about the status, correctness and time line (Dependency)

## National Body Reference Architecture / NB Functional View

### National Body Reference Architecture/NB Functional View
- diagram **02 National Body Functional View** — elements added: Accepted, Access information, Accompanying Documents, Compliance assessment registry, General Public, General requests, Management of self-declaration, Managing general requests regarding self-declaration, Provide general information, Provide information, Provide relevant information, Provide self-declaration, Provide status of SD, Provides self-declaration form, Provision of information …; elements removed: Access Information, Acompanying Documents, Manage Requests, Management of Self Declaration, Provide Information, Provide Relevant Information, Provide general Information, Provides Self declaration form, Provision of Information, Receive Information, Receive Self-Declaration, Reporting of self declaration and compliance assessment results, Request Data, Request Self Declaration, Request Status of SD …
- **Package** Datastores `{3D4AD125-19DF-463e-8E2B-8880704E84E2}` — *metadata change*
  - package: `National Body Reference Architecture/02 NB Functional View` → `National Body Reference Architecture/NB Functional View`
- **Package** Information Objects `{879D67AB-7CEB-4962-8331-7D046F2EB2B4}` — *metadata change*
  - package: `National Body Reference Architecture/02 NB Functional View` → `National Body Reference Architecture/NB Functional View`
- **Package** LL DataFlows `{08776BAB-E60F-47ef-9174-081FE64F6D71}` — *metadata change*
  - package: `National Body Reference Architecture/02 NB Functional View` → `National Body Reference Architecture/NB Functional View`
- **Package** LL Functions `{C487BDE5-FA3A-4156-B3C6-33C9E7153EBA}` — *metadata change*
  - package: `National Body Reference Architecture/02 NB Functional View` → `National Body Reference Architecture/NB Functional View`
- **Package** Terminators `{87DFD2A8-168C-41d6-ABBC-1355C8C6757F}` — *metadata change*
  - package: `National Body Reference Architecture/02 NB Functional View` → `National Body Reference Architecture/NB Functional View`

### National Body Reference Architecture/NB Functional View/Datastores
- **FRAME_Datastore** Compliance assessment registry `{D2A4C9B8-BDD7-427c-81A6-1411C0F7B280}` — *title change; substantive description change; metadata change*
  - name: ~~Results Compliance Assessment Store~~ → **Compliance assessment registry**
  - ~~Todo: Harmonized CA check list per DR Results~~ **The storage "Results Compliance Assessment Store” fulfills the need for official storage of results of compliance assessments.The stored documents form the basis for reporting and back questioning of results. The compliance assessment store should contain the link to the used harmonized forms or comparable information (Member State specific). Furthermore, it should contain the contact details** … ~~CA Comments regarding CA~~ **people involved and a clear description of the result reasoning, and a description of inconsistencies.**
  - package: `National Body Reference Architecture/02 NB Functional View/Datastores` → `National Body Reference Architecture/NB Functional View/Datastores`
- connection added: Compliance assessment registry → Store CA result (Association «IN»)
- **FRAME_Datastore** Self-declaration Journal `{4EA8D521-CA96-4ea3-90A3-D303CC0AACA8}` — *title change; substantive description change; metadata change*
  - name: ~~Self Declaration Journal~~ → **Self-declaration Journal**
  - **like a journal** … ~~from~~ **regarding** … ~~on a self declaration like a journal.~~ **of self-declarations.**
  - package: `National Body Reference Architecture/02 NB Functional View/Datastores` → `National Body Reference Architecture/NB Functional View/Datastores`
- connection added: Self-declaration Journal → Status request on SD (Association «IN»)
- **FRAME_Datastore** Self-declaration Storage `{3D7503E7-23C4-4846-A45A-D63C8A3B4CC5}` — *title change; substantive description change; metadata change*
  - name: ~~Self Declarations~~ → **Self-declaration Storage**
  - ~~Todo:~~ … ~~Self Declarations needs~~ **self-declarations need** … ~~Should~~ **At least the latest version of a self-declaration should be stored either digitally or physically . Inactive, withdrawn or rejected self-declarations are stored according to national regulations and existing processes. The self-declaration metadata shoud follow the harmonized approach of NAPCORE and** … ~~a~~ **the following data entities: - Version number (Unique** … ~~number~~ **Identifier) - Status based on “Self-declaration State Diagram" - Reception date (When the SD is received) - Stakeholder name from stak …
  - package: `National Body Reference Architecture/02 NB Functional View/Datastores` → `National Body Reference Architecture/NB Functional View/Datastores`
- connection added: Self-declaration Storage → Template for self-declaration (Association «adheres to»)
- **FRAME_Datastore** Stakeholder List `{28C2E2B1-65B4-47fd-8903-FE3449030F55}` — *substantive description change; metadata change*
  - ~~Todo:~~ … ~~/ Competent Authority~~ … **information** … **to the stakeholders for fulfilling their tasks according to delegated regulations, national law and GDPR conformity. The stakeholder list should be updated when new** … ~~and the status~~ **is provided. Proposed structure** … ~~the self- declaration and assessment processes. !! Detail structure needs to be defined in WG5~~ **stakeholder contact information: - Stakeholder Name - Stakeholder identification (registration number, VAT number,...) - Registration Country Code - Contact details (at least mail address of organization or person …
  - package: `National Body Reference Architecture/02 NB Functional View/Datastores` → `National Body Reference Architecture/NB Functional View/Datastores`
- connection added: Stakeholder List → Request information (Association «IN»)
- connection removed: Stakeholder List → Request stakeholder (Association «IN»)

### National Body Reference Architecture/NB Functional View/Information Objects
- **FRAME_Information_Object** Self-declaration status `{E20F665C-1292-4b0b-98FA-C4339CC86620}` — *title change; substantive description change; metadata change*
  - name: ~~Self Declaration status~~ → **Self-declaration status**
  - ~~Self Declaration~~ **self-declaration status stores necessary information about the status and adaptations of a self-declaration within the several processes at the National Body. The Self-declaration** … ~~self declaration)~~ **self-declaration)** … ~~name~~ **information (according to stakeholder list) -) status of self-declaration** … ~~changed~~ **lead to version or status change**
  - package: `National Body Reference Architecture/02 NB Functional View/Information Objects` → `National Body Reference Architecture/NB Functional View/Information Objects`

### National Body Reference Architecture/NB Functional View/LL DataFlows
- **FRAME_Low_Level_Data_Flow** Accepted `{07E61B1B-8832-4b8a-A195-03143D401995}` — *new object*
- connection added: Accepted → Provide NB support (Association «OUT»)
- **FRAME_Low_Level_Data_Flow** Access information `{37D92C6B-5199-4a9d-8837-0740EF3B1A41}` — *title change; metadata change*
  - name: ~~Access Information~~ → **Access information**
  - package: `National Body Reference Architecture/02 NB Functional View` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** General requests `{867F3DE7-6F39-43bf-A1C0-A31185A4482C}` — *title change; metadata change*
  - name: ~~general requests~~ → **General requests**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Information `{795AD710-6C2B-413d-82BC-EEAFA1766EDB}` — *metadata change*
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Information about SD obligation `{7BA75E54-A1DD-420f-B358-F2B59B2985F5}` — *metadata change*
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Information about status `{601B22D4-F573-4e35-A0DC-8F110BD53E3E}` — *metadata change*
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Provide general information `{6442F7CD-399A-445c-B5F5-DDF9E7793EEF}` — *title change; metadata change*
  - name: ~~Provide general Information~~ → **Provide general information**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Provide information `{FE7E453C-D410-48c5-941E-318C5EA83B2F}` — *title change; metadata change*
  - name: ~~Provide Information~~ → **Provide information**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Provide relevant information `{1F4A95C9-FA17-476b-9132-B64B2502702F}` — *title change; metadata change*
  - name: ~~Provide Relevant Information~~ → **Provide relevant information**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Provide self-declaration `{E7A8112B-9F75-4601-B108-9964DC50FED0}` — *title change; metadata change*
  - name: ~~Request Self Declaration~~ → **Provide self-declaration**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Provide status of SD `{CB5D3CF4-3486-4ced-AFF0-E84DF5C64C48}` — *title change; metadata change*
  - name: ~~Request Status of SD~~ → **Provide status of SD**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Provides self-declaration form `{E0D893E9-3F96-49c4-9FBF-48591C8B77A4}` — *title change; metadata change*
  - name: ~~Provides Self declaration form~~ → **Provides self-declaration form**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Provision of information `{355BC2B3-2112-47fb-8CE0-D3677715B5D8}` — *title change; metadata change*
  - name: ~~Provision of Information~~ → **Provision of information**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Receive information `{A7C5E4D2-4C96-488d-9021-DE2192FDD1E3}` — *title change; metadata change*
  - name: ~~Receive Information~~ → **Receive information**
  - package: `National Body Reference Architecture/02 NB Functional View` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Request `{D92DEB09-7102-4a53-B622-F98C50736668}` — *new object*
- **FRAME_Low_Level_Data_Flow** Request `{DAA1751E-B997-47be-9076-48B04D2051EC}` — *new object*
- connection added: Request → Compliance Assessment (Association «OUT»)
- connection added: Request → Managing general requests regarding self-declaration (Association «OUT»)
- connection removed: Request Data → Validation of Completness (Association «OUT»)
- **FRAME_Low_Level_Data_Flow** Request data `{A0A7EF5B-0F75-48ac-9FD3-C6DB2915A800}` — *title change; metadata change*
  - name: ~~Request Data~~ → **Request data**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Request for providing information `{04FE4FC1-5A04-424c-8D06-96D805AA1556}` — *title change; metadata change*
  - name: ~~Request for providing Information~~ → **Request for providing information**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Request general information `{2D8D8356-1D5E-42b7-B9BB-BCDFD97F2C95}` — *title change; metadata change*
  - name: ~~Request general Information~~ → **Request general information**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Request information `{61F9DAAD-6D92-4838-91FA-32D72DE2C4F4}` — *new object*
- connection added: Request information → Validation of completeness (Association «OUT»)
- **FRAME_Low_Level_Data_Flow** Request relevant SD information `{05F09947-F13A-4ae9-B944-9672D5872516}` — *metadata change*
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Request report `{DF5BDDBC-E821-466c-AB68-27AD7E5038CF}` — *new object*
- connection added: Request report → Reporting of self-declaration and compliance assessment results (Association «OUT»)
- **FRAME_Low_Level_Data_Flow** Request self-declaration `{A8DDF368-5294-4b6d-9BA7-4AD1436DC838}` — *new object*
- **FRAME_Low_Level_Data_Flow** Request self-declaration `{B7AFE5CB-2A70-48ce-9ACC-91B5CA776A2B}` — *title change; metadata change*
  - name: ~~Request Self Declaration~~ → **Request self-declaration**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- connection added: Request self-declaration → Self-declaration Storage (Association «OUT»)
- **FRAME_Low_Level_Data_Flow** Request status of SD `{D53E8616-4F42-4b0d-9A5B-35DB6ABA28D3}` — *new object*
- connection added: Request status of SD → Self-declaration Journal (Association «OUT»)
- **FRAME_Low_Level_Data_Flow** Response `{3F75E697-74ED-4d4f-852D-4F9B4927C399}` — *new object*
- **FRAME_Low_Level_Data_Flow** Response `{BB8C1624-E80F-46f9-9D4E-137043169ED0}` — *new object*
- connection added: Response → Handling Non-Compliance (Association «OUT»)
- connection added: Response → Handling Non-Compliance (Association «OUT»)
- **FRAME_Low_Level_Data_Flow** SD details `{6F33D268-087B-4626-946B-36BE3CE60116}` — *title change; metadata change*
  - name: ~~SD Details~~ → **SD details**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Send report `{616DB36E-4251-4b12-BD54-58105CB20637}` — *title change; metadata change*
  - name: ~~Send Report~~ → **Send report**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Status SD `{80647EEC-C009-432c-9451-A433608E8B8B}` — *new object*
- connection added: Status SD → Validation of completeness (Association «OUT»)
- **FRAME_Low_Level_Data_Flow** Status details SD `{89A547AC-1519-4a98-8C0B-35A678FA7586}` — *title change; metadata change*
  - name: ~~Status Details SD~~ → **Status details SD**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Status of CA `{863DE7F6-BB4C-4bf5-A4F1-2351D0273C65}` — *metadata change*
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Status of CA `{89C549FA-9351-4a9f-B8CB-02E00D983144}` — *title change; metadata change*
  - name: ~~status of CA~~ → **Status of CA**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Status of CA `{B966942A-D11B-46f8-8082-B2CAAAF82E75}` — *new object*
- connection added: Status of CA → Compliance assessment registry (Association «OUT»)
- **FRAME_Low_Level_Data_Flow** Status of SD `{17E98F9A-7E4B-4e4c-9D4E-61F335A5A284}` — *metadata change*
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Status of request `{4A25B12D-81DB-4e1a-9F7A-61545373A048}` — *metadata change*
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Status of requested SD `{524E697F-9C46-42bb-B366-74B380D7F591}` — *metadata change*
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Status request on SD `{043B9875-7D84-4fa5-A611-0D64FC6EB57D}` — *new object*
- connection added: Status request on SD → Handling Non-Compliance (Association «OUT»)
- **FRAME_Low_Level_Data_Flow** Status update `{28B4DEC2-D621-4b4e-AF18-B8E34B28E0A2}` — *title change; metadata change*
  - name: ~~Status Update~~ → **Status update**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Store CA result `{49E07AE1-EBBA-436a-8648-93FBA8754532}` — *new object*
- **FRAME_Low_Level_Data_Flow** Store CA result `{9105DF71-6B49-44e7-B2E3-4EFC9779D6BB}` — *metadata change*
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- connection added: Store CA result → Handling Non-Compliance (Association «OUT»)
- **FRAME_Low_Level_Data_Flow** Store Information `{FE598186-5858-44b4-8B51-2BE7D8C848BD}` — *new object*
- connection added: Store Information → Stakeholder List (Association «OUT»)
- **FRAME_Low_Level_Data_Flow** Store registered SD in storage `{A4486CEE-A577-4037-BEAA-01463BFDDF78}` — *title change; metadata change*
  - name: ~~Store registered SD in Storage~~ → **Store registered SD in storage**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Store self-declaration `{648DBA1F-EA00-43e6-B28A-C5E117297931}` — *title change; metadata change*
  - name: ~~Store Self Declaration~~ → **Store self-declaration**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Store stakeholder information `{D58832E7-6942-4a0f-A4C3-89BC3C2C25B5}` — *title change; metadata change*
  - name: ~~Store Stakeholder Information~~ → **Store stakeholder information**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Stores changed self-declaration `{AAD2DC61-766E-46de-B2D7-C07D8651F447}` — *title change; metadata change*
  - name: ~~Stores changed Self Declaration~~ → **Stores changed self-declaration**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Update journal information `{0CDB1EF8-4915-400e-8562-F5460060C37F}` — *title change; substantive description change; metadata change*
  - name: ~~Update Journal Information~~ → **Update journal information**
  - ~~Update~~ **An update or change of a** … ~~Journal by creating~~ **or a change of related stakeholder will lead to** … ~~if~~ **within** … ~~Self-declaration, Stakeholder or other related information changed. Register~~ **Self-declaration journal. All** … ~~respondents.~~ **respondents should be registered.**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** Update journal information `{82BB9579-0354-4fa1-91CC-A01F31ED41DF}` — *new object*
- connection added: Update journal information → Self-declaration Journal (Association «OUT»)
- **FRAME_Low_Level_Data_Flow** Validation results `{950BA35B-7663-4e1f-91FC-5EA5A52C2934}` — *title change; metadata change*
  - name: ~~Validation Results~~ → **Validation results**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`
- **FRAME_Low_Level_Data_Flow** receives relevant SD information `{2EA36102-8FB4-41e5-8384-277130A0855B}` — *title change; metadata change*
  - name: ~~receivs relevant SD information~~ → **receives relevant SD information**
  - package: `National Body Reference Architecture/02 NB Functional View/LL DataFlows` → `National Body Reference Architecture/NB Functional View/LL DataFlows`

### National Body Reference Architecture/NB Functional View/LL Functions
- **FRAME_Low_Level_Function** Access Information on NAP `{0C0582A3-C5C5-4ea0-8504-DE328D35C702}` — *substantive description change; metadata change*
  - ~~not defined in WG5 yet Todo~~ … ~~/ Competent Authority~~
  - package: `National Body Reference Architecture/02 NB Functional View/LL Functions` → `National Body Reference Architecture/NB Functional View/LL Functions`
- **FRAME_Low_Level_Function** Compliance Assessment `{91C7B206-E453-4ab9-B0B6-D08FDE6075D8}` — *substantive description change; metadata change*
  - ~~NBs/CAs~~ **National Bodies** … ~~NBs/CAs~~ **National Bodies** … **A National Body should be capable to perform at least 1 compliance assessment per year for delegated regulation where active self-declarations exist. The National Body should direct its efforts to perform compliance assessments according to the number of active self-declarations related to each delegated act.**
  - package: `National Body Reference Architecture/02 NB Functional View/LL Functions` → `National Body Reference Architecture/NB Functional View/LL Functions`
- connection added: Compliance Assessment → Response (Association «IN»)
- **FRAME_Low_Level_Function** Handling Non-Compliance `{1D8C33F8-CF43-44a6-8E15-D5CC49B29943}` — *substantive description change; metadata change*
  - ~~preferable in~~ **recommended throughout** … ~~national body~~ **National Body** … **Details are shown within the Non-compliance process description.**
  - package: `National Body Reference Architecture/02 NB Functional View` → `National Body Reference Architecture/NB Functional View/LL Functions`
- connection added: Handling Non-Compliance → Status of CA (Association «IN»)
- connection added: Handling Non-Compliance → Request (Association «IN»)
- connection added: Handling Non-Compliance → Request (Association «IN»)
- connection added: Handling Non-Compliance → Update journal information (Association «IN»)
- **FRAME_Low_Level_Function** Manage Stakeholder List `{35C53FD1-0C8A-49dc-85AE-E2D72F886A54}` — *substantive description change; metadata change*
  - ~~Management of the~~ **The National Body has to manage a** … ~~Requirements:~~ **to perform stakeholder SD requests, keep track of the status of stakeholders and for any other request.** … **stakeholder list has to be established and maintained in compliance with GDPR which means that only necessary information should be included and stored. The initial** … ~~respondents~~ **stakeholders** … **field research and** … ~~The following data is a proposal for the content to be stored in the list: company name, address, contact information, ID of self-declaration form (Template), submitting date, e …
  - package: `National Body Reference Architecture/02 NB Functional View/LL Functions` → `National Body Reference Architecture/NB Functional View/LL Functions`
- **FRAME_Low_Level_Function** Management of self-declaration `{12F2142B-1179-455b-9F44-335FE9CBB4D2}` — *title change; substantive description change; metadata change*
  - name: ~~Management of Self Declaration~~ → **Management of self-declaration**
  - ~~Management~~ **The management** … ~~repository~~ **self-declaration describes a basic work principle** … ~~declaration forms Requirements: All types of self-declaration forms (templates) with~~ **<ins>a </ins>NB. The principles for processing self-declarations are: (1) Self -declarations have unique identifiers (2) Self-declarations received and accepted by the national body are immutable (3) Self-declarations are stateful (always have** … ~~detailed description and filling instructions are uploaded in~~ **defined status) (4) Self-declarations can be withdrawn by** … ~~repository. Each templ …
  - package: `National Body Reference Architecture/02 NB Functional View/LL Functions` → `National Body Reference Architecture/NB Functional View/LL Functions`
- connection added: Management of self-declaration → Status SD (Association «IN»)
- **FRAME_Low_Level_Function** Managing general requests regarding self-declaration `{45963755-0898-4846-8129-F2724C86B673}` — *title change; substantive description change; metadata change*
  - name: ~~Manage Requests~~ → **Managing general requests regarding self-declaration**
  - ~~Todo: Handle Requests: Withdraw SD General~~ **The National Body may receive** … **related to self-declarations at any time. These requests may be requests for information about the self-declaration, request from the stakeholder to replace the self-declaration with a newer version or other requests which may change the state of a self-declaration.**
  - package: `National Body Reference Architecture/02 NB Functional View/LL Functions` → `National Body Reference Architecture/NB Functional View/LL Functions`
- connection added: Managing general requests regarding self-declaration → Response (Association «IN»)
- **FRAME_High_Level_Function** Provide NB support `{3577F755-7777-4b9e-AAF8-F0A7532ACE4A}` — *substantive description change; metadata change*
  - ~~/ Competent Authority has~~ **shall, within its competence, provide its customers, as necessary, with advice on dealing with administrative matters and respond to questions and enquiries concerning** … ~~task to provide information to private and public stakeholders, organization, interested persons and answer any other related information request. Stakeholder: Stakeholder as main focus group can~~ **use of its services. Advice shall** … ~~informed about their tasks and obligations based on the ITS directive 2010/40/EU and their delegated regulations which includes deadlines,~~ **provided fr …
  - package: `National Body Reference Architecture/02 NB Functional View/LL Functions` → `National Body Reference Architecture/NB Functional View/LL Functions`
- **FRAME_Low_Level_Function** Receive self-declaration `{F49ACE9E-16BD-430e-AAFF-5A858FC334B9}` — *title change; substantive description change; metadata change*
  - name: ~~Receive Self-Declaration~~ → **Receive self-declaration**
  - ~~/ Competent Authority~~ … ~~self declarations~~ **self-declarations** … ~~self declarations~~ **self-declarations** … **provided by an authorized person or**
  - package: `National Body Reference Architecture/02 NB Functional View/LL Functions` → `National Body Reference Architecture/NB Functional View/LL Functions`
- **FRAME_Low_Level_Function** Reporting of self-declaration and compliance assessment results `{395DED00-A80C-418c-A674-B65B7434A6E0}` — *title change; substantive description change; metadata change*
  - name: ~~Reporting of self declaration and compliance assessment results~~ → **Reporting of self-declaration and compliance assessment results**
  - ~~received self-declarations,~~ … ~~assessments, expired~~ **assessments** … ~~changes in the stakeholders~~ **received self-declaration** … ~~in the long run, to the~~ **further** … ~~may need to adopt!~~
  - package: `National Body Reference Architecture/02 NB Functional View/LL Functions` → `National Body Reference Architecture/NB Functional View/LL Functions`
- connection added: Reporting of self-declaration and compliance assessment results → Request self-declaration (Association «IN»)
- connection added: Reporting of self-declaration and compliance assessment results → Request status of SD (Association «IN»)
- connection removed: Validation of Completness → Store Stakeholder Information (Association «IN»)
- **FRAME_Low_Level_Function** Validation of completeness `{3D931997-C649-47cd-B6F6-261C8137D773}` — *title change; substantive description change; metadata change*
  - name: ~~Validation of Completness~~ → **Validation of completeness**
  - ~~/ Competent Authority~~ … **stakeholder contact details. At minimum,** … ~~Stakeholder~~ **National Body shall validate that all required** … ~~and validation~~ **have been provided. The National Body may validate contact information** … ~~registration including~~ **the stakeholder based on business** … ~~Check~~ **The National Body should check** … ~~correctness~~ **completeness** … ~~Requirements: Base~~ **based** … ~~(agreed~~ **agreed** … ~~NAPCORE) system check the correctness of the filled-in declaration form(s) and/or other documents/information The NB/CA has to check if the self-decl …
  - package: `National Body Reference Architecture/02 NB Functional View/LL Functions` → `National Body Reference Architecture/NB Functional View/LL Functions`
- connection added: Validation of completeness → Store Information (Association «IN»)

### National Body Reference Architecture/NB Functional View/Terminators
- **FRAME_Terminator** Data- and/or Service provider(s) `{4BBDECD9-7CB6-4269-9AA6-DE1A948C9995}` — *metadata change*
  - package: `National Body Reference Architecture/02 NB Functional View/Terminators` → `National Body Reference Architecture/NB Functional View/Terminators`
- **FRAME_Terminator** General Public `{DEC15748-EB48-4dce-BABA-FDB1698EC9A9}` — *title change; substantive description change; metadata change*
  - name: ~~general Public~~ → **General Public**
  - ~~General Public~~ **“General Public”** … ~~public Persons~~ **physical or juridical persons, companies, and authorities** … ~~has~~ **have** … ~~NB/CA. Any person, company~~ **National Body** … ~~authority which is not affected by the ITS directive is part of the General Public. The Terminator "General Public" represents~~ … ~~real entity which is generating information to start a process or functionality or receives information to end a process or functionality~~ **related topic.**
  - package: `National Body Reference Architecture/02 NB Functional View/Terminators` → `National Body Reference Architecture/NB Functional View/Terminators`
- **FRAME_Terminator** Member States `{E2280DC8-3870-4bca-B9D9-0B0F048FF2BE}` — *metadata change*
  - package: `National Body Reference Architecture/02 NB Functional View/Terminators` → `National Body Reference Architecture/NB Functional View/Terminators`
- connection added: Member States → Accepted (Association «IN»)
- connection added: Member States → Request report (Association «IN»)
- **FRAME_Terminator** National Access Point(s) `{6902FEFA-51CE-4958-A449-99F7F9CA5213}` — *substantive description change; metadata change*
  - **The Terminator "National Access Point(s)" represents authorized National Access Points (NAPs) for the Delegated Regulations of the ITS Directive 2010/40/EU per Member State. The NAP has to provide information about registered stakeholders, registered data sets and related service publications. In the case that a NAP is a data portal, the NAP has to provide access to data or service content while a compliance assessment is performed.**
  - package: `National Body Reference Architecture/02 NB Functional View` → `National Body Reference Architecture/NB Functional View/Terminators`

## National Body Reference Architecture / NB Motivational Layer

### National Body Reference Architecture/NB Motivational Layer
- diagram **00_NB_Motivational View** — elements added: Benefit of harmonized data and service provision, Enhance compatibility and interoperability, European Commission, Guideline for a harmonised National Body setup, Harmonize the National Body services within the EU, National Access Point, National Body, Support for reporting related to ITS Directive 2010/40/EU; elements removed: Benefit of harmonized data and service provission, Competent Authority / National Body, Enhance compatibility and Interoperability, European Commision, Guideline for a harmonised NB / CA setup, Harmonize the NB/CA services within the EU, Support for Reporting related to ITS Directive 2010/40/EU
- **Package** Actors `{CFB13735-5244-4131-BB33-66128934DB41}` — *metadata change*
  - package: `National Body Reference Architecture/00 NB Motivational Layer` → `National Body Reference Architecture/NB Motivational Layer`
- **Package** Business Expectations `{A5823C66-53E9-4a12-B24C-E7D63763F03E}` — *metadata change*
  - package: `National Body Reference Architecture/00 NB Motivational Layer` → `National Body Reference Architecture/NB Motivational Layer`
- **Package** Further Elements `{717646F4-55FF-4355-AE83-03588DD83945}` — *metadata change*
  - package: `National Body Reference Architecture/00 NB Motivational Layer` → `National Body Reference Architecture/NB Motivational Layer`
- **Package** ITS added Value `{65B6FE48-9CD0-4540-84D0-54C6859CC201}` — *metadata change*
  - package: `National Body Reference Architecture/00 NB Motivational Layer` → `National Body Reference Architecture/NB Motivational Layer`
- **Package** Stakeholders `{8D17021F-3C5A-4fb4-800F-1C2019C30E2D}` — *metadata change*
  - package: `National Body Reference Architecture/00 NB Motivational Layer` → `National Body Reference Architecture/NB Motivational Layer`

### National Body Reference Architecture/NB Motivational Layer/Actors
- **FRAME_Actor** Data and Service provider `{519E02B4-F4D7-495f-ACC1-B82E0680B31E}` — *metadata change*
  - package: `National Body Reference Architecture/00 NB Motivational Layer/Actors` → `National Body Reference Architecture/NB Motivational Layer/Actors`
- **FRAME_Actor** European Commission `{9999A38F-B70B-4274-BB81-5A16EB37D298}` — *title change; substantive description change; metadata change*
  - name: ~~European Commision~~ → **European Commission**
  - ~~European Commission~~ **The** … **“European Commission”** … ~~Stakeholder~~ **linked** … ~~reference architecture.~~ **Reference Architecture.**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/Actors` → `National Body Reference Architecture/NB Motivational Layer/Actors`
- **FRAME_Actor** Member State `{1B1FBA82-B717-4b02-AE66-E1142B61E091}` — *substantive description change; metadata change*
  - ~~Member State~~ **The** … **“Member State”** … **linked**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/Actors` → `National Body Reference Architecture/NB Motivational Layer/Actors`
- **FRAME_Actor** NAP `{31B3A51A-5110-47a3-BAEF-C16326164254}` — *substantive description change; metadata change*
  - ~~NAP~~ **actor “NAP** … ~~Point) Actor~~ **Point)”** … **linked**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/Actors` → `National Body Reference Architecture/NB Motivational Layer/Actors`
- **FRAME_Actor** National Body / Competent Authority `{49B680E5-0E20-48ea-8253-4FEEF7CEBB85}` — *substantive description change; metadata change*
  - ~~NB/CA (National~~ **National** … ~~/ Competent Authority) Actor~~ **actor** … ~~NB/CA~~ **National Body** … **linked** … ~~National Body Reference Architecture.~~ **NB reference architecture.**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/Actors` → `National Body Reference Architecture/NB Motivational Layer/Actors`

### National Body Reference Architecture/NB Motivational Layer/Business Expectations
- **FRAME_Business_Expectation** Guideline for a harmonised National Body setup `{BC7D188D-EF51-432d-98F0-DCFFBC7DD15D}` — *title change; substantive description change; metadata change*
  - name: ~~Guideline for a harmonised NB / CA setup~~ → **Guideline for a harmonised National Body setup**
  - ~~A guideline~~ **Guidelines** … ~~NB/CA operating~~ **National Body to operate**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/Business Expectations` → `National Body Reference Architecture/NB Motivational Layer/Business Expectations`
- **FRAME_Business_Expectation** Guideline for operation of National Bodies `{5E9DF39C-6000-43d3-9226-88DCD911CCC0}` — *editorial description change; metadata change*
  - ~~/ Competent Authority~~
  - package: `National Body Reference Architecture/00 NB Motivational Layer/Business Expectations` → `National Body Reference Architecture/NB Motivational Layer/Business Expectations`
- **FRAME_Business_Expectation** Obligations and Interactions `{4355144F-8BD4-4b25-94CB-E69C5B98871A}` — *editorial description change; metadata change*
  - ~~The~~ … ~~the~~ … ~~NB/CA~~ **National Body**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/Business Expectations` → `National Body Reference Architecture/NB Motivational Layer/Business Expectations`
- **FRAME_Business_Expectation** Requirements `{A25E0F1A-B731-4e92-B10F-C75E52119119}` — *substantive description change; metadata change*
  - ~~NB/CA~~ **National Body** … ~~Data~~ **data** … ~~Metadata.~~ **metadata.** … ~~NB/CA~~ **National Body** … ~~Data~~ **data** … ~~Metadata.~~ **metadata.**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/Business Expectations` → `National Body Reference Architecture/NB Motivational Layer/Business Expectations`
- **FRAME_Business_Expectation** facilitate a harmonized implementation `{01EE4DC2-403A-4982-AD07-A61EEB10017F}` — *metadata change*
  - package: `National Body Reference Architecture/00 NB Motivational Layer/Business Expectations` → `National Body Reference Architecture/NB Motivational Layer/Business Expectations`

### National Body Reference Architecture/NB Motivational Layer/Further Elements
- **FRAME_ITS_Domain** Delegated Regulations of ITS Directive 2010/EU/40 `{2C719A1A-9DD9-4d49-B156-FE9A59A7297C}` — *substantive description change; metadata change*
  - ~~Description~~ **Priority Action a** … **the ITS Directive 2010/40/EU • Commission** … ~~Acts Decription by Anna~~ **Regulation (EU) 2017/1926 • Abbreviation: MMTIS the provision of EU-wide multimodal travel information services Priority Action c of the ITS Directive 2010/40/EU • Commission Delegated Regulation (EU) No 886/2013 • Abbreviation: SRTI the provision of road safety related minimum universal traffic information free of charge to users Priority Action b of the ITS Directive 2010/40/EU • Commission Delegated Regulation (EU) 2015/962 • Commission Delegated Regulation (EU) 2022/670 • A …
  - package: `National Body Reference Architecture/00 NB Motivational Layer/Further Elements` → `National Body Reference Architecture/NB Motivational Layer/Further Elements`
- **FRAME_ITS_Service** Fulfilling National Body activities and reliabilities according to ITS directive 2010/EU/40 `{01809F43-C4B8-4445-BF4A-91BFA2C95612}` — *substantive description change; metadata change*
  - ~~or Competent Authority (CA)~~ … ~~validate~~ **ensure that data publishers, service providers and NAP meet** … ~~fulfillment of~~ **obligations and requirements expressed in** … ~~Regulation by data publishers, service providers and NAP.~~ **Regulation.**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/Further Elements` → `National Body Reference Architecture/NB Motivational Layer/Further Elements`
- **FRAME_Mission_Statement** National Body Mission_Statement `{19CCAB3F-C533-4107-9E55-E64EF97E7204}` — *substantive description change; metadata change*
  - ~~NBs/CAs~~ **National Bodies** … ~~by the government~~ … ~~recognized~~ **appointed** … ~~regulate,~~ **regulate** … ~~This project has received funding from the European Commission’s Directorate General for Transport and Mobility under Grant Agreement no. MOVE/B4/SUB/2020-123/SI2.8522338~~ … ~~NB/CA~~ **NATIONAL BODY** … ~~assessments~~ **declaration**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/Further Elements` → `National Body Reference Architecture/NB Motivational Layer/Further Elements`

### National Body Reference Architecture/NB Motivational Layer/ITS added Value
- **FRAME_ITS_Service_Added_Value** Benefit of harmonized data and service provision `{AD0AB7BA-9057-4189-A00C-62FE78C9D5AE}` — *title change; editorial description change; metadata change*
  - name: ~~Benefit of harmonized data and service provission~~ → **Benefit of harmonized data and service provision**
  - ~~Service~~ **service**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/ITS added Value` → `National Body Reference Architecture/NB Motivational Layer/ITS added Value`
- **FRAME_ITS_Service_Added_Value** Clear set of requirements for interaction with National Body `{4C158BCC-CD38-45a7-9FF6-FDED6FDBC52F}` — *substantive description change; metadata change*
  - ~~shall provide~~ **provides a** … ~~the NB/CA~~ **a National Body** … ~~their~~ **its**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/ITS added Value` → `National Body Reference Architecture/NB Motivational Layer/ITS added Value`
- **FRAME_ITS_Service_Added_Value** EU-wide common understanding of Delegated Regulations `{580E3C77-C562-473c-BBD2-D6585D8DD756}` — *substantive description change; metadata change*
  - ~~NB/CA carry~~ **National Body carries**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/ITS added Value` → `National Body Reference Architecture/NB Motivational Layer/ITS added Value`
- **FRAME_ITS_Service_Added_Value** Enhance compatibility and interoperability `{8486EBB2-0EEA-436d-A342-48C3BC633C4F}` — *title change; metadata change*
  - name: ~~Enhance compatibility and Interoperability~~ → **Enhance compatibility and interoperability**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/ITS added Value` → `National Body Reference Architecture/NB Motivational Layer/ITS added Value`
- **FRAME_ITS_Service_Added_Value** Enhance the findability of data and services `{86293EBE-E7A8-420e-918D-71348D4A2179}` — *substantive description change; metadata change*
  - ~~metadata~~ **meta data** … ~~NB/CA~~ **National Body** … ~~findability~~ **find ability** … ~~services~~ **services.**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/ITS added Value` → `National Body Reference Architecture/NB Motivational Layer/ITS added Value`
- **FRAME_ITS_Service_Added_Value** Fulfilling National Body activities and reliabilities according to ITS directive 2010/EU/40 `{CDF218F4-473F-4efb-BF89-FFA69FBEB182}` — *editorial description change; metadata change*
  - ~~NB/CA~~ **National Body** … ~~NB/CA~~ **National Body** … **that**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/ITS added Value` → `National Body Reference Architecture/NB Motivational Layer/ITS added Value`
- **FRAME_ITS_Service_Added_Value** Harmonize the National Body services within the EU `{50BDB632-68AD-4fee-A070-2BFE8F8CB099}` — *title change; editorial description change; metadata change*
  - name: ~~Harmonize the NB/CA services within the EU~~ → **Harmonize the National Body services within the EU**
  - ~~NB/CA~~ **National Body**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/ITS added Value` → `National Body Reference Architecture/NB Motivational Layer/ITS added Value`
- **FRAME_ITS_Service_Added_Value** Harmonized approach to engage with international Data and Service provider `{9D476FCC-FC0A-4a0c-BCBF-E471CEB6B2B3}` — *substantive description change; metadata change*
  - ~~Create~~ **Aim is to create** … ~~Todo:~~ **Many stakeholders affected by the Delegated Regulations are multinational companies. By working together, National Bodies not only gain more credibility but also strengthen their negotiating power, enabling them** … ~~be proposed by WG 5.3/5.4 in 2024 cross boarder situation Service provider is located outside the EU~~ **engage effectively with these large multinational entities. Finally, collaboration among National Bodies reduces duplication of efforts, leading to more efficient and consistent compliance assessments, information sharing and stake …
  - package: `National Body Reference Architecture/00 NB Motivational Layer/ITS added Value` → `National Body Reference Architecture/NB Motivational Layer/ITS added Value`
- **FRAME_ITS_Service_Added_Value** Harmonized self-declaration process for international data and service provider `{4A4D2B0E-B0EE-425a-ABDE-41C38E9D1124}` — *substantive description change; metadata change*
  - ~~the~~ **a** … **for handling** … ~~the handling the~~ … ~~the~~ … ~~procedure~~ … ~~procedure~~ **procedures**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/ITS added Value` → `National Body Reference Architecture/NB Motivational Layer/ITS added Value`
- **FRAME_ITS_Service_Added_Value** Increased findability and visibility of data and services EU-wide `{01C4D60E-1558-4de7-9575-728A916C7F27}` — *substantive description change; metadata change*
  - ~~a~~ … ~~the~~ … ~~NB / CA,~~ **National Body,** … ~~completness,~~ **completeness,** … **of the datasets** … ~~findability~~ **find ability** … **increases** … ~~an EU-wide level increases.~~ **EU level.**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/ITS added Value` → `National Body Reference Architecture/NB Motivational Layer/ITS added Value`
- **FRAME_ITS_Service_Added_Value** Seamless National Body Services `{16E637F0-B3DD-4413-9C65-E245232818AD}` — *editorial description change; metadata change*
  - ~~a~~ **an**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/ITS added Value` → `National Body Reference Architecture/NB Motivational Layer/ITS added Value`
- **FRAME_ITS_Service_Added_Value** Support for reporting related to ITS Directive 2010/40/EU `{8AAF2D23-1131-42a5-89A7-087AB2944800}` — *title change; substantive description change; metadata change*
  - name: ~~Support for Reporting related to ITS Directive 2010/40/EU~~ → **Support for reporting related to ITS Directive 2010/40/EU**
  - ~~(2010/40/EU~~ **(2010/40/EU)** … ~~their delegated acts,~~ **related Delegated Regulations,** … **the**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/ITS added Value` → `National Body Reference Architecture/NB Motivational Layer/ITS added Value`

### National Body Reference Architecture/NB Motivational Layer/Stakeholders
- **FRAME_Stakeholder** Data and Service provider `{18125799-A9C0-4e9d-B88E-C02A31FA9163}` — *editorial description change; metadata change*
  - ~~National and~~ **A national or** … ~~self declaration~~ **self-declaration**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/Stakeholders` → `National Body Reference Architecture/NB Motivational Layer/Stakeholders`
- **FRAME_Stakeholder** European Commission `{09ACD865-46B3-4ea8-A5A9-5D8F4AF58CF6}` — *title change; substantive description change; metadata change*
  - name: ~~European Commision~~ → **European Commission**
  - **The European Commission may adopt delegated acts under the scope of the European ITS Directive (Directive 2010/40/EU). The Commission may adopt specifications to ensure compatibility, interoperability and continuity of services especially for the priority actions and priority areas defined in the Directive. The Commission shall establish a working program indicating the specifications to be developed and data types to be made available by the Member States. The Commission also receives reports from the Member States on the implementation of the Directive and related delegated acts and provid …
  - package: `National Body Reference Architecture/00 NB Motivational Layer/Stakeholders` → `National Body Reference Architecture/NB Motivational Layer/Stakeholders`
- **FRAME_Stakeholder** Member State `{F67994D2-8F28-40c3-AB94-56CBB3C33B7E}` — *substantive description change; metadata change*
  - **Each Member State has to fulfil the requirement of the ITS Directive and the related Delegated Regulations. Therefore, they have to setup a national body or announce a competent authority (see 1.2.6.1.1). In addition, the Member State has to report status and progress to the European Commission.**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/Stakeholders` → `National Body Reference Architecture/NB Motivational Layer/Stakeholders`
- **FRAME_Stakeholder** National Access Point `{045541C2-0CC6-4ed9-B36B-9A432B2E67EC}` — *title change; substantive description change; metadata change*
  - name: ~~NAP~~ → **National Access Point**
  - **A National Access Point (NAP) is a node in which ITS-related data are concentrated and published in the form of metadata or full datasets. NAPs are set up to facilitate access, and to allow easy exchange and reuse of transport and mobility related data in Europe, in order to help support the provision of EU-wide interoperable travel and traffic services to end users.**
  - package: `National Body Reference Architecture/00 NB Motivational Layer/Stakeholders` → `National Body Reference Architecture/NB Motivational Layer/Stakeholders`
- **FRAME_Stakeholder** National Body `{FA078449-0B55-43fd-85F0-BC2273EB6B8F}` — *title change; substantive description change; metadata change*
  - name: ~~Competent Authority / National Body~~ → **National Body**
  - **A stakeholder established by the government or appointed by authorities. Their task is to oversee, manage, regulate or represent various aspects of national affairs. They have to be impartial and independent. According to Delegated Regulation (EU) No 886/2013 and (EU) No 885/2013 a National Body has to be appointed. According to Delegated Regulation (EU) 2015/962 and (EU) 2017/1926 Competent Authorities of the Member States shall carry out the compliance assessment. In this reference architecture the term "National Body" is used to refer to both "national body" and "competent authority" used …
  - package: `National Body Reference Architecture/00 NB Motivational Layer/Stakeholders` → `National Body Reference Architecture/NB Motivational Layer/Stakeholders`

## National Body Reference Architecture / NB Organisational View

### National Body Reference Architecture/NB Organisational View
- diagram **03 NB Organisational View** — elements added: Compliance Assessment, Delegated Regulation, European Commission, Self-declaration, Template for compliance assessment, Template for self-declaration; elements removed: Compliance Assement, Delegated Reguation, European Commision, Self Declaration, Template for Self Declaration, Template for compliance Assessment
- **Package** Agreements `{7548A7CA-47C0-40e6-8EA8-DE18501B7B12}` — *metadata change*
  - package: `National Body Reference Architecture/03 NB Organisational View` → `National Body Reference Architecture/NB Organisational View`
- **Package** Roles `{D756E993-3CF4-49fd-BBF5-E6670E55F179}` — *metadata change*
  - package: `National Body Reference Architecture/03 NB Organisational View` → `National Body Reference Architecture/NB Organisational View`

### National Body Reference Architecture/NB Organisational View/Agreements
- **FRAME_Agreement** Compliance Assessment `{741A6BF3-3785-4285-B769-6E5BA4860A45}` — *title change; substantive description change; metadata change*
  - name: ~~Compliance Assement~~ → **Compliance Assessment**
  - **The element Compliance Assessment represents the results of the compliance assessment carried out by the national body for a stakeholder according to the delegated regulations enacted under the ITS Directive 2010/40/EU. The compliance assessment covers one data set or service publication. Self Declaration Version 1.0 Phase 1.0 Proposed**
  - package: `National Body Reference Architecture/03 NB Organisational View` → `National Body Reference Architecture/NB Organisational View/Agreements`
- **FRAME_Agreement** Delegated Regulation `{18BED502-4259-4737-9DD1-6B52EBF5BA0F}` — *title change; editorial description change; metadata change*
  - name: ~~Delegated Reguation~~ → **Delegated Regulation**
  - ~~is available~~ … ~~version on the EUR-Lex website.~~ **version.**
  - package: `National Body Reference Architecture/03 NB Organisational View/Agreements` → `National Body Reference Architecture/NB Organisational View/Agreements`
- **FRAME_Agreement** National Law or Contract MS - NAP `{9A594D51-2CA2-4048-B043-981F4DF70F2D}` — *substantive description change; metadata change*
  - **Parties: Member State and Content Provider. Objective: To identify Content Providers and set up obligations of the Content Provider s. Form: National law implementing the ITS Directive and direct execution of EU Regulations and Delegated Acts. Obligations: - Member State to Content Provider: --- - Content Provider to Member State: - To ensure that data is provided in a correct format to the content consumers under fair, reasonable and non-discriminatory (FRAND) conditions. - To publish relevant information about data/services (e.g., metadata) and information on the data quality at the NAP. - …
  - package: `National Body Reference Architecture/03 NB Organisational View/Agreements` → `National Body Reference Architecture/NB Organisational View/Agreements`
- **FRAME_Agreement** National Law or Contract MS - NB `{0BDE8A5E-CC0E-4fa9-89DD-1DCD42A5AA0B}` — *substantive description change; metadata change*
  - **Parties:** … ~~shall designate an impartial~~ **(MS)** … ~~independent NB/CA~~ **National Body. Objective: Setting up the framework** … **responsibilities of the National Body operation. From: National law implementing the ITS Directive and direct execution of EU Regulations and Delegated Acts or a contract for nonessential parts of the National Body Obligations: - Member State to National Body:- - National Body to Member State: - To identify relevant stakeholders (content provider) that are obliged to** … ~~sure that this NB/CA is properly authorised, according~~ **data accessible via NAP.  …
  - package: `National Body Reference Architecture/03 NB Organisational View/Agreements` → `National Body Reference Architecture/NB Organisational View/Agreements`
- **FRAME_Agreement** Self-declaration `{EB8F2E83-0D00-458a-8C55-0EB4EC40B71C}` — *title change; substantive description change; metadata change*
  - name: ~~Self Declaration~~ → **Self-declaration**
  - **The self-declaration (SD) is the declaration of compliance with a Delegated Regulation of a stakeholder which is affected by one of the Delegated Regulations of the ITS Directive 2010/40/EU. The SD forms are based on the harmonization activities within NAPCORE.**
  - package: `National Body Reference Architecture/03 NB Organisational View/Agreements` → `National Body Reference Architecture/NB Organisational View/Agreements`

### National Body Reference Architecture/NB Organisational View/Roles
- **FRAME_Role** Data or Service Provider `{2EE5FD1F-AC4F-40b2-9C2B-52A2CE6A979C}` — *substantive description change; metadata change*
  - **Actor "Data or service provider" refers to any stakeholder who has an ITS service or a data publication covered by any of the delegated acts enacted under the European ITS Directive and therefore has an obligation to submit a self-declaration.**
  - package: `National Body Reference Architecture/03 NB Organisational View/Roles` → `National Body Reference Architecture/NB Organisational View/Roles`
- **FRAME_Role** European Commission `{1EC60CD8-B204-450d-9238-47BEC17A4785}` — *title change; substantive description change; metadata change*
  - name: ~~European Commision~~ → **European Commission**
  - **The European Commission may adopt delegated acts under the scope of the European ITS Directive (Directive 2010/40/EU). The Commission may adopt specifications to ensure compatibility, interoperability and continuity of services, especially for the priority actions and priority areas defined in the directive. The Commission shall establish a working program indicating the specifications to be developed and data types to be made available by Member States. The Commission also receives reports from Member States on the implementation of the Directive and related delegated acts and provides temp …
  - package: `National Body Reference Architecture/03 NB Organisational View/Roles` → `National Body Reference Architecture/NB Organisational View/Roles`
- **FRAME_Role** General Public `{BBDE56DE-DE8B-4a1d-AC6F-9E35202ED36D}` — *new object*
- **FRAME_Role** Member State `{06C05CA6-B06C-4ca9-AE2B-B93C77D2BECA}` — *metadata change*
  - package: `National Body Reference Architecture/03 NB Organisational View/Roles` → `National Body Reference Architecture/NB Organisational View/Roles`
- **FRAME_Role** National Access Point `{98435A5F-0A74-4cea-BA8E-AE02988208EE}` — *metadata change*
  - package: `National Body Reference Architecture/03 NB Organisational View/Roles` → `National Body Reference Architecture/NB Organisational View/Roles`
- **FRAME_Role** National Body / Competent Authority `{DB0FFB19-1B79-4dbd-9F2B-5B224D345C66}` — *substantive description change; metadata change*
  - ~~Todo: check From 2013/886~~ **According to the delegated regulations enacted under the ITS Directive 2010/40/EU** … ~~From 2017/1926 Member States shall designate an impartial and independent national body competent to assess whether the requirements set out in Articles 3 to 8 are fulfilled by public and private road operators and service providers and broadcasters dedicated to traffic information. Two or more Member States may designate a common body competent to assess compliance with these requirements on their territories. Member States shall notify the national bodies to the Commission. …
  - package: `National Body Reference Architecture/03 NB Organisational View/Roles` → `National Body Reference Architecture/NB Organisational View/Roles`
- connection removed: National Body / Competent Authority → Template for compliance Assessment (Usage)

## National Body Reference Architecture / Supplements

### National Body Reference Architecture/Supplements
- **model document** Change History `{E1490E31-8101-47d1-9D77-AF97D60AFFAD}` — *new object*
- **Artifact** Issues Tracking and Wiki `{5615A50E-7D95-4b83-A0CB-74A7443E4075}` — *new object*
- **GlossaryEntry** NB Glossary `{0396DED8-928E-450d-BC2B-16B42FC84087}` — *new object*
- diagram **Self Declaration State Diagram** — elements added: Accepted and stored self-declaration, Self-declaration is within Non-Compliance process, Self-declaration valid and stored, Self-declaration within comliance assement process, Submitted Draft self-declaration; elements removed: Accepted and stored SelfDeclaration, Self Declaration is within Non-Compliance process, Self Declaration valid and stored, Self Declaration within comliance assement process, Submitted Draft Self Declaration
- **Package** Specifications `{57522110-54AA-43d6-8F37-AD43F6D68D72}` — *metadata change*
  - package: `National Body Reference Architecture/03 NB Organisational View` → `National Body Reference Architecture/Supplements`

### National Body Reference Architecture/Supplements/SD States
- **FRAME_ITS_Business_Process** Accepted and stored self-declaration `{F6AD5280-746D-47a2-97EB-132D8A0FF4AC}` — *title change*
  - name: ~~Accepted and stored SelfDeclaration~~ → **Accepted and stored self-declaration**
- **FRAME_ITS_Business_Process** Self-declaration is within Non-Compliance process `{A8B262D2-DDDB-4234-8D31-2B6803F4AF68}` — *title change*
  - name: ~~Self Declaration is within Non-Compliance process~~ → **Self-declaration is within Non-Compliance process**
- **FRAME_ITS_Business_Process** Self-declaration valid and stored `{A354892E-9CB6-4ae0-A468-51CDD570B10F}` — *title change*
  - name: ~~Self Declaration valid and stored~~ → **Self-declaration valid and stored**
- **FRAME_ITS_Business_Process** Self-declaration within comliance assement process `{ED0BE400-2DC9-4b70-9244-686D28656E99}` — *title change*
  - name: ~~Self Declaration within comliance assement process~~ → **Self-declaration within comliance assement process**
- **FRAME_ITS_Business_Process** Submitted Draft self-declaration `{A873CB1D-4170-4716-91F1-41D6366B835C}` — *title change*
  - name: ~~Submitted Draft Self Declaration~~ → **Submitted Draft self-declaration**

### National Body Reference Architecture/Supplements/Specifications
- **FRAME_Specification** Accompanying Documents `{E658AAFB-2923-41e3-BFA8-0B79A2B57C3D}` — *title change; substantive description change; metadata change*
  - name: ~~Acompanying Documents~~ → **Accompanying Documents**
  - **Accompanying documentation shall be provided by the data/service provider that provides (meta)data in accordance with the respective Delegated Regulations on the NAP. The information in the accompanying documentation shall support the National Body in carrying out the compliance assessment. If existing organisational documents provide answers or information to requested topics, they shall be added to the annex of the accompanying documentation. Per Delegated Regulation one template for the accompanying documentation was prepared within NAPCORE. The templates are linked in the table below. Th …
  - package: `National Body Reference Architecture/03 NB Organisational View/Specifications` → `National Body Reference Architecture/Supplements/Specifications`
- **FRAME_Specification** Directive (EU) 2023/2661 `{C3C38386-12EB-44c2-8976-75E3D86C7AD2}` — *metadata change*
  - package: `National Body Reference Architecture/03 NB Organisational View/Specifications` → `National Body Reference Architecture/Supplements/Specifications`
- **FRAME_Specification** Guidline and Timelines `{80021436-2426-48b8-924C-F76DC5D338BC}` — *substantive description change; metadata change*
  - **The timings and other guidelines will be found in the planed handbook published by NAPCORE X. This includes:** … **a** … ~~Timelines~~ **timelines** … ~~validity for~~ … ~~self declaration~~ **self-declaration** … ~~for validity~~
  - package: `National Body Reference Architecture/03 NB Organisational View/Specifications` → `National Body Reference Architecture/Supplements/Specifications`
- **FRAME_Specification** ITS directive 2010/EU/40 `{838FF400-30C2-465b-A815-907FD87D213B}` — *metadata change*
  - package: `National Body Reference Architecture/03 NB Organisational View/Specifications` → `National Body Reference Architecture/Supplements/Specifications`
- **FRAME_Specification** Template for EU reporting `{931FCB16-30EE-46d1-A710-1551EE357C47}` — *substantive description change; metadata change*
  - **Harmonised forms for EU reporting are available at: https://napcore.eu/material-hub/ The latest version of the EU reporting template could be found here: https://napcore.eu/national-bodies-3/**
  - package: `National Body Reference Architecture/03 NB Organisational View/Specifications` → `National Body Reference Architecture/Supplements/Specifications`
- **FRAME_Specification** Template for compliance assessment `{44D1CCEA-5154-46a4-804A-E19E0A79FC2B}` — *title change; substantive description change; metadata change*
  - name: ~~Template for compliance Assessment~~ → **Template for compliance assessment**
  - ~~NAPCORE developed a harmonized Accompanaying~~ **Harmonised forms for provision of accompanying** … ~~form witch can~~ **are available at: https://napcore.eu/material-hub/ The latest version of the accompanying document forms could** … ~~https://napcore.eu/material-hub/~~ **https://napcore.eu/national-bodies-3/**
  - package: `National Body Reference Architecture/03 NB Organisational View/Specifications` → `National Body Reference Architecture/Supplements/Specifications`
- connection added: Template for compliance assessment → Compliance Assessment (Association)
- **FRAME_Specification** Template for national reporting `{82FF01BC-5818-40e7-A1AC-5BA1B47FA5DF}` — *substantive description change; metadata change*
  - ~~https://rupprechtconsultde.sharepoint.com/:w:/r/sites/NAPCOREallpartners/Shared%20Documents/WG5/WG%205.2%20-%20Forms%20%26%20CA%20Processes/WG5.2_Reporting%20process%20and%20templates/NAPCORE_WG5_Reporting%20templates%20to%20MS%26EC_v1.docx?d=w1fd077eb74c246a08034482843931cf6&csf=1&web=1&e=P9Y3fI Need to~~ **Harmonised forms for national reporting are available at: https://napcore.eu/material-hub/ The latest version of the national reporting template could** … ~~approved und published by WG5~~ **found here: https://napcore.eu/national-bodies-3/**
  - package: `National Body Reference Architecture/03 NB Organisational View/Specifications` → `National Body Reference Architecture/Supplements/Specifications`
- **FRAME_Specification** Template for self-declaration `{7D17E92C-40B9-4747-8B9D-5D52B942D18F}` — *title change; substantive description change; metadata change*
  - name: ~~Template for Self Declaration~~ → **Template for self-declaration**
  - ~~Self Declaration~~ **self-declaration** … ~~witch~~ **which**
  - package: `National Body Reference Architecture/03 NB Organisational View/Specifications` → `National Body Reference Architecture/Supplements/Specifications`
