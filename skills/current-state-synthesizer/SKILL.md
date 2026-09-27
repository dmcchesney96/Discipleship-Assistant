---
name: current-state-synthesizer
description: Produce a reliable as-of-now picture from multiple ministry sources while separating current, pending, tentative, historical, and superseded information.
---

# Current State Synthesizer

## Purpose

Answer: **What is actually true now?**

## Inputs

Relevant canonical documents, data, recent decisions, local evidence, and conflicts retrieved by `ministry-context-retriever`.

## Workflow

1. Set an explicit as-of date and scope.
2. Classify each material statement by CURRENT / PENDING / TENTATIVE / HISTORICAL / SUPERSEDED.
3. Resolve conflicts using authority, recency, specificity, and provenance; if unresolved, show both.
4. Separate official intention from actual delivered practice and lived experience.
5. Distinguish confirmed state from interpretation.
6. Identify what changed recently and what is still uncertain.
7. Produce only the level of detail needed for the downstream task.

## Output

- As-of date/scope
- Current state
- Pending/tentative items
- Recent changes
- Historical/superseded context that still matters
- Conflicts/unknowns
- Sources

Do not invent owners, dates, approvals, or implementation status.
