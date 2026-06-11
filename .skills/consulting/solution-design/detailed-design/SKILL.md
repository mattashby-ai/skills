---
name: detailed-design
description: Creates professional Detailed Design (DD) documents for The Instillery, a New Zealand IT consultancy. Accepts meeting notes, transcripts, bullet points, or detailed briefs as input. Use when creating a Detailed Design document for an approved solution, typically after an HLD has been accepted. For high-level architecture overviews before detailed scoping, use high-level-design instead. Requires the docx and pdf pre-built skills to be enabled in the project for Word and PDF output.
metadata:
  author: The Instillery
  version: "1.0.0"
---

# Detailed Design Writer — The Instillery

Produces Detailed Design documents for The Instillery's professional services engagements.
Documents are written in The Instillery's voice, structured to a defined DD template,
and formatted according to brand guidelines.

> **Required Skills:** This Skill delegates Word (.docx) output to the `docx` pre-built skill and PDF output to the `pdf` pre-built skill. Enable both in your Claude project settings (Anthropic platform skill library). Without them, this Skill produces Markdown output only.

---

## About The Instillery

**The Instillery** is a 100% Kiwi-owned technology consultancy and Managed Service Provider
operating across New Zealand and Australia. They are NZ's highest-level Azure partner and
have completed more cloud migrations in NZ than any other provider.

**Always refer to the company as "The Instillery"** — never abbreviate to TI or TIG.
Refer to the company collectively using "we", "us", and "our".

**Core service pillars:**
- **Cloud** — Strategy, Landing Zones, Migration, App Modernisation, Data Platforms
- **Modern Work** — M365 Discovery, Migration, Management, Endpoint, Collaboration, AI, Automation
- **Data** — Data Mapping, Data Lineage, Data Classification
- **Security** — SOC/SIEM, Vulnerability Management, Zero Trust, Identity & PAM, Threat Emulation
- **Connectivity** — SD-WAN, Network-as-a-Service, Megaport, Transit VPC/VNET
- **Managed Services** — 24x7 Support, Managed IT, Cloud Care, Data Care, Server & Desktop Care

**Service delivery model (Professional Services):**
- **Security** — Platform design and implementation
- **Optimisation** — Configuration alignment with best practices  
- **Governance** — Technology planning and policy development

**Credentials:** All-of-Government panel registration, Azure CSP status, 270+ individual certifications.

**Target customers:**
- **Medium Business** (50–250 employees, $1–50m revenue): "Just do it all for me"
- **Corporate — No internal capability** (250–2,000 employees): "Be my internal IT team"
- **Corporate — With internal capability** (250–2,000 employees): "Give me the experts"
- **Enterprise** (2,000+ employees): "Complex whales" — respond to RFPs selectively

---

## Tone of Voice

Write in The Instillery's brand voice: **truth-teller, straight-up, sharp, challenging and smart.**

In practice for a DD document, this means:
- Clear, confident, and direct — no hedging or filler
- Technically credible but accessible — avoid jargon without explanation
- Outcome-focused — tie technical decisions back to business value
- Collaborative and assured — "we recommend" not "it is suggested"
- No marketing waffle — every sentence earns its place

DD documents are professional client-facing deliverables. The tone should be polished
and authoritative while still feeling distinctly Instillery — not generic consultancy-speak.

---

## Brand Formatting

### Colours
| Name       | Hex       | Use                                      |
|------------|-----------|------------------------------------------|
| Carbon     | `#0B0B0C` | Body text, H2, H3                        |
| Copper     | `#AD6A40` | H1, H4, table headers (text), accents    |
| White Gold | `#F0EDE7` | Backgrounds, page breaks                 |
| Steel      | `#7D9695` | Secondary accents                        |
| Verdigris  | `#5DBBA2` | Status indicators (green/positive)       |
| Rose Gold  | `#F8976C` | Status indicators (amber/caution)        |

### Typography (Word Documents)
| Style       | Font                  | Size | Colour    |
|-------------|-----------------------|------|-----------|
| Title       | Bebas Neue            | 36pt | `#AD6A40` |
| Subtitle    | Bebas Neue            | 28pt | `#0B0B0C` |
| Heading 1   | DM Sans Medium        | 20pt | `#AD6A40` |
| Heading 2   | DM Sans Medium        | 18pt | `#0B0B0C` |
| Heading 3   | DM Sans Medium        | 14pt | `#0B0B0C` |
| Heading 4   | DM Sans Medium        | 12pt | `#AD6A40` |
| Body        | DM Sans Regular       | 11pt | `#0B0B0C` |
| Pull Quote  | PT Serif Italic       | 12pt | `#0B0B0C` |
| Table Header| DM Sans               | 10pt | `#FFFFFF`  |
| Table Body  | DM Sans               | 10pt | `#0B0B0C` |

### Traffic Light System
Use for status and risk ratings:
- 🟢 **Green** — Good / Low risk / On track
- 🟡 **Amber** — Caution / Medium risk / Needs attention
- 🔴 **Red** — Critical / High risk / Action required

---

## DD Document Structure

Every DD produced by this skill follows this structure:

### 1. Cover Page
- Document title (solution name + "Detailed Design")
- Customer name
- Prepared by: The Instillery
- Version and date
- Document status (Draft / Final)

### 2. Document Control
Table containing:
- Version history (version, date, author, changes)
- Distribution list
- Document status

### 3. Executive Summary
2–4 paragraphs covering:
- Why this document exists (the business problem or opportunity)
- What The Instillery is proposing at a high level
- The key outcomes the customer should expect
- Any critical dependencies or decisions made

Write for a non-technical executive audience. No acronyms without expansion on first use.

### 4. Current State (As-Is)
Describe the customer's existing environment relevant to this engagement:
- Key systems, platforms, and infrastructure in scope
- Identified pain points, risks, or limitations
- Any constraints that have shaped the proposed design

If current state information is limited in the input, note what assumptions have been made
and flag these in the Risks & Assumptions section.

### 5. Proposed Solution (To-Be)
The core of the document. Cover:
- Solution overview — what is being built or implemented
- Key design decisions and rationale
- Component breakdown (services, products, integrations)
- How the solution addresses the current state issues
- Alignment to The Instillery's service pillars where relevant

Use Heading 2 for major components and Heading 3 for sub-components.

### 6. Architecture Diagram
Generate a Mermaid diagram representing the proposed solution architecture.

Use appropriate diagram types:
- `flowchart TD` or `LR` for system/data flows
- `graph` for component relationships
- `sequenceDiagram` for process flows

Label all components clearly. Group related components using subgraphs where helpful.
Include a brief description above the diagram explaining what it shows.

### 7. Risks & Assumptions
Present as a table with columns: ID | Risk/Assumption | Type | Rating | Mitigation/Note

**Type:** Risk or Assumption
**Rating (for risks):** 🔴 High / 🟡 Medium / 🟢 Low

Include at minimum:
- Any assumptions made due to gaps in the input
- Dependencies on customer actions or third parties
- Common risks for this type of engagement

### 8. Next Steps & Recommendations
Numbered list of concrete next steps, typically 3–7 items. Each should:
- Be actionable and clearly owned (customer or The Instillery)
- Have a suggested timeframe where appropriate
- Build logically toward implementation

---

## Input Handling

The skill should handle a wide range of input quality:

| Input type              | Approach |
|-------------------------|----------|
| Full brief / intake     | Generate complete DD with high confidence |
| Meeting notes / transcript | Extract key facts, flag gaps as assumptions or add a recommendation based on supplied knowledge about the customer |
| Bullet points only      | Expand each point, make reasonable inferences, flag assumptions |
| Thin input              | Generate DD structure with clearly marked placeholders, note where customer decisions are needed, always provide a recommendation from The Instillery |

**When making inferences**, always:
1. Base them on The Instillery's known service pillars and typical engagement patterns
2. Flag them explicitly in the Risks & Assumptions section
3. Use language like "The Instillery understands that..." or "Based on the information provided..."

**Never fabricate specific technical details** (IP addresses, server names, exact user counts)
unless provided in the input.

---

## Output Formats

Produce output in the formats requested. Default is all three unless specified:

### Word (.docx)
Use the `docx` skill. Apply The Instillery brand styles as defined above.
Include a professional cover page. Apply table formatting with Copper header rows.

### PDF
Convert from the Word document using the `pdf` skill, or generate directly.

### Markdown
Clean, well-structured Markdown suitable for internal review or pasting into Confluence/Notion.
Use ATX headings (`#`, `##`, `###`). Include the Mermaid diagram in a fenced code block.

---

## Process

1. **Read the input** — identify the customer, the solution, and the engagement context
2. **Identify gaps** — note what's missing that would typically appear in a DD
3. **Draft each section** — follow the structure above; be specific where possible, flag assumptions where not
4. **Generate the architecture diagram** — use Mermaid; keep it clear and accurate to the described solution
5. **Review risks and assumptions** — ensure all inferences and dependencies are captured
6. **Produce output** — generate in requested format(s); apply brand formatting for docx/PDF
7. **Surface gaps to the user** — after producing the document, summarise what decisions need to be made to finalise the document

---

## Example Trigger Phrases

This skill should activate when a user says things like:
- "Create a DD for [customer] covering [topic]"
- "Here are my meeting notes from [customer] — turn these into a DD"
- "Draft a detailed design for this Azure Landing Zone"
- "I've got bullet points from a discovery call, can you supplement the existing high level design with these to create a DD?"
