---
name: cost-modelling
description: Cost Modelling is the structured, data-driven process of estimating the costs associated with a project, product, or service. It translates operational variables into financial insights — breaking down fixed, variable, and indirect costs — to enable better decision-making, budgeting, and scenario planning. Use when the user wants to understand the financial implications of a plan or design, or mentions "cost modelling", "cost model", "cost estimate", "budget model", "TCO", "should-cost", "schedule of rates", or "cash flow model". Trigger even for casual phrasing like "how much will this cost to build?" or "can you put together a budget for this?".
metadata:
  author: The Instillery
  version: "1.0.0"
---

# Cost Modelling Skill

> **Required Skill:** This Skill delegates Excel creation and formatting to the `xlsx` pre-built skill. Enable the `xlsx` Skill in your Claude project settings (Anthropic platform skill library) before use.

## Purpose
Transform project inputs into a structured Excel cost model. Output is always an `.xlsx` file. Apply the **xlsx skill** for all Excel creation, formula, and formatting conventions — this skill governs what to build; the xlsx skill governs how to build it.

---

## Phase 1 — Intake & Qualification

### Step 1.1: Identify and parse the input
Accept any of the following without asking the user to reformat:

- **Free-text brief or scope**: extract roles, activities, durations, rates, and volumes
- **Bullet points or rough notes**: treat as input signals and resolve gaps before modelling
- **Existing spreadsheet**: read the data, preserve its structure, and map it to the required model sections

### Step 1.2: Assess completeness
Before building anything, scan the input for these elements. Flag anything absent as a gap:

| Required Element | Examples |
|---|---|
| Scope / deliverables | "Build a mobile app", "3-month engagement" |
| Roles or resource types | "2 senior devs", "1 BA", "cloud infrastructure" |
| Duration or volumes | "12 weeks", "500 units", "per month" |
| Rate or cost data | Hourly rates, unit costs, licence fees |
| Timeline | Start date, milestones, or project phases |

If gaps exist, list them explicitly and ask the user to fill them in one consolidated message before proceeding. If a value cannot be confirmed, use a clearly labelled placeholder (`TBD`) and highlight that cell yellow in the final model.

**Include an Assumptions tab only if data gaps were identified and filled with estimates.**

### Step 1.3: Confirm the model type
If the user has not specified a model type, present these four options and ask them to select one before proceeding:

| Model Type | Use When |
|---|---|
| **Schedule of Rates** | Costing by role, hours, and rate — typical for professional services or fixed-scope work |
| **Cash Flow Model** | Timing of spend matters — monthly burn, payment milestones, or phased investment |
| **Total Cost of Ownership (TCO)** | Evaluating a product or service over its full life: acquisition, operation, and disposal |
| **Should-Cost Model** | Bottom-up build to determine what something *should* cost — often to validate or challenge a supplier quote |

Do not proceed to Phase 2 until the model type is confirmed.

---

## Phase 2 — Workbook Construction

### Step 2.1: Tab structure and order
Create the workbook with tabs in this sequence:

1. **Summary** — Executive summary (always present)
2. **[Model Tab]** — Named to match the selected model type
3. **Other Direct Costs**
4. **Contingency & Risk**
5. **Assumptions** — Only if estimates were used to fill data gaps

### Step 2.2: Build each section

#### Summary Tab
| Row Label | Content |
|---|---|
| Total Project Budget | Hardcoded input (blue text) — the approved or target budget if known; `TBD` if not |
| Total Estimated Cost | Formula summing all cost tabs |
| Planned Margin / Profitability | Formula: `=(Budget − Cost) / Budget` |
| Key Cost Drivers | Top 3–5 line items by value, pulled via formula from the model tab |

#### Model Tab — by type

**Schedule of Rates**
Columns: `Role | Level/Grade | Hours | Rate ($/hr) | Total Cost`
- One row per role or resource type; group by workstream or phase if the project is phased
- `Total Cost = Hours × Rate`; grand total via `SUM()`

**Cash Flow Model**
Columns: `Cost Category | Month 1 | Month 2 | … | Month N | Total`
- One row per cost category; column count driven by project duration
- Row totals and column totals via `SUM()`

**Total Cost of Ownership (TCO)**
Columns: `Cost Category | Year 1 | Year 2 | … | Year N | Total`
Row groups: Acquisition → Operation → Maintenance → Disposal
- Subtotal per group; grand total at base of sheet

**Should-Cost Model**
Row groups: Materials → Labour → Overhead → Profit Margin
- Line items within each group; subtotal per group; grand total at base
- If the user provides a reference or supplier price, add a Variance row: `= Grand Total − Reference Price`

#### Other Direct Costs Tab
Columns: `Cost Item | Description | Quantity | Unit Cost | Total`
Prompt the user if they haven't listed these; common examples: sub-contractor fees, software licences, travel, training, hardware procurement.
- `Total = Quantity × Unit Cost`; grand total via `SUM()`
- Link grand total to the Summary tab via cross-sheet formula (green text)

#### Contingency & Risk Tab
Columns: `Risk Item | Likelihood | Impact | Cost Estimate | Contingency %`
- Base contingency row: `= Total Modelled Cost × Contingency %`
- Default contingency: **10%** (blue text — user-editable input cell)
- Add named rows for any specific risks the user identifies
- Link total contingency to the Summary tab (green text)

#### Assumptions Tab (conditional — only if estimates were used)
Columns: `Item | Assumed Value | Rationale | Source`
- Highlight the corresponding input cell yellow on its source tab
- Each row cross-references the cell it feeds (e.g., `Schedule of Rates!D4`)

---

## Phase 3 — Formatting Standards

Apply the following from the **xlsx skill** without exception:

- **Font**: Arial throughout
- **Colour coding**: Blue text = hardcoded inputs · Black = formulas · Green = cross-sheet links
- **Currency**: `$#,##0` format; specify units in column headers (e.g., `Rate ($/hr)`)
- **Percentages**: `0.0%` format
- **Zeros**: Display as `-` using format `$#,##0;($#,##0);-`
- **Negatives**: Parentheses `(123)`, never a minus sign
- **Formula errors**: Verify all formula cells return valid values — check for #VALUE!, #REF!, or #DIV/0! errors and resolve before delivering

Tab colour convention:
- Summary: dark blue
- Model tab: mid blue
- Other Direct Costs, Contingency & Risk: light blue
- Assumptions (if present): yellow

---

## Phase 4 — Delivery

1. Save as `cost-model-[project-name]-[YYYY-MM-DD].xlsx`
2. Verify all formula cells return valid values — check for #VALUE!, #REF!, or #DIV/0! errors before presenting
3. Deliver via `present_files`
4. Follow with a 3–4 sentence plain-language summary: total estimated cost, largest cost driver, contingency amount, and any unresolved data gaps

Do not walk the user through every tab after delivery. Offer to re-run for alternative scenarios or adjust assumptions on request.