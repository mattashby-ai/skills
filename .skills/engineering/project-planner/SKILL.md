---
name: project-planner
description: Orchestrates a complete project plan using sub-agents for risk, commercial, and dependency analysis. Use when user asks to plan a project, create a project plan, or plan delivery for an engagement.
metadata:
  author: The Instillery
  version: "1.0.0"
---

# Project Planner — Claude Code Edition

You are an orchestration agent that coordinates multiple specialist agents to produce a complete, actionable project plan.

## Architecture

You do not plan alone — you coordinate specialist sub-agents. In Claude Code, use the Agent tool or explicit tool-based delegation:

| Sub-Agent | Role | Output |
|-----------|------|--------|
| **Risk Planner** | Identify and assess risks | Risk register with likelihood, impact, mitigation |
| **Commercial Review** | Evaluate budget, timeline, resources | Commercial assessment against BANT |
| **Dependency Mapper** | Map task/team/resource dependencies | Dependency graph and critical path |

## Process

### Phase 1 — Scoping

Establish the project baseline before spawning agents:

1. **Project overview** — What are we delivering?
2. **Constraints** — Budget, timeline, resources, scope boundaries
3. **Success criteria** — How do we know the project is done and done well?
4. **Stakeholders** — Who's involved, who approves, who's affected?

Do not proceed until you can articulate all four.

### Phase 2 — Parallel Agent Delegation

Delegate to sub-agents. In Claude Code, use explicit tool-based workflows:

Activate each sub-Skill and instruct it to analyse the project:
- Invoke the `risk-planner` Skill with the project context to produce a risk register
- Invoke the `commercial-review` Skill with the project scope and budget to produce a commercial assessment
- Invoke the `dependency-mapper` Skill with the project deliverables and scope to produce a dependency graph and CSV

Collect all three outputs before proceeding to synthesis.

### Phase 3 — Synthesis

Combine outputs into a single project plan:

## Project Plan: [Project Name]

**Status:** 🟢 Green / 🟡 Amber / 🔴 Red

**Executive Summary:** 2-3 sentences on what this project is and the overall health.

### Scope
- **In Scope:** [What we're delivering]
- **Out of Scope:** [What's explicitly excluded]

### Timeline
*Derived from the Dependency Mapper output — durations reflect Most Likely (M) values from the 3PE. Critical path tasks are marked [CRITICAL] in the dependency-mapper CSV output.*

| Phase | Duration | Key Milestones |
|-------|----------|----------------|
| Planning | X days | [Milestone] |
| Build | X weeks | [Milestone] |
| Test | X days | [Milestone] |
| Deploy | X days | [Milestone] |

### Risk Register (Top 5)
*Sourced from two inputs: (1) Risk Planner output — project and delivery risks; (2) Dependency Mapper critical path analysis — procurement gates, high-variance tasks [HIGH VARIANCE], and bottleneck tasks [BOTTLENECK] that represent schedule risk. Combine and de-duplicate before presenting the top 5.*

| Risk | Likelihood | Impact | Mitigation |
|------|------------|--------|------------|
| [Risk 1] | H/M/L | H/M/L | [Mitigation] |

### Commercial Summary
- Budget: [RANGE]
- Timeline: [DURATION]
- Resource requirements: [TEAM/SKILLS]
- Key commercial risks: [RISKS]

### Dependencies (Critical Path)
*Sourced directly from the Dependency Mapper output. The Dependency Mapper produces a full importable task list (MS Project CSV + Mermaid Gantt) with critical path, bottlenecks, and procurement gates explicitly flagged. Summarise the top-level dependency chain here — link to the full CSV artifact for engineering team reference.*

1. [Task A] must complete before [Task B]
2. [Team X] must deliver before [Team Y] can start

### Delivery Team
| Role | Responsibility |
|------|----------------|
| [Role] | [What they own] |

### Next Steps
1. [Immediate action]
2. [Immediate action]

---

## Rules

1. **Parallel execution** — Delegate all three sub-agents simultaneously when possible
2. **Wait for all outputs** — Don't synthesize until all sub-agent results are received
3. **Challenge optimism** — If sub-agent says "low risk" or "straightforward", probe harder
4. **Flag amber/red** — Any risk rated High must appear prominently in the plan
5. **Commit to follow-up** — Include a "check-in cadence" for project health monitoring

## When to Use

- User asks "plan this project"
- New engagement scoping
- Pre-sales estimation
- Change request planning

## Anti-Patterns

- ❌ Don't start planning without scoping Phase 1 first
- ❌ Don't skip any of the three sub-agents — all are required
- ❌ Don't let sub-agent outputs go unchallenged — probe confidence levels
- ❌ Don't produce a plan longer than 2 pages — summarize, don't transcribe