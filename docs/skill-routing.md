# Skill Routing

Use the narrowest skill that owns the requested work. Do not run a chain of skills merely because it is available.

| User intent | Primary skill |
|---|---|
| Capture Dan's own discipleship philosophy, strategy instincts, curriculum feedback, what rings true/false, or what should/should not be included | `discipleship-convictions-capture` |
| Retrieve Dan's stored convictions/preferences to shape substantial strategy, system, curriculum, Bible-study, training, or implementation work | `discipleship-alignment-lens-retriever` |
| Run the entire research process from gap/question through report, verification, Brain updates, and final readout | `full-discipleship-research-cycle` |
| Run the practical workflow from Southbrook problem through practice options, fit, and test/pilot design | `full-discipleship-practice-design-cycle` |
| Run an end-to-end multi-session curriculum build from relevant Brain retrieval through gap research, course design, assessment, and run-ready assets | `full-discipleship-curriculum-build-cycle` |
| Design/redesign a discipleship course, class, syllabus, or week-by-week curriculum from a defined outcome/evidence base | `discipleship-curriculum-architect` |
| Build concrete practice options/Practice Cards from churches, books, movements, or research | `discipleship-practice-intelligence-builder` |
| Mine a large historical research/library corpus into deduplicated Practice Intelligence | `discipleship-practice-intelligence-backfill` |
| Assess candidate practices for Southbrook fit and action warrant | `southbrook-practice-fit-assessor` |
| Evaluate completed/in-progress Southbrook pilot results and decide what was learned | `discipleship-pilot-learning-evaluator` |
| Build ready-to-run training/tools/coaching assets for a selected pilot/practice | `discipleship-practice-implementation-kit-builder` |
| Apply Southbrook logo/colors/typography/style to a ministry-facing DOCX/PDF/slide/handout/tool | `southbrook-brand-artifact-stylist` |
| Create Southbrook weekly public Message Notes / sermon-outline handout from a sermon manuscript or outline | `southbrook-sermon-notes-artifact-builder` |
| Conduct a defined research contract and produce the complete sourced report | `discipleship-deep-research-executor` |
| Publish a completed research report as the standard professional PDF + editable master | `discipleship-research-report-publisher` |
| Add a new research/source set to the Brain | `discipleship-research-source-ingestor` |
| Generate today's next Genspark prompt | `daily-discipleship-research-prompt` |
| Decide what the next research agenda should be | `discipleship-research-scout-agenda-builder` |
| Evaluate AI-generated research and verify claims | `ai-research-verification-integration` |
| Compare a research collection and explain the biggest learnings/common themes simply | `compare-big-picture` |
| Deep study one church/network/movement | `church-movement-case-study-analyzer` |
| Analyze local interview transcripts qualitatively | `southbrook-interview-qualitative-evidence-analyzer` |
| Build/update local discipleship diagnostic | `southbrook-discipleship-diagnostic` |
| Backfill an existing corpus into traceable, verified durable disciple-making principles (not Practice Cards) | `discipleship-principle-backfill` |
| Update project-level principles/conclusions | `living-discipleship-synthesis-maintainer` |
| Design metrics/scorecards/instruments | `discipleship-measurement-architect` |
| Design a test/pilot | `discipleship-experiment-pilot-designer` |
| Design church-wide integrated system | `southbrook-discipleship-operating-system-designer` |
| Organize/index/curate Drive | `discipleship-research-librarian-drive-curator` |
| Prepare leadership decision memo | `strategy-decision-brief-builder` |
| Process any new ministry knowledge safely | `ministry-second-brain-intake` |
| Retrieve relevant current context | `ministry-context-retriever` |
| Answer “what is true now?” | `current-state-synthesizer` |
| Assess a source/claim's support | `source-evidence-checker` |
| Reconcile conflicting records | `knowledge-conflict-resolver` |
| Extract decisions/actions/owners/dates | `decision-action-extractor` |
| Preserve durable rationale/history | `institutional-memory-writer` |
| Connect patterns across evidence | `pattern-connector` |

## Common sequences

### Full research cycle
`context retriever → scout/redundancy gate → prompt builder (SELF_EXECUTE) → deep research executor → preserve raw report → AI verification → evidence checker → compare-big-picture → pattern connector only if warranted → living synthesis only if warranted → research-report publisher → librarian verify → simple-first readout`

This sequence is used only when the user explicitly requests the whole cycle.

### Full practice / design cycle
`local context/diagnostic → pastoral alignment lens → practice intelligence → selective case-study deep dives → mechanism/evidence backbone → Southbrook practice-fit assessment → pilot designer → measurement architect → implementation kit when requested → decision brief when needed → pilot runs → pilot-learning evaluator → updated local learning/action warrant`

Use this when the user asks **what Southbrook should do/how to implement**, not when they only want the evidence landscape.

### Full curriculum build
`course contract → ministry-context-retriever → pastoral alignment lens → bounded source/gap audit → targeted verification/research only where material → evidence packet → discipleship-curriculum-architect → discipleship-measurement-architect when needed → implementation-kit builder when run-ready assets are requested → artifact creation when requested → curriculum QA → authorized Brain persistence`

Use this when the requested artifact is specifically a complete multi-session curriculum/course/class shaped by the Brain and research.

### Southbrook weekly sermon notes
`southbrook-sermon-notes-artifact-builder → southbrook-brand-artifact-stylist / current series identity → DOCX/PDF production → render/inspect/QA`

Keep public Message Notes distinct from Study Questions. Preserve the preacher's sequence, points, Scripture, and response rather than replacing the sermon with a generic summary.

### Artifact production
`content-owning skill → southbrook-brand-artifact-stylist when Southbrook-facing → artifact-specific production skill → render/inspect/QA`

Use branding as a visual layer after the artifact's ministry purpose and content architecture are clear. Do not let branding make a proposal look approved.

### New AI report
`intake → ai verification → compare-big-picture when the user wants a readable cross-report view → living synthesis only if durable conclusions change`

### Historical evidence-to-principle backfill
`live Brain inventory + source-family map → existing synthesis/index baseline → evidence assessment/verification → compare/pattern → living synthesis only when warranted → Master Principles Index sync → resumable manifest/QA`

Use `discipleship-principle-backfill` only for a user-requested bounded retrospective corpus or whole-Brain synthesis backfill. Concrete practices use `discipleship-practice-intelligence-backfill` instead.

### Topic synthesis / "bring all this research together"
`context/relevant assessed evidence → compare-big-picture → living synthesis only if a durable project conclusion should change`

### New interview batch
`intake → qualitative analyzer → diagnostic → pattern connector → experiment/decision only if warranted`

### Strategy question
If concrete practice options are **not yet known**:
`full-discipleship-practice-design-cycle`

If concrete options are already known and the task is a leadership choice:
`context retriever → current-state synthesizer → southbrook-practice-fit-assessor → decision brief`

### New external church to study
`source ingestor → case-study analyzer → evidence checker → synthesis maintainer`

### Experiment lifecycle
`diagnostic/synthesis/practice-fit → pilot designer → measurement architect → implementation kit when needed → pilot runs → discipleship-pilot-learning-evaluator → practice-fit reassessment → decision/synthesis/current-state update as warranted`

## Stop rule

If the requested result is already supported, stop. A handoff is useful only when it adds new evidence, a required transformation, or an authorized next action.


## Natural-language auto-trigger

The user never needs to say the skill name.

Automatically use `discipleship-convictions-capture` when Dan is substantially expressing his own durable view of discipleship, ministry strategy, Bible/curriculum design, implementation, what rings true, what he dislikes, what should/should not be included, or an unresolved idea he wants the project to keep learning from. Do not trigger on ordinary factual questions, and do not persist when he says not to save the thought.

Automatically use `discipleship-alignment-lens-retriever` before substantial discipleship strategy, system, curriculum, Bible-study, training, implementation, or major revision work when the stored pastoral lens could materially improve fit. Keep the retrieved lens distinct from evidence and approved Southbrook decisions.

Automatically use `full-discipleship-research-cycle` when the user clearly asks for the research process to continue from existing-Brain retrieval/gap selection through prompt/contract creation, actual research, report preservation, verification, evaluation, and warranted Brain updates **without stopping for separate prompts between stages**.

This full-cycle trigger takes precedence over prompt-only or compare-only routing.

Automatically use `full-discipleship-practice-design-cycle` when the user asks for a complete practical path from a Southbrook discipleship problem to concrete external practices, contextual fit, and a bounded test/pilot.

Automatically use `full-discipleship-curriculum-build-cycle` when the user asks for a complete multi-session discipleship curriculum/course/class and wants the Brain/research/resources to shape the build through source-gap analysis, any needed targeted research, full session design, assessment/transfer, and run-ready materials without separate intermediate prompts. This curriculum trigger takes precedence over practice-design and implementation-kit routing when the requested artifact is the curriculum itself.

Automatically use `discipleship-curriculum-architect` when the user asks to design/redesign a syllabus, course outline, week-by-week curriculum, facilitator/participant learning journey, or curriculum architecture from a defined outcome/evidence base but does not request the entire research-to-artifact pipeline.

Automatically use `discipleship-practice-intelligence-builder` when the user asks what churches/practitioners actually do or wants concrete practice options/Practice Cards without yet asking for local selection.

Automatically use `discipleship-principle-backfill` when the user asks to go backward through a substantial existing research corpus, assess cross-source principles, deduplicate claims, and update durable Living Synthesis/central principle indexing. Prefer this over practice backfill when the desired output is principles rather than how-to Practice Cards.

Automatically use `discipleship-practice-intelligence-backfill` when the user asks to go backward through a large existing folder/library of research, books, reports, or transcripts and convert the corpus into Practice Cards, practice families, landscapes, and a deduplicated manifest.

Automatically use `southbrook-practice-fit-assessor` when candidate practices are already known and the question is which are worth exploring/testing locally and why.

Automatically use `discipleship-practice-implementation-kit-builder` when a practice/pilot has already been selected and the user asks to make it ready to run with leader training, participant tools, coaching rhythms, checklists, or troubleshooting.

Automatically use `discipleship-pilot-learning-evaluator` when the user asks what a completed/in-progress Southbrook experiment taught us or whether to stop, adapt, repeat, expand, integrate, or scale.

Automatically use `compare-big-picture` whenever the user asks to compare, review, synthesize, bring together, or identify the biggest learnings/common themes across a **specified group of Brain files, reports, a folder, or a bounded topic collection**.

Respect the user's stated source boundary. Do not widen "these files" into the whole Brain unless requested.


Automatically use `southbrook-brand-artifact-stylist` when Dan asks for a Southbrook-branded/on-brand artifact or when a polished artifact is clearly intended for Southbrook ministry use and branding would materially improve it. Use it as a visual layer after the content-owning skill. Do not brand raw Brain research by default, do not substitute a ministry sub-brand for the church brand, and do not let branding imply approval.


Automatically use `southbrook-sermon-notes-artifact-builder` when Dan asks for the weekly Southbrook Message Notes, sermon outline handout, or a public notes artifact built from a manuscript/sermon outline. Keep Study Questions separate unless explicitly requested. After content shaping, apply current series identity and the Southbrook brand/artifact layer before final DOCX/PDF production.
