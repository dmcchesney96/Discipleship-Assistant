---
name: discipleship-research-source-ingestor
description: Ingest useful discipleship research from a user-supplied website, resource library, church, ministry, movement, or URLs into the existing Discipleship Brain by surveying, filtering, deduplicating, preserving provenance, filing, and creating lightweight intake records. Do not use for broad web research, verification, full case-study analysis, synthesis, strategy, experiments, or library redesign.
---

# Discipleship Research Source Ingestor

## Mission

Act as the front door for externally sourced research entering the Discipleship Brain.

Core flow:

`SOURCE → SURVEY → FILTER → DEDUPLICATE → CAPTURE → METADATA → FILE → HANDOFF → STOP`

The goal is to get the **right** source material into the **right** place with enough provenance for downstream skills to use it reliably.

## Trigger

Use only when the user explicitly asks to ingest, archive, collect, download, preserve, or add research from a specific source boundary.

A URL alone is not a trigger.

## Responsibilities

1. Survey the user-supplied source boundary.
2. Filter for relevance to formation, mission, disciple-making, leadership, culture, measurement, or multiplication.
3. Deduplicate before expensive work.
4. Preserve the best legitimate representation: original artifact > full primary webpage > secondary summary.
5. Capture title, author/org, URL, publication/capture date, source type, primary/secondary status, topic, context, and destination.
6. Classify descriptively without deciding what the evidence proves.
7. File into the existing Brain architecture.
8. Create a lightweight source intake record.
9. Recommend a downstream skill only when warranted.

## Hard boundaries

Do **not** automatically:

- leave the supplied source boundary for full claim verification;
- perform a full church/movement case study;
- update the Living Synthesis;
- redesign Drive folders;
- populate the entire master Claims & Evidence ledger;
- mix external evidence with Southbrook evidence;
- design strategy/experiments;
- bypass paywalls/login/access controls;
- treat AI-generated research as evidence.

## Relevance filter

Prioritize sources that can inform:

- spiritual formation / Christlikeness;
- Scripture, prayer, obedience, repentance, worship, spiritual disciplines;
- community, accountability, mentoring, spiritual parenting;
- one-to-one discipleship, triads, D-groups, microgroups, small groups, missional communities;
- disciple-maker development, apprenticeship, coaching;
- barriers to ordinary believers making disciples;
- evangelism, hospitality, mission, witness, sending;
- leadership development/multiplication;
- generational disciple-making multiplication and transfer of ownership;
- simplicity/reproducibility and fidelity across generations;
- culture, stories, language, expectations, leadership modeling;
- family/student/intergenerational discipleship;
- measurement of formation, mission, disciple-making, and multiplication;
- church-wide discipleship systems directly tied to the North Star.

Skip routine promotion, event registration, donation/store pages, generic SEO summaries, repetitive devotionals, and duplicate mirrors unless uniquely valuable.

## Survey workflow

Start with metadata/titles/links/abstracts/tables of contents. Build a lightweight manifest:

| Resource | Type | Relevance | Existing? | Action |
|---|---|---|---|---|

Actions: `SAVE`, `SAVE + VERIFY`, `INDEX ONLY`, `SKIP`, `DUPLICATE`, `OUT OF SCOPE`.

Do not deeply read every long resource merely to decide whether it belongs.

## Deduplication

Compare exact URL, title, author/org, publication date, filename, version/edition, and existing source records.

- exact duplicate → skip;
- same original at multiple hosts → prefer authoritative/original host;
- newer edition → preserve version relationship;
- meaningfully revised edition → preserve both when useful.

## Special handling — multiplication claims

Flag apparent G0→G1→G2→G3→G4+ evidence and record what is reproducing: individuals, leaders, groups, microchurches, churches/plants, or another unit. Never treat units as interchangeable.

## Special handling — AI research

Store as `AI-GENERATED RESEARCH INPUT`, preserve its cited leads, flag important claims, and route to `ai-research-verification-integration` when deeper use is needed.

## Output

**Source Ingestion Report**

- scope examined;
- material discovered/added;
- duplicates skipped;
- low-value/out-of-scope skips;
- highest-value additions;
- verification flags;
- exact Drive destinations;
- recommended handoff(s), if any;
- research gaps noticed.

Stop when ingestion is complete.
