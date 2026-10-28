---
name: discipleship-practice-intelligence-builder
description: Build concrete practice intelligence from churches, movements, practitioners, books, historical examples, and existing research. Document what people actually do, how it works, mechanism candidates, reported outcomes, evidence backbone, failure modes, transferability, and reusable Practice Cards without requiring direct causal proof of every practice.
metadata:
  short-description: Turn external ministry practice into reusable Practice Cards
---

# Discipleship Practice Intelligence Builder

## Purpose

Answer:

> **What are credible people/churches/movements actually doing around this discipleship problem, how exactly do they do it, why might it work, and what can Southbrook learn before choosing what to test?**

This skill exists because practical ministry knowledge is often richer than the direct empirical literature on named church programs.

It treats research as a **backbone and corrective**, not as a gatekeeper that blocks learning from practice.

Use `docs/research-practice-action-framework.md`.

## Trigger

Use when the user asks:

- What practices do churches use for ___?
- How do churches actually train/equip/coach people to ___?
- Compare concrete discipleship methods/models.
- What can we learn from churches/books/practitioners?
- Build a practice library around ___.
- What are realistic options Southbrook could consider?
- Extract practical ministry practices from this research/case-study set.

Also use in **CAPTURE MODE** when a full research cycle uncovers concrete practices worth preserving even though the user did not ask for local design yet.

## Source posture

Prioritize operational detail from:

- primary church/network training materials;
- ministry manuals/toolkits;
- practitioner books;
- substantive interviews/podcasts/transcripts;
- conference workshops;
- ministry websites with actual process detail;
- historical/missionary accounts;
- case studies;
- annual reports / internal-public metrics;
- existing Brain case-study artifacts;
- academic/empirical research on the underlying mechanism.

For practice intelligence, a primary ministry source can be very valuable for answering **what they do** even when it cannot prove **that it causes the outcome**.

Keep those claims separate.

## Workflow

1. Define the practical problem/outcome narrowly.
2. Retrieve existing Brain research and Practice Cards first.
3. Identify 5–15 meaningfully distinct practices or implementations when the source base supports that breadth.
4. For each, recover operational detail:
   - who initiates;
   - who participates;
   - exact steps;
   - cadence/duration;
   - group/relationship size;
   - tools/materials;
   - training before launch;
   - coaching/check-ins;
   - theological/pastoral oversight;
   - maturity threshold;
   - handoffs;
   - what happens when someone struggles;
   - staff/volunteer load;
   - how reproduction is expected;
   - what is measured/celebrated.
5. Separate:
   - **DOCUMENTED PRACTICE** — the source shows they actually do it;
   - **REPORTED OUTCOME** — the organization/practitioner says happened;
   - **INDEPENDENT EVIDENCE** — outside research supports the outcome;
   - **MECHANISM SUPPORT** — research supports why the practice could work;
   - **INTERPRETATION** — project reasoning;
   - **HYPOTHESIS** — worth testing.
6. Look for similar practices across independent contexts.
7. Identify variations rather than flattening all practices into one generic model.
8. Identify failure modes, implementation burdens, adaptations, and conditions.
9. Use:
   `PRACTICE → OBSERVED/REPORTED OUTCOME → MECHANISM CANDIDATE → RESEARCH BACKBONE → TRANSFERABILITY LIMIT`
10. Create standardized Practice Cards.
11. Persist durable cards/comparisons in the Practice Intelligence Library when authorized.

## Practice Card

For each meaningful practice return:

### Practice name

**Status**  
OBSERVED PRACTICE / REPEATED PRACTICE PATTERN / PROMISING PRACTICE

**Problem it addresses**  
What bottleneck or outcome it is designed to affect.

**Seen in**  
Churches, movements, books, practitioners, historical examples.

**What actually happens**  
Concrete operational description.

**People / roles**  
Who does what.

**Cadence / duration**  
How often and for how long.

**Training & coaching**  
How people are prepared and supported.

**Tools / content**  
What is in people's hands.

**Maturity / authority threshold**  
What newer believers can do vs what requires greater maturity.

**Reproduction mechanism**  
What could plausibly cause another disciple-maker/leader/group to emerge.

**Reported outcomes**  
Clearly label organizational/practitioner claims.

**Independent evidence**  
Direct evidence for the exact practice, if any.

**Mechanism evidence**  
Research that supports/complicates the underlying mechanism.

**Failure modes / cautions**  
What can go wrong.

**Transferability conditions**  
What may depend on context.

**Staff dependence**  
LOW / MEDIUM / HIGH with explanation.

**Ordinary-person reproducibility**  
What makes it easy/hard to carry.

**What remains unknown**  
Important unanswered questions.

**Sources**  
Primary + independent sources.

## Cross-practice comparison

After the cards, identify:

- recurring mechanisms;
- practices that solve the same problem differently;
- practices with heavy staff dependence;
- practices that most clearly transfer ownership;
- practices where exact-program evidence is weak but mechanism support is strong;
- practices with compelling claims but weak evidence;
- gaps where Southbrook needs more operational detail.

Do not rank practices for Southbrook unless routed to `southbrook-practice-fit-assessor`.

## Persistence

Default Brain destination:

`04 — RESEARCH INTELLIGENCE → 06 Practice Intelligence Library`

Use:

- `01 Practice Cards` for individual practice records;
- `02 Practice Comparisons & Landscapes` for topic-level comparisons.

Practice Cards are derived intelligence, not proof and not approved Southbrook strategy.

## Output contract

- Practice question/scope
- Existing Brain context used
- Practice landscape
- Practice Cards
- Cross-practice patterns
- Mechanism/evidence backbone
- Failure modes
- Research gaps
- Persistence status
- Suggested next handoff:
  - `southbrook-practice-fit-assessor` when local fit should be judged;
  - `church-movement-case-study-analyzer` when one exemplar needs deeper operational study;
  - `source-evidence-checker` when a consequential effect claim needs verification.

## Source verification and operational completeness

Use `discipleship-practice-source-verifier` for consequential operational claims in practical research. Retain exact locators, date/version, access depth and per-field DOCUMENTED / PARTIAL / UNKNOWN / NOT APPLICABLE status. Explain whether instructions are prescribed, reported in use or observed in a record. Legacy OBSERVED PRACTICE does not establish observed compliance when the source is only a manual. Missing coaching/cadence/readiness details mean unknown, not nonexistent. Keep operational completeness, effect confidence and local action warrant separate. Reuse existing cards and preserve distinct implementations rather than averaging incompatible methods.
