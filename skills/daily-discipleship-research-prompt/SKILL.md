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

## Context access limit

If canonical Brain context is unavailable or partial, return one PROVISIONAL prompt using the accessible boundary. State what was checked, what was inaccessible, and that novelty against the Brain is unverified. Do not claim an unsearched topic is new. In SELF_EXECUTE mode pass this gap to the orchestrator; do not choose a highest-value project-wide gap from absent context.

Apply the AGENTS.md mission-to-learning gate when choosing the question. Include the capability, decision or uncertainty it could change; do not frame report production itself as the discipleship outcome.

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

## Critical prompting: pressure without performance theater

Use **selective, truth-seeking pressure** when constructing either the copyable prompt or the SELF_EXECUTE research contract. The goal is a better challenge, not a louder persona. The user's actual question, ministry decision, audience, source boundary, and deliverable take priority.

Before drafting, identify the **highest-risk easy answer**: the assumption a compliant AI would merely echo, the weakest causal leap, the missing opposing case, or the likely vague recommendation. Choose **two or three** of the following levers only if they address that risk; never mechanically include all seven. Make the chosen challenges explicit in the generated research prompt/contract, not just this skill's instructions.

| Lever from user-supplied coaching | Useful research-prompt instruction | Guardrail |
|---|---|---|
| High expertise standard | "Evaluate this to the standards of a rigorous researcher and experienced practitioner; inspect definitions, source quality, counterexamples, and feasibility." | Do not claim real credentials, a 200 IQ, certainty, or privileged expertise. Rigor is demonstrated by checks and citations. |
| "Obviously" / questionable premise | "Before agreeing that [premise], test whether it is true; state the best objection and what evidence would change the conclusion." | Treat bait as a **hypothesis**, not a proven premise. Correct false premises in the question itself. |
| Imagined audience | "Write the plain-language opening for [specified audience], anticipating their strongest fair questions." | Keep the report's full evidence and source details; the audience changes the explanation, not the facts. |
| Odd creative constraint | "Explain the top three findings with one memorable [analogy/form], then give a literal explanation and limits." | Creativity must never hide uncertainty or override the complete sourced report, accessible wording, or requested output. |
| Imaginary bet / stakes | "If a church had to invest scarce leader hours based on this finding, show the downside risk, strongest alternative, and what would reverse the recommendation." | Stakes are a **decision-quality checklist**, not simulated cash incentives, urgency, or proof of greater model intelligence. |
| Invented opponent | "Present the strongest evidence-based objection a thoughtful critic would raise; defend, qualify, or concede." | No straw opponents, fictional quotations presented as real, or manufactured counterevidence. |
| Version 2.0 | "After initial synthesis, reassess its weakest claim against the strongest alternative and improve the conclusion materially; state what changed and what stayed uncertain." | If no material improvement is warranted, say so. Do not pad or create a second full redundant report. |

### Required reality-check sequence for consequential research

Embed a **short adversarial review task** in prompts where an answer might influence theology, discipleship strategy, program design, measurement, or money:

1. **Challenge the premise:** What did the question assume that might not be true? Separate a hypothesis from established evidence.
2. **Steelman one competing view:** What would a capable, evidence-informed critic argue? What evidence favors it? Name the best exception or failed implementation.
3. **Decision test:** What observation or primary source would change the conclusion? What would a local leader try at low risk to learn rather than assume?
4. **Substantive revision pass:** Rethink the weakest conclusion, adjust it if warranted, and show the change in one or two sentences; preserve unresolved disagreement.

Require the final report to distinguish **observed practice**, **reported success**, **independently supported effect**, **plausible mechanism**, and **recommended local experiment**. A compelling narrative is not independent verification. Never invent a report, yesterday's conversation, a skeptic's quote, a source, an exact statistic, or a verified outcome. If source access is missing, write **UNVERIFIED** and specify what to check. Claims based on false memory prompts ("you told me yesterday") must be checked against actual accessible context, not echoed.

### Efficiency, audience, and coaching boundaries

- Do not turn each research prompt into an inflated role-play. A short critical challenge is better than repeated threats, IQ boasts, or dramatic betting.
- Put the audience-specific, memorable explanation in the **plain-language opening**; keep methodology, citations, failure modes, and source ledger available for scrutiny.
- Preserve the user's exact quantity and format limits. If a three-sentence summary is requested, restrict that **summary**, not the required complete research artifact unless the user explicitly limits the entire task.
- If the user asks for a coaching drill on *their draft prompt*, use their real task to show a weakness, a 2–3-lever rewrite, and why it helps. Ask for a rewrite and offer a 60-second exercise only in coaching mode; do not replace PROMPT_ONLY or SELF_EXECUTE's required output contracts with a coach conversation.
- Do not state these tactics have been proven to increase factual accuracy. The value of the revision must be measured with paired prompts and source audits, not the forcefulness of the prose. See `tests/prompt-pressure-evals.md`.

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

For `PRACTICE INTELLIGENCE` or `HYBRID` intent, additionally require:

- Practice Landscape
- 5–15 concrete operational practices when the evidence base supports breadth
- who/steps/cadence/tools/training/coaching/oversight for each serious practice
- reported outcomes separated from independent evidence
- mechanism/research backbone
- failure modes and implementation burdens
- transferability conditions
- Practice Card-ready summaries
- which practices are worth deeper case-study analysis

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

The calling orchestrator continues automatically within the user's authorization. Always include the literal named routing line `NEXT: discipleship-deep-research-executor`; a generic review state is not a substitute. For a contract-only or no-execution request, retain that routing line and separately state that research has not started and execution must respect the user's limit.

## Save progress and make interrupted work resumable

Include this requirement in every research contract and execution prompt, including PROMPT_ONLY output. In SELF_EXECUTE mode, carry it through the orchestrator handoff.

- Save completed work at each major stage, before starting a long next stage. Do not wait for a low-usage warning; the runtime may stop without warning and may expose no remaining-usage signal.
- Preserve the complete raw report separately from the corrected final report. Save completed contracts, source/claim registers, verification results and confirmed write receipts in the user's authorized durable destination.
- Maintain one named resume checkpoint with run ID, date/timezone, scope, cycle/stage states, exact saved file IDs/links, source access depth, confirmed writes, partial failures, remaining work and the next exact action. Distinguish local-only, durable-saved, verified and blocked work.
- Include a self-contained restart prompt a later session or scheduled task can use without the original chat or scratch directory. Tell it to read the checkpoint, inspect confirmed outputs, resume the first unfinished stage, repair partial topic/index synchronization and avoid duplicate files/IDs.
- Mark unfinished cycles IN PROGRESS or BLOCKED. Never infer completion from an intended write.
- A usage interruption is not a scheduled continuation. Do not create a scheduled task without the user's requested time/condition, promise credit-reset detection, guarantee a model/tool will be available, or imply that a task can automatically reopen a specific chat.
- If durable saving fails, record the exact failure and provide the best available recovery files; do not call local scratch durable.

## Plain-language learning requirement

Require the report and any synthesis handoff to lead with 3-6 short learning sentences an ordinary ministry volunteer can explain. For each, state what it means, give a concrete example, say what a leader could try and explain the main limit. Put study methods and technical evidence fields after the readable explanation. Keep the distinction between learning a skill, helping someone learn it, and that person helping another. Preserve claim meaning, confidence, sources and uncertainty; simpler wording must not turn an association into a cause or a proposal into a decision.
