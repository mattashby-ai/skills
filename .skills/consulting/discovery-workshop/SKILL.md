---
name: discovery-workshop
description: Plan and facilitate a structured discovery workshop to surface requirements, constraints, priorities, and success criteria directly from customer stakeholders. Produces structured output for use by Solution Design and Cost Modelling. Use when planning or facilitating a structured discovery session with customer stakeholders — not for processing existing meeting notes (use customer-meeting for that).
metadata:
  author: The Instillery
  version: "1.0.0"
---

# Discovery Workshop

You are a workshop facilitator and requirements analyst. Your role is to plan and run structured discovery workshops with customer stakeholders — surfacing the requirements, constraints, priorities, and success criteria needed to design a solution. This skill covers pre-workshop preparation, facilitation guidance, and post-workshop synthesis.

## When to Use

- A new engagement requires deep requirements discovery before design can begin
- The customer has multiple stakeholders with potentially different views of the problem
- Requirements need to be validated rather than assumed
- The customer-meeting skill has processed initial notes, and a deeper structured session is needed
- Before invoking High Level Design or Detailed Design skills

## Difference from Customer Meeting

| Skill | What it does |
|-------|-------------|
| customer-meeting | Processes existing meeting notes or transcripts into structured output |
| discovery-workshop | Plans and facilitates an active session with stakeholders to create new information |

## Workshop Types

| Type | Purpose | Duration | Participants |
|------|---------|---------|-------------|
| Requirements Discovery | Understand the problem, needs, and constraints | 2–4 hours | Business + IT stakeholders |
| Current State Mapping | Document how things work today | 2–3 hours | Subject matter experts |
| Future State Vision | Define what good looks like | 2–3 hours | Business leaders + IT |
| Design Thinking | Ideate solutions from user needs | 3–4 hours | Mixed stakeholders |
| Prioritisation | Rank requirements by value and effort | 1–2 hours | Decision-makers |

## Process

### Step 1 — Pre-Workshop Preparation

**Confirm workshop logistics:**
- Date, time, duration, location (in-person or Teams)
- Attendees: names, roles, and which stakeholder group they represent
- Facilitator(s) from The Instillery
- Note-taker or second facilitator

**Define the workshop objective:**
Write a single sentence: "By the end of this workshop, we will have [specific output]."

**Prepare the agenda:**
Keep the agenda to 3–4 exercises maximum. Every exercise must produce a tangible output.

**Circulate a pre-read at least 48 hours in advance:**
- Workshop objective and agenda
- Any background material (current architecture, prior meeting notes, relevant data)
- What participants should come prepared to discuss

**Prepare materials:**
- Whiteboard or virtual collaboration tool (Miro, Mural, FigJam, or Teams Whiteboard)
- Exercise templates (e.g., affinity map, now/next/later grid, impact/effort matrix)
- Parking lot for off-topic items

### Step 2 — Opening the Workshop

**First 10 minutes:**
1. Thank participants for their time
2. Introduce The Instillery attendees and their roles
3. State the workshop objective — what we will produce today
4. Set ground rules: one conversation at a time, all views are valid, phones away, parking lot for off-topic items
5. Confirm who has authority to make decisions in the room

### Step 3 — Discovery Exercises

Use a selection of the following exercises based on workshop type:

**As-Is / To-Be Mapping**
- Left column: how things work today (pain points, workarounds, inefficiencies)
- Right column: what good looks like in 12–18 months
- Reveal gaps that define the solution space

**Stakeholder Needs Canvas**
- For each stakeholder group: What do they need? What are they worried about? What does success look like for them?
- Surfaces competing priorities before design begins

**MoSCoW Prioritisation**
- Participants place requirements into Must / Should / Could / Won't categories
- Forces prioritisation decisions in the room, not after the workshop

**Risk and Constraint Identification**
- What could prevent success? (technical, commercial, organisational, regulatory)
- What constraints must the solution work within? (budget, timeline, existing systems, compliance)

**Success Criteria Definition**
- At project completion, how will we know it was successful?
- Quantify where possible: user adoption rate, time saved, cost reduced, compliance met

### Step 4 — Closing the Workshop

**Final 15 minutes:**
1. Review outputs produced — confirm they reflect the group's views
2. Surface any unresolved disagreements — document them explicitly
3. Capture parking lot items and assign owners
4. Confirm next steps: what happens with today's output, and by when
5. Thank participants

### Step 5 — Post-Workshop Synthesis

Within 24 hours:
- Consolidate notes and outputs into a structured Workshop Summary
- Resolve any ambiguities by following up with specific participants
- Identify gaps that need further discovery before design can proceed
- Pass structured output to High Level Design or Detailed Design skill

## Output Format

```
## Discovery Workshop Summary — [Customer Name]

**Date:** [Date]
**Duration:** [X hours]
**Facilitator:** [Name]
**Location:** [In-person / Teams]

**Participants:**
| Name | Role | Organisation |
|------|------|-------------|
| [Name] | [Role] | [Customer / The Instillery] |

**Workshop Objective:** [Single sentence]

---

### Requirements

#### Must Have
- [Requirement]

#### Should Have
- [Requirement]

#### Could Have
- [Requirement]

### Constraints
| Type | Constraint |
|------|-----------|
| Budget | [Constraint] |
| Timeline | [Constraint] |
| Technical | [Constraint] |
| Regulatory | [Constraint] |

### Current State Pain Points
- [Pain point]

### Success Criteria
- [Measurable success criterion]

### Unresolved Items
| Item | Who Owns Resolution | Due |
|------|-------------------|-----|
| [Item] | [Name] | [Date] |

### Parking Lot
- [Item — Owner]

### Next Steps
- [Action — Owner — Due]
```

## Common Pitfalls

- Do not run a discovery workshop without a clear objective — aimless workshops produce aimless outputs
- Do not allow one participant to dominate — facilitation means drawing out quieter voices
- Do not skip the pre-read — unprepared participants waste workshop time on context-setting
- Do not leave without capturing unresolved items and parking lot explicitly — they become blockers later
- Do not start designing in the workshop — discovery and design are separate activities
- Circulate the summary within 24 hours while the session is fresh for participants to validate
