---
name: sow-quality-check
description: First-pass quality review of a Statement of Work (SoW) document. Use when a user provides a SoW file or asks to review, check, or QA a SoW. Produces a structured checklist showing pass/fail status for each required section. Triggers on phrases like "review this SoW", "check my SoW", "QA this statement of work", or whenever a SoW document is attached.
metadata:
  author: The Instillery
  version: "1.0.0"
---

# SoW Quality Check

Perform a first-pass structural and completeness review of a Statement of Work. This is a lightweight check — not a technical review. The goal is to ensure every required section exists, is populated with real content, and is internally consistent before it goes to a technical reviewer.

Do not assess the quality of the content itself. Only assess whether it is present, complete, and consistent.

---

## Review Process

Read the SoW in full before producing output. Then work through each section in the checklist below.

---

## Checklist Sections

For each section, mark as **PASS**, **FAIL**, or **N/A** (where explicitly optional per template).

Output format per section:
```
### [Section Name] — PASS / FAIL / N/A
- ✅ or ❌ [specific finding]
- ✅ or ❌ [specific finding]
```

---

### Required Sections

Check that every section below exists in the document. If a section is missing entirely, mark FAIL and note it is absent.

1. **Background** — Describes current state and motivation. Not a task list.
2. **Objectives** — Customer requirements as stated by them. Min. 1 objective listed.
3. **Approach** — High-level approach / exec summary. Not a task list.
4. **Target Dates & Completion Criteria** — Start date, estimated completion date, and completion criteria present.
5. **Services & Deliverables** — At least 1 service task and 1 deliverable listed.
6. **Milestones** — N/A if milestone table is not included. FAIL if table exists but is empty.
7. **Dependencies** — At least 1 item listed, or explicitly states none.
8. **Out of Scope** — Standard OOS items present. At least 1 custom OOS item listed or confirmed as complete.
9. **Assumptions** — At least 1 assumption listed beyond the standard boilerplate.
10. **Your Responsibilities** — At least 1 client responsibility listed. PM vs Project Admin option resolved.
11. **Risks** — At least 1 risk listed beyond the standard boilerplate.
12. **Business Hours** — One timezone/location option selected. Others removed.
13. **Expenses** — One option selected (expenses expected / not expected). Others removed.
14. **Terms & Termination** — Fixed Cost or T&M clause selected. Unused option removed.
15. **Billing** — One billing model selected (T&M / Fixed Cost / Fixed Cost Milestone). Others removed.
16. **Deposit & Minimum Fees** — One option selected or section removed. Not both options present.
17. **Your Resources & Roles** — Resource table populated with real names or confirmed TBC. Role descriptions present.
18. **Version History** — At least one version entry present with date and author.
19. **Appendix A** — N/A if not required. FAIL if referenced in the body but missing.

---

## Completeness Checks (apply across all sections)

### Placeholder Text
Flag any of the following if still present anywhere in the document:

- `<Delete this instruction after reading` or any `<Delete...>` tags
- `Internal Note:` text
- Generic placeholders: `Task 1`, `Task 2`, `Objective 1`, `Deliverable 1`, `Dependency Item #1`, `Risk Item #1`, `OOS Item #1`, `Assumption Item #1`, `Client Deliverable Item #1`
- `[SERVICES]`, `[` or `]` used as unfilled placeholders
- `TBC` unless inside a specifically named field where it is expected (e.g. Start Date before engagement confirms)
- `Month and Year`, `Date`, `Person` in Version History

### Unresolved Multiple-Choice Options
Flag where the template offered two or more options and both/all remain:

- Expenses section: both "no expenses expected" and "some expenses expected" present
- Billing section: more than one billing model present
- Terms & Termination: both T&M release clause and Fixed Cost clause present
- Deposit & Minimum Fees: both deposit and minimum fee options present
- Business Hours: more than one timezone/location present
- Your Responsibilities: both PM and Project Admin options present

### Name & Consistency
- Customer/company name used consistently throughout (no mix of trading name vs legal name, no blank fields)
- Stakeholder names in Your Resources & Roles match names used elsewhere in the document
- "The Instillery" referred to consistently (not abbreviated inconsistently)

---

## Output Format

Begin with a one-line summary:

> **Overall: READY FOR TECHNICAL REVIEW** / **NOT READY — [N] issues found**

Then produce the section-by-section checklist.

After the checklist, output two grouped lists:

**Issues to Resolve** — all FAILs, numbered and actionable. One line each.
**Flagged for Attention** — anything ambiguous that a human should confirm but is not a definitive fail.

Do not provide suggestions for improving content. Do not rewrite sections. Do not assess whether the scope is sensible. Only assess structure, completeness, and consistency.