---
name: customer-researcher
description: Conducts customer research in two modes: (1) Light — a concise context snapshot used to feed the translation skill with customer-specific insight; (2) Dossier — a structured, in-depth profile for project teams that may have no prior exposure to this customer. Light mode is the default. Switch to Dossier mode when the user mentions "dossier", "kickoff", "kick-off pack", "onboarding pack", or wants something the team can read. Use when the user wants to research a specific company or its stakeholders from external sources (web, LinkedIn, CRM) before an engagement. For strategic account growth planning, use account-planning. For technical solution research, use research.
metadata:
  author: The Instillery
  version: "1.0.0"
---

# Customer Researcher

## Mode Detection

Run in **Light mode** by default.  
Switch to **Dossier mode** if the user mentions: *dossier, kickoff, kick-off, onboarding pack, project team, team brief*.  
If intent is ambiguous after reading the request, ask: *"Do you want a quick snapshot or a full dossier the team can read?"*

---

## Phase 1: Intake

Before researching, confirm:
1. **Customer name** (company name, not just a contact)
2. **Known stakeholders** — names and roles if available (ask if not provided)
3. **Project context** — what are we delivering? (Dossier mode only)

If the user hasn't provided these, ask for them in a single message before proceeding. Do not begin research with incomplete intake.

---

## Phase 2: Research Process

### Source Priority (always follow this order)

**1. HubSpot (internal CRM)**
- Check if a HubSpot MCP tool is available in your current session.
- If connected: query for the company record, associated contacts, deal history, notes, and any logged activity.
- If not connected: inform the user — *"HubSpot isn't connected in this session. I'll proceed with public sources. Paste any relevant CRM notes if you have them."* — then continue with Step 2.

**2. Web & LinkedIn (public sources)**
Use web search and LinkedIn to fill gaps left by HubSpot or build the full picture. Research in this order:
- Company website → About, Leadership, News/Press
- LinkedIn company page → size, recent posts, leadership team
- LinkedIn profiles → individual stakeholders (current role, career history, stated priorities, posts)
- News, industry press, analyst coverage → strategy, challenges, market position
- Any publicly available annual reports, case studies, or conference talks

### Research Rules
- Do not invent facts. If a data point cannot be confirmed from a source, mark it `[unconfirmed]` or omit it.
- Do not summarise a source verbatim — synthesise across sources into your own assessment.
- For each stakeholder, the core question is: *what does this person need to be successful in their role?* Answer that explicitly.
- Flag contradictions between sources rather than silently picking one.

---

## Phase 3: Output

### Light Mode Output

Produce a compact context block (300–500 words) structured as:

```
## [Company Name] — Research Snapshot

**Who they are:** [2–3 sentences: industry, size, what they do]

**Current situation:** [Key pressures, initiatives, or priorities relevant to our engagement]

**Key contacts:**
- [Name], [Title] — [One sentence: what drives them / what they care about]
- (repeat per stakeholder)

**Relationship context:** [How long a customer, tone of relationship, anything notable]

**Watch points:** [Risks, sensitivities, or gaps in research]
```

This output is designed to be passed directly into the translation skill as customer context. Keep it factual and specific — not generic.

---

### Dossier Mode Output

Produce a structured markdown document with these sections in order:

---

**# [Company Name] — Customer Dossier**
*Prepared for: [project/team name if known] | Date: [today's date]*

**## 1. Company Overview**
Industry, size (headcount/revenue if findable), ownership structure, geographic footprint, strategic direction, and any recent significant news (acquisitions, restructures, product launches).

**## 2. Relationship History**
How long they've been a customer, key milestones in the relationship, previous projects or engagements, and the overall health/tone of the relationship based on CRM data.

**## 3. Project Context**
What we are delivering for them. Scope summary, timeline if known, and why this engagement exists (what problem are we solving?).

**## 4. Key Stakeholders**
For each stakeholder, one named sub-section:

```
### [Full Name] — [Title]
**What they do:** [Role scope in 1–2 sentences]
**What they care about:** [Their stated or inferred priorities — professional, not personal]
**What success looks like for them:** [Explicit answer — what outcome makes them look good / solves their problem]
**How to work with them:** [Communication style, decision-making role, any known preferences]
**Source:** [Where this came from — LinkedIn, HubSpot, web]
```

**## 5. Pain Points & Challenges**
Current known pressures: operational, strategic, technical, or political. Distinguish between *confirmed* (sourced) and *inferred* (reasoned from context).

**## 6. Risks & Sensitivities**
Anything the team should know before engaging: sensitivities to raise carefully, internal politics to be aware of, reputational or commercial risks, gaps in our research that could bite us.

---

## Output Rules (both modes)

- Write in plain, direct prose. No filler phrases ("It is worth noting that…").
- Use bullet points only inside structured fields (e.g. stakeholder blocks). Sections are prose.
- Clearly distinguish confirmed facts from inferences. Use *"likely"*, *"appears to"*, or `[inferred]` for the latter.
- If a section cannot be completed due to lack of data, say so explicitly — do not pad it with generics.
- End every output with a `**Research gaps:**` line listing what could not be confirmed and why (or state "None identified").