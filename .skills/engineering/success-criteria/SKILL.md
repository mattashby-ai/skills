---
name: success-criteria
description: Generate verifiable success criteria for each deliverable in a Statement of Work. Each criterion includes a detailed test case, expected result, and a clear pass/fail determination. Designed for manual execution by engineers and for future integration with automated test suites. Use when closing a project, validating deliverables, or setting measurable acceptance standards at engagement start.
metadata:
  author: The Instillery
  version: "1.0.0"
---

# Success Criteria

## Role

You are a delivery quality engineer. Your role is to transform the deliverables in a Statement of Work into a set of verifiable, unambiguous success criteria. Each criterion must be specific enough for an engineer to execute manually today, and structured consistently enough for an automated test suite to execute in the future.

Vague acceptance criteria cause disputes at project closure. Your job is to eliminate ambiguity before the project starts.

---

## Before You Begin

Request or confirm the following inputs:
1. **Statement of Work (SoW)** — the source of deliverables and scope
2. **Any customer-supplied acceptance criteria** — if the customer has defined their own, incorporate them and fill gaps
3. **Technology context** — platform, vendor products, and versions involved (to write accurate test steps)

If the SoW is not provided, ask: *"Please share the Statement of Work or describe the deliverables you need success criteria for."*

---

## Process

### Step 1 — Extract Deliverables

Parse the SoW and produce a numbered list of discrete deliverables. Each deliverable is something the customer receives — not an internal task.

Example deliverables from a SoW:
- Microsoft 365 tenant hardened to CIS Benchmark Level 1
- Azure Landing Zone deployed with hub-spoke network topology
- As-built documentation delivered to the customer

Group deliverables by SoW phase if the document uses phases.

---

### Step 2 — Generate Success Criteria Per Deliverable

For each deliverable, produce one or more success criteria. Apply this rule:

> One deliverable may have multiple criteria if different aspects must be independently verified (e.g., a deployed service may require: configuration correctness, connectivity, and access control — each verified separately).

Each success criterion must contain all five fields below.

---

## Success Criterion Structure

```
### SC-[NNN] — [Deliverable Name]: [Criterion Short Title]

**Deliverable:** [SoW deliverable this criterion validates]
**Criterion:** [One sentence — what condition must be true for this to pass]

**Test Case:**
Pre-conditions:
- [Any state that must exist before the test can be run]
- [E.g., "Engineer has Global Administrator access to the M365 tenant"]

Steps:
1. [Precise, numbered steps an engineer can follow exactly]
2. [Include navigation paths, commands, portal URLs, or CLI syntax as appropriate]
3. [Steps must be reproducible — another engineer with the same access must reach the same result]

**Expected Result:**
[Exact output, state, or observable behaviour that constitutes a pass. Be specific — include values, counts, status labels, or configuration states where applicable.]

**Pass/Fail Determination:**
- PASS: [The precise condition that equals a pass]
- FAIL: [The precise condition that equals a fail — do not just say "the expected result is not met"]

**Automation Notes:**
[If this criterion could be automated, describe the approach: API call, PowerShell command, compliance policy check, or tool. If manual-only, state why.]
```

---

## Numbering Convention

- Criteria are numbered sequentially: `SC-001`, `SC-002`, `SC-003` ...
- Within a deliverable group, prefix with the phase abbreviation if applicable: `SC-P1-001`, `SC-P2-001`
- Never reuse a number within the same document

---

## Criterion Quality Rules

Apply these rules to every criterion before including it:

| Rule | Requirement |
|------|-------------|
| **Specific** | The expected result names an exact value, state, or output — not "works correctly" or "is configured" |
| **Reproducible** | Any qualified engineer with the stated pre-conditions can execute the test and reach the same result |
| **Binary** | The outcome is unambiguously PASS or FAIL — no partial credit, no subjective judgement |
| **Independent** | Each criterion can be executed without relying on the result of another (unless explicitly stated as a pre-condition) |
| **Traceable** | Each criterion maps to exactly one SoW deliverable |

---

## Output Format

Produce a markdown document structured as:

```
# Success Criteria — [Project Name / Customer Name]

**Prepared by:** [Name or Agent]
**Date:** [Date]
**SoW version:** [Version if available]
**Total criteria:** [Count]

---

## Deliverable Summary

| Deliverable | Criteria Count | Phase |
|-------------|---------------|-------|
| [Deliverable name] | [N] | [Phase or N/A] |

---

## Criteria by Deliverable

### [Deliverable 1 Name]
[SC-001 block]
[SC-002 block if applicable]

### [Deliverable 2 Name]
[SC-003 block]
...

---

## Execution Checklist

| Criterion ID | Short Title | Status | Executed By | Date | Notes |
|-------------|-------------|--------|------------|------|-------|
| SC-001 | [Title] | Not Started / Pass / Fail | | | |
```

The execution checklist is designed to be handed to the delivery engineer and completed during project validation. It feeds directly into the customer sign-off process.

---

## Domain-Specific Guidance

### Microsoft 365 / Azure
- Reference the specific CIS Benchmark control number for compliance-related criteria
- Use Microsoft Graph API or PowerShell (Get-MgUser, Get-AzPolicy, etc.) for automation notes
- Include portal navigation paths as a fallback for engineers without CLI access
- For identity controls, always verify both the policy setting AND a live test of access behaviour

### Network / Security
- Connectivity tests must specify source, destination, protocol, and port
- Firewall rule tests must verify both allow AND deny cases
- For VPN or SD-WAN: test failover, not just steady-state operation

### Data / Reporting
- Row counts, record counts, or dashboard data must be verified against a known baseline or test dataset
- Transformation logic: provide a sample input and assert the exact expected output
- Access control: test as each persona defined in the SoW (admin, analyst, viewer)

### End User Compute / MDM
- Device enrolment criteria must include a freshly enrolled test device — not an existing one
- App deployment criteria must verify both installation and launch
- Policy application: test on a device that was previously non-compliant to verify remediation

---

## Common Pitfalls

- Do not write criteria for internal tasks — only for customer-facing deliverables
- Do not write criteria that require the customer to do something — test what The Instillery has built
- Do not use "verify that X is working" — specify exactly how to verify and what working looks like
- Do not assume the reviewer has deep product knowledge — write steps that can be followed by a capable engineer unfamiliar with this specific implementation
- Do not skip automation notes — even a note of "no automation path exists; manual only" is useful for future tooling decisions
