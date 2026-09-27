# Skills

The skill library has two layers.

## Shared ministry intelligence core

Reusable across ministry assistants:

1. `ministry-second-brain-intake`
2. `ministry-context-retriever`
3. `current-state-synthesizer`
4. `source-evidence-checker`
5. `knowledge-conflict-resolver`
6. `decision-action-extractor`
7. `institutional-memory-writer`
8. `pattern-connector`

## Discipleship-specific skills

1. `discipleship-research-source-ingestor`
2. `daily-discipleship-research-prompt`
3. `discipleship-research-scout-agenda-builder`
4. `ai-research-verification-integration`
5. `church-movement-case-study-analyzer`
6. `southbrook-interview-qualitative-evidence-analyzer`
7. `southbrook-discipleship-diagnostic`
8. `living-discipleship-synthesis-maintainer`
9. `discipleship-measurement-architect`
10. `discipleship-experiment-pilot-designer`
11. `southbrook-discipleship-operating-system-designer`
12. `discipleship-research-librarian-drive-curator`
13. `strategy-decision-brief-builder`

## Skill rule

A skill owns one bounded transformation. The master assistant chooses which skill(s) to use and which tools/evidence sources are appropriate. Skills should not independently trigger expensive chains of other skills unless a calling workflow explicitly requests that handoff.

Each skill inherits `AGENTS.md` and governance rules.
