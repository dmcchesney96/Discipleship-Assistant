---
name: discipleship-deep-research-executor
description: Execute a defined discipleship research contract and produce a complete, source-traceable deep research report. Use after the research question/contract is set. This skill conducts the research; it does not choose the agenda, verify its own final claims as an independent audit, or update the Living Synthesis.
metadata:
  short-description: Conduct the actual deep research and produce the full report
---

# Discipleship Deep Research Executor

## Purpose

Fill the gap between **writing a research prompt** and **having a complete research report**.

This skill receives a research contract and actually performs the investigation. It is the primary research-production skill for substantial external discipleship research.

It must not stop at:

- a prompt;
- a research plan;
- a bibliography;
- a source list;
- a short answer;
- a preliminary summary.

The required product is a complete, evidence-labeled, source-traceable **content report**. In a full-cycle workflow, this is the raw research input; the final human-facing PDF is produced later by `discipleship-research-report-publisher` after independent verification.

## Inputs

Required:

- exact research question;
- research contract from the prompt-builder or equivalent;
- relevant existing-Brain context: current conclusion, confidence, known source families, unresolved gap;
- user/source boundaries;
- as-of date.

Optional:

- required churches/movements/authors/studies;
- local decision context;
- desired report length;
- source exclusions.

## Research posture

Research to discover what is true or most supportable, not to validate a preferred model.

Actively test:

- competing explanations;
- failure cases;
- contrary findings;
- contextual limits;
- source-family dependence;
- marketing/self-report bias;
- transferability.

Treat the North Star as the ministry relevance filter, not as permission to force all evidence toward multiplication claims.

## Source hierarchy

Prefer, as appropriate:

1. Scripture and responsible biblical/theological scholarship for theological claims;
2. peer-reviewed research / academic books / dissertations / systematic reviews;
3. longitudinal and high-quality survey research;
4. primary church/network/movement documents and published data;
5. denominational/seminary/research-organization studies;
6. books and substantive practitioner interviews/training materials;
7. credible case studies and conference materials;
8. secondary summaries only when stronger sources are unavailable.

For a named church or movement, pair primary organizational material with independent analysis where possible.

Do not rely on SEO summaries when an original source is available.

## Evidence distinctions

Every major claim should be classifiable as one of:

- `DOCUMENTED_EVIDENCE`
- `ORGANIZATIONAL_CLAIM`
- `PRACTITIONER_OPINION`
- `INTERPRETATION`
- `HYPOTHESIS`

Use project confidence vocabulary only after weighing evidence:

- `HIGH CONFIDENCE`
- `PROMISING`
- `CONTEXT DEPENDENT`
- `UNCERTAIN`
- `CONTRADICTED`

Do not inherit a source's confidence label without project evaluation.

## Search/research method

1. Start from the contract's exact unresolved question.
2. Build a source map before over-reading any single model.
3. Seek multiple genuinely independent evidence families.
4. Prefer original studies/primary documents for major claims.
5. Search for evidence that could disconfirm the emerging answer.
6. Record source family relationships so repeated citation chains are not mistaken for independent convergence.
7. Keep populations, time periods, denominations/cultures, and units explicit.
8. Distinguish formation outcomes from attendance/program outcomes.
9. Distinguish disciple multiplication from leader/group/church multiplication.
10. Stop when additional searching is producing repetition rather than material new evidence.

## Multiplication discipline

For every generational claim, record:

- exact reproducing unit;
- G0/G1/G2/G3/G4+ definition;
- geography;
- time period;
- who reported it;
- independent verification status;
- whether the claim measures actual disciple-making relationships or another unit.

Never convert church-planting generations into individual disciple-making generations.

## Causality discipline

Do not write "X causes Y" unless the evidence design supports causal inference.

Use more precise language:

- associated with;
- predicts;
- correlated with;
- repeatedly co-occurs with;
- practitioner consensus suggests;
- case evidence is consistent with;
- plausible mechanism;
- causal evidence remains limited.

## Cross-context discipline

For external cases use:

`PRACTICE → OBSERVED OUTCOME → MECHANISM CANDIDATE → PRINCIPLE → TRANSFERABILITY LIMIT → POSSIBLE LOCAL APPLICATION`

Do not conclude "Church X does it, therefore Southbrook should."

## Required report structure

# [Research title]

**Research question**  
**As-of date**  
**Scope / populations / contexts**  
**Existing Brain starting point**

## START HERE — Short answer in normal language

A concise explanation of the answer and the 3–6 most important findings.

## 1. Why this question matters

Explain relevance to mature disciples, mission, disciple-making, multiplication, culture, systems, or implementation.

## 2. What was already known vs. what this investigation tested

Prevent the report from presenting repeated prior knowledge as a new discovery.

## 3. Research method and source map

Include:
- source types;
- major source families;
- inclusion/exclusion logic;
- independence limitations;
- major evidence gaps.

## 4. Key findings

For each finding:
- plain-language claim;
- evidence classification;
- confidence;
- strongest supporting evidence;
- contrary/limiting evidence;
- population/context;
- mechanism candidate;
- what the evidence does not prove.

## 5. Biblical/theological analysis

When relevant, distinguish:
- what the text/theological tradition supports;
- interpretive disagreements;
- what empirical research can and cannot establish.

## 6. Empirical / academic evidence

Organize by strongest evidence streams rather than by source order.

## 7. Case studies / movement evidence

When applicable, include:
- definition of disciple/maturity/multiplication;
- pathway/process;
- ordinary-person role;
- apprenticeship/coaching;
- multiplication mechanism;
- documented outcomes vs organizational claims;
- failure points;
- transferability.

## 8. Failure modes and counterevidence

What breaks, what does not work reliably, and what attractive claims are weaker than they appear?

## 9. Practice → Mechanism → Principle

Translate major practices into underlying transferable principles without jumping directly to programs.

## 10. Implications for an established local church

Use hypotheses/questions/experiment ideas unless evidence warrants more.

## 11. Ideas worth testing

For each:
- hypothesis;
- target people;
- practice;
- duration;
- support/coaching;
- measurement;
- learning decision.

Keep this light unless the contract specifically asks for pilot design.

## 12. What this research does not prove

Make boundaries explicit.

## 13. Biggest unresolved questions

Prioritize what would most change the conclusion or implementation.

## 14. Claim register

For every consequential claim include:

| ID | Claim | Evidence type | Best source(s) | Independence | Support strength | Verification priority |
|---|---|---|---|---|---|---|

Verification priority: `HIGH`, `MEDIUM`, `LOW`.

## 15. Source ledger

Provide enough bibliographic/link information for another agent to reopen each important source.

## Research integrity requirements

- Cite major factual claims.
- Do not fabricate bibliographic details.
- If a source cannot be located, say so.
- Do not silently upgrade organizational claims.
- Do not count multiple reports quoting the same study as independent support.
- Prefer direct quotations sparingly; summarize faithfully.
- Preserve important contrary evidence.
- Label exact numbers whose provenance is uncertain.
- Identify when evidence comes from a different population/context than the intended application.
- Do not treat program completion as spiritual maturity.
- Do not treat attendance growth as disciple multiplication.

## Output contract

Return:

1. **Complete Research Report**
2. **Claim Register**
3. **Source Ledger**
4. **Verification Handoff**, naming the 5–15 claims that most need independent second-pass checking
5. **Persistence Metadata**:
   - suggested title;
   - artifact type = `AI-GENERATED RESEARCH INPUT`;
   - topic/domain;
   - date;
   - recommended Drive evidence destination;
   - related existing synthesis domains.
6. **Publisher Handoff Metadata**:
   - short display title;
   - one-sentence evidence-weighted answer draft;
   - 3–6 candidate executive takeaways;
   - source-key-ready source ledger;
   - figures/tables worth publishing, if any;
   - sections that should remain appendix-level detail.

## Boundary

This skill does not independently certify its own report.

After completion, a full-cycle workflow must route the report through:

`ai-research-verification-integration → source-evidence-checker`

before durable conclusions are promoted to the Living Synthesis.

After verification and Brain-impact decisions, route the final content to `discipleship-research-report-publisher` for the standard professional PDF + editable master.
