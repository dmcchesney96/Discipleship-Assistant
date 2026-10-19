# Ledger hardening — controlled implementation experiment

Date: 2026-10-19. Target: the newly implemented improvement ledger, before integration; no existing research specialist revision.

Observed evidence: independent code-review probes in ../../reviews/code-review-2026-10-19/repro.py and baseline-results.json establish five defects in the initial implementation: duplicate replay/held-out bytes accepted; one candidate's second allowed trial rejected as another candidate; lexical experiment path permits a symlink into skills/; later unreviewed failure inherits an old review disposition; and a previously rejected unchanged candidate can receive a later recommendation with altered scores.

Cause: deterministic validation and state accounting defects, not research model behavior. The proposed patch resolves artifact paths canonically, counts distinct candidate hashes with cumulative trial budgets, disallows reuse of an input hash across splits, tracks issue review coverage per run, pins each candidate's evaluation contract and retains earlier rejection. Defensive deep copies prevent callers from mutating saved history through input references (discovered by a new regression case).

Expected effect: credible evaluation bookkeeping and isolated experiments. Risk: stricter acceptance can defer otherwise useful changes; that is intentional pending review. No standard, mission, approval or specialist purpose is weakened. The paired fixture outputs are synthetic; a RECOMMEND_REVIEW value inside a probe is the algorithm's reported decision, not a real improvement adoption.

Tests: run the exact same five independent probes against baseline.py and candidate.py, plus the full deterministic regression suite. New cases exercise changed test contracts, mutation, and pending work. Results are in ../../reviews/code-review-2026-10-19/. These are software behavior tests; no LLM original-versus-revision research trial was performed. Broad skill-quality evidence remains INCONCLUSIVE. No existing specialist patch is proposed from insufficient evidence.

Budget: local Python only, no paid model API calls by this experiment. Agent engineering time is outside the future post-research batch budget; do not report unknown host usage as measured zero. The demonstration packet records only its local CLI execution cost/time.

Rollback: restore baseline.py only in an isolated branch to reproduce bugs; revert the integration PR if needed. Baseline is retained for reproducibility, never installed into production. Human review of the draft PR is pending.

Privacy review: code, synthetic test inputs and sanitized engineering receipts only; no ministry corpus. Resume: run repro.py against both pinned files and the unit suite, inspect any mismatch before creating a new candidate. Do not rewrite previous results as a new historical run.
