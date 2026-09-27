---
name: ministry-second-brain-intake
description: Process new ministry/research information into durable knowledge by separating raw evidence, current-state implications, decisions, actions, and reusable institutional memory.
metadata:
  short-description: Intake new knowledge safely
---

# Ministry Second Brain Intake

## Purpose

Prevent useful knowledge from disappearing into chats, notes, emails, research reports, transcripts, or one-off documents while avoiding accidental promotion of tentative information into permanent truth.

## Trigger

Use when new information enters the Discipleship Brain and needs classification/routing. For a whole external website/source-library ingestion, prefer `discipleship-research-source-ingestor`.

## Process

1. Identify source, date/version, author/context, and access/sensitivity.
2. Extract confirmed facts, claims, decisions, actions, owners, deadlines, and questions.
3. Separate raw evidence from interpretation, hypothesis, recommendation, and approved decision.
4. Assign knowledge status: CURRENT / PENDING / TENTATIVE / HISTORICAL / SUPERSEDED as supported.
5. Determine whether it changes current state, adds historical evidence, feeds research intelligence, creates durable memory, or only belongs in intake.
6. Flag material inconsistencies with existing records.
7. Recommend the exact existing Brain destination.
8. Route unresolved source disagreement through `knowledge-conflict-resolver`.

## Rules

- Never delete/rewrite source evidence to make history cleaner.
- Do not make tentative ideas authoritative.
- External evidence and Southbrook-local evidence remain separate.
- AI-generated research stays identified as AI research until verified.
- Do not store sensitive case narratives in GitHub.
- Do not redesign the Drive structure.

## Output

- Source summary
- Evidence/claim classification
- Facts / decisions / actions
- Current-state impact
- Durable-memory candidates
- Conflicts / unknowns
- Recommended destination
- Suggested next skill only if needed
