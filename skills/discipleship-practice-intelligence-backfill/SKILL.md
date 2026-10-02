---
name: discipleship-practice-intelligence-backfill
description: Systematically mine a large existing corpus of discipleship resources for concrete ministry practices, deduplicate source families, triage by practice yield, extract/merge practice families, create or update Practice Cards and topic landscapes, preserve provenance, and identify what deserves later Southbrook fit assessment. Use for large historical backlogs such as the Exponential library or AI-generated research folder.
metadata:
  short-description: Backfill Practice Intelligence from a large existing research corpus
---

# Discipleship Practice Intelligence Backfill

## Purpose

Turn a large historical research/library corpus into **usable Practice Intelligence** without creating another warehouse of summaries.

This skill is for corpus-scale retrospective work: dozens of books, PDFs, reports, transcripts, or mixed-format research artifacts already stored in the Brain.

The goal is not to summarize every file. The goal is to recover and organize the **practices hidden across the corpus**:

- what people actually do;
- how they do it;
- who does it;
- what support it requires;
- what outcome is reported;
- what mechanism may explain it;
- what research supports or challenges that mechanism;
- what repeats across independent contexts;
- what belongs in a durable Practice Card or Practice Landscape.

Use `docs/research-practice-action-framework.md`.

## Trigger

Use when the user asks to:

- go backward through an existing research/library folder;
- mine a large set of books/reports for practices;
- convert an old evidence library into Practice Intelligence;
- review all resources in a corpus and extract what is practically useful;
- backfill Practice Cards from historical material.

## Core flow

`INVENTORY → DEDUPLICATE → TRIAGE → MINE → EXTRACT → MERGE PRACTICE FAMILIES → CREATE/UPDATE CARDS → BUILD LANDSCAPES → LINK EVIDENCE → IDENTIFY GAPS → VERIFY FILING`

## Stage 1 — Inventory

Create a manifest with:

- file title;
- folder/source collection;
- file type;
- source family / organization;
- likely topic;
- duplicate/alternate-format relationship;
- preliminary practice-yield level;
- processing status.

Do not treat audio + transcript + PDF versions of the same work as independent evidence.

## Stage 2 — Deduplicate / source-family map

Group together:

- duplicate files;
- alternate formats;
- AI reports based on the same underlying sources;
- multiple books/resources from the same organization;
- derivative summaries of one study/source.

Preserve every file, but count source independence accurately.

## Stage 3 — Triage by Practice Yield

Classify:

- **HIGH PRACTICE YIELD** — likely to contain concrete process, training, coaching, leadership, evangelism, formation, family, multiplication, or implementation detail.
- **MEDIUM PRACTICE YIELD** — contains some usable practice/process detail but is mainly conceptual, strategic, or research-oriented.
- **LOW PRACTICE YIELD / REFERENCE ONLY** — little direct discipleship-practice value; inventory and link, but do not overprocess unless a later question needs it.

Triage is about **processing priority**, not source quality.

## Stage 4 — Mine the high- and medium-yield corpus

For each useful source, extract practice candidates with:

- practice name;
- problem addressed;
- people/roles;
- exact steps;
- cadence/duration;
- group/relationship size;
- tools/content;
- training;
- coaching/feedback;
- authority/maturity threshold;
- oversight/correction;
- staff/volunteer load;
- reproduction mechanism;
- reported outcomes;
- independent evidence;
- mechanism evidence;
- failure modes;
- transferability;
- source location.

Keep:
- DOCUMENTED PRACTICE
- REPORTED OUTCOME
- INDEPENDENT EVIDENCE
- MECHANISM SUPPORT
- PRACTITIONER OPINION
- INTERPRETATION
- HYPOTHESIS

separate.

## Stage 5 — Merge practice families

Do not create one card per source.

Merge materially similar practices into a **practice family** when they share the same core mechanism and operational logic.

Preserve meaningful variants, such as:

- one-to-one vs triad;
- weekly vs monthly;
- staff-led vs volunteer-led;
- formal curriculum vs simple reproducible questions;
- mature-believer-only vs graduated early participation;
- centralized coaching vs peer coaching.

A repeated practice family across independent source families becomes a **REPEATED PRACTICE PATTERN**, not automatically a proven effect.

## Stage 6 — Create/update Practice Cards

Use `templates/discipleship-practice-card-template.md`.

Prefer updating an existing card when the new corpus:
- adds another independent example;
- adds operational detail;
- adds mechanism support;
- adds a failure mode;
- adds a transferability condition;
- weakens/qualifies an outcome claim.

Do not proliferate near-duplicate cards.

## Stage 7 — Build topic Practice Landscapes

Create comparison documents for meaningful domains, such as:

- Disciple-Maker Development
- Apprenticeship & Coaching
- Evangelism & Mission
- Scripture / Prayer / Obedience
- Relational Discipleship Conversations
- Groups / Microgroups / D-Groups
- Leadership Reproduction
- Church-Wide Multiplication Culture
- Family Discipleship
- Children / Students / Faith Ownership
- New Believer Follow-Up
- Sending / Missional Communities / Microchurch

Each landscape should show:

- major practice families;
- who uses them;
- key variants;
- mechanism candidates;
- evidence backbone;
- common failure modes;
- staff dependence;
- ordinary-person reproducibility;
- transferability;
- important unresolved questions.

## Stage 8 — Link evidence without overclaiming

For each practice family, distinguish:

- evidence that the practice exists;
- evidence that an outcome was reported;
- independent/direct effect evidence;
- mechanism support;
- counterevidence;
- local Southbrook evidence, if any.

Do not convert frequency of mention into causal confidence.

## Stage 9 — Identify deeper-research / case-study gaps

Flag only gaps that would materially improve a future decision, for example:

- process is unclear;
- outcome claims are consequential but unverified;
- two models use the same label differently;
- mechanism is uncertain;
- transferability to an established church is unclear.

Route:
- deep exemplar → `church-movement-case-study-analyzer`
- effect claim → `source-evidence-checker`
- unresolved truth question → `discipleship-research-scout-agenda-builder`
- Southbrook fit question → `southbrook-practice-fit-assessor`

## Stage 10 — Persistence

Default destinations:

`04 — RESEARCH INTELLIGENCE → 06 Practice Intelligence Library → 01 Practice Cards`

and

`04 — RESEARCH INTELLIGENCE → 06 Practice Intelligence Library → 02 Practice Comparisons & Landscapes`

Also preserve a **Backfill Manifest** in the landscapes folder containing:

- source inventory;
- deduplication/source-family map;
- triage;
- processing status;
- practice families discovered;
- cards created/updated;
- landscapes created/updated;
- unresolved gaps.

## Batch strategy

For large corpora:

1. inventory the entire corpus first;
2. process high-yield sources first;
3. merge cards continuously so duplicate practice families do not multiply;
4. process medium-yield sources next;
5. low-yield sources may remain reference-only after inventory unless they contain a unique practice lead;
6. stop when further mining mostly repeats already-captured practice intelligence.

Do not process in arbitrary filename order if triage indicates a more useful sequence.

## Output contract

# Practice Intelligence Backfill Report

## Corpus
Folders/files included.

## Inventory / source-family summary
Counts, duplicates/alternate formats, source-family cautions.

## Practice-yield triage
High / medium / low counts and rationale.

## Practice families discovered
Major recurring practice families.

## Practice Cards
Created / updated / merged.

## Practice Landscapes
Created / updated.

## Key practical learnings
The most important operational insights discovered.

## Evidence boundaries
What is documented practice vs claimed outcome vs independent/mechanism evidence.

## Research / case-study gaps
Only gaps worth further work.

## Southbrook handoff
Do not select a local practice unless the user asked for local fit. Otherwise, identify which practice families are now ready for `southbrook-practice-fit-assessor`.

## Persistence status
Links/locations for manifest, cards, and landscapes.
