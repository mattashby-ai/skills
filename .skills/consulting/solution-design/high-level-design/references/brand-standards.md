# The Instillery — Brand Standards for HLD Documents

## Colours

| Name       | Hex       | Use                                      |
|------------|-----------|------------------------------------------|
| Carbon     | `#0B0B0C` | Body text, H2, H3                        |
| Copper     | `#AD6A40` | H1, H4, table headers (text), accents    |
| White Gold | `#F0EDE7` | Backgrounds, page breaks                 |
| Steel      | `#7D9695` | Secondary accents                        |
| Verdigris  | `#5DBBA2` | Status indicators (green/positive)       |
| Rose Gold  | `#F8976C` | Status indicators (amber/caution)        |

---

## Typography (Word Documents)

| Style        | Font             | Size | Colour    |
|--------------|------------------|------|-----------|
| Title        | Bebas Neue       | 36pt | `#AD6A40` |
| Subtitle     | Bebas Neue       | 28pt | `#0B0B0C` |
| Heading 1    | DM Sans Medium   | 20pt | `#AD6A40` |
| Heading 2    | DM Sans Medium   | 18pt | `#0B0B0C` |
| Heading 3    | DM Sans Medium   | 14pt | `#0B0B0C` |
| Heading 4    | DM Sans Medium   | 12pt | `#AD6A40` |
| Body         | DM Sans Regular  | 11pt | `#0B0B0C` |
| Pull Quote   | PT Serif Italic  | 12pt | `#0B0B0C` |
| Table Header | DM Sans          | 10pt | `#FFFFFF`  |
| Table Body   | DM Sans          | 10pt | `#0B0B0C` |

---

## Traffic Light System

Use for status and risk ratings:
- Green — Good / Low risk / On track
- Amber — Caution / Medium risk / Needs attention
- Red — Critical / High risk / Action required

---

## HLD Document Structure

Every HLD produced by the high-level-design Skill follows this structure:

### 1. Cover Page
- Document title (solution name + "High Level Design")
- Customer name
- Prepared by: The Instillery
- Version and date
- Document status (Draft / Final)

### 2. Executive Summary
2–4 paragraphs covering:
- Business context and the problem or opportunity being addressed
- Proposed solution overview at a conceptual level
- Key outcomes the customer should expect
- Critical dependencies or decisions required

Write for a non-technical executive audience. No acronyms without expansion on first use.

### 3. Current State (As-Is)
- Key systems, platforms, and infrastructure in scope
- Identified pain points, risks, or limitations
- Any constraints that have shaped the proposed approach

### 4. Proposed Solution (To-Be)
The core of the document. Cover:
- Solution overview — what is being recommended and why
- Key design decisions and rationale at a high level
- Major components (services, products, integrations) — no configuration detail at HLD stage
- How the solution addresses the current state issues
- Alignment to The Instillery's service pillars where relevant

### 5. Architecture Diagram
Generate a Mermaid diagram representing the proposed solution architecture.

Use appropriate diagram types:
- `flowchart TD` or `LR` for system/data flows
- `graph` for component relationships
- `sequenceDiagram` for process flows

Label all components clearly. Group related components using subgraphs where helpful.

### 6. Risks & Assumptions
Table with columns: ID | Risk/Assumption | Type | Rating | Mitigation/Note

**Type:** Risk or Assumption
**Rating (for risks):** High / Medium / Low

### 7. Next Steps & Recommendations
Numbered list of 3–7 actionable items, each with a suggested owner (customer or The Instillery) and timeframe. Items should lead logically toward detailed design or procurement.

---

## Company Reference

**Always refer to the company as "The Instillery"** — never abbreviate to TI or TIG.
Refer to the company collectively using "we", "us", and "our".

**Core service pillars:**
- **Cloud** — Strategy, Landing Zones, Migration, App Modernisation, Data Platforms
- **Modern Work** — M365 Discovery, Migration, Management, Endpoint, Collaboration, AI, Automation
- **Data** — Data Mapping, Data Lineage, Data Classification
- **Security** — SOC/SIEM, Vulnerability Management, Zero Trust, Identity & PAM, Threat Emulation
- **Connectivity** — SD-WAN, Network-as-a-Service, Megaport, Transit VPC/VNET
- **Managed Services** — 24x7 Support, Managed IT, Cloud Care, Data Care, Server & Desktop Care
