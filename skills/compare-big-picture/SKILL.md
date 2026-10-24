---
name: compare-big-picture
description: Compare a defined body of discipleship research and produce a simple, evidence-weighted big-picture brief of the strongest recurring learnings, common themes, disagreements, mechanisms, and practical implications without automatically changing the Living Synthesis.
metadata:
  short-description: Bring many research documents into one simple big-picture view
---

# Compare Big Picture

## Purpose

Answer questions like:

- "Looking across all of this research, what are the biggest things we are learning?"
- "What themes keep showing up?"
- "Where do these reports agree or disagree?"
- "Bring this whole research folder together in simple terms for me."
- "What should I understand before I think about application?"

This is a **comparison-and-communication skill**. It turns a bounded research corpus into a pastor-friendly big-picture brief.

It is intentionally lighter than `living-discipleship-synthesis-maintainer` and broader than `pattern-connector`.

## Invocation rule

This skill is selected automatically by the manager from natural-language intent. The user does not need to say "use Compare Big Picture" or know the skill exists.

## Trigger

When the dominant request is “teach me this book efficiently,” practical tool-belt nuggets, or tools/insights for building Dan's own resources, use `discipleship-practical-learning-distiller` instead. Keep this skill for evidence-weighted cross-source comparison; honor an explicit request to compare evidence.


Use when the user asks to compare, review, or synthesize a **defined collection** of research into the biggest learnings/common themes in simple terms.

Typical source boundaries:

- one Brain folder;
- one topic cluster such as family discipleship;
- a selected batch of reports;
- one research campaign;
- all currently assessed material on a specific question.

Do not silently expand to the entire Brain when the user named a narrower corpus.

## Source handling

1. Inventory the defined source set.
2. Prefer assessed/verified evidence already in the Brain when available.
3. Read enough of the underlying reports to preserve their actual framing, definitions, and caveats.
4. Distinguish:
   - verified/assessed evidence;
   - raw AI-generated research;
   - organizational claims;
   - practitioner opinion;
   - interpretation/hypothesis.
5. **Do not count repeated claims in multiple AI reports as independent convergence when they trace to the same underlying study, author, dataset, church, or source family.**
6. When several reports rely on the same foundational evidence, say that the theme is **repeated across reports** but not independently replicated.
7. If an existing audit has corrected or downgraded a report claim, use the audited/corrected form.
8. Do not perform a full new verification campaign unless the user asks. Flag material unverified claims rather than quietly treating them as fact.

## Comparison workflow

1. State the question, source boundary, and as-of date.
2. Group reports into meaningful source families/topics.
3. Identify the 5–8 most important recurring conclusions—not merely the most frequently repeated phrases.
4. For each candidate conclusion, compare:
   - how many genuinely distinct source families support it;
   - source/evidence quality;
   - population/context;
   - outcome being measured;
   - whether evidence is causal, correlational, theological, adjacent-domain, practitioner, or organizational;
   - important contrary/limiting evidence.
5. Separate:
   - **CONVERGING LEARNING** — supported across reasonably independent evidence;
   - **REPEATED BUT NOT INDEPENDENT** — recurring across reports that share underlying sources;
   - **PROMISING IDEA** — plausible and useful but thinly tested;
   - **DISAGREEMENT / UNCERTAINTY** — material conflict, weak evidence, or context dependence.
6. Look for mechanisms underneath practices. Use:
   `PRACTICE → MECHANISM → PRINCIPLE`.
7. Identify recurring failure modes and what the research warns leaders not to assume.
8. Translate the findings into plain language.
9. Add Southbrook implications only as questions/hypotheses unless the user explicitly asks for strategy.
10. Stop after the big-picture brief. Do not automatically update the Living Synthesis.
11. If the corpus contains concrete ministry practices that are operationally useful, identify them as **Practice Intelligence candidates** and suggest `discipleship-practice-intelligence-builder`; do not force practice details into the Living Synthesis.

## Cross-source convergence requirement

The brief must make the **cross-document convergence visible**, not merely state a synthesized conclusion.

For every major finding:

1. Name the distinct reports/source families that support it.
2. Identify the different evidence streams involved (for example: longitudinal sociology of religion, developmental psychology, learning science, implementation science, mentoring/relationship research, transition/transfer research, church case material).
3. Explain in one sentence **how those different streams converge on the same underlying mechanism or principle**.
4. Note when apparent agreement is only repetition of the same underlying study/source family.
5. Cite or link the relevant Brain source artifacts when the output format supports links.

If the user specifies a number of findings (for example, "only 3 things"), return **exactly that number of primary findings** and prioritize the strongest, broadest convergence.

## Priority rule


The goal is **signal over volume**.

Do not create a document-by-document summary unless needed to explain the synthesis. The user should finish the brief knowing:

- what matters most;
- why it seems to matter;
- how sure we are;
- where the evidence is weak;
- what deserves attention next.

## Default output

# Big Picture Brief — [Topic]

## 1. The big picture
A concise 3–6 paragraph explanation in ordinary language answering the user's core question.

## 2. The biggest learnings
Usually 5–8 items. For each:

### [Plain-language learning]
- **What keeps showing up:** one or two sentences.
- **Why it may matter / mechanism:** one or two sentences.
- **Evidence read:** `HIGH CONFIDENCE`, `PROMISING`, `CONTEXT DEPENDENT`, `UNCERTAIN`, or `CONTRADICTED` when warranted.
- **Important caution:** what this does not prove or where evidence is thinner.

## 3. What keeps showing up across the research
A short cluster of recurring practices, conditions, mechanisms, and failure modes.

## 4. Where the research is weaker, overstated, or disagrees
Surface:
- claims repeated without independent evidence;
- exact numbers/dosages that are not actually established;
- church/program claims without outcome data;
- contradictory or context-dependent findings.

## 5. What this may mean for Southbrook
3–6 concise **implications, hypotheses, or questions**, not approved recommendations.

## 6. What I would keep studying
Only the highest-value unresolved questions.

## 7. Source map
List the major source families/reports behind each big learning so the conclusion remains traceable.

## Style

- Write for a pastor/leader, not an academic journal.
- Lead with conclusions, not methodology.
- Prefer simple sentences and concrete language.
- Preserve nuance without drowning the reader in caveats.
- Use tables only when they make comparison easier.
- Do not inflate the number of findings; five strong learnings are better than fifteen weak ones.
- Make confidence and uncertainty obvious without making the brief feel technical.

## Boundaries

Do not:

- treat AI-generated research as verified merely because multiple AI reports repeat it;
- convert attendance, affiliation, or program completion into mature discipleship without evidence;
- claim causation from correlation;
- promote exact ministry formulas or dosages that the research does not establish;
- turn external research into Southbrook current-state evidence;
- recommend a major church-wide strategy unless separately asked;
- update the Living Synthesis automatically.

If the brief reveals a conclusion that may deserve durable project status, suggest:

`compare-big-picture → living-discipleship-synthesis-maintainer`

If the main value is **concrete practice** rather than a new durable principle, suggest:

`compare-big-picture → discipleship-practice-intelligence-builder`

Use only the handoff(s) actually warranted.

## Candidate-principle handoff (additional required output)

After the readable brief, produce a compact **Candidate Principle Disposition** table only for the most consequential candidates:

| Candidate finding | Existing ID / overlap | Independent source families | Evidence role and limitations | Disposition | Next owning skill |
|---|---|---|---|---|---|

Use one disposition for each: NEW PRINCIPLE CANDIDATE, STRENGTHENS, NARROWS, COMPLICATES, CONTRADICTS, REPEATED PRACTICE ONLY, NEW LEAD, or NO DURABLE CHANGE. Explain why *another report* does or does not add new knowledge, and identify the exact original sources that would need checking for promotion.

This section is a **handoff**, not permission to make durable changes. The comparison skill ends after delivering the brief and dispositions unless an explicit full-cycle orchestrator has requested the next skill. Maintain a manageable output: no quota or invented confidence improvement. Follow `docs/principle-synthesis-system.md`.
