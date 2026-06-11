---
name: translation
description: Translate technical documents, plans, designs, or meeting notes into clear language tailored to a specific stakeholder audience — without changing the content, facts, goals, or components. Use this skill whenever the user wants to make technical information accessible to a non-technical audience, needs to communicate a plan or design to business stakeholders, mentions "translation" or "translate this for", wants to explain a technical decision to leadership or customers, or needs to connect technical work to business goals and the "why". This Skill operates on existing source material — for drafting new communications where no source document exists, use communicator.
metadata:
  author: The Instillery
  version: "1.0.0"
---

# Translation Skill

Translate technical content into audience-appropriate language. The substance — facts, goals, components, risks, timelines — must be preserved exactly. Only the vocabulary, framing, and examples change.

---

## Phase 1: Qualify Before Writing

Before producing any output, gather the following. If the user has already provided answers, skip those questions.

### 1.1 — Identify the Input
Confirm what the source material is:
- Document (paste or upload)
- Free text / notes
- Meeting transcript or summary

If unclear, ask: *"What's the source — a document, rough notes, or something else?"*

### 1.2 — Identify the Target Audience

Ask: *"Who is this for?"*

Prompt with examples if needed:
- **Executive / Board** — outcomes, risk, cost, strategic fit
- **Business Stakeholder / Product Owner** — impact on goals, timelines, decisions needed
- **Customer / End User** — what it means for them, what they need to do
- **Operations / Support** — what changes, how it affects their work
- **Finance** — cost drivers, ROI, budget implications
- **Legal / Compliance** — obligations, risk exposure, process changes

If the user names an audience not listed above, accept it and infer the appropriate framing.

### 1.3 — Identify Geographic and Operating Context

The translation must reflect the real-world conditions of each audience, not generic assumptions. Geography matters because economic climate, regulatory environment, and industry pressures differ.

**Step 1 — Determine organisation type:**
- **NZ-owned organisation** → Executive and board-level comms must be grounded in the current NZ economic climate and relevant industry news. Search for this if not already known.
- **Multi-geography organisation** → Each audience's translation must reflect their specific operating context. An exec in Auckland faces different pressures than a finance lead in Sydney or an ops team serving Australian customers.
- **Unclear** → Ask: *"Is this organisation NZ-based, or do they operate across multiple geographies? And where are the specific people I'm writing for based?"*

**Step 2 — Determine audience-level geography:**
Even within one organisation, audiences may be in different locations with different operating constraints. Establish where each audience is based before translating for them.

**Step 3 — Research if needed:**
If the geographic context or relevant industry conditions are not provided or obvious, search online for:
- Current economic conditions in the relevant market (e.g. NZ GDP outlook, interest rate environment, sector-specific headwinds)
- Recent industry news relevant to the organisation's sector and the audience's geography
- Any regulatory or compliance changes relevant to the audience's location

Apply this context in the "Why this matters" section of the output — connect the content to what is actually happening in that audience's world, not a generic version of it.

Add `[CONTEXT SOURCED]` flag with the source and date when external research has been applied.

### 1.4 — Identify the Business Drivers (the "Why")

The translation must connect the content to what the audience cares about. Confirm or establish the relevant drivers.

Common drivers by audience:

| Audience | Typical Drivers |
|---|---|
| Executive | Revenue, risk reduction, competitive position, regulatory compliance |
| Business stakeholder | Delivery speed, customer satisfaction, operational efficiency |
| Customer | Ease of use, reliability, cost, time saved |
| Operations | Process clarity, reduced errors, support burden |
| Finance | Cost control, ROI, budget adherence |

Ask (or infer if obvious): *"What does this audience need to achieve or avoid? Or should I infer from the audience type?"*

### 1.5 — Confirm Scope

Ask (or infer if obvious):
- Is there a specific section to prioritise, or translate the whole thing?
- Is there a preferred length — executive summary vs. full translation?
- Are there terms that must be kept (product names, regulatory terms)?

---

## Phase 2: Translate

### 2.1 — Rules (Non-Negotiable)

- **Preserve all substance.** Facts, numbers, timelines, risks, components, decisions, and goals must not be altered, removed, or softened.
- **Change only language.** Vocabulary, sentence structure, technical jargon, and framing adapt to the audience. The message does not.
- **Do not add opinions.** Do not editorialize, validate, or critique the content. Translate it.
- **Do not omit inconvenient content.** If something is a risk, a gap, or a failure — it stays. Reframe the language, not the reality.
- **Resolve ambiguity explicitly.** If the source material is unclear, flag it as [UNCLEAR — original states: "..."] rather than interpreting it.

### 2.2 — Translation Method

Work through the source material systematically:

1. **Identify the core message** of each section or block of content.
2. **Map technical terms** to audience-appropriate equivalents. Use the audience's vocabulary — not the author's.
3. **Reframe around drivers.** Connect each point to what the audience cares about. Lead with impact, follow with explanation.
4. **Simplify structure.** Group related points. Remove redundancy. Use active voice.
5. **Preserve specifics.** Metrics, dates, names, and figures are kept exactly. They are not rounded, generalised, or replaced with qualitative language.

### 2.3 — Flagging

Use these inline markers where needed:
- `[UNCLEAR]` — source material is ambiguous; original text quoted
- `[ASSUMED]` — an inference was made; state the assumption
- `[TERM KEPT]` — a technical term was retained because no suitable equivalent exists
- `[CONTEXT SOURCED — {source}, {date}]` — geographic or industry context was sourced externally and applied to framing

---

## Phase 3: Output Format

### Default Structure

```
## [Document / Section Title] — For: [Audience]

**Why this matters:** [1–2 sentences connecting content to audience drivers]

**What it says:**
[Translated body — adapted language, preserved substance]

**What it means for you:**
[Practical implication for this audience — decisions needed, actions, risks]

**Flags:**
[Any UNCLEAR, ASSUMED, or TERM KEPT items — or "None"]
```

### Format Variants

Adapt format if the user specifies:
- **Executive summary only** → Single page, 3–5 bullet points per section, lead with outcomes
- **Full translation** → Use the default structure above per section
- **Side-by-side** → Original text | Translated text in two columns (use a table)
- **Email / message** → Conversational format, no headers, appropriate sign-off

If no format is specified, use the default structure.

---

## Phase 4: Quality Check

Before delivering output, verify:

- [ ] All facts from the source are present in the translation
- [ ] No technical jargon remains that the target audience would not understand
- [ ] Business drivers are explicitly connected in the "Why this matters" section
- [ ] Geographic and economic context has been applied at the audience level, not generically
- [ ] Any externally sourced context is flagged with source and date
- [ ] Flags are included for any ambiguity or inference
- [ ] Nothing has been added that was not in the source or sourced context

If the content covers multiple stakeholder groups, offer to produce separate translations for each.