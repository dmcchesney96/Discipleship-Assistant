---
name: full-discipleship-practice-design-cycle
description: Orchestrate a practical discipleship design cycle from Southbrook's local problem through concrete external practice intelligence, mechanism/evidence backbone, contextual fit, action warrant, and bounded test/pilot/decision design. Use when the user asks what Southbrook should do or how to implement a discipleship outcome, not merely what research says.
metadata:
  short-description: Move from local problem to practice options to a testable Southbrook response
---

# Full Discipleship Practice & Design Cycle

## Purpose

Turn research and practitioner learning into **useful, contextualized, testable ministry practice** without copying churches or waiting for impossible levels of direct causal evidence.

Core flow:

`LOCAL PROBLEM → CONTEXT/DIAGNOSTIC → PRACTICE LANDSCAPE → OPERATIONAL DETAIL → MECHANISM/EVIDENCE BACKBONE → SOUTHBROOK FIT → ACTION WARRANT → TEST/PILOT DESIGN → MEASUREMENT → DECISION/LEARNING → STOP`

Use `docs/research-practice-action-framework.md`.

## Natural-language trigger

Route here when the user asks things like:

- What should Southbrook actually do about ___?
- How should we build/implement ___?
- What practices should we consider?
- Show me how churches do ___ and what would fit us.
- Take the research and turn it into something we can test.
- Compare practical models and tell me what is worth piloting here.
- Run the full practice/design cycle.

This is distinct from `full-discipleship-research-cycle`, whose primary question is **what appears to be true**.

## Authorization boundary

A practice/design-cycle request authorizes bounded internal analysis **and Drive writes** for artifacts created by that cycle when connector permissions exist:

- practice intelligence / Practice Cards;
- practice comparisons;
- local fit assessment;
- proposed experiments/pilots;
- proposed measurement plan;
- minimum viable implementation kit when requested;
- decision brief draft when needed.

Use the existing Brain architecture and verify destinations/results.

It does not authorize launching ministry changes, committing staff/volunteers, spending money, or recording a proposal as an approved Southbrook decision.

## Stage 1 — Define the local problem

Retrieve the smallest sufficient Southbrook context.

Use:

`ministry-context-retriever → current-state-synthesizer and/or southbrook-discipleship-diagnostic`

State:

- current reality;
- affected people;
- desired transformation;
- current bottleneck;
- what is already healthy and should be preserved;
- known constraints/capacity;
- what decision or learning is actually needed.

Do not begin from a favorite program.

## Stage 2 — Build the practice landscape

Route to `discipleship-practice-intelligence-builder`.

Start with the Brain's Practice Intelligence Library and existing research.

Then, only where gaps remain, gather targeted external practice detail from:

- church/network primary materials;
- practitioner books/manuals;
- historical/missionary examples;
- interviews/training;
- case studies.

The goal is concrete practice options, not a generic list of principles.

## Stage 3 — Deepen the most relevant exemplars

Use `church-movement-case-study-analyzer` selectively when:

- a practice seems especially relevant;
- implementation detail is unclear;
- the mechanism depends on system context;
- multiplication/outcome claims need careful examination.

Do not deep-dive every church merely because it appears in the scan.

## Stage 4 — Build the mechanism/evidence backbone

Use existing Living Synthesis first.

Use `source-evidence-checker` or targeted research only for the claims that could materially change the design.

Ask:

- Why could this practice work?
- What evidence supports the mechanism?
- What counterevidence or failure mode matters?
- Is the claimed outcome direct evidence, organizational report, practitioner experience, or inference?

Do not demand direct causal proof of the exact church practice before considering a reversible test.

## Stage 5 — Assess Southbrook fit

Route to `southbrook-practice-fit-assessor`.

For each serious candidate, assess:

- theology/North Star;
- mechanism;
- evidence;
- practice precedent;
- local bottleneck fit;
- ordinary-person reproducibility;
- staff dependence;
- capacity;
- culture;
- risk;
- reversibility;
- measurement;
- multiplication potential.

Assign an **action warrant**, not a universal “best practice” verdict.

## Stage 6 — Choose the smallest responsible next action

Possible outcomes:

- EXPLORE;
- SMALL-TEST CANDIDATE;
- PILOT CANDIDATE;
- INTEGRATION CANDIDATE;
- SCALE CANDIDATE;
- NOT NOW / POOR FIT.

If uncertainty is material, prefer a smaller learning move over a larger structural recommendation.

## Stage 7 — Design the test/pilot when warranted

For SMALL TEST / PILOT candidates, route to:

`discipleship-experiment-pilot-designer → discipleship-measurement-architect`

The pilot should specify:

- hypothesis;
- people;
- practice;
- duration;
- support/coaching;
- fidelity;
- measures;
- stories/qualitative learning;
- reproduction/ownership indicators;
- risks/guardrails;
- stop/adapt/expand criteria.

## Stage 8 — Build implementation assets when requested

If the user wants the selected test/pilot **ready to run**, route to `discipleship-practice-implementation-kit-builder`.

Create only the minimum viable assets needed:
- practice overview;
- leader quick-start;
- participant tool;
- training outline;
- coaching rhythm;
- fidelity essentials vs adaptable elements;
- launch checklist;
- measurement prompts;
- troubleshooting/safeguards.

Do not create a giant curriculum by default, and do not launch/send/commit the church merely because the toolkit exists.

## Stage 9 — Prepare a leadership decision when required

If the next move requires leadership approval, resources, cross-ministry change, or broad integration, route to:

`strategy-decision-brief-builder`

Keep:
- evidence;
- practice precedent;
- local fit;
- pilot learning;
- tradeoffs;
- uncertainty;
- decision request

distinct.

## Stage 10 — Evaluate local results when they already exist

If this request includes results from a completed/in-progress pilot, route to `discipleship-pilot-learning-evaluator` before making a larger recommendation.

Distinguish:
- implementation failure;
- mechanism/outcome failure;
- insufficient evidence;
- promising local signal;
- strong local learning.

If the pilot has not happened yet, stop at the designed test/pilot and do not invent future learning.

## Stage 11 — Preserve learning

External practices → Practice Intelligence Library.

Local tests/results → `09 — EXPERIMENTS, PILOTS & LEARNING`.

Changed local current reality → Southbrook Diagnostic/current-state.

Approved decisions → `10 — STRATEGY & DECISIONS`.

General mechanisms/principles → Living Synthesis only when evidence warrants.

## Final readout

Lead with:

# START HERE — What I think is worth trying to learn

Explain the practical problem, the 1–3 most useful candidate practices, and why they are worth consideration.

# What other churches/practitioners actually do

Concrete operational summary.

# Why these practices may work

Mechanism + research backbone.

# What seems to fit Southbrook

Action warrant and fit reasoning.

# Smallest responsible next test

Pilot/test outline.

# What we should not assume yet

Uncertainty and boundaries.

# What was saved in the Brain

Explicitly report:
- Practice Cards/comparison saved: yes/no + link(s) when available;
- local fit assessment saved: yes/no + destination;
- pilot/test draft saved: yes/no;
- measurement plan saved: yes/no;
- decision brief status;
- what remains proposed vs approved.

## Stop conditions

Stop when:

- there is enough practice intelligence to choose a learning move;
- the next step requires a human decision;
- no candidate practice has sufficient fit/warrant;
- additional external examples are repetitive;
- a pilot has been designed and the user did not authorize launch.

## Success test

A successful run does not merely say what research shows.

It helps Southbrook understand:

1. the real local problem;
2. concrete practices used elsewhere;
3. how those practices actually work;
4. why they might work;
5. what evidence supports or limits them;
6. what fits or does not fit Southbrook;
7. what is worth testing;
8. how to learn before scaling;
9. how pilot results will later be evaluated without moving the goalposts.
