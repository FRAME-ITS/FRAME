# NB Reference Architecture – Functional View: changes after the review of R. Bossom

For: Benjamin Witsch (NB RA maintainer) · Prepared by: Petr Bureš · 7 Nov 2026
Branch `fix/nb-ra-review`, commit dce0890 (script `tools/fixes/2026-11-07_nb_ra_functional_view.py`, log `reports/fix_2026-11-07_nb_ra_functional_view.md`).
References in square brackets are Richard's comment numbers (review of 09/2026).

All changes are in the diagram **02 National Body Functional View** and in the packages *LL DataFlows* and *LL Functions*.
No element was added or deleted. One connector changed direction (section 3).

## 1. IN/OUT labels hidden in the diagram [F1, F2, F8, F10]

**Change:** The connector labels are hidden in this diagram. The arrows still show the direction. The «IN» and «OUT» stereotypes stay in the model.

**Why:** Richard found the labels confusing. In the element pages of the web export, «IN»/«OUT» seem to contradict the "To/From" columns.
The labels add nothing to the diagram, because a data flow is drawn as a box between two arrows. FRAME 5.3 keeps the convention
producer → «IN» → data flow → «OUT» → consumer, so the model stays consistent with the FRAME Repository.

## 2. Data flows renamed

### 2.1 Requested by Richard [F3] – four flows

There were two flows called *Request* and two called *Response*, with different content. Each is now named after what it carries.

| Old name | From → To | New name |
|---|---|---|
| Request | Handling Non-Compliance → Managing general requests regarding self-declaration | Request for self-declaration information |
| Response | Managing general requests regarding self-declaration → Handling Non-Compliance | Self-declaration information for non-compliance |
| Request | Handling Non-Compliance → Compliance Assessment | Request for compliance assessment |
| Response | Compliance Assessment → Handling Non-Compliance | Compliance assessment result for non-compliance |

### 2.2 Proposed in addition – eight flows (please confirm or reject)

These flows run **from** a data store **to** a function, so they carry data out of the store.
Their names, however, describe a request or a storing action, which reads as the opposite direction. Each is renamed after the data it delivers.
Richard did not ask for these changes. If you prefer the old names, the script reverts them by removing the lines from its list.

| Old name | From → To | New name | Reason |
|---|---|---|---|
| Request data | Stakeholder List → Manage Stakeholder List | Stakeholder data | delivers stakeholder data, it is not a request |
| Request information | Stakeholder List → Validation of completeness | Stakeholder contact details | the function validates contact details |
| Request self-declaration | Self-declaration Storage → Compliance Assessment | Self-declaration for compliance assessment | delivers the stored self-declaration |
| Provide self-declaration | Self-declaration Storage → Reporting of self-declaration and compliance assessment results | Self-declarations for reporting | named after the content, not the action |
| Provide status of SD | Self-declaration Journal → Reporting of self-declaration and compliance assessment results | Self-declaration status for reporting | named after the content, not the action |
| Status request on SD | Self-declaration Journal → Handling Non-Compliance | Self-declaration status for non-compliance | delivers the status, it is not a request |
| Store CA result | Compliance assessment registry → Handling Non-Compliance | Compliance assessment result | data read from the registry; *Store CA result* also remains the name of the flow Compliance Assessment → registry |
| Status of CA | Compliance assessment registry → Compliance Assessment | Previous compliance assessment results | see section 3; *Status of CA* also remains the name of the flow Compliance Assessment → Data- and/or Service provider(s) |

The new names also write *compliance assessment* in full, because the NB glossary defines **CA** as *Competent Authority*.
The remaining flows *Status of CA* and *Store CA result* still use the abbreviation. This is one of the open questions for the maintainers (question 9).

## 3. Direction of *Status of CA* corrected (registry → Compliance Assessment)

**Before:** The flow had two «OUT» connectors (to *Compliance Assessment* and to *Compliance assessment registry*) and no «IN». It had no producer, which is an error in a data-flow model.

**After:** The registry produces the flow («IN» from the registry), and *Compliance Assessment* consumes it.
Compliance Assessment already writes its results to the registry through the flow *Store CA result*.
The only reading that fits is that it also reads previous results from the registry. Hence the new name *Previous compliance assessment results*.
Please confirm that this is the intended meaning.

## 4. Source and target in every data-flow description [F11, F12]

**Change:** Each of the 50 data-flow descriptions now starts with two lines taken from the connectors, for example:

    From: Compliance assessment registry
    To: Compliance Assessment

Any existing description follows after an empty line. Most flows had no description before.

**Why:** Richard noted that the flow descriptions miss the content, the source and the target, and that a flow looks different depending on where it is opened.
Source and target can be stated reliably from the model, so they are now in the text. The **content** of each flow still has to be written by the NB RA authors.

## 5. Inputs and outputs in every function description [F6, F9 – first step]

**Change:** The descriptions of the 9 functions in the diagram end with their inputs and outputs, taken from the connectors, for example (*Receive self-declaration*):

    Inputs: Provides self-declaration form; Validation results
    Outputs: Information about status; SD details

**Why:** Richard found that the function descriptions mainly quote the legislation, so software cannot be specified from them.
Listing the inputs and outputs is the part that can be derived from the model. The descriptions themselves need rewriting in the FRAME form (Overview and Functional Requirements, User Guide section 6.2), and that is a task for the authors (question 10).

## 6. Not changed – open questions for the maintainers

Listed in `_inbox/20261107_NB_RA_review.md`, group D:
- Compliance Assessment as process or function [F4, F5, F7, C2, C5]
- "Provide NB support" is a High-Level Function placed among the low-level functions
- the ambiguous abbreviation "CA"
- rewriting the function descriptions

Layout items (wrapping long flow names [F1], tidying the area around the Compliance assessment registry [F2]) are left for editing in EA.
