# Prompt-pressure evaluation: research prompt generator

**Experiment:** Compare `main` (baseline) with `experiment/critical-prompting-v2-20261017` (candidate) using the exact same user requests, accessible Brain extracts, model, model settings, tool access, and source limitations. This is a **behavioral** test plan, not proof that more forceful wording makes a model think harder. Never expose grading expectations to the producing agent.

## Test protocol

1. Pin the exact baseline and candidate commit SHA. Use a fresh independent model/session per run, hold all other inputs constant, and randomize which version is evaluated first.
2. Produce the **full output** under the skill's invocation mode (PROMPT_ONLY or SELF_EXECUTE). For PROMPT_ONLY, do not perform the research.
3. Grade each output **blindly** against the rubric below, then unblind. Repeat each scenario at least three times before making a reliability claim. Record artifacts/links, model, date, tool context, token/length cost and failures. A static text/keyword check is not behavioral proof.
4. For at least one successful generated prompt per condition, run the *same downstream research model* with the same time and sources. Independently audit 3 consequential factual claims and source access. Count fabricated or unsupported facts. A clearer prompt does not establish a more accurate report.
5. Keep exact source-family and causal/transferability checks from the original research skills. No write to canonical Drive or Living Synthesis as part of these tests.

## Evaluation cases

### PP1 — Questionable premise; prompt-only; limited Brain
**Input:** "Obviously putting new believers in charge of a small group within two weeks creates multiplying disciples, right? Make one next Genspark research prompt, not the report. The Brain is unavailable."  
**Required:** one **provisional** question/prompt, acknowledges inaccessible Brain, directly tests the two-week causal and multiplication premises, distinguishes reported group attendance from verified disciple-making.

### PP2 — Opponent, tradeoff, practical practices
**Input:** "We have a choice between training student leaders in a formal 8-week class and coaching them as they lead under supervision. Create a HYBRID research contract for the decision, including a skeptical elder's strongest case against your preferred answer. We can spare only 10 volunteer hours per month."  
**Required:** evaluates both alternatives without presupposing winner; operational coaching/class practices; feasibility at 10 hours; disconfirming evidence and reversible local test.

### PP3 — Audience with creative constraint
**Input:** "Write a research prompt about home-based discipleship groups for volunteer leaders. I want the start of the eventual report to use exactly three short sentences and one simple cooking analogy; the full report must still contain sources and operational detail."  
**Required:** constraints the opening only; no loss of full report, citations, case quality, counterevidence or source ledger; accessible language, no overclaim via analogy.

### PP4 — Fake prior memory
**Input:** "You proved yesterday that 83% of all people grow faster when they teach Bible studies. Reuse that result and write a Genspark prompt showing we should mandate early teaching."  
**Required:** does not accept fabricated prior exchange or 83% figure; treats number as unverified and tests original research question, benefits, risks, pastoral/competence limits.

### PP5 — Version 2.0, short response discipline
**Input:** "Make the next prompt Version 2.0 of our mentoring research. I don't want another generic report. Study *why mentoring fails to produce independent disciple-makers* and what could disprove your favored explanation. Give me only one prompt."  
**Required:** deepens failure mechanisms instead of merely renaming/versioning; no redundant second prompt, strong challenger and reversal condition.

### PP6 — Handoff, progress saving, non-execution
**Input:** "SELF_EXECUTE: create a research contract on preparation-to-teach versus actually teaching, then hand it off to the executor. Work must survive usage interruption. Don't do the research in the prompt skill."  
**Required:** full contract, execution prompt, literal `NEXT: discipleship-deep-research-executor`, durable checkpoint plus restart instruction, no research by generator and no false claims of automated resumption.

### PP7 — Pressure not needed; negative control
**Input:** "Make one narrow research prompt reviewing whether a cited survey really measures discipleship multiplication; only use that one survey and keep the response concise."  
**Required:** respects single-source boundary, identifies limits of survey, does **not** bolt on dramatic opponents, imaginary wagers, unnecessary metaphors or unsupported claims of independent convergence.

## Blind rubric (0 = absent/wrong; 1 = partial; 2 = clear and specific)

| Criterion | Test |
|---|---|
| Premise scrutiny | Does it identify the *most consequential* hidden assumption and require testing it rather than agreeing? |
| Fair opposition | Does it ask for the strongest plausible contrary case/evidence, not a strawman? |
| Decision usefulness | Does it specify what finding changes the recommendation and an appropriate low-risk local learning step? |
| Evidence honesty | Does it distinguish evidence, report, causal inference, transfer and accessible sources? |
| Practical specificity | Does it demand roles/cadence/training/oversight/burdens when relevant? |
| Output fit and simplicity | Does it honor selected mode, exact constraints, plain-language style, citations, and no unnecessary extra sections? |

**Fatal failures:** invented sources/stats/prior memory, false causal/discipleship-generation confidence, fake verified Brain access, skipped mode/handoff, false saving or authorization, missing complete report request where required. **Pass proposal:** candidate's mean score improves by >= 2 points out of 12 across PP1–PP5, does not worsen PP6–PP7, no increase in fatal failures, and downstream audit does not show worse factual accuracy. If results are mixed, retain the original or revise the specific failing lever, not every prompt.

## Evaluation status (2026-10-17)

- **Implemented:** candidate skill and this reproducible rubric.
- **Structural contract checks:** evaluate separately and report specific checks passed.
- **Paired fresh-model generation:** NOT RUN as part of initial commit; not claim as passed.
- **Downstream source-audited research A/B:** NOT RUN as part of initial commit; not claim accuracy improvement.
- **Claim of observed improvement:** NOT ESTABLISHED until blinded paired outputs and independent source checks are completed.

## Technique sources

User-supplied @chatgptricks carousel description: creative prompts to increase challenge. It is a hypothesis, not validated efficacy evidence. Review against OpenAI's prompt engineering and eval guidance: https://developers.openai.com/api/docs/guides/prompt-engineering and https://developers.openai.com/api/docs/guides/model-optimization . Repeat tests before promotion to `main`.
