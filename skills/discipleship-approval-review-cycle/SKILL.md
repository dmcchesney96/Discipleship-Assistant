---
name: discipleship-approval-review-cycle
description: Orchestrate a selective evidence-to-pitch-to-human-approval-to-record loop from the existing Discipleship Brain. Build shortlist and review board, stop for Dan's item-by-item choices, then on a later turn record selections in a distinct approved design synthesis. No automatic approval.
metadata:
  short-description: Review promising practice ideas and require Dan's choice
---

# Discipleship Approval Review Cycle

## Aim
Turn abundant accumulated research into a manageable **Southbrook design selection pipeline**, not a further content warehouse.

## Sequence
`ministry-context-retriever → discipleship-alignment-lens-retriever → relevant Practice Intelligence + Living Synthesis + Dan-selected library → source verification only where consequential → southbrook-practice-fit-assessor (if enough local evidence; otherwise provisional) → discipleship-practice-approval-pitch-builder → HUMAN DECISION GATE → discipleship-practice-approval-recorder → optional pilot/implementation design → later local learning`.

Use `docs/practice-approval-review-workflow.md` for statuses, source rules and persistence.

## First invocation
- Check whether a review ledger and a Dan-approved Southbrook design synthesis already exist in the Brain; **reuse** rather than duplicating.
- If missing, create separate canonical **Pending Review Queue** and **Dan-Approved Southbrook Design Practices — Living Selection Synthesis** in a coherent Brain folder after verifying destination. The latter begins empty unless Dan has explicitly authorized importing specific earlier selections; cross-link the existing Dan-selected learnings rather than silently reclassifying them.
- Prioritize no more than 3–5 current candidates, preserving source links and the not-yet-verified flags.
- Stop after presenting the review batch. No approval claims.

## Later invocations
- Interpret precise item IDs / description and Dan's choice. Run the decision recorder; verify the ledger and approved synthesis updates.
- When a new relevant report is assessed, offer up to 1–3 new pitches if material, avoiding repeated pitches of already-selected or declined ideas. This is opportunistic on active turns, not an unscheduled background agent.
- If the user asks for all past research to be processed, stage a deduplicated practice backlog with coverage and status, then work through bounded review batches. Do not claim whole-Brain completion from a partial scan.

## Completion
Report pitched count, explicit decisions recorded, latest approved synthesis and queue links, source verification gaps, and next review boundary. No program launch or policy change without additional authorization.
