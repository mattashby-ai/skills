# Skills

A collection of portable, tool-agnostic skills for MSP (Managed Service Provider) teams. Skills follow the open [Agent Skills specification](https://agentskills.io/specification) and work across multiple AI agent platforms: Claude Code, Cursor, Antigravity, and others.

## What are Skills?

Skills are instruction manuals that agents read before executing tasks. They enable the "read the manual first" approach — rather than guessing, an agent consults the relevant `SKILL.md` file to follow a consistent, repeatable process. This is designed for **agents** (tools that can complete tasks and retain context), not simple chat interfaces.

## Repository Structure

```
skills/
├── .skills/                  # Skill library (4 categories, 35+ skills)
│   ├── consulting/           # Customer-facing skills
│   ├── engineering/          # Project delivery skills
│   ├── manager/              # Team leadership skills
│   └── sales/                # Sales and proposal skills
└── skills-index.json         # Top-level index of all skills
```

## Skill Categories

### Consulting
Customer-facing skills for solution development. Skills often chain together (e.g. Customer Meeting → Solution Design → Cost Modelling).

| Skill | Description | Directory |
|---|---|---|
| Commercial Review | Evaluates contracts for scope, liability, IP, and payment risk. | `.skills/consulting/commercial-review/` |
| Cost Modelling | Translates project variables into structured financial estimates and budgets. | `.skills/consulting/cost-modelling/` |
| Customer Meeting | Extracts requirements and decisions from meeting transcripts for downstream use. | `.skills/consulting/customer-meeting/` |
| Define Requirements | Clarifies vague problem statements before solution design begins. | `.skills/consulting/define-requirements/` |
| Discovery Workshop | Plans and facilitates structured workshops to surface requirements from stakeholders. | `.skills/consulting/discovery-workshop/` |
| High Level Solution Estimate | Produces a rough order of magnitude estimate to qualify early-stage opportunities. | `.skills/consulting/hlse/` |
| Pattern Maker | Codifies repeatable delivery approaches and frameworks from successful engagements. | `.skills/consulting/pattern-maker/` |
| Process Map | Creates BPMN process maps and written narratives from user-described workflows. | `.skills/consulting/process-map/` |
| Research | Provides technical depth on vendor solutions to inform consultant designs. | `.skills/consulting/research/` |
| Solution Design (Detailed) | Creates implementation-ready detailed design documents with full technical configuration. | `.skills/consulting/solution-design/detailed-design/` |
| Solution Design (High Level) | Creates high-level architecture design documents for early engagement stages. | `.skills/consulting/solution-design/high-level-design/` |
| Sounding Board | Stress-tests plans and designs through relentless structured questioning. | `.skills/consulting/sounding-board/` |
| SOW Quality Check | First-pass structural completeness review of a Statement of Work. | `.skills/consulting/sow-quality-check/` |
| Technical Review | Validates technical designs for feasibility, best practices, and partner alignment. | `.skills/consulting/technical-review/` |
| Translation | Rewrites technical content for non-technical stakeholder audiences. | `.skills/consulting/translation/` |

### Engineering
Project delivery lifecycle from planning through execution.

| Skill | Description | Directory |
|---|---|---|
| Change Request | Drafts formal change request documents from a standard template. | `.skills/engineering/change-request/` |
| Dependency Mapper | Maps task dependencies and sequencing for import into project tools. | `.skills/engineering/dependency-mapper/` |
| MS Graph API | Searches 27,700+ Microsoft Graph API endpoints and schemas locally. | `.skills/engineering/msgraph/` |
| Project Closure | Formally closes projects with sign-off, lessons learned, and archiving. | `.skills/engineering/project-closure/` |
| Project Meetings | Drafts focused agendas and talking points for project meetings. | `.skills/engineering/project-meetings/` |
| Project Planner | Orchestrates a complete project plan using risk, commercial, and dependency agents. | `.skills/engineering/project-planner/` |
| Risk Planner | Identifies, assesses, and mitigates risks threatening project delivery. | `.skills/engineering/risk-planner/` |
| Status Update | Drafts concise stakeholder status updates rated green, amber, or red. | `.skills/engineering/status-update/` |
| Success Criteria | Generates verifiable acceptance criteria and test cases for deliverables. | `.skills/engineering/success-criteria/` |

### Manager
Team leadership, resource allocation, financial planning, and client relationship management.

| Skill | Description | Directory |
|---|---|---|
| Client Success | Reviews account health and surfaces at-risk customers before they escalate. | `.skills/manager/client-success/` |
| Communicator | Drafts standalone business communications — announcements, blogs, and emails. | `.skills/manager/communicator/` |
| Customer Researcher | Researches companies and stakeholders from external sources before engagements. | `.skills/manager/customer-researcher/` |
| Financial Forecast | Prepares revenue forecasts and explains actuals versus forecast variances. | `.skills/manager/financial-forecast/` |
| Practice Governance | Produces monthly or quarterly practice health reports for leadership. | `.skills/manager/practice-governance/` |
| Product Creator | Defines new service offerings with value propositions, scope, and pricing. | `.skills/manager/product-creator/` |
| PS Coach | Mentors delivery engineers through 1:1s, growth plans, and skills reviews. | `.skills/manager/ps-coach/` |
| Resource Planner | Allocates team capacity across engagements based on skills and workload. | `.skills/manager/resource-planner/` |

### Sales
Sales pipeline, proposals, and partner engagement.

| Skill | Description | Directory |
|---|---|---|
| Account Planning | Develops strategic growth plans for existing customer accounts. | `.skills/sales/account-planning/` |
| Opportunity Qualification | Determines whether to pursue or walk away from a sales opportunity. | `.skills/sales/opportunity-qualification/` |
| Partner Engagement | Leverages Microsoft, AWS, Google, and other partner programmes for deals. | `.skills/sales/partner-engagement/` |
| Proposal | Writes compelling commercial proposals to formalise a solution approach. | `.skills/sales/proposal/` |
| RFP Response | Structures responses to formal RFPs, RFQs, and government tenders. | `.skills/sales/rfp-response/` |

## Skill File Organisation

Each skill lives in its own directory:

```
.skills/[category]/[skill-name]/
├── SKILL.md          # The skill definition (required)
└── references/       # Supporting files (rate cards, templates, checklists)
```

- Directory names use kebab-case (e.g. `cost-modelling`, `resource-planner`)
- Reference files go in `references/` within the skill directory
- Supporting scripts go in `scripts/` within the skill directory

## Content Standards

Each skill follows the Agent Skills specification format and includes:

- Step-by-step guidance for consistent outputs
- Common pitfalls to avoid
- Formatting standards and tool-specific techniques

## Skill Philosophy

1. **Systematic over ad-hoc** — Process over guessing
2. **Complexity reduction** — Simplicity as primary goal
3. **Evidence over claims** — Verify before declaring success

## Contributing

Skills are meant to be iteratively improved through team collaboration:

- Capture institutional knowledge that can be reused
- Focus on consistency and repeatability
- Update skills based on lessons learned from real-world usage
- Consider how skills interact when used together in orchestration workflows
