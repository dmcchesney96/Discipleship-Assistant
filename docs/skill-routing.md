# Skill Routing

Use the narrowest skill that owns the requested work. Do not run a chain of skills merely because it is available.

| User intent | Primary skill |
|---|---|
| Add a new research/source set to the Brain | `discipleship-research-source-ingestor` |
| Generate today's next Genspark prompt | `daily-discipleship-research-prompt` |
| Decide what the next research agenda should be | `discipleship-research-scout-agenda-builder` |
| Evaluate AI-generated research and verify claims | `ai-research-verification-integration` |
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
`intake → ai verification → (case study/pattern analysis if needed) → living synthesis only if conclusions change`

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
