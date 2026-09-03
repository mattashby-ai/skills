# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository is a collection of portable, tool-agnostic skills designed for MSP (Managed Service Provider) teams. The skills follow the open Agent Skills specification (https://agentskills.io/specification) and are designed to work across multiple AI agent platforms: Claude Code, Cursor, Antigravity, and others.

Skills live under `.skills/`, organised into four categories: `consulting/` (customer-facing solution development, often chained e.g. Customer Meeting → Solution Design → Cost Modelling), `engineering/` (project delivery lifecycle), `manager/` (team leadership, resourcing, financial planning), and `sales/` (pipeline, proposals, partners). `skills-index.json` is the top-level index.

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
