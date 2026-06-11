---
name: dependency-mapper
description: Maps dependencies in a professional services delivery project to produce an importable task list for Microsoft Planner or Microsoft Project. Use when a user wants to understand task sequencing, critical path, bottlenecks, procurement gates, or risks — or mentions "dependency mapping", "task order", or "predecessor". When used as part of a full project plan, project-planner calls this Skill automatically — use dependency-mapper directly only when the user specifically asks for dependency analysis as a standalone artefact.
metadata:
  author: The Instillery
  version: "1.0.0"
---

# Dependency Mapper

## Purpose

Transform a Statement of Work (SoW) and Three-Point Effort Estimate (3PE) into an exhaustive, dependency-mapped task list importable into Microsoft Project (primary) or Microsoft Planner (secondary), plus a Mermaid Gantt chart. The SoW and 3PE are intentionally high-level — your role is to apply domain knowledge to fill the gaps, not to reflect only what is written.

---

## Process

### Phase 1 — Document Parsing

Extract from the SoW and 3PE:
- Deliverables, milestones, and phases (explicit scope)
- Named technologies, vendors, and platforms
- Constraints: go-live dates, freeze windows, sign-off requirements
- Procurement items: hardware, licences, third-party services
- Assumptions and exclusions (potential hidden dependencies)
- 3PE values per task: Optimistic (O), Most Likely (M), Pessimistic (P)

If documents are not provided, ask: *"Please share the SoW and 3PE — or describe the project scope and effort estimates."*

---

### Phase 2 — Project Classification & Enrichment

Identify the project type(s) from the parsed content. Consult the Domain Reference section and add industry-standard tasks absent from the documents.

**Rules for enrichment:**
- Tag every inferred task `[INFERRED]` in the Notes column
- Do not invent scope — only add tasks standard for the identified domain
- Place inferred tasks at the earliest logical point in the dependency chain
- Procurement items always become explicit tasks with their own predecessor chain

**Identify and flag:**
- **Procurement gates** — hardware/licence delivery blocking downstream tasks
- **Customer dependencies** — access provisioning, sign-offs, UAT, data provision
- **Third-party dependencies** — vendor delivery, ISP circuits, cloud tenant readiness
- **Parallel workstreams** — tasks with shared predecessors that can run concurrently

---

### Phase 3 — Dependency Mapping

For each task assign:
- A sequential **Task ID**
- An **Outline Level** (1 = Phase, 2 = Work Package, 3 = Task)
- **Predecessor IDs** (comma-separated; FS by default; note SS/FF/SF and lag where relevant, e.g. `5FS+2d`)
- **Duration** — use M from 3PE; where O–P spread exceeds 50% of M, flag `[HIGH VARIANCE]`

Annotate accordingly:
- **Critical path** — longest chain with zero float; mark tasks `[CRITICAL]`
- **Bottlenecks** — tasks with 3+ successors; mark `[BOTTLENECK]`
- **Risk flags** — external dependencies, high-variance estimates; mark `[RISK]`

---

### Phase 4 — Output

Produce three outputs in this order:

**1. CSV** — MS Project importable task list (schema below)

**2. Mermaid Gantt chart** — visual schedule derived from the CSV (schema below)

**3. Plain-text summary** covering:
- Critical path: start task → end task, total duration
- Top 3 bottleneck tasks and why
- Top 3 risks with a one-line mitigation each
- Procurement items with back-calculated required-by dates

---

## Output Format — MS Project CSV Schema

```
ID,Outline_Level,Name,Duration,Optimistic,Pessimistic,Predecessors,Notes
1,1,Project Kickoff,,,,,"[PHASE]"
2,2,Stakeholder alignment,1d,1d,2d,,"[CUSTOMER]"
3,2,SoW sign-off,0d,,,2,"[MILESTONE][CUSTOMER]"
4,1,Procurement,,,,,"[PHASE]"
5,2,Raise hardware PO,1d,,,3,"[PROCUREMENT]"
6,2,Hardware delivery,10d,7d,21d,5,"[PROCUREMENT][RISK][CRITICAL]"
```

**Field rules:**
- `Duration` = M from 3PE in days (`5d`); `0d` for milestones
- `Optimistic` / `Pessimistic` — populate for high-variance tasks only
- `Predecessors` — comma-separated IDs; append lag if needed (`3FS+2d`)
- `Outline_Level` — 1 Phase, 2 Work Package, 3 Task

**MS Planner note:** Planner has no native predecessor support. Open the CSV in Excel and use Import to Planner — map Name → Task, Notes → Notes, Outline Level 1 → Bucket. Predecessor logic must be enforced via board ordering or Power Automate.

---

## Output Format — Mermaid Gantt Chart

Render a Mermaid `gantt` block as a fenced code block. Derive start dates and durations from the CSV task list — the Gantt is a visual derivative of the CSV, not an independent calculation.

**Gantt rules:**
- Use `dateFormat YYYY-MM-DD` and `axisFormat %d %b`
- If no absolute start date is provided in the SoW, anchor day 1 as `today` and use relative offsets
- Group tasks by `section` matching Outline Level 1 phases from the CSV
- Use M (Most Likely) duration for all bars
- Milestones (`0d` tasks in CSV) use `milestone` type
- Mark critical path tasks with the `crit` modifier
- Mark customer/external dependencies with the `active` modifier
- Omit sub-task detail if total task count exceeds 40 — show Work Package level only to keep the chart readable
- Procurement items with high variance: append ` [P: Xd]` to the task label to surface the pessimistic duration inline

**Syntax example:**
```
gantt
  title Project Title
  dateFormat YYYY-MM-DD
  axisFormat %d %b
  section Kickoff
    Stakeholder alignment     :active, t2, 2025-06-02, 1d
    SoW sign-off              :milestone, t3, after t2, 0d
  section Procurement
    Raise hardware PO         :t5, after t3, 1d
    Hardware delivery [P:21d] :crit, t6, after t5, 10d
  section Build
    Server configuration      :crit, t7, after t6, 5d
    Network configuration     :t8, after t3, 3d
```

**Dependency notation:** Use `after <taskId>` for FS relationships. For SS or parallel starts, align start dates explicitly. Mermaid does not support lag natively — absorb lag into the successor's start date and note the lag in the task label (e.g. `Config (+2d lag)`).

**Section ordering:** Sections must follow the critical path top-to-bottom. Parallel workstreams sit in their own section beneath the phase that triggers them.

---

## Domain Reference — Enrichment Catalogues

### All Projects (always include)
Kickoff and RACI confirmation · risk register creation · change management process agreement · phase-gate sign-offs · project closure and handover documentation

### Cloud Migrations / Infrastructure
**Sequence:** Design → Procurement → Build → Migrate → Validate → Cutover → Handover
**Infer:** Landing zone / account structure setup · IAM/RBAC design and implementation · network peering and routing · firewall rule migration · DNS cutover plan and execution · backup validation · DR test · hypercare period

### Software / Application Delivery
**Sequence:** Discovery → Design → Dev/Config → Integration → UAT → Go-live → Support transition
**Infer:** Environment provisioning (dev/test/prod) · CI/CD pipeline setup · data migration scripts · regression test execution · performance baseline capture · rollback plan documentation

### Network & Security Deployments
**Sequence:** Design → Procurement → Staging → Site Prep → Install → Commission → Handover
**Infer:** Low-level design (LLD) sign-off · circuit provisioning (long-lead — assume 30–65 business days) · firewall policy peer review · penetration test scheduling · NOC/SOC integration · runbook creation

### End-User Compute / Device Rollouts
**Sequence:** SOE Build → Pilot → Wave deployments → Legacy decommission
**Infer:** Standard Operating Environment (SOE) build and approval · MDM enrolment profile configuration · user communications · helpdesk briefing · asset disposal / ITAD engagement

### Data Platform Implementation
**Sequence:** Discovery → Architecture → Ingestion → Transformation → Reporting → UAT → Go-live
**Infer:** Data classification exercise · source system access agreements · schema mapping · data quality baseline · BI licence provisioning · retention policy configuration

### Security Service Onboarding
**Sequence:** Scoping → Integration design → Deployment → Tuning → Handover
**Infer:** SIEM/XDR integration testing · alert rule baseline · false-positive tuning window (allow 10–15 business days) · SOC runbook creation · escalation path and SLA agreement

### Managed Service Onboarding
**Sequence:** Discovery → Documentation → Tooling integration → Runbook creation → Hypercare → BAU
**Infer:** Asset and configuration discovery · monitoring baseline establishment · service desk integration and ticket routing · on-call schedule and escalation setup · SLA agreement sign-off

### Hybrid Compute Design & Build
**Sequence:** Design → Procurement → Network prep → Compute build → Integration → Validation
**Infer:** HLD and LLD sign-off · rack elevation and cabling design · power and cooling confirmation · hypervisor licensing · vMotion/replication testing · storage tiering validation

### Procurement (apply to all project types where applicable)
- Identify every hardware, software, and third-party service requiring purchase
- Create an explicit chain per item: Raise PO → Vendor confirmation → Delivery → Goods receipt → Staging
- Back-calculate required-by dates from the first dependent task
- Flag all procurement tasks `[PROCUREMENT]`; assess each for `[CRITICAL]` and `[RISK]`
- Default lead times if not specified in SoW: standard hardware 10–15 business days `[INFERRED]`; networking equipment 15–30 business days `[INFERRED]`; circuits 30–65 business days `[INFERRED][RISK]`