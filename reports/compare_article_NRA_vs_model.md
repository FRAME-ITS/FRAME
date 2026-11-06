# Article "Leveraging FRAME Methodology for EU-Wide Harmonization of National Access Points" (v93, 2025) vs. model, Meta Model and MDG V1.3

Bureš, Witsch, Bělinová – Transactions on Transport Sciences. Compared on 2026-11-06 with `model/FRAME.qea`
(fix/model-conventions, technology V1.3). The article's Fig. 1–4 show the building blocks of each view and their links;
each arrow was looked up in the V1.3 Quick Linker rules and in the FRAME Meta Model diagram.

Legend: ✓ rule in the same direction · ↔ rule only in the opposite direction · ✗ no rule.

## Fig. 1 – Motivational Layer

| Article arrow | MDG V1.3 | Meta Model |
|---|---|---|
| Domain → ITS Service | ↔ ITS Service «has» ITS Domain | ↔ same |
| ITS Service → Requirements | ✓ «defines» | ✓ |
| ITS Service → Added Values | ✓ «delivered by» | ✗ **missing** |
| Added Values → Stakeholder | ✓ «delivers value to» | ✓ |
| Stakeholder → Business Expectations | ✓ «has» | ✓ |
| **Business Expectations → ITS Service** | ✗ **missing** (only Business Expectation «defines» Mission Statement / Requirement) | ✗ (has «defines» Mission Statement) |
| Stakeholder → Vision | ✓ «defines» | ✓ |
| Vision → Mission | ✓ «associate» | ✓ |
| Mission → ITS Service | ✓ «defines» | ✓ |
| ITS Service → User Needs | ✓ «defines» | ✓ |
| Actor → Stakeholder | ✓ «is Type of» | ✓ |

Section 6 of the article names the missing interactions *expectations – services, services – added values, stakeholders*.
After today's changes services – added values and added values – stakeholders exist in the MDG; **expectations → services is still missing**,
and the Meta Model lacks ITS Service → Added Value.

## Fig. 2 – Functional View
Terminator → functional data flow → Function → data flow → Function / Datastore → data flow → Terminator: all ✓ (IN for producer → flow,
OUT for flow → consumer), in the MDG and the Meta Model.

## Fig. 4 – Physical and Communications View

| Article arrow | MDG V1.3 | Meta Model |
|---|---|---|
| Terminator → Physical data flow | ✓ «use» | ✗ **missing** |
| Physical data flow → Subsystem | ↔ Component «use» Physical Data Flow | ↔ |
| Subsystem → Physical data flow | ✓ «use» | ✓ |
| Physical data flow → Module | ↔ Application «contains» Physical Data Flow | ↔ |
| Subsystem → Module | ↔ Application «hosted by» Component | ↔ |
| Physical data flow ⇢ Interface | ✓ «use» | ✓ |
| Interface → Requirement | ✓ «defines» (also Requirement «fulfilled by» Interface) | ↔ only Requirement «fulfilled by» Interface |
| Specification → Requirement | ✓ «defines» | ✓ |

Terminology: the article (and D4.2) speak of **Subsystem** and **Module**; the MDG has FRAME_Component and FRAME_Application
(plus FRAME_System, unused in the NAP RA). The NAP RA uses Component for the two NAP types and Application for the modules.

## Fig. 3 – Organisational View

| Article arrow | MDG V1.3 | Meta Model |
|---|---|---|
| **Actor → Role** | ↔ Role «defines» Actor | ↔ |
| Role → Agreement | ✓ «accepted by» (also Agreement «adheres to» Role) | ✓ |
| Role → Subsystem | ↔ Component «owned by» Role (and Role «associate» Component) | ↔ |
| **Role → Module** | ✗ **missing** | ✗ |

Note: on 2026-11-06 the RA links Actor → Role (SSTP 5, C-ITS 2) were reversed to Role «defines» Actor, following the MDG.
The article draws the opposite direction ("actors performing roles").

## Attributes described in the article but not available as tagged values
- ITS Domain: Transport Network, ITS Service, ITS Service Type, Level of Detail, Perspective, Focus (also D4.2 Table 4).
- Actor: "Represented by".
- Role: tasks and responsibilities (Role has *Key Issue, Role Value, Role View, Role Part Of Value Chain*).
- Agreement: parties, objective, form, obligations of each party, referenced law and citations.
- Interface: types of data, physical mode of transfer, security requirements, capacity (communications view).
- Safety and Security View: no stereotypes in the MDG (only Datastore *DataStore_SecurityLevel*).
In the NAP RA these are written into the element notes.

## NAP RA content vs. the article
| Article | Model (NAP Reference Architecture) |
|---|---|
| 6 stakeholders, 6 business expectations | 7 stakeholders (incl. "NAP"), 6 business expectations |
| 19 added values | 24 ITS Service Added Values |
| 6 actors | 8 actors – *Content Consumer* and *NAP Content Consumer*, *Content Provider* and *NAP Content Provider* look like duplicates |
| 7 roles | 7 roles ✓ (typo *European Commision (EC)*) |
| metadata directory: 1 subsystem, 4 modules; data platform + Data Management | 2 components (Metadata Directory NAP, Data Platform NAP), 6 applications (incl. *Data Quality Checks Application*) |
| 6 interfaces for the metadata directory | 12 interfaces in total (typo *…metadata vie machine to machine…*) |
| standards linked to interfaces | 26 specifications, incl. placeholders *FRAME_Specification1*, *Specification tbd* |

## Proposed decisions
1. Add **Business Expectation «defines» ITS Service** to the MDG and the Meta Model (the gap named in the article).
2. Meta Model: add ITS Service «delivered by» Added Value, Terminator «use» Physical Data Flow, Interface «defines» Requirement.
3. **Actor – Role direction**: keep Role «defines» Actor (MDG, Meta Model, now also the RAs) and adjust the article figure, or
   introduce Actor «performs» Role and reverse the links.
4. Add **Application «owned by» Role** (Role → Module in the article).
5. Display names: alias *Sub-system* for FRAME_Component and *Module* for FRAME_Application in the toolbox, so tool and documentation use the same words.
6. Decide which attributes (list above, together with D4.2) the toolbox should carry as tagged values – input for W07 (definitions and vocabulary).
7. NAP RA clean-up: duplicate actors, stakeholder "NAP", typos, placeholder specifications.
