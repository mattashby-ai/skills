---
name: change-request
description: Drafts a formal Change Request (CR) document using a standard markdown template. Use when the user needs to document a proposed change to a system or service, or provides a ticket ID, change summary, or asks to write a CR.
metadata:
  author: The Instillery
  version: "1.0.0"
requiredFields:
  - "[TicketID]"
  - "[Affected User]"
  - "[DateTime Reported]"
  - "[Change Summary]"
  - "[Reason for Change]"
  - "[Change Type]{Normal / Emergency}"
  - "[Involved Asset List]"
  - "[Change Start]"
  - "[Change End]"
  - "[Backups Paused?]{Yes / No}"
  - "[Risk Level]{Low / Medium / High}"
  - "[Risk Description]"
  - "[Impact Level]{Low / Medium / High}"
  - "[Impact Description]"
  - "[Implementation Plan]"
  - "[Test Plan]"
  - "[Backout Plan]"
  - "[Communication Plan]"
---

# Change Request Writer

This skill helps you draft a technical Change Request (CR) for the user. Your goal is to fill out the standard template below with information provided by the user or inferred from the context.

## Instructions

1.  **Analyse Context**: Read the user's request and any available file context to gather details for the CR fields (e.g., Change Title, Reason, Dates, Risk).
2.  **Identify Missing Info**:
    - If critical information is missing (especially **Risk Level**, **Impact Level**, **Backout Plan**, **Test Plan**), ask the user for it.
    - If you can make a reasonable guess based on context (e.g., Username, Date Reported), do so, but mention it to the user.
3.  **Generate Output**: Once you have enough information, output the CR in the exact markdown format below.

## Change Request Template

```markdown
**Subject:** [Change Title]
**Type:**  [Change Type]
**Start:** [Change Start]
**End:** [Change End]
**Notes:** [Change Notes]

## Details:

| Field                                       | Value                               |
| ------------------------------------------- | ----------------------------------- |
| Ticket ID                                   | [TicketID]                          |
| Ticket Type                                 | Change Request                      |
| Username                                    | [Affected User]                     |
| Date Reported                               | [DateTime Reported]                 |
| Summary                                     | [Change Summary]                    |
| Reason for Change                           | [Reason for Change]                 |
| Change Type                                 | [Change Type]{Normal / Emergency}   |
| Asset                                       | [Involved Asset List]               |
| Start Date & Time                           | [Change Start]                      |
| End Date & Time                             | [Change End]                        |
| Does the work require backups to be paused? | [Backups Paused?]{Yes / No}         |
| Risk Level                                  | [Risk Level]{Low / Medium / High}   |
| Risk Description                            | [Risk Description]                  |
| Impact Level                                | [Impact Level]{Low / Medium / High} |
| Impact Description                          | [Impact Description]                |
| Implementation Plan                         | [Implementation Plan]               |
| Test Plan                                   | [Test Plan]                         |
| Backout Plan                                | [Backout Plan]                      |
| Communication Plan                          | [Communication Plan]                |
```
