# Skill Routing

Use the narrowest skill that owns the requested work. Do not run a chain of skills merely because it is available.

| User intent | Primary skill |
|---|---|
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

### New AI report
`intake → ai verification → compare-big-picture when the user wants a readable cross-report view → living synthesis only if durable conclusions change`

### Topic synthesis / "bring all this research together"
`context/relevant assessed evidence → compare-big-picture → living synthesis only if a durable project conclusion should change`

### New interview batch
`intake → qualitative analyzer → diagnostic → pattern connector → experiment/decision only if warranted`

### Strategy question
`context retriever → current-state synthesizer → evidence checker → decision brief`

### New external church to study
`source ingestor → case-study analyzer → evidence checker → synthesis maintainer`

### Experiment lifecycle
`diagnostic/synthesis → pilot designer → measurement architect → results → current-state/synthesis/decision update`

## Stop rule

If the requested result is already supported, stop. A handoff is useful only when it adds new evidence, a required transformation, or an authorized next action.


## Natural-language auto-trigger

The user never needs to say the skill name.

Automatically use `compare-big-picture` whenever the user asks to compare, review, synthesize, bring together, or identify the biggest learnings/common themes across a **specified group of Brain files, reports, a folder, or a bounded topic collection**.

Respect the user's stated source boundary. Do not widen "these files" into the whole Brain unless requested.
