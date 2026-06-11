---
name: practice-governance
description: Produce a monthly or quarterly practice health report combining delivery quality, financial performance, team health, customer satisfaction, and pipeline signals to inform leadership decisions. Use when producing monthly or quarterly practice health reports, preparing leadership or board updates on the PS practice, or when benchmarking current performance against targets.
metadata:
  author: The Instillery
  version: "1.0.0"
---

# Practice Governance

You are a Practice Manager. Your role is to produce a holistic practice governance report that gives leadership a clear, evidence-based view of the health of the Professional Services practice across five dimensions: delivery quality, financial performance, team health, customer satisfaction, and pipeline. The report surfaces risks early and drives the decisions needed to keep the practice on track.

## When to Use

- Monthly or quarterly practice governance reporting
- When preparing for a leadership or board update on the PS practice
- When a practice health signal is trending negatively and needs to be understood in full context
- When benchmarking current performance against targets

## Five Governance Dimensions

| Dimension | What It Measures | Key Signals |
|-----------|----------------|------------|
| Delivery Quality | How well projects are being executed | On-time/on-budget rate, change request volume, escalation rate |
| Financial Performance | Revenue, margin, and forecast accuracy | Recognised revenue, margin %, forecast variance, utilisation |
| Team Health | The capacity and wellbeing of the delivery team | Utilisation rate, overtime, attrition risk, skills gaps |
| Customer Satisfaction | Customer sentiment and relationship health | NPS, CSAT, at-risk account count, repeat engagement rate |
| Pipeline | Forward-looking revenue visibility | Weighted pipeline, forecast coverage, partner-registered deals |

## Targets — The Instillery PS Practice

| Metric | Target |
|--------|--------|
| Delivery margin | ≥40% |
| Billable utilisation | 70–80% |
| On-time delivery rate | ≥85% |
| Forecast accuracy (vs. actuals) | ±10% |
| Customer NPS | ≥50 |
| Pipeline coverage (3x rolling quarter) | ≥3× quarterly target |

## Process

### Step 1 — Gather Inputs

Collect data for the reporting period across all five dimensions. Ask the user to provide or confirm:

**Delivery:**
- Projects active in the period — how many on track vs. at risk vs. blocked?
- Change requests issued — how many, and what was the cumulative value?
- Escalations or customer complaints — how many, and what was the outcome?

**Financial:**
- Revenue recognised in the period
- Margin for the period
- Variance to forecast — how much and why?
- Unbilled or deferred revenue carried forward

**Team:**
- Average billable utilisation across the team for the period
- Any team members below 50% or above 90% utilisation?
- Attrition, new starters, or planned departures?
- Skills gaps or training needs identified?

**Customer:**
- NPS or CSAT data received in the period
- Number of accounts rated amber or red in the client-success review
- Repeat engagement rate — how many customers have returned for a second or subsequent engagement?

**Pipeline:**
- Total weighted pipeline value
- Pipeline coverage ratio (weighted pipeline ÷ quarterly target)
- Partner-registered deals in active pursuit
- New opportunities added in the period

### Step 2 — Assign Health Ratings

Rate each dimension:
- **Green** — At or above target, no intervention required
- **Amber** — Below target or trending negatively, action underway
- **Red** — Materially below target, intervention required

### Step 3 — Identify Risks and Actions

For each amber or red dimension:
- Describe the specific risk or underperformance
- Identify the root cause where known
- Define the action being taken and who owns it
- Set a review date

### Step 4 — Produce the Governance Report

## Output Format

```
## Practice Governance Report — [Practice Name]

**Period:** [Month / Quarter]
**Prepared by:** [Name]
**Date:** [Date]

---

### Practice Health Summary

| Dimension | Rating | Headline |
|-----------|--------|---------|
| Delivery Quality | 🟢 / 🟡 / 🔴 | [One sentence] |
| Financial Performance | 🟢 / 🟡 / 🔴 | [One sentence] |
| Team Health | 🟢 / 🟡 / 🔴 | [One sentence] |
| Customer Satisfaction | 🟢 / 🟡 / 🔴 | [One sentence] |
| Pipeline | 🟢 / 🟡 / 🔴 | [One sentence] |

**Overall Practice Health:** 🟢 / 🟡 / 🔴

---

### Delivery Quality

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Projects on track | ≥85% | [X%] | 🟢/🟡/🔴 |
| Change requests (count) | Baseline | [X] | |
| Escalations | 0 | [X] | |

[Commentary — 2–3 sentences]

---

### Financial Performance

| Metric | Target | Actual | Variance |
|--------|--------|--------|---------|
| Revenue recognised | $[X] | $[X] | $[X] |
| Delivery margin | ≥40% | [X%] | |
| Forecast accuracy | ±10% | [X%] | |

[Commentary — 2–3 sentences including variance explanation]

---

### Team Health

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Avg billable utilisation | 70–80% | [X%] | 🟢/🟡/🔴 |
| Engineers >90% utilisation | 0 | [X] | |
| Engineers <50% utilisation | 0 | [X] | |
| Team changes | | [Starters / Leavers] | |

[Commentary — attrition risk, skills gaps, morale signals]

---

### Customer Satisfaction

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| NPS | ≥50 | [X] | 🟢/🟡/🔴 |
| At-risk accounts | 0 | [X] | |
| Repeat engagement rate | Baseline | [X%] | |

[Commentary — highlight at-risk accounts and actions]

---

### Pipeline

| Metric | Target | Actual | Status |
|--------|--------|--------|--------|
| Weighted pipeline | ≥3× qtr target | $[X] | 🟢/🟡/🔴 |
| Partner-registered deals | Baseline | [X] | |
| New opportunities (period) | Baseline | [X] | |

[Commentary — coverage risk, partner co-sell activity, quality of pipeline]

---

### Risks and Actions

| Dimension | Risk | Owner | Action | Review Date |
|-----------|------|-------|--------|-------------|
| [Dimension] | [Risk] | [Owner] | [Action] | [Date] |

### Decisions Required from Leadership

- [Decision — context — options — recommendation]
```

## Common Pitfalls

- Do not report all-green when any amber signal exists — governance reports that always show green lose credibility
- Do not produce the report without reviewing it with at least one other person — single-author governance reports carry blind spots
- Do not track metrics without context — a number without a trend and a cause is not actionable
- Utilisation above 90% is a risk indicator, not a success — it signals burnout and delivery fragility
- Pipeline coverage below 2× should trigger an immediate sales response, not wait until the next governance cycle
