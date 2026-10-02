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
3. `discipleship-research-report-publisher` — creates the reusable professional PDF + editable master
4. `full-discipleship-practice-design-cycle` — orchestrates local problem → practice → fit → test/pilot
5. `discipleship-practice-intelligence-builder` — creates concrete external Practice Cards and comparisons
6. `southbrook-practice-fit-assessor` — evaluates local fit and action warrant
7. `discipleship-pilot-learning-evaluator` — evaluates local pilot results and updates action warrant
8. `discipleship-practice-implementation-kit-builder` — creates ready-to-run tools/training for selected pilots
9. `discipleship-research-source-ingestor`
10. `daily-discipleship-research-prompt`
11. `discipleship-research-scout-agenda-builder`
12. `ai-research-verification-integration`
13. `compare-big-picture`
14. `church-movement-case-study-analyzer`
15. `southbrook-interview-qualitative-evidence-analyzer`
16. `southbrook-discipleship-diagnostic`
17. `living-discipleship-synthesis-maintainer`
18. `discipleship-measurement-architect`
19. `discipleship-experiment-pilot-designer`
20. `southbrook-discipleship-operating-system-designer`
21. `discipleship-research-librarian-drive-curator`
22. `strategy-decision-brief-builder`

## Skill rule

A skill owns one bounded transformation. The master assistant chooses which skill(s) to use and which tools/evidence sources are appropriate. Skills should not independently trigger expensive chains of other skills unless a calling workflow explicitly requests that handoff.

`full-discipleship-research-cycle` and `full-discipleship-practice-design-cycle` are intentional orchestrator exceptions. Their bounded job is to manage complete handoff sequences while leaving research, practice intelligence, fit assessment, verification, synthesis, pilot design, measurement, and library work to the specialist skills.

Each skill inherits `AGENTS.md` and governance rules.
