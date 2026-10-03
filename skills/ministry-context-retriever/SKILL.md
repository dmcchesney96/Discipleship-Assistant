---
name: ministry-context-retriever
description: Retrieve the smallest sufficient set of current, authoritative project context for a ministry/research question without flooding the task with irrelevant history.
---

# Ministry Context Retriever

## Purpose

Get the right evidence before reasoning. This skill reduces hallucination, stale assumptions, and unnecessary broad searches.

## Process

1. Restate the operational/research question and identify the missing context categories.
2. Search the canonical Drive Brain first for project-specific state.
3. When the task is substantial design/creation and Dan's stored ministry philosophy could materially change the output, retrieve the smallest relevant `USER ALIGNMENT / PASTORAL LENS` through `discipleship-alignment-lens-retriever`. Keep it separate from evidence and approved decisions.
4. Prefer current/approved records; include historical/tentative material only when it affects interpretation.
5. Retrieve source-level evidence, not only summaries, when the decision depends on exact wording/data.
6. Note provenance, date/version, status, and any access/sensitivity constraints.
7. Stop when additional retrieval is unlikely to change the answer materially.

## Priority

Current explicit user instruction → approved current decisions/policies → current canonical docs/data → converging local evidence → historical records → memory/inference.

For external research questions, use the strongest research sources appropriate to the claim rather than treating Drive summaries as automatically verified.

For **practice/design questions**, retrieve the smallest sufficient combination of:
- current Southbrook diagnostic/current state;
- relevant `USER ALIGNMENT / PASTORAL LENS` entries;
- relevant Living Synthesis mechanisms/principles;
- relevant Practice Cards/comparisons;
- active/previous local pilots and learning;
- approved constraints/decisions.

Do not flood a practice decision with unrelated research merely because it exists.

## Output

- Question/scope
- Sources retrieved
- Current authoritative context
- Relevant historical/tentative context
- Conflicts/gaps
- Retrieval sufficiency note

Do not synthesize a full strategy; this is retrieval.
