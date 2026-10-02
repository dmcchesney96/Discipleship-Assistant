---
name: full-discipleship-research-cycle
description: Orchestrate one end-to-end discipleship research cycle from existing-Brain retrieval and gap selection through prompt/contract creation, deep research, Drive preservation, independent claim verification, cross-Brain comparison, durable synthesis updates, filing, and a simple-first final readout. Use only when the user asks for the whole research process to run without stopping between stages.
metadata:
  short-description: Run the entire discipleship research workflow from question to durable learning
---

# Full Discipleship Research Cycle

## Purpose

Turn one user request into one complete research-and-learning cycle.

This is an **explicitly multi-skill orchestrator**. It does not replace specialist skills. It sequences them, carries their handoffs forward, enforces evidence gates, persists authorized artifacts, and prevents the workflow from stopping after prompt generation or report creation.

Core flow:

`CONTEXT → GAP/REDUNDANCY CHECK → RESEARCH CONTRACT → DEEP RESEARCH → PRESERVE RAW REPORT → VERIFY → STRESS-TEST → COMPARE/PATTERN → KNOWLEDGE IMPACT → DURABLE UPDATES → PUBLISH PROFESSIONAL PDF → LIBRARY CHECK → SIMPLE-FIRST READOUT → STOP`

## Natural-language trigger

Use when the user asks for the complete research process, for example:

- "Run the full research cycle on..."
- "Find the next research gap and do the whole thing."
- "Build the prompt, give it to yourself, research it, evaluate it, and add what matters to the Brain."
- "Research this from start to finish."
- "Do not make me ask for each step."
- "Take this all the way through the Living Synthesis."
- equivalent language clearly requesting an end-to-end research workflow.

Do **not** invoke merely because a task involves several research actions. The user must be asking for a whole-cycle workflow.

## Authorization boundary

A full-cycle request is standing authorization for **bounded internal Drive writes created by this research cycle** when the relevant connector permissions exist:

- preserve the complete research report;
- preserve the verification/audit artifact;
- create or update Research Intelligence records;
- update the Living Discipleship Synthesis **only when the evidence gate is met**;
- create source/index links and file the cycle artifacts using the existing Brain architecture.

It does **not** authorize:

- deleting sources;
- changing sharing/access permissions;
- sending external messages;
- making ministry commitments or approved Southbrook decisions;
- changing personnel/pastoral/safeguarding decisions;
- automatically editing GitHub governance, AGENTS.md, or evidence guardrails.

If research suggests a change to how the assistant should evaluate future evidence, create a **Guardrail Candidate** in Research Intelligence and report it. GitHub operating-system changes require explicit authorization unless a separate standing authorization clearly covers them.

## Inputs

Accept either:

1. **Specific-question mode** — the user names the research question/topic.
2. **Agenda-selected mode** — the user asks the system to find the highest-value next question.
3. **Bounded-follow-up mode** — the user points to an existing report/topic and asks the system to deepen/test/resolve it through the full cycle.

## Stage 1 — Retrieve the smallest sufficient Brain context

Route to `ministry-context-retriever`.

Retrieve only what is needed to know:

- what the Brain already concludes on the topic;
- current confidence;
- existing reports/source families;
- unresolved contradictions;
- research gaps/open questions;
- relevant Southbrook strategy/diagnostic context when it materially affects the research question.

Prefer Living Synthesis + Research Intelligence + directly relevant assessed evidence. Do not flood the run with the whole Brain.

### Context handoff

Carry forward:

- current conclusion(s);
- confidence;
- known evidence families;
- unresolved gaps;
- research already completed;
- material local application questions.

## Stage 2 — Gap and redundancy gate

If agenda-selected, route to `discipleship-research-scout-agenda-builder`.

If specific-question mode, perform the same gap logic without replacing the user's question.

Ask:

- Has this exact question already been adequately researched?
- Would another full research run likely change a conclusion, mechanism, implementation question, or confidence level?
- Is there a narrower unresolved question underneath the user's wording?

### Gate outcomes

**A. Already sufficiently answered**
- Do not manufacture redundant external research.
- Use existing assessed evidence to produce the requested synthesis/readout.
- Explain that the evidence gap was already substantially closed.
- Continue to durable update only if the user's request reveals a needed synthesis correction.

**B. Partly answered**
- Narrow the contract to the unresolved portion.

**C. Genuine gap**
- Continue to the full research contract.

## Stage 3 — Build the research contract

Route to `daily-discipleship-research-prompt` in `SELF_EXECUTE` mode.

The contract must include:

- exact research question;
- why this question matters now;
- what is already known;
- what remains uncertain;
- source types required;
- important counterclaims to test;
- case-study boundaries when applicable;
- definitions/units that must remain explicit;
- required report sections;
- success criteria;
- exclusions / redundancy to avoid.

The prompt-builder still owns prompt design; it does not conduct the research.

## Stage 4 — Execute the contract

Route to `discipleship-deep-research-executor`.

The executor must actually conduct the research and produce the complete report. It must not return only a plan, source list, or prompt.

Require source traceability for major claims and a claim register suitable for second-pass verification.

## Stage 5 — Preserve the complete research report

Before interpreting the report as project truth, preserve it with provenance.

When a Drive document/file-creation capability is available:

1. preserve the **complete raw executor output** before verification rather than only a short summary;
2. preserve the research question, as-of date, claim register, source ledger, and links/citations;
3. classify it as `AI-GENERATED RESEARCH INPUT`;
4. use `discipleship-research-librarian-drive-curator` to resolve the live destination, deduplicate, index, and verify the raw artifact.

Do not treat this raw artifact as the final human-facing report. The polished PDF is created after verification in Stage 11A.

Default classification:

- artifact type: `AI-GENERATED RESEARCH INPUT`;
- original research report preserved intact;
- derived audit/synthesis artifacts remain separate;
- link the report to its research contract and source ledger.

Use the verified Drive architecture. Do not invent parallel top-level folders or guess folder IDs.

If Drive creation or filing is unavailable/blocked, report `PERSISTENCE BLOCKED` with the reason and continue the analysis without falsely claiming the artifact was saved.

## Stage 6 — Independent second-pass verification

Treat the newly produced report as AI-generated input.

Route to:

`ai-research-verification-integration → source-evidence-checker`

This stage must **re-open original/stronger sources** rather than relying on the executor's wording.

For consequential claims, test:

- citation/source existence;
- exact wording and whether the claim is actually supported;
- date and population;
- sample/method;
- denominator and baseline;
- causal vs correlational inference;
- organizational self-report vs independent evidence;
- independence of repeated source families;
- transferability;
- contrary evidence;
- multiplication unit and generation definition where relevant.

Deliberately search for disconfirming or limiting evidence for the top findings.

Do not "self-verify" merely by rereading the generated report.

## Stage 7 — Identify what actually matters

Use `compare-big-picture` to compare:

- the new verified/assessed evidence;
- the prior Brain conclusion;
- genuinely independent evidence families already in the Brain.

Use `pattern-connector` only when the research changes or sharpens a recurring cross-source mechanism/pattern.

For every major candidate takeaway, move through:

`PRACTICE → MECHANISM → PRINCIPLE → POSSIBLE LOCAL APPLICATION`

Do not turn a church's program into a transferable recommendation without identifying the mechanism.

## Stage 8 — Stress-test candidate conclusions

For each takeaway that might affect ministry design or the Brain, ask:

1. What directly supports it?
2. How many genuinely independent source families support it?
3. What pushes against it?
4. What is the likely mechanism?
5. What outcome was actually measured?
6. Is the evidence theological, causal, correlational, longitudinal, adjacent-domain, practitioner, organizational, or anecdotal?
7. Does the conclusion travel across contexts?
8. What would falsify or materially weaken it?
9. What would this change in discipleship ministry if true?
10. What should **not** change yet?

## Stage 9 — Classify knowledge impact

Every cycle must classify its impact:

- `NO DURABLE CHANGE` — useful report, but current synthesis remains adequate.
- `NEW LEAD` — interesting but unverified/thin; Research Intelligence only.
- `STRENGTHENS` — adds independent support to an existing conclusion.
- `NARROWS` — makes an existing conclusion more precise/context-limited.
- `COMPLICATES` — adds meaningful counterevidence or tension.
- `CONTRADICTS` — materially challenges an existing conclusion.
- `NEW DURABLE PRINCIPLE` — sufficiently supported to add to Living Synthesis.
- `GUARDRAIL CANDIDATE` — may change how future evidence should be evaluated; record as a candidate, do not self-modify GitHub governance.

## Stage 10 — Durable Brain updates

### Research Intelligence

Update when the cycle creates a meaningful:

- verified claim/evidence relationship;
- contradiction/disagreement;
- research gap;
- strongest-convergence finding;
- verification warning;
- guardrail candidate.

### Living Synthesis

Route to `living-discipleship-synthesis-maintainer` only when assessed evidence materially confirms, strengthens, narrows, complicates, contradicts, or adds a durable project-level conclusion.

Do not promote:

- a single AI report;
- a single organizational claim;
- repeated reports that trace to one underlying source family;
- an attractive but thin case study;
- a Southbrook recommendation masquerading as general evidence.

A synthesis update must preserve prior conclusion/history and changed confidence.

### Southbrook strategy

Research may produce:

- implications;
- hypotheses;
- experiments worth testing;
- questions for leaders.

It does not automatically create an approved ministry decision.

## Stage 11 — Publish the professional research report

After verification, comparison, pattern analysis, and any warranted Brain updates, route to `discipleship-research-report-publisher`.

The publisher creates the final **verification-aware publication package**:

1. a polished professional PDF using `docs/research-report-pdf-standard.md`;
2. an editable DOCX master using the same content hierarchy;
3. claim-level source keys immediately beside supported claims;
4. a complete keyed source ledger with direct links/DOIs when available;
5. final confidence/evidence labels;
6. visible limitations/counterevidence;
7. a "What changed in the Discipleship Brain" section.

Default filename:

`YYYY-MM-DD - [Short Research Title] - Discipleship Research.pdf`

Editable master:

`YYYY-MM-DD - [Short Research Title] - Discipleship Research.docx`

### Required publication QA

When authoring/rendering tools support it:

- author text-heavy research in DOCX or an equivalent structured format;
- export/convert to PDF;
- render every PDF page to images;
- inspect every page for clipping, overlap, broken glyphs, broken tables, stranded headings, citation collisions, and page-number issues;
- fix and re-render until clean.

The polished report must incorporate verification corrections. Do not publish the pre-verification executor wording unchanged when the verification pass weakened or corrected a claim.

If professional PDF generation is unavailable in the current environment, report `PDF PUBLICATION BLOCKED` and preserve the structured final content rather than falsely claiming a PDF exists.

## Stage 12 — Library verification

Route to `discipleship-research-librarian-drive-curator` to ensure:

- report, audit, and derived artifacts are in the correct layer;
- provenance links are intact;
- duplicates are not created unnecessarily;
- source and synthesis artifacts remain distinct;
- the cycle is findable later.

## Stage 13 — Final user-facing readout

Always lead with ordinary language before technical detail.

Use this order:

# START HERE — What this means in normal language

3–6 concise paragraphs. Explain the few things worth remembering without jargon.

# The biggest takeaways that may affect discipleship ministry

Usually 3–6. For each:
- simple takeaway;
- why it matters;
- confidence;
- what it does **not** prove.

# What changed in the Discipleship Brain

Explicitly report:
- Raw research input saved: yes/no + location/link when available;
- Professional PDF published: yes/no + location/link when available;
- Editable master published: yes/no + location/link when available;
- Verification artifact saved: yes/no;
- Research Intelligence changes;
- Living Synthesis changes;
- Confidence changes;
- Contradictions/open questions;
- Guardrail candidate(s), if any;
- Southbrook strategy status: hypothesis/experiment/recommendation/approved decision.

# Detailed research findings

Provide the deeper evidence-weighted explanation with citations/source links, competing evidence, mechanisms, and context limits.

# Research integrity / limitations

State meaningful evidence gaps and what could change the conclusion.

# Suggested next move

Only one next move if needed. Do not create another chain after the cycle is complete.

## Stop conditions

Stop the cycle when:

- the user-requested outcome has been achieved;
- additional research is unlikely to materially change the conclusion;
- the question is already adequately answered;
- verification reveals the evidence base is too weak to justify durable promotion;
- the next action requires new user authorization;
- a human-only judgment boundary is reached.

Do not keep running skills to maximize activity.

## Success test

A successful run should allow the user to give **one request** and receive:

1. a non-redundant research question/contract;
2. a complete sourced raw research report;
3. a preserved raw Drive artifact;
4. a second-pass evidence audit;
5. the few findings that genuinely matter;
6. explicit stress-testing and uncertainty;
7. durable Brain updates only where warranted;
8. a polished professional PDF with claim-level source keys and source appendix;
9. an editable source/master artifact;
10. a simple-language readout first;
11. detailed sourced analysis below;
12. no need to ask for each intermediate handoff.
