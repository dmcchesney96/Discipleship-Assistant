# Skill Routing

Use the narrowest skill that owns the requested work. Do not run a chain of skills merely because it is available.

| User intent | Primary skill |
|---|---|
| Run the entire research process from gap/question through report, verification, Brain updates, and final readout | `full-discipleship-research-cycle` |
| Run the practical workflow from Southbrook problem through practice options, fit, and test/pilot design | `full-discipleship-practice-design-cycle` |
| Build concrete practice options/Practice Cards from churches, books, movements, or research | `discipleship-practice-intelligence-builder` |
| Assess candidate practices for Southbrook fit and action warrant | `southbrook-practice-fit-assessor` |
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
`local context/diagnostic → practice intelligence → selective case-study deep dives → mechanism/evidence backbone → Southbrook practice-fit assessment → pilot designer → measurement architect → decision brief when needed → local learning`

Use this when the user asks **what Southbrook should do/how to implement**, not when they only want the evidence landscape.

### New AI report
`intake → ai verification → compare-big-picture when the user wants a readable cross-report view → living synthesis only if durable conclusions change`

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
`diagnostic/synthesis → pilot designer → measurement architect → results → current-state/synthesis/decision update`

## Stop rule

If the requested result is already supported, stop. A handoff is useful only when it adds new evidence, a required transformation, or an authorized next action.


## Natural-language auto-trigger

The user never needs to say the skill name.

Automatically use `full-discipleship-research-cycle` when the user clearly asks for the research process to continue from existing-Brain retrieval/gap selection through prompt/contract creation, actual research, report preservation, verification, evaluation, and warranted Brain updates **without stopping for separate prompts between stages**.

This full-cycle trigger takes precedence over prompt-only or compare-only routing.

Automatically use `full-discipleship-practice-design-cycle` when the user asks for a complete practical path from a Southbrook discipleship problem to concrete external practices, contextual fit, and a bounded test/pilot.

Automatically use `discipleship-practice-intelligence-builder` when the user asks what churches/practitioners actually do or wants concrete practice options/Practice Cards without yet asking for local selection.

Automatically use `southbrook-practice-fit-assessor` when candidate practices are already known and the question is which are worth exploring/testing locally and why.

Automatically use `compare-big-picture` whenever the user asks to compare, review, synthesize, bring together, or identify the biggest learnings/common themes across a **specified group of Brain files, reports, a folder, or a bounded topic collection**.

Respect the user's stated source boundary. Do not widen "these files" into the whole Brain unless requested.
