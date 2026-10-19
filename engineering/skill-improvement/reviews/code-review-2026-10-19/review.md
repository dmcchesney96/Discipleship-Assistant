# Independent implementation review — 2026-10-19

Scope: `improvement_loop.py`, its unit tests, the improvement skill, and system documentation. Read repository `AGENTS.md` first. Work was local and used synthetic temporary files only. No production edits, network calls, ministry data, or live writes were made by this reviewer.

The original 22 unit tests passed. Additional probes found these actionable software defects; the implementation owner made the corrections separately.

| Finding | Reproduction and effect | Required correction |
|---|---|---|
| Duplicate held-out input | Bind the replay and held-out cases to the same raw input artifact/hash. Original returns `RECOMMEND_REVIEW`. | Reject identical input hashes across the two splits. This prevents an exact duplicate; it does not certify unseen status. |
| Candidate limit counts packets | Submit two evaluations for the identical candidate, each using one iteration. With defaults (one candidate, two iterations), original rejects the second as over budget. | Count distinct candidate hashes; continue accumulating reported resource use. |
| Experimental path alias | Point an experimental candidate symlink to a file under `skills/`. Original accepts it because the experimental-prefix check uses the lexical path. | Check the canonical repository-relative path. This is a path-isolation check, not a sandbox or semantic security claim. |
| New issue inherits old review | Collect another failure for the same issue while a batch is active, then close that batch as `NO_CHANGE`. Original marks the whole backlog issue `NO_CHANGE` although the new run was outside that batch. | Bind review dispositions to covered run IDs; keep unreviewed occurrences open. |
| Unchanged failed candidate later recommended | With a valid two-candidate limit, first report a candidate citation-gate failure; resubmit the identical candidate/case artifacts with that grade changed to PASS. Original can recommend it without resolving the prior rejection. | Preserve a rejection for the same candidate and bind its baseline, proposal and case/input contract across iterations. A different grading claim alone must not erase a rejection. |

`repro.py` exercises these cases and prints JSON. `baseline-results.json` and `revised-results.json` are separately captured results; their scope is determined by the scenarios listed inside each packet. `current-results.json` was an interim run, not the original baseline. Final verification is recorded in `final-results.json`: all five defect probes now show the required behavior. A fresh no-patch lifecycle probe collects three explicitly excluded cycles, closes their issue-free review, repeats closure idempotently, and preserves all three runs; it passes. The final 27 unit tests pass.

The Python gate checks a reported contract. It cannot establish source truth, evaluator independence, unseen inputs, honest scores, privacy of narrative artifacts, actual model usage, or successful live integration. The documentation correctly describes these as evidence/reviewer responsibilities. No behavioral skill-quality or semantic-safety certification follows from these synthetic probes.
