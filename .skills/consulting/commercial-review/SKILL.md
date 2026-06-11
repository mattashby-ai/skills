---
name: commercial-review
description: Evaluate agreements for services such as consulting, software implementation, or specialised expertise to ensure they mitigate risks and align with business objectives. A thorough review ensures that scope, liability, and payment terms are clearly defined, protecting the commercial interests of both parties and ensuring compliance with relevant laws. Use when reviewing contracts, vendor agreements, statements of work, variations, or any document that defines scope, payment, or liability. For first-pass SoW structural completeness checks, use sow-quality-check. For technical design validation, use technical-review. This Skill focuses on commercial risk, liability, IP, and payment terms.
metadata:
  author: The Instillery
  version: "1.0.0"
---

# Commercial Review Skill

Review service agreements — contracts, variations, statements of work, plans, or designs — for commercial risk, clarity, and alignment with business objectives.

---

## Phase 1: Identify the Document

Before reviewing, establish:

- **Document type**: Contract, variation, SOW, proposal, plan, or design
- **Parties**: Who is the client, who is the vendor/provider
- **Service type**: Consulting, software implementation, managed services, specialised expertise, or other
- **Perspective**: Whose interests are being protected (client or vendor)

If not clear from the document, ask before proceeding.

---

## Phase 2: Primary Review

Evaluate the following in order. Flag issues as **[RISK]**, **[GAP]**, or **[RECOMMENDATION]**.

### 1. Scope Definition
- Is the scope of work specific, bounded, and unambiguous?
- Are deliverables and acceptance criteria defined?
- Is there a change control process for scope variations?
- Are exclusions explicitly stated?

### 2. Liability and Risk Allocation
- Are liability caps defined and proportionate?
- Is indemnification mutual or one-sided?
- Are consequential/indirect damages excluded?
- Are insurance requirements specified and adequate?
- Is there a force majeure clause?

### 3. Payment Terms
- Are payment milestones clearly tied to deliverables or dates?
- Are late payment penalties defined?
- Is there a dispute resolution process for contested invoices?
- Are expenses reimbursable, and if so, under what conditions?

### 4. Termination
- Are termination-for-cause and termination-for-convenience provisions present?
- Are notice periods reasonable?
- Are obligations on termination (handover, data return, final payment) specified?

### 5. Intellectual Property
- Is IP ownership clearly assigned post-delivery?
- Are background IP rights (pre-existing materials) distinguished from foreground IP?
- Are licence terms defined if ownership is not transferred?

### 6. Compliance and Governing Law
- Is the governing jurisdiction stated?
- Are relevant regulatory obligations referenced (privacy, data protection, sector-specific)?
- Are confidentiality obligations present and adequately scoped?

---

## Phase 3: Pricing Model Check (Secondary — run only if issues are present)

Load `references/pricing-models.md` if any of the following are true:

- The pricing model is ambiguous or unstated
- Payment terms appear mismatched to how the work is scoped or delivered
- Milestone schedules seem disconnected from actual deliverables
- The model introduces disproportionate risk for one party

**When loaded, assess:**

1. **Model identification** — What pricing model does this agreement use (or appear to use)?
2. **Model-scope fit** — Is the model appropriate for this type of engagement and delivery method?
3. **Risk alignment** — Does the model distribute commercial risk fairly between parties?
4. **Milestone alignment** — Do payment trigger points correspond to meaningful, verifiable deliverables?
5. **Flag** — If the model is clearly problematic, raise it as **[RISK: PRICING MODEL]** with a brief explanation and suggested alternative.

Do not raise pricing model issues if the model is conventional for the engagement type and terms are internally consistent.

---

## Phase 4: Output

### Structure
Produce a structured review with the following sections:

```
## Commercial Review — [Document Title or Description]

### Summary
[2–3 sentence overview: what the document is, overall risk level (Low / Medium / High), and primary concern if any]

### Key Findings
[Organised by Phase 2 categories. Each finding labelled [RISK], [GAP], or [RECOMMENDATION]. Include clause references where possible.]

### Pricing Model Assessment *(include only if Phase 3 was triggered)*
[Model identified, fit assessment, specific issues if any]

### Suggested Next Steps
[Prioritised list of actions: what to negotiate, clarify, or escalate]
```

### Tone and Standards
- Be direct. Label problems clearly.
- Do not soften material risks with hedging language.
- Recommendations should be actionable, not generic.
- Where best practice guidance is needed, consult vendor documentation first, then organisational document repositories (e.g. Confluence).
- If the document is incomplete or ambiguous, state what is missing rather than assuming.

---

## Reference Files

| File | When to Load |
|------|-------------|
| `references/pricing-models.md` | Phase 3 — when pricing model is absent, ambiguous, or problematic |
