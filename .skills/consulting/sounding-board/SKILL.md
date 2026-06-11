---
name: sounding-board
description: Interview the user relentlessly about a plan or design until reaching shared understanding, resolving each branch of the decision tree. Use when user wants to stress-test a plan, get grilled on their design or mentions "sounding board".
metadata:
  author: The Instillery
  version: "1.0.0"
---

Interview the user relentlessly about every aspect of their plan until reaching shared understanding. Walk down each branch of the decision tree, resolving dependencies between decisions one-by-one.

If a question can be answered by exploring the codebase or documentation, explore the codebase or documentation instead.

## Completion Criteria

The interview is complete when:
- All major decision branches have been explored and resolved
- The user explicitly confirms they have no remaining uncertainties, or
- A full pass through every identified branch of the decision tree is complete

When complete, move directly to producing the output below — do not ask for permission.

## Output

After the interview is complete, produce a structured summary:

**Plan as understood:**
[2–3 sentence synthesis of the plan]

**Decisions made:**
- [Decision] — [Rationale]

**Open questions and risks:**
- [Unresolved question or identified risk]