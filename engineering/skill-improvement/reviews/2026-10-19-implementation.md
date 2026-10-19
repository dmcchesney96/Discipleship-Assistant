# Skill improvement implementation and initial evaluation — 2026-10-19

Built and tested on an isolated branch from upstream `202c95a0ba4214db6f966c369653ffd414b1bf4a`. Human review is pending; no merge, deployment or installed-skill synchronization is authorized by these results.

## What exists now

- Dedicated `discipleship-skill-improvement-loop` skill with UI metadata, representative evaluation tasks and a local Python ledger/gate.
- Closed sanitized cycle records; pinned skill versions, observations, retries, separate root-cause judgments and issue backlog.
- Atomic memory, immutable attempt identity, unique-cycle batch frequency, critical override, checkpoints, idempotent replay and local writer locking.
- Fixed paired-evaluation contract with hashes, eleven dimensions, seven hard gates, replay/held-out requirements, distinct evaluator attestation and conservative recommendations.
- Per-batch limits for candidate count, reported cost/time/iterations/retries. The agent must reserve resources before calls; Python does not meter or stop external models.
- Manager-owned post-research collection hook and existing checkpoint handoff. Research outputs are saved first; hook failures stay separate.
- Proposal template, engineering records, old/new code experiment, reproducible tests and CI integration.

The existing specialist bodies and the research-cycle body are unchanged. AGENTS.md, mission, theological/safeguarding boundaries, approval rules, Brain research content and Drive permissions are unchanged. Proposed manager, routing, registry, checkpoint and CI wiring require human review of this draft PR. No background schedule or service was created.

## Reused and missing components

Reused existing cycle checkpoint, T1–T5 evaluation definitions, synthesis/recovery fixtures, check_skills.py, check_principle_contract.py, test_skill_validation.py, existing Actions job and dated historical test reports. Historical reports were inspected as inherited evidence; their claimed runs were not relabeled as new executions. No runtime research service, model-metering integration or scheduled improvement runner was found in the inspected tree. The new system supplies agent instructions plus deterministic local infrastructure, not a replacement research engine.

## Executed tests

| Test | Actual result | Limit |
|---|---|---|
| New deterministic improvement suite | 27 passed | Synthetic packets/reported grades; no semantic truth certification |
| Existing validator regression suite | 9 passed | Metadata/registry handling only |
| Combined unittest discovery | 36 passed | Local Python |
| Skill metadata/registry/taxonomy | 39 skills passed | Static; does not prove host discovery |
| Existing synthesis contract | 12 files passed | Structural markers, not reasoning |
| New skill quick validator | Passed | Frontmatter/name only |
| Local workflow/diff checks | Passed | Remote CI status belongs to GitHub checks |
| Fresh improvement-skill use | Collect → critical batch → review/finish → repeated collection/finish/resume, one record and one batch; no duplicates | Synthetic tool observation; no source receipt bytes, no live connector fault |
| Full local improvement pipeline | Collect → batch → isolated code candidate → same-input probes → compare → finish | Correctly returned INCONCLUSIVE for broad skill quality; code tests alone do not supply semantic rubric/held-out evidence |
| Independent code review | Five defects reproduced and corrected; fresh no-patch/excluded-cycle lifecycle passed | Local synthetic software evidence only |
| Bounded verification on actual attachments | Two consequential claims checked against two live originals; numeric result supported in narrow context; another required qualification; duplicate formats/source-family dependence retained | No whole-report audit, Brain comparison or Drive write |

Detailed evidence: [forward review](forward-2026-10-19/review.md), [independent code review](code-review-2026-10-19/review.md), [live-source engineering receipt](verification-2026-10-19/review.md), [code experiment](../experiments/ledger-hardening/proposal.md). Full research excerpts/audit remain outside GitHub; only the sanitized engineering receipt is included.

## Initial existing-specialist trials

A fresh task agent received raw synthetic packets and task scope, without evaluation assertions or intended fixes. Its outputs are in specialists-2026-10-19. The following are manual assessments of observed output artifacts, not automated grades or paired original/revision trials.

| Skill | Work actually performed | Assessment and evidence limit |
|---|---|---|
| full-discipleship-research-cycle | Recovery/checkpoint readout | Kept INDEX OUT OF SYNC, unknown historical stages and denied source explicit; did not launch new research or claim recovery writes |
| discipleship-deep-research-executor | Complete bounded packet-based content report, claim register and source ledger | Actual report produced; source originals unavailable; no theological or church-outcome proof invented |
| ai-research-verification-integration | Separate fresh live-source pass on assigned actual attachments | Original-source reopening/access depth demonstrated for two claims; no whole-corpus or full-cycle claim |
| living-discipleship-synthesis-maintainer | Proposed PR-017 correction | Retained identity/history and null result; counted A/B once; removed unsupported timetable/G2 inference; no live sync |
| discipleship-research-report-publisher | Publication handoff and QA/exclusion disposition | Final-content/citation/QA obligations explicit; PDF/DOCX production excluded by bounded test scope, so rendering is NOT TESTED |
| discipleship-research-librarian-drive-curator | Proposed operation ledger | Raw/derived identity distinguished, live targets unresolved, no guessed IDs or successful filing claimed; live filing NOT TESTED |

No genuine instruction defect in these existing specialists was established by this bounded evidence. Retain them; do not claim improved research accuracy, practical outcomes or quality without fresh paired trials. Full original T1–T5 suite and production publication/Drive workflow were not rerun. Research content was not integrated into the Brain during this engineering assignment.

## Changes that testing actually improved

The initial new ledger had five software defects documented by an independent reviewer. The identical probe program was run against the saved initial code and corrected code:

1. Duplicate replay/held-out input was accepted; now rejected.
2. Allowed second trial of the same candidate was rejected as another candidate; now accepted within iteration budget.
3. A symlink into skills/ passed experimental-path isolation; now rejected using canonical paths.
4. An unreviewed new failure inherited an old review's NO_CHANGE; now stays OPEN with per-run review coverage.
5. An unchanged rejected candidate could be recommended by later altered scores; rejection now persists and the test/input/baseline/proposal contract stays pinned.

A new regression test also exposed input-object aliasing; saved records now take defensive copies. All 27 new tests pass after correction. Saved baseline/candidate code and before/after probe outputs permit reproduction. The extra no-patch lifecycle was introduced independently after the fixes and passed; this is useful generalization evidence for local bookkeeping, not held-out LLM skill superiority.

The demonstration gate intentionally returned INCONCLUSIVE: rubric dimensions for real research quality are unknown, method is static code probing, and no held-out behavioral research trial was supplied. This is expected safe behavior. Deterministic bug fixes are included in the implementation PR; no experimental rewrite of an existing research specialist is proposed.

## Operation, approval and limits

After human review and merge, future agents loading the manager instructions collect after each research cycle, review after three unique cycles or a critical failure, and prepare bounded proposals/draft PRs. Defaults allow 10 cycles/batch, 1 distinct candidate, 2 iterations, 1 retry, 300 seconds and USD 2 reported external cost. They are configurable in config/skill-improvement.json. No unattended process runs between requests; host Skills-page copies need separate synchronization if desired. Before merge, invoke the new skill explicitly from this branch.

`engineering/skill-improvement/memory.json` starts empty: synthetic tests and historical reviews are not fabricated production research cycles. Their records are separate under reviews/experiments. Resume from saved batch IDs, artifacts and branch commit. A successful local write is not a remote save until the branch is pushed and verified.

Remaining limits: honest scoring, fresh evaluator identity, true held-out novelty, semantic privacy, source accuracy and real usage metering require evidence and reviewer judgment. Local locking is not distributed GitHub/Drive concurrency. A full live cycle with post-run GitHub collection, publication rendering, real connector interruption and original-versus-revised specialist trial remains untested. Human approval is required to merge; nothing automatically merges or changes mission/governance/Drive permissions.
