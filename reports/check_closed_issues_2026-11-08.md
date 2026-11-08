# FRAME-ITS/FRAME – issues closed before 11/2026: were they really resolved?

Checked 8 Nov 2026 against the released model V5.2 (`v5.2.0`) and the current model (PR #95 + branch `fix/nb-ra-review`),
the MDG technology V1.3, the User Guide draft and the website. 59 closed issues (2020-12 … 2026-04).

## Summary

| Verdict | Issues |
|---|---|
| Resolved in the model / tool (already in V5.2) | #3, #6, #7, #8, #9, #10, #11, #17, #18, #19, #20, #22, #24, #33, #53, #63, #65, #66, #73 |
| Resolved only now by PR #95 (V5.2 still had the problem) | #31 Test Package, #32/#70 old FrameNext stereotypes, #16 hierarchy direction – **partly**, see below |
| Partly resolved or open – follow-up needed | #16, #14, #60/#61, #30, #68, #37 |
| Decided without a model change (discussion closed, decision recorded) | #13, #15, #21, #26, #48, #51, #52, #47, #23 |
| Closed without a recorded outcome (cannot be verified) | #27 Communications View elements, #28 Data model diagram |
| Closed as obsolete in 03/2026 (no change; topic superseded) | #12, #34, #35, #38, #39, #40, #41, #42, #43, #44, #45, #46, #49, #50, #74, #77 |
| Not about the model (repository, website, process) | #1, #5, #75 |

## Findings that need action

1. **#16 – user-need hierarchy still reversed in 42 links.** In the FRAME Repository 42 «belongs to» links still run
   User Need Topic → User Need or User Need Group → User Need Service (V5.2: 45). They are the user needs of group 9
   (9.10.1, 9.11.1–9.11.3, "9 Freight") and of "1 General"/1.1. The function hierarchy is correct after PR #95.
   `tools/check.py` does not test the direction of «belongs to», so the check reported no error.
   → *Proposal:* reverse the 42 links (no duplicates exist) and add the rule to `check.py`; can go into PR #95.
2. **#32 / #70 – one element keeps an old FrameNext stereotype:** "PSAP - eCall Mamagement Application"
   (`FrameNext::HighLevelFunction`, also a typo in the name). Everything else was moved to FRAME_Profile in PR #95.
   → *Proposal:* give it the FRAME stereotype it should have (Application?) and fix the name.
3. **#60 / #61 – User Needs search.** The FRAME Repository landing page has the link "FRAME User Needs Search"
   (`$search://Name=FRAME User Needs`), but no search definition is stored in the model or in the MDG technology.
   EA keeps user-defined searches on the computer of the person who created them, so the link most likely does
   nothing for other users. → *Proposal:* verify in EA; if confirmed, add the search to the MDG technology V1.3 (ModelSearches).
4. **#14 – Stakeholder links.** Decided: Terminator, Organisation and Actor are instances of Stakeholder. The model has only
   Actor «is Type of» Stakeholder (28 links); there is no rule or link for Terminator or Organisation.
   → *Proposal:* confirm whether the 2021 decision still holds (the NRA article uses Actor → Stakeholder only); otherwise close as superseded.
5. **#68 – sub-terminators.** Closed as obsolete, but the Meta Model shows Terminator «is Type of» Sub-terminator,
   while the FRAME Repository uses «component of» (70 links) and one «Instantiate» (Parking Operator → NAP Content Provider).
   → *Proposal:* align the Meta Model with the repository («component of», as in MDG V1.3) and retype the one «Instantiate».
6. **#30 – Tool Setup in the published tool.** The question was not answered; V5.2 and 5.3 contain the packages
   *FRAME Toolsetup* and *FRAME Functionalities* at top level. → *Proposal:* decide for 5.3 – keep (documented as
   maintainers' packages in the User Guide) or move under one "Maintenance" package.
7. **#37 – eCall mission statements.** The issue proposed two mission statements; the eCall Reference Architecture
   has none (the content is modelled as ITS Service Added Value). The issue was closed without a decision.
   → *Proposal:* accept as is (note in the issue) or add the two mission statements.

## Notes on single issues

| Issue | Closed | What was asked | State in the model |
|---|---|---|---|
| #8 | 2020-12 | User Need stereotypes based on Requirement | yes – FRAME_User_Need applies to Requirement |
| #10 | 2020-12 | delete the old meta model | yes – only FRAME Meta Model / FRAME_Metamodel |
| #11 | 2021-01 | stereotype for the transport network | yes – FRAME_ITS_Domain (ArchiMate Location) |
| #14 | 2021-02 | Stakeholder stereotype and instance links | stereotype yes; links only for Actor (finding 4) |
| #16 | 2021-03 | hierarchy part → whole | functions yes (PR #95); user needs 42 links reversed (finding 1) |
| #17/#18/#19 | 2021-02/03 | navigation cells FRAME User Needs / Functional View / Create Your Own Architecture | yes |
| #20/#7/#65 | 2021 | data-flow stereotypes: one, later high/low level | yes – FRAME_High_Level_Data_Flow / FRAME_Low_Level_Data_Flow |
| #21 | 2021-03 | template = structure of the reference architectures | yes – 00–05 + Supplements (+ 06 Security View) |
| #24 | 2021-03 | F/D prefixes for functions and data stores | yes |
| #31 | 2021-04 | Test Package in the published tool | was still in V5.2; removed in PR #95 |
| #32/#70 | 2021/2026 | old FrameNext toolbox and connectors | V5.2: 3 618 FrameNext references; PR #95: all on FRAME_Profile except one element (finding 2) |
| #33 | 2021-04 | C-ITS and Truck Parking landing pages | yes – both exist |
| #53 | 2021-05 | standards in subset architectures | yes – Specification artefact |
| #60/#61 | 2021 | User Needs search template | link exists, definition not in the model (finding 3) |
| #63 | 2021-09 | functions linked directly to data stores | yes – no such link left |
| #66/#73 | 2021 | high/low level data flows mixed up | yes; PR #95 check: 0 errors |
| #75 | 2026-03 | downloads and "read me" on the website | new website: FRAME Tool page, release history, guides with each release (#94 still open) |
| #6 | 2026-04 | broken diagrams after XMI import | resolved by the redesign of the data flows; Installation Guide 3.0 adds the troubleshooting hint |
