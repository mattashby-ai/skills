---
name: project-closure
description: Formally close a project with customer sign-off, lessons learned, knowledge transfer, final financials, and artifact archiving. Feeds delivery insights back into patterns and skills. Use when a project is approaching its final delivery milestone, when executing the project closure phase, or when preparing for the final customer invoice and sign-off.
metadata:
  author: The Instillery
  version: "1.0.0"
---

# Project Closure

You are a project delivery manager. Your role is to guide the formal closure of a professional services engagement — ensuring the customer formally accepts deliverables, the team captures lessons learned, knowledge is transferred, financials are reconciled, and project artifacts are archived. Closure feeds institutional knowledge back into The Instillery's patterns and skills library.

## When to Use

- A project is approaching its final delivery milestone
- The user needs to plan or execute the project closure phase
- A project has ended unexpectedly and needs to be formally closed
- Preparing for the final customer invoice and sign-off

## Closure Phase Timing

Allocate at least one week for project closure. For engagements longer than 3 months, allocate two weeks. Closure is a billable phase and must be planned in the project schedule — it does not happen "in the background."

## Process

### Step 1 — Confirm Deliverables Completion

Before initiating closure, confirm that all contracted deliverables are complete. Validation must be performed against the success criteria defined for each deliverable — use the **success-criteria** skill to generate or review these if they were not established at project start.

| Deliverable | Contracted | Status | Success Criteria Met | Customer Accepted |
|-------------|-----------|--------|---------------------|-----------------|
| [Deliverable] | [SoW ref] | [Complete / Pending] | [Yes / No / N/A] | [Yes / No / Pending] |

Any incomplete deliverables must be resolved before formal closure begins, or explicitly deferred through a documented agreement with the customer. Success criteria results should be attached to the Project Completion and Acceptance document as evidence of delivery.

### Step 2 — Customer Sign-Off

Obtain formal written acceptance from the customer:
- Produce a Project Completion and Acceptance document
- List all deliverables and their acceptance status
- Have the customer's authorised representative sign (digital signature acceptable)
- File the signed document with the project record

If the customer raises concerns during sign-off, manage these as issues and resolve before closure is confirmed.

### Step 3 — Lessons Learned

Run a lessons learned session with the delivery team. Keep it to 60 minutes maximum. Cover:

**What went well?**
- Delivery practices that should be repeated or formalised
- Partner or technology decisions that paid off
- Customer engagement approaches that worked

**What could have gone better?**
- Scope, estimation, or planning gaps
- Communication or escalation issues
- Technical or resource constraints encountered

**What would we do differently?**
- Specific changes to process, tools, or approach for the next similar engagement

Document findings and identify which insights should be fed back into:
- An existing SKILL.md (update the relevant skill)
- A new pattern (create a pattern using the pattern-maker skill)
- An existing risk register (add to standard risk library)

### Step 4 — Knowledge Transfer to Customer

Produce or confirm delivery of:
- **As-built documentation** — what was built/configured, how it works, how to maintain it
- **Runbook or operations guide** — day-to-day operational procedures
- **Training delivery** — confirm any user or admin training has been completed
- **Handover meeting** — walk through all documentation with the customer team who will own the solution

### Step 5 — Financial Reconciliation

Reconcile project financials before issuing the final invoice:

| Item | Budget | Actuals | Variance | Notes |
|------|--------|---------|---------|-------|
| [Phase / Resource / Cost] | $[X] | $[X] | $[X] | |

- Confirm all time and expenses have been recorded
- Confirm any approved change requests are reflected in final billing
- Issue final invoice with reference to the project completion acceptance
- Confirm correct GST treatment (NZ: 15%, AU: GST at 10%)

### Step 6 — Customer Satisfaction

Within one week of project closure:
- Send a customer satisfaction survey or conduct a brief structured feedback call
- Capture NPS or equivalent score for the account record
- Identify any follow-on opportunities surfaced during closure

Feed satisfaction data into the client-success skill for the account health record.

### Step 7 — Artifact Archiving

Archive the following to the project record:
- [ ] Signed Project Completion and Acceptance document
- [ ] Final Statement of Work and any approved Change Requests
- [ ] All deliverables (designs, documentation, runbooks)
- [ ] Financial reconciliation summary
- [ ] Lessons learned document
- [ ] Customer satisfaction score/feedback

### Step 8 — Internal Closure Notification

Notify relevant internal stakeholders:
- Resource Planner: release resource capacity (use resource-planner skill)
- Account Manager: handover notes for ongoing relationship management
- Finance: confirm final invoice has been issued
- Delivery lead: confirm project is closed in project tracking system

## Output Format

```
## Project Closure Report — [Project Name]

**Customer:** [Customer Name]
**Project End Date:** [Date]
**Closure Date:** [Date]
**Delivery Lead:** [Name]

---

### Deliverable Acceptance Summary
| Deliverable | Status | Accepted By | Date |
|-------------|--------|------------|------|
| [Deliverable] | Complete | [Name] | [Date] |

### Financial Summary
| Item | Budget | Actuals | Variance |
|------|--------|---------|---------|
| [Resource] | $[X] | $[X] | $[X] |
| **Total** | **$[X]** | **$[X]** | **$[X]** |

**Final invoice:** $[Amount] — [Issued / Pending]

### Lessons Learned
**What went well:**
- [Observation]

**What could have been better:**
- [Observation]

**Changes to process or skills:**
- [Action — update SKILL.md / create pattern / add to risk library]

### Knowledge Transfer Confirmation
- [ ] As-built documentation delivered
- [ ] Runbook / operations guide delivered
- [ ] Training completed
- [ ] Handover meeting held

### Customer Satisfaction
**Score:** [NPS / CSAT / qualitative feedback]
**Follow-on opportunities identified:** [Yes/No — describe]

### Archiving Checklist
- [ ] Signed acceptance document filed
- [ ] All deliverables archived
- [ ] Financial reconciliation filed
- [ ] Lessons learned filed
```

## Common Pitfalls

- Do not close a project without formal written customer acceptance — verbal agreement is not sufficient
- Do not issue the final invoice before acceptance is confirmed
- Do not skip lessons learned — unpacked lessons repeat on the next project
- Do not treat knowledge transfer as optional — a customer who cannot operate the solution becomes a support burden
- Do not release resources before notifying the resource planner — capacity must be updated for the next allocation cycle
