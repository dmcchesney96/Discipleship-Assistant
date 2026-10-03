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

`INVENTORY → DEDUPLICATE → TRIAGE → MINE → EXTRACT → MERGE PRACTICE FAMILIES → CREATE/UPDATE CARDS → BUILD LANDSCAPES → LINK EVIDENCE → IDENTIFY GAPS → INDEX → CROSS-CORPUS SYNTHESIS → COMPLETION / LOCAL-READINESS GATE → VERIFY FILING`

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
- unresolved gaps;
- completion status / last-updated date.

When the corpus is substantial, preserve beside it:
- a **Practice Intelligence Library Index**;
- a **Backfill Synthesis**;
- a short **targeted verification / case-study queue** inside the synthesis or manifest.

## Stage 11 — Build a library index

When the backfill creates more than a small handful of cards/landscapes, create or update a **Practice Intelligence Library Index** that:

- groups Practice Cards by practical domain/problem;
- links directly to every active card;
- links to Practice Landscapes and deeper case analyses;
- points to the Backfill Manifest;
- explains the intended flow: landscape → card → fit assessment → pilot → learning;
- avoids duplicating the content of the cards themselves.

The library should be navigable in under two minutes by a pastor who did not run the backfill.

## Stage 12 — Cross-corpus synthesis + completion gate

Create a concise **Backfill Synthesis** that answers:

- What practice patterns recur most strongly?
- Which are genuinely cross-source versus repeated inside one ecosystem?
- Which mechanisms have stronger research support than the named programs?
- What practical cautions/failure modes repeat?
- Which practices are mature enough for Southbrook fit assessment?
- Which claims/practices still deserve targeted primary-source verification?
- Which existing analyses already close a gap and therefore should not be duplicated?

### Local-readiness gate

Before automatically moving into Southbrook fit assessment, check whether enough verified/current local evidence exists.

If the Southbrook Diagnostic/current-state layer is empty, stale, thin, or based mainly on proposals rather than observed reality:

- **do not invent a whole-church fit assessment**;
- report the diagnostic gap;
- identify the practices now ready for later fit assessment;
- route to diagnostic/interview/current-state work first.

A strong external Practice Intelligence library does not substitute for local reality.

### Completion rule

A backfill is **COMPLETE ENOUGH FOR DESIGN USE** when:

- the whole requested corpus has been inventoried;
- alternate formats/source families have been deduplicated;
- high-yield sources have been mined;
- medium-yield sources have been reviewed for unique practice intelligence;
- low-yield sources are safely inventoried/reference-only;
- materially distinct practice families are represented;
- new sources mostly repeat already-captured practices;
- the library has cards, landscapes, an index, and a cross-corpus synthesis;
- remaining work is better expressed as targeted verification, a case study, or local fit/diagnostic work.

Do not keep extracting merely to maximize the number of cards.

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

## Library index
Created / updated + link.

## Cross-corpus synthesis
Strongest recurring practice patterns, ecosystem/source-independence cautions, and what the corpus adds practically.

## Completion status
IN PROGRESS / COMPLETE ENOUGH FOR DESIGN USE / BLOCKED, with reason.

## Key practical learnings
The most important operational insights discovered.

## Evidence boundaries
What is documented practice vs claimed outcome vs independent/mechanism evidence.

## Research / case-study gaps
Only gaps worth further work.

## Southbrook handoff
Do not select a local practice unless the user asked for local fit. Identify which practice families are ready for `southbrook-practice-fit-assessor`.

Also report whether the current Southbrook Diagnostic/current-state evidence is sufficient for responsible fit assessment. If not, route to diagnostic/current-state work before making whole-church recommendations.

## Persistence status
Links/locations for manifest, cards, and landscapes.
