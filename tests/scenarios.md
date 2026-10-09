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


42. **User says, "Go backward through the whole Exponential folder and AI research folder and mine them for practical discipleship practices."** Expected: route to `discipleship-practice-intelligence-backfill`; inventory the entire corpus, deduplicate alternate formats/source families, triage by practice yield, deeply mine high/medium-yield material, merge similar practices into families, create/update Practice Cards and landscapes, and preserve a backfill manifest rather than summarizing every file independently.
43. **The corpus contains a PDF, transcript, and audio episode for the same AI research project.** Expected: preserve all artifacts but treat them as one source family / alternate formats rather than three independent signals.
44. **Six Exponential books describe versions of leader apprenticeship.** Expected: create/update one apprenticeship practice family with meaningful variants and multiple source links, not six near-duplicate Practice Cards.
45. **A low-practice-yield resource contains no unique discipleship process after triage.** Expected: inventory it as REFERENCE_ONLY and do not spend disproportionate extraction effort.

46. **User says, "Use the Brain and build the full eight-week Bible-study class with everything we need."** Expected: route to `full-discipleship-curriculum-build-cycle`; retrieve only the relevant Brain evidence, audit source gaps, do targeted research/verification only where material, define the final authentic capability, build the full course + assessment/transfer + run-ready assets, and preserve PROPOSED vs APPROVED status without asking for separate prompts between stages.
47. **A curriculum request causes the assistant to load/summarize the entire Discipleship Brain before designing the course.** Expected: fail the retrieval discipline; use the smallest sufficient topic-bounded evidence set and stop retrieving when additional material is unlikely to change the design.
48. **An eight-week skill-building curriculum consists mostly of eight lectures and a final knowledge quiz.** Expected: fail curriculum QA; route to `discipleship-curriculum-architect` and redesign around authentic capability, modeling, guided/independent practice, feedback, responsibility transfer, between-session repetition, and fresh-task transfer.
49. **A Bible-study curriculum uses an AI-generated report as the sole support for a consequential hermeneutical claim.** Expected: do not teach the claim as established; verify against Scripture, responsible scholarship/primary theological sources, and relevant Southbrook doctrinal/pastoral guardrails before using it as course authority.
50. **Participants can confidently repeat the Bible-study method on the same practiced passage but have never tried an unfamiliar passage.** Expected: do not label the skill transferred; use fresh-passage performance and textual/contextual reasoning as a transfer signal, with access to wise resources/help preserved.
51. **The course aims for multiplication, so a new participant is immediately released to teach the entire method independently.** Expected: distinguish early bounded helping from full teaching authority; match reproduction responsibility to demonstrated competence, observation, correction, and coaching.
52. **User asks only, "Give me a week-by-week outline for an eight-week prayer course using this existing evidence packet."** Expected: route directly to `discipleship-curriculum-architect`; do not automatically launch the full curriculum-build orchestrator or new external research unless a material source gap blocks responsible design.


53. **A Practice Intelligence backfill creates 20+ cards and several landscapes but leaves no navigation/index artifact.** Expected: do not treat the backfill as finished; create/update a concise Practice Intelligence Library Index and cross-corpus synthesis so pastors can navigate the library without opening every file.
54. **A large external backfill is complete, but the Southbrook current-state/diagnostic folders contain no verified current-reality evidence.** Expected: do not jump straight to a whole-church fit recommendation; report the diagnostic readiness gap, identify practice families ready for later fit assessment, and route to diagnostic/current-state work first.
55. **Further corpus mining mostly repeats practice families already captured with no meaningful new variants, mechanisms, failure modes, or transferability conditions.** Expected: mark the backfill COMPLETE ENOUGH FOR DESIGN USE and stop broad extraction; route only targeted verification, case study, or local-fit gaps onward.

### Principle synthesis and historical-backfill acceptance

53. **Two AI reports paraphrase the same peer-reviewed study.** Expected: one independent source family; do not raise confidence due to two reports; trace original study.
54. **A strong meta-analysis shows students learn more by teaching, but no church follow-up data exists.** Expected: mechanism support; do NOT report proven G2/G3 disciple-maker reproduction.
55. **Five respected churches use apprenticeship, but public outcome data are only marketing.** Expected: DOCUMENTED PRACTICE / REPEATED PRACTICE PATTERN if independently sourced; PROMISING mechanism may be reasonable; not established causal effectiveness.
56. **A new review directly challenges an existing high-confidence principle.** Expected: precise contradiction and quality comparison, preserve old version, narrow/downgrade if warranted; update topic and Master Index together.
57. **Same claim appears under two topic domains.** Expected: one stable principle ID, one topic owner, cross-links from other domains; no duplicate row in Master Index.
58. **Historical corpus has 120 files but the agent opens only 12.** Expected: 120 INVENTORIED, 12 DEEP REVIEWED (or fewer), explicit remaining/deferred count and resume checkpoint; cannot declare 120 assessed.
59. **An original reference is inaccessible and verification cannot establish its claim.** Expected: research lead/verification queue only; no current high-confidence principle created.
60. **An existing synthesis uses BRP01–BRP06 stable IDs.** Expected: retain legacy identifiers or explicit aliases, no silent renumbering; register in thin index as existing working records.
61. **Master Index write works but topic synthesis write fails.** Expected: report INDEX OUT OF SYNC and recovery action; no claim that the knowledge update is complete.
62. **A source reports four generations of churches, while recommendation claims four generations of individual disciple-makers.** Expected: fail the claim; multiplication unit must be explicit.
63. **Candidate repeats an already-covered principle without new independent source/outcome/context.** Expected: NO DURABLE CHANGE; do not create a new record.
64. **One-month pilot gives favorable attendance but no formation/reproduction evidence.** Expected: local participation learning only; no universal principle or proved generational outcome.

See `tests/principle-synthesis-cases.md` for a concrete bounded test packet and `docs/principle-synthesis-system.md` for the required index/provenance contract.
