# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository is a collection of portable, tool-agnostic skills designed for MSP (Managed Service Provider) teams. The skills follow the open Agent Skills specification (https://agentskills.io/specification) and are designed to work across multiple AI agent platforms: Claude Code, Cursor, Antigravity, and others.

## Repository Structure

```
skills/
├── .skills/                  # Skill library (4 categories, 35+ skills)
│   ├── consulting/           # Customer-facing skills
│   ├── engineering/          # Project delivery skills
│   ├── manager/              # Team leadership skills
│   └── sales/                # Sales and proposal skills
└── skills-index.json               # Top-level index of all skills
```

## Skill Categories

### Consulting (`.skills/consulting/`)
Customer-facing skills for solution development. Skills often chain together (e.g. Customer Meeting → Solution Design → Cost Modelling).

| Skill | Directory |
|---|---|
| Commercial Review | `commercial-review/` |
| Cost Modelling | `cost-modelling/` |
| Customer Meeting | `customer-meeting/` |
| Define Requirements | `define-requirements/` |
| Discovery Workshop | `discovery-workshop/` |
| High Level Solution Estimate | `hlse/` |
| Pattern Maker | `pattern-maker/` |
| Process Map | `process-map/` |
| Research | `research/` |
| Solution Design (Detailed) | `solution-design/detailed-design/` |
| Solution Design (High Level) | `solution-design/high-level-design/` |
| Sounding Board | `sounding-board/` |
| SOW Quality Check | `sow-quality-check/` |
| Technical Review | `technical-review/` |
| Translation | `translation/` |

### Engineering (`.skills/engineering/`)
Project delivery lifecycle from planning through execution.

| Skill | Directory |
|---|---|
| Change Request | `change-request/` |
| Dependency Mapper | `dependency-mapper/` |
| MS Graph API | `msgraph/` |
| Project Closure | `project-closure/` |
| Project Meetings | `project-meetings/` |
| Project Planner | `project-planner/` |
| Risk Planner | `risk-planner/` |
| Status Update | `status-update/` |
| Success Criteria | `success-criteria/` |

### Manager (`.skills/manager/`)
Team leadership, resource allocation, financial planning, and client relationship management.

| Skill | Directory |
|---|---|
| Client Success | `client-success/` |
| Communicator | `communicator/` |
| Customer Researcher | `customer-researcher/` |
| Financial Forecast | `financial-forecast/` |
| Practice Governance | `practice-governance/` |
| Product Creator | `product-creator/` |
| PS Coach | `ps-coach/` |
| Resource Planner | `resource-planner/` |

### Sales (`.skills/sales/`)
Sales pipeline, proposals, and partner engagement.

| Skill | Directory |
|---|---|
| Account Planning | `account-planning/` |
| Opportunity Qualification | `opportunity-qualification/` |
| Partner Engagement | `partner-engagement/` |
| Proposal | `proposal/` |
| RFP Response | `rfp-response/` |

## Skill File Organization

- Each skill lives in its own directory: `.skills/[Category]/[Skill Name]/SKILL.md`
- Use kebab-case for directory names (e.g. `cost-modelling`, `resource-planner`)
- Reference files (rate cards, templates, checklists) go in `references/` within the skill directory
- Supporting scripts go in `scripts/` within the skill directory

## Content Standards

- All skills follow the Agent Skills specification format
- Include step-by-step guidance for consistent outputs
- Document common pitfalls to avoid
- Specify formatting standards and tool-specific techniques
- Structure content as instruction manuals that agents read before starting tasks

## Key Concepts

### Agent vs Chat Pattern
This project is designed for **agents** (tools that can complete tasks and retain context) rather than simple chat interfaces. Skills enable the "read the manual first" approach where agents consult relevant SKILL.md files before executing tasks.

### Skill Philosophy
1. **Test-Driven Development** — Write tests first, always
2. **Systematic over ad-hoc** — Process over guessing
3. **Complexity reduction** — Simplicity as primary goal
4. **Evidence over claims** — Verify before declaring success

### Collaborative Improvement
Skills are meant to be iteratively improved through team collaboration. When working on skills:
- Capture institutional knowledge that can be reused
- Focus on consistency and repeatability
- Update skills based on lessons learned from real-world usage
- Consider how skills interact with orchestration agents that use multiple skills together
