# FRAME NEXT documentation vs. the FRAME model (5.3-dev, fix/model-conventions)

Compared on 2026-11-06:
- **D4.5 FRAME Architecture Theory of Operations (2021)**, Parts 1–13 (Word; Part 2 from the PDF because its Word file is damaged);
- **D4.2 FRAME Architecture artefacts (2019)**;
- the model `model/FRAME.qea` (FRAME Repository, technology V1.3).

## 1. D4.5 – functional view

| Item | D4.5 (2021) | Model | Result |
|---|---|---|---|
| Functions (HL + LL) with number and name | 367 | 363 (FRAME Repository) | 4 sets of differences, below |
| LL function Overview Description | 308 compared | | 298 identical, 5 minor edits, 5 rewritten (all NAP F3.6.x) |
| LL function Functional Requirements | 308 compared | | 295 identical, 9 minor edits, 3 stored under a misspelt type, 1 item missing |
| Data stores | 42 | 58 numbered | numbering identical; 2 names differ; D3.15 and D3.17 appear twice in the model |
| User Needs (Part 12) | groups 1–10 | groups 1–11 | texts identical; numbering error in group 1, 3 typos in topic names |
| Terminators (Part 2, App. 1) | 81 mnemonics | 89 | 1 name difference, mnemonics (aliases) missing for most terminators in the model |

### 1.1 Functions

**In D4.5, not in the model (numbering)**
- F3.1.5.8 *Rest Area Booking Management*, F3.1.5.9 *Provide Rest Area Fleet Operator Interface* – the model has F3.1.5.10 *Manage Rest Area Usage* and F3.1.5.11 *Manage Rest Area Booking* instead (renumbered/renamed after 2021, D4.5 not updated).

**In the model, not in D4.5 (added after 2021)**
- F3.6.6 – F3.6.10 (NAP functions).

**Naming errors in the model**
- 8 low-level functions of F3.4 are named without the `F` prefix: `3.4.1 Monitor Weather Conditions`, 3.4.2, 3.4.3, 3.4.4, 3.4.7, 3.4.8, 3.4.10, 3.4.11 (all other functions are `F<number> <name>`).
- F3.1.2.14 *Implement Inter-urban **Management Traffic** Strategy* – D4.5: *Implement Inter-urban Traffic Management Strategy*.

**Other name differences (model is the newer source, D4.5 to be updated)**

| Function | D4.5 | Model |
|---|---|---|
| F2.1.11.2 | Manage Store of PSAP Data | Manage PSAP Data Stores |
| F2.2 | Manage Stolen Vehicle Reporting | Manage Stolen Vehicle Notification |
| F3.6.1 | Manage NAP Meta-Data Repository | Manage NAP Metadata Repository |
| F3.6.2 | Manage Content Provider Registrations | Manage Registrations and Provide Authorisation Service |
| F3.6.3 | Provide Interface for Content Providers | Manage Content Providers Metadata |
| F3.6.4 | Provide Access for NAP Meta-Data Retrieval | Manage Metadata Retrieval |
| F5.14 | … Trip Planning and Implementation | … Trip Planning & Implementation |
| F5.15 | Provide In-vehicle Detection | Provide In-vehicle Detection and Analysis |
| F5.15.1 | Provide Detection for Vehicle Surroundings | Provide Detection for the Vehicle Surroundings |
| F8.6 | Implement and Monitor FTEP | Provide Freight Transport Service |
| F9.3 | *Mange* Vehicle Access to Sensitive Areas (typo in D4.5) | Manage Vehicle Access to Sensitive Areas |
| F5.14.12.1–3 | names empty in D4.5 headings | Check for Rest Area Requirement, Find Suitable Rest Areas, Book Suitable Rest Areas Places |

D4.5 heading formatting is inconsistent in places (`“F1.1.2 …”`, `F”4.4.7 …”`, `F 6.3.13`) – relevant only when D4.5 is regenerated.

### 1.2 Descriptions of low-level functions

- **NAP F3.6.1 – F3.6.5**: Overview Descriptions in the model are 2–4× longer than in D4.5 (extended for NAP after 2021); Functional Requirements are identical.
- **Functional Requirements stored under a misspelt requirement type** (the text is there, but tools that read type *Functional* miss it):
  F3.1.5.1 (`Functionality`), F5.14.12.1 (`Function`), F8.4.2 (`Fuctional`); all others use `Functional`.
- **F1.3.7**: the model lacks requirement (e) of D4.5 – *“in case of a payment made from a Freight Vehicle, send a receipt to functionality in the Manage Freight and Fleet Operations Functional Area”*.
- Minor edits (one sentence or a few words): F2.1.10, F2.1.11.3, F3.1.1.5.23, F3.1.2.14.3, F5.11.8, F5.14.13 (+52 words), F5.14.16, F7.3.6, F7.6, F8.4.1, F8.5.3 (+26/+35 words), F8.6.4.
- 45 low-level functions of the reference architectures (C-ITS 31, NB 9, NAP 5) have no Functional Requirements – they are not in D4.5.

### 1.3 Data stores
- D3.15: D4.5 *NAP Meta-Data* – model *NAP Metadata*.
- D3.17: D4.5 *NAP Data Providers* – model *NAP Users*.
- D3.15 and D3.17 exist twice in the model (FRAME Repository and NAP RA) – check whether the RA should reuse the repository element.

### 1.4 User Needs (Part 12)
- All 4-level User Needs of groups 2–10 and their texts match D4.5 (one difference is only the HTML entity `&lt;` in 4.1.3.4).
- **The duplicate User Need 1.1.4** (the open item from the convention check) is a numbering error: *“Systems that conform to the Framework Architecture shall exchange information in a manner that permits road and traffic conditions to be understood by all parties.”* is **1.2.4** in D4.5. The model has no 1.2.4.
- Model 1.2.8 (*coherent and consistent advice to all drivers affected by an incident or congestion*) is not in D4.5 (added later).
- Topic names: model *Adapability* (1.3), *Constrains* (1.4), *Quality of Data* (1.9) – D4.5 *Adaptability*, *Constraints*, *Quality of Data Content*.
- Group 11 C-ITS exists only in the model (added after 2021).

### 1.5 Terminators (Part 2, Appendix 1)
- All model terminators are described in D4.5 (D4.5 spells *Hunan Machine Interface*); D4.5 also has *Vehicle Renting Agency* (esp.vra), not in the model.
- The model keeps the mnemonic as element alias for only 21 of 89 terminators; D4.5 gives a mnemonic for every terminator (e.g. o.bo, bti.bs, esp.dvip, ors.ems).
- Mnemonics used in data-flow names that D4.5 does not define: `d.evd` (D4.5 `d.e`), `t.c` (D4.5 `t.cy`), `o.ulzo`, `t.ptt` (27 flows), `mms.mms` (20 flows), `esp.tpfsp`, `nap.cp`, `nap.dps`, `nap.drs`, `nap.mdrs` (NAP, after 2021), and two likely typos: `ft.fton` (1 flow, probably `ft.ftom`) and `mmms` (1 flow `tmmms-mffo_outputs`, probably `mms`).

## 2. D4.2 – artefacts vs. the MDG technology V1.3

D4.2 (2019) describes the artefacts the End User should fill in, view by view. The model covers the
functional view fully; most attributes of the other views are not represented as tagged values.

| D4.2 artefact (table) | MDG stereotype | Attributes in D4.2 | Tagged values in V1.3 |
|---|---|---|---|
| Stakeholder (T1) | FRAME_Stakeholder | ID, Name, Contact, Interest (Want/Make/Use/Rule) | none |
| ITS Mission Statement (T2) | FRAME_Mission_Statement | ID, Name, ITS Service ID, Guiding Principle, Explanatory Component | none |
| Stakeholder Aspiration (T3) | – | ID, Stakeholder, Description, related ITS Service | no stereotype (closest: Business Expectation) |
| ITS Domain (T4) | FRAME_ITS_Domain | Service type, Transport network, Level of detail, Perspective, Focus | none |
| ITS Service (T5) | FRAME_ITS_Service | Group, Short description, Field of application, Vision, Qualitative goals, Barriers, Functional/technological aspects | *Field of Application* only |
| Added Value (T6) | FRAME_ITS_Service_Added_Value | Customer, Safety, Efficiency, Environment, Other benefits | *ITS Added Value Type* |
| Aspiration ↔ User Need (T7) | – | link | no relationship |
| Function, Data Store, Data Flow, Terminator (T8–T11) | FA / HL / LL Function, Datastore, LL / HL Data Flow, Terminator | overview, parent, I/O flows, functional requirements, allocated UN | covered (notes, requirements, connectors) |
| Sub-system, Module (T12–T13) | FRAME_System, FRAME_Component, FRAME_Application | Name, Physical location (Roadside / Centre / Vehicle / Personal device), Description, constituent functions and data stores | Component: *LocationDescription*, *Standrdization* (typo) |
| Internal / External Physical Data Flow (T14–T15) | FRAME_Physical_Data_Flow | Source, Target, constituent functional data flows | none; internal/external not distinguished |
| Communications View (T16) | – (Physical Data Flow / Information Object) | Data type, Max bytes/message, Max delay, Message interval, Transfer mode, Max data rate, Max message gap, Relevant standards | none on Physical Data Flow; Information Object has *Size, Source, Structure, Subtype, Type, Validity period* |
| ITS Role (T17) | FRAME_Role | ID, Actor stereotype, Name, View, Key issue, Value | *Key Issue, Role Part Of Value Chain, Role Value, Role View* ✓ |
| Role responsibilities, data, capabilities (T18–T20) | – | Areas of responsibility, Tasks, Required/Generated data, Capability | none |
| ITS Actor (T21) | FRAME_Actor | Stakeholder, Customer, Role | none (linked by «is Type of», «defines») |
| Desired Business Results (T22) | FRAME_Business_Expectation | Vision, Goals, Objectives, Missions, Policies, Tactics, Influencing factors, Benefits | none |
| Architecture Results (T23) | FRAME_Desired_Architecture_Goals | Targets, Vision, Goals, Action options, Action patterns | none |
| Business Process (T24) | FRAME_ITS_Business_Process | 20 attributes (responsible, start/end, purpose, goal, input, output, sub/high-level process, participants, measurement variables, regulations…) | none |
| Information Flow (T25) | – (Information Object?) | Originating / destination organisation, Communication type and frequency, Content | none |
| Safety (T26), Security (T27) | – | System / HMI / Traffic safety; GDPR data, DoS potential, mitigation responsibility | Datastore *DataStore_SecurityLevel* only |

Other D4.2 findings: the functional-area table gives FA6 the mnemonic **psle** (should be **ptja**) and names FA5
*Provide Support for Host Vehicle **Services*** (model and D4.5: *Systems*); its terminator list (2019) is older than D4.5.
MDG tag names with typos: *Standrdization* (Component), *… operationg in parallel …* (Datastore).

## 3. Proposed model corrections (1–5, 7, 8 applied: reports/fix_2026-11-06_doc_alignment.md)

1. Rename the 8 F3.4 low-level functions to `F3.4.x …`.
2. F3.1.2.14 → *Implement Inter-urban Traffic Management Strategy*.
3. Second User Need 1.1.4 → **1.2.4** (as in D4.5).
4. Topic names: *Adaptability*, *Constraints*, *Quality of Data Content*.
5. Requirement type `Functionality` / `Function` / `Fuctional` → `Functional` (F3.1.5.1, F5.14.12.1, F8.4.2).
6. F1.3.7: decide whether requirement (e) (receipt for payments from Freight Vehicles) was removed on purpose.
7. Data-flow prefixes `ft.fton` → `ft.ftom`, `tmmms-…` → `tmms-…` (after checking the flows).
8. Terminator aliases: fill in the mnemonics from D4.5 Part 2 Appendix 1.

## 4. Documentation to update (D4.5 / User Guide)
- F3.1.5.8/9 → F3.1.5.10/11, F3.6.6–F3.6.10, NAP descriptions F3.6.1–5, group 11 C-ITS, User Need 1.2.8, renamed functions and data stores (tables in 1.1 and 1.3).
- Terminator mnemonics added after 2021 (`nap.*`, `o.ulzo`, `t.ptt`, `mms.mms`, `esp.tpfsp`, `d.evd`, `t.c`).
- D4.2 attribute sets for the motivation, organisational, communication and safety & security views are not implemented as tagged values – decide which of them the toolbox should carry (input for the definitions/vocabulary work, W07).
