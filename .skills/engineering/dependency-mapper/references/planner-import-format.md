# Task Import Formats — Microsoft Planner and Microsoft Project

Reference for producing tool-compatible output from dependency-mapper skill results.

---

## Microsoft Project — CSV Import

Microsoft Project supports CSV import and export. This is the preferred format for dependency mapping output because it supports predecessor relationships.

### Column Reference

| Column | Required | Format | Notes |
|--------|---------|--------|-------|
| ID | Yes | Integer | Unique task identifier; used by Predecessors column |
| Name | Yes | Text | Task name — keep under 100 characters |
| Outline Level | Yes | Integer | 1 = phase, 2 = task, 3 = sub-task |
| Duration | No | `Xd`, `Xw`, `Xh` | e.g. `5d`, `2w`, `4h` |
| Start | No | DD/MM/YYYY | Leave blank to let Project calculate from dependencies |
| Finish | No | DD/MM/YYYY | Leave blank to let Project calculate |
| Predecessors | No | ID or `IDtype+lag` | See dependency types below |
| Resource Names | No | Comma-separated text | Role names or person names |
| Notes | No | Text | Task description or acceptance criteria |
| % Complete | No | Integer 0–100 | |
| Milestone | No | `Yes` / `No` | Mark key sign-off or delivery gates |

### Dependency Types (Predecessors Column)

| Notation | Type | Meaning |
|----------|------|---------|
| `3` | Finish-to-Start (FS) | Task starts after Task 3 finishes (default) |
| `3SS` | Start-to-Start | Task starts when Task 3 starts |
| `3FF` | Finish-to-Finish | Task finishes when Task 3 finishes |
| `3SF` | Start-to-Finish | Task finishes when Task 3 starts (rare) |
| `3+2d` | FS with 2-day lag | Task starts 2 days after Task 3 finishes |
| `3-1d` | FS with 1-day lead | Task starts 1 day before Task 3 finishes |
| `3,5` | Multiple predecessors | Task depends on both Task 3 and Task 5 |

### Sample CSV

```csv
ID,Name,Outline Level,Duration,Start,Finish,Predecessors,Resource Names,Notes,Milestone
1,Project,1,,,,,,,No
2,Planning Phase,2,,,,,,,No
3,Kick-off Workshop,3,1d,,,,"Delivery Lead","Schedule all stakeholders",No
4,Requirements Discovery,3,5d,,,"3","Senior Consultant","Customer workshops and stakeholder interviews",No
5,Requirements Sign-off,3,1d,,,"4","Customer","Customer sign-off required",Yes
6,Design Phase,2,,,,,,,No
7,High Level Design,3,8d,,,"5","Solution Architect","",No
8,Design Review,3,2d,,,"7","Principal Consultant","Internal QA",No
9,Design Sign-off,3,1d,,,"8","Customer","",Yes
10,Implementation Phase,2,,,,,,,No
11,Environment Preparation,3,3d,,,"9","Consultant","",No
12,Configuration,3,10d,,,"11","Senior Consultant, Consultant","",No
13,Integration Testing,3,5d,,,"12","Senior Consultant","",No
14,UAT,3,5d,,,"13","Customer","Customer-led; Instillery support",No
15,UAT Sign-off,3,1d,,,"14","Customer","",Yes
16,Deployment Phase,2,,,,,,,No
17,Cutover Planning,3,2d,,,"15","Delivery Lead","",No
18,Production Deployment,3,2d,,,"17","Senior Consultant","",No
19,Hypercare,3,5d,,,"18","Consultant","Business hours support",No
20,Closure Phase,2,,,,,,,No
21,Documentation Handover,3,2d,,,"18","Consultant","As-built and runbook",No
22,Training Delivery,3,2d,,,"18","Senior Consultant","",No
23,Project Sign-off,3,1d,,,"19,21,22","Customer","",Yes
```

---

## Microsoft Planner — Grid View Import

Microsoft Planner supports CSV import via the **Grid view** (Planner web → switch to Grid view → Import). Planner does **not** support predecessor/dependency relationships — tasks are organised by bucket only.

Use Planner import for task assignment and tracking; use Microsoft Project for dependency and critical path management.

### Column Reference

| Column | Required | Notes |
|--------|---------|-------|
| Task Name | Yes | Max 255 characters |
| Bucket | No | Must match an existing bucket name in the plan |
| Start Date | No | MM/DD/YYYY |
| Due Date | No | MM/DD/YYYY |
| Assigned To | No | Email address of assignee |
| Priority | No | `Urgent`, `Important`, `Medium`, `Low` |
| Notes | No | Task description |
| Labels | No | Comma-separated label names |
| Checklist | No | Pipe-separated checklist items: `Item 1|Item 2` |

### Sample CSV

```csv
Task Name,Bucket,Due Date,Start Date,Assigned To,Priority,Notes
Kick-off Workshop,Planning,01/15/2026,01/12/2026,,Important,Schedule with all stakeholders
Requirements Discovery,Planning,01/22/2026,01/15/2026,,Urgent,Customer workshops and interviews
Requirements Sign-off,Planning,01/23/2026,01/22/2026,,Urgent,Customer sign-off required before design begins
High Level Design,Design,02/06/2026,01/26/2026,,Important,Solution Architect lead
Design Review,Design,02/10/2026,02/06/2026,,Medium,Internal QA review
Design Sign-off,Design,02/11/2026,02/10/2026,,Important,Customer sign-off required
Environment Preparation,Implementation,02/14/2026,02/12/2026,,Medium,
Configuration,Implementation,02/28/2026,02/14/2026,,Important,
Integration Testing,Implementation,03/07/2026,02/28/2026,,Important,
UAT,Implementation,03/14/2026,03/07/2026,,Urgent,Customer-led; Instillery support
Production Deployment,Deployment,03/18/2026,03/16/2026,,Urgent,
Hypercare,Deployment,03/25/2026,03/18/2026,,Medium,Business hours support
Documentation Handover,Closure,03/20/2026,03/18/2026,,Medium,As-built and runbook
Project Sign-off,Closure,03/26/2026,03/25/2026,,Urgent,Customer sign-off
```

---

## Output Guidance for Dependency Mapper

When producing output, generate all three of the following:

1. **Dependency table** (Markdown) — for human review and stakeholder communication
2. **Microsoft Project CSV** — for project managers to import into MPP
3. **Critical path summary** — list the longest dependency chain from start to finish

The critical path is the sequence of tasks where any delay directly delays the project end date. Highlight these tasks in the dependency table.
