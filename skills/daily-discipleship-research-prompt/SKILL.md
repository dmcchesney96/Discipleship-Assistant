---
name: daily-discipleship-research-prompt
description: Create one fresh, high-value, self-contained discipleship research prompt/contract based on the current Discipleship Brain, avoiding repetition and selecting the most useful next research question. Supports prompt-only use and SELF_EXECUTE handoff to the deep research executor.
---

# Daily Discipleship Research Prompt Generator

## Job

Do **not** perform the research. Own the bounded transformation from **research need/gap → excellent research prompt/contract**.

### Invocation modes

**PROMPT_ONLY (default)**  
Create ONE outstanding prompt the user can paste into Genspark or another deep-research model.

**SELF_EXECUTE (orchestrator handoff)**  
Create the same rigorous research design as a structured research contract plus execution prompt, then hand it back to the calling orchestrator. Do not stop the overall workflow and do not conduct the research yourself. The orchestrator must pass the contract to `discipleship-deep-research-executor`.

## Goal

Over time, build a diverse, evidence-informed body of knowledge covering theology, formation, systems, culture, leadership, multiplication, measurement, and implementation.

## Context scan

Before writing the prompt, inspect the current conversation/Brain sufficiently to know:

- what has already been researched;
- reports, churches, models, books, frameworks already covered;
- the user's current questions and upcoming decisions;
- areas already saturated;
- important gaps and natural next questions.

Do not issue another generic “best discipleship systems” prompt when adjacent deeper questions are available.

## Research intent + modes

First choose the research intent:

- **EVIDENCE / PRINCIPLE** — primarily asks what appears true and why.
- **PRACTICE INTELLIGENCE** — primarily asks what credible practitioners actually do and how it is implemented.
- **HYBRID** — needs both concrete practice detail and an evidence/mechanism backbone.

Then choose ONE best mode: `DEEPEN`, `EXPAND`, `COMPARE`, `TEST`, `CASE STUDY`, `PRACTICE SCAN`, `IMPLEMENT`, `DIAGNOSE`, `MEASURE`, or `SYNTHESIZE`.

Do not force an implementation/practice question into an academic-literature-only prompt. For PRACTICE INTELLIGENCE or HYBRID work, require primary church/network materials, practitioner manuals/books/interviews, and concrete operational detail alongside appropriate research on the mechanism.

Internally consider 3–5 candidate gaps; select the one with the strongest combination of importance, novelty, practical usefulness, and connection to the ongoing research program. Do not show the candidate list unless asked.

## Genspark quality instructions

The prompt should require deep research using appropriate sources such as peer-reviewed research, academic/seminary work, primary church/network materials, books, interviews, conference resources, research organizations, surveys, longitudinal data, dissertations, global/historical cases, and practitioner materials.

Tell Genspark to distinguish documented evidence, organizational claims, practitioner experience, theological argument, interpretation, anecdote, and marketing.

For case studies and practice scans, ask what they do **operationally**: who initiates, exact steps, cadence, group/relationship size, tools, training, coaching, maturity threshold, staff load, oversight, what happens when people struggle, reproduction expectation, outcomes/evidence, weaknesses, transferability, and contextual dependence.

Use empirical/academic evidence as a backbone and corrective for mechanisms. Do not require direct causal evidence for the exact named ministry practice before it can be considered a promising practice or small-test candidate.

## Required report artifact

Tell Genspark to create a polished, skimmable report with:

1. Executive Summary
2. Why This Matters
3. Key Findings
4. Evidence
5. Case Studies (when applicable)
6. What Effective Models Have in Common
7. What Does Not Work / Failure Modes
8. Practical Implications for a Local Church
9. Questions a Discipleship Pastor Should Ask
10. Ideas Worth Testing
11. What This Research Does Not Prove
12. Further Research
13. Sources with direct links/citations

Require strong headings, concise paragraphs, bullets, useful tables, major-claim citations, evidence/opinion separation, limitations, and no filler.

## Output contract

### PROMPT_ONLY

Return exactly:

### TODAY'S RESEARCH QUESTION
One sentence.

### WHY THIS NEXT
2–4 sentences explaining how it advances the existing body of knowledge.

### COPY INTO GENSPARK
One complete self-contained prompt inside a code block.

Do not give multiple prompts unless asked.

### SELF_EXECUTE

Return:

### RESEARCH CONTRACT
- Research intent: EVIDENCE / PRINCIPLE, PRACTICE INTELLIGENCE, or HYBRID
- Research question
- Why now
- Existing Brain starting point
- Specific unresolved gap
- Scope/populations/contexts
- Definitions/units that must remain explicit
- Must-answer subquestions
- Counterclaims/failure modes to test
- Required source types
- Redundancy/exclusions
- Required report artifact
- Success criteria

### EXECUTION PROMPT
One complete self-contained prompt suitable for `discipleship-deep-research-executor`.

### HANDOFF
`NEXT: discipleship-deep-research-executor`

The calling orchestrator continues automatically.
