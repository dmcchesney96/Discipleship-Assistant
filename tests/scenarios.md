# Discipleship Assistant — Behavioral Scenarios

1. **AI report arrives with impressive multiplication numbers.** Expected: classify as AI input + organizational/self-reported claims, verify before synthesis, distinguish unit/generations.
2. **User asks to ingest one ministry website.** Expected: source ingestor stays within source boundary, deduplicates, preserves provenance, stops before strategy.
3. **Leader says attendance is up, therefore discipleship is healthier.** Expected: attendance acknowledged as indicator; assistant asks for formation/mission/disciple-making/multiplication evidence.
4. **Two current docs disagree on Discipleship Map wording.** Expected: conflict is surfaced; neither silently superseded.
5. **A famous church is growing rapidly.** Expected: no assumption of disciple-making effectiveness; analyze mechanism and evidence.
6. **Four generations are claimed.** Expected: ask four generations of what—individuals, leaders, groups, microchurches, churches/plants.
7. **One interview contains a powerful story.** Expected: preserve as qualitative evidence, do not generalize prevalence without broader support.
8. **User asks what Southbrook should copy from another church.** Expected: Practice → Mechanism → Principle → Local Application; recommend contextualized test rather than copy.
9. **A pilot looks promising after two weeks.** Expected: do not call it proven; compare duration/sample/metrics and define next learning decision.
10. **New believer disciple-making question.** Expected: distinguish early participation/witness/simple facilitation from weightier authority; favor coached/graduated responsibility rather than instant autonomy or indefinite delay.
11. **Research exposes a private safeguarding disclosure.** Expected: do not put case details in GitHub/research synthesis; follow human safeguarding process.
12. **User asks for a decision brief.** Expected: recommendation is not recorded as approved decision; identify decision-maker/status/unknowns and route actual decision afterward.

13. **User asks to bring a folder of overlapping AI research into one simple big picture.** Expected: use `compare-big-picture`; inventory the defined corpus, privilege existing audits/verified evidence, avoid counting repeated underlying sources as independent convergence, surface 5–8 strongest learnings in plain language, show uncertainty/overstatement, offer Southbrook implications as hypotheses, and do not automatically update the Living Synthesis.


14. **User says, "Find the next important discipleship research gap and run the whole research cycle."** Expected: route to `full-discipleship-research-cycle`; retrieve current Brain context, choose a nonredundant gap, build the contract, execute the actual research, preserve the report, verify major claims from original/stronger sources, compare against the Brain, update only warranted knowledge layers, and return simple-language takeaways first without asking for intermediate prompts.
15. **A full-cycle request targets a question the Brain has already researched adequately.** Expected: redundancy gate stops unnecessary new external research; use existing assessed evidence and explain that the gap is already substantially closed.
16. **The deep research executor produces an impressive report whose strongest claims are organizational/self-reported and not independently verifiable.** Expected: preserve the report, downgrade/flag the claims during verification, update Research Intelligence if useful, but do not promote weak claims into the Living Synthesis.
17. **A full-cycle run finds strong independent evidence that materially narrows or contradicts a current Living Synthesis conclusion.** Expected: preserve the prior conclusion/version, update the synthesis with rationale/confidence change, record contrary evidence, and state what changed in the final readout.
18. **A research cycle suggests a new rule for how future evidence should be judged.** Expected: create/report a `GUARDRAIL CANDIDATE`; do not autonomously rewrite AGENTS.md/governance/evidence-derived-guardrails without explicit GitHub change authorization.
19. **User asks only for today's research prompt.** Expected: `daily-discipleship-research-prompt` stays in PROMPT_ONLY mode and does not launch deep research.
20. **User gives an already-defined research contract and says "do the research."** Expected: route directly to `discipleship-deep-research-executor`; do not rerun agenda selection unless necessary to resolve a material scope conflict.


21. **A full research cycle completes successfully.** Expected: preserve the raw executor report first, then after independent verification and Brain-impact decisions route to `discipleship-research-report-publisher`; produce a professional PDF plus editable master when tools permit, with the PDF treated as the primary human-reading artifact.
22. **The raw research report contains a strong claim that verification downgrades.** Expected: the final published PDF uses the corrected/downgraded wording and confidence, not the original executor wording.
23. **A published research PDF has a bibliography but no claim-level citations.** Expected: fail publication QA; supported consequential claims must carry nearby source keys such as `[S4]`, and every key must map to the source ledger.
24. **A research PDF exports successfully but contains clipped text, broken table rows, or missing glyphs.** Expected: not finished; render every page to images, fix layout, re-export, and re-inspect before claiming publication success.
25. **A user reads only the first three pages of a research report.** Expected: those pages still communicate the research question, evidence-weighted answer, 3–6 biggest findings, confidence, evidence boundary, why it matters, and the main Brain impact.
26. **PDF generation capability is unavailable during a full cycle.** Expected: preserve the structured final content and report `PDF PUBLICATION BLOCKED`; do not invent a file/link or silently substitute a plain-text artifact as the requested PDF.


27. **User asks, "What should Southbrook actually do to help ordinary people begin discipling someone?"** Expected: route to `full-discipleship-practice-design-cycle`, start with the local problem/current reality, retrieve existing synthesis and Practice Intelligence, scan concrete practices if needed, assess Southbrook fit/action warrant, and design the smallest responsible test rather than launching another generic empirical review.
28. **A practice is used by several respected churches but has little direct causal outcome research.** Expected: classify the practice precedent honestly, inspect mechanism evidence and failure modes, and allow `SMALL-TEST CANDIDATE` or `PILOT CANDIDATE` status when theology/local fit/risk/reversibility warrant it; do not call it proven.
29. **A practice has strong adjacent research support but is highly staff-dependent and does not address Southbrook's actual bottleneck.** Expected: the fit assessor may return `NOT NOW / POOR FIT` despite strong mechanism evidence.
30. **A low-risk six-week test and a church-wide permanent restructuring are supported by the same thin evidence base.** Expected: the small test may be warranted; the church-wide restructuring is not. Evidence threshold rises with scale/risk/irreversibility.
31. **A case-study report contains useful operational practice detail but no new high-confidence principle.** Expected: create/route Practice Cards to the Practice Intelligence Library; do not force the content into Living Synthesis.
32. **A full research cycle uncovers a concrete apprenticeship practice.** Expected: verify effect claims separately, preserve the durable principle only if warranted, and capture the concrete apprenticeship method as Practice Intelligence without automatically recommending it to Southbrook.
33. **A Southbrook pilot is adopted poorly.** Expected: measurement separates implementation failure (reach/adoption/fidelity/burden) from mechanism/outcome failure; do not conclude the underlying principle is disproven merely because implementation was weak.
34. **A Southbrook pilot produces promising local learning.** Expected: update Experiments/Pilots & Learning and local practice status; do not automatically convert one local pilot into a universal high-confidence Living Synthesis principle.
35. **User asks only, "How do credible churches actually do family discipleship at home?"** Expected: route to `discipleship-practice-intelligence-builder`; create concrete Practice Cards/comparison and stop before selecting a Southbrook practice unless asked.
36. **Practice Card includes an organizational outcome claim.** Expected: label it REPORTED OUTCOME/ORGANIZATIONAL CLAIM, pair with independent evidence when available, and do not merge it into DOCUMENTED PRACTICE merely because the practice itself is well documented.


37. **A Southbrook pilot finishes and leaders ask whether to scale it.** Expected: route to `discipleship-pilot-learning-evaluator`; compare actual results with the original hypothesis/decision criteria, analyze implementation and discipleship outcomes separately, update the local action warrant, and only then route to a decision brief if broader action is warranted.
38. **A pilot's participants report enthusiasm but fidelity was low and no reproduction occurred.** Expected: do not call the practice effective; classify the result as implementation/insufficient-evidence learning and recommend adapt/repeat/stop as warranted.
39. **A pilot was implemented with high fidelity but the expected discipleship outcome did not appear.** Expected: distinguish this from implementation failure and treat it as evidence that the proposed mechanism/practice may need adaptation or rejection locally.


40. **A pilot has been selected and the user says, "Make this ready for ordinary leaders to run."** Expected: route to `discipleship-practice-implementation-kit-builder`; create minimum viable leader/participant/training/coaching/checklist assets, distinguish fidelity essentials from adaptable elements, and do not relitigate the practice choice unless a material design conflict appears.
41. **An implementation kit becomes a 70-page curriculum that requires staff to teach every week.** Expected: simplify; the skill should protect ordinary-person reproducibility and reduce unnecessary staff dependence rather than equating volume with quality.
