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

1. `full-discipleship-research-cycle` — explicit multi-skill orchestrator for one-command research
2. `discipleship-deep-research-executor` — conducts a defined deep research contract
3. `discipleship-research-source-ingestor`
4. `daily-discipleship-research-prompt`
5. `discipleship-research-scout-agenda-builder`
6. `ai-research-verification-integration`
7. `compare-big-picture`
8. `church-movement-case-study-analyzer`
9. `southbrook-interview-qualitative-evidence-analyzer`
10. `southbrook-discipleship-diagnostic`
11. `living-discipleship-synthesis-maintainer`
12. `discipleship-measurement-architect`
13. `discipleship-experiment-pilot-designer`
14. `southbrook-discipleship-operating-system-designer`
15. `discipleship-research-librarian-drive-curator`
16. `strategy-decision-brief-builder`

## Skill rule

A skill owns one bounded transformation. The master assistant chooses which skill(s) to use and which tools/evidence sources are appropriate. Skills should not independently trigger expensive chains of other skills unless a calling workflow explicitly requests that handoff.

`full-discipleship-research-cycle` is the intentional exception: it is an orchestrator whose bounded job is to manage the complete handoff sequence while leaving research, verification, comparison, synthesis, and library work to the specialist skills.

Each skill inherits `AGENTS.md` and governance rules.
