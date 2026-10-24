# Tests

The tests here are scenario/behavior checks for the assistant's operating system. They are not unit tests for a software package.

A future automation layer can convert these into executable evaluations. For now, use `tests/scenarios.md` during meaningful architecture or skill changes.

## Practical learning acceptance cases

Use `tests/practical-learning-cases.md` to evaluate source-faithful teaching, usable tool creation, honest partial coverage, routing, and save verification. Cases are supplied for later behavioral runs and are marked NOT RUN until observed. Metadata/registry validation does not certify teaching quality or live Brain operations.

## Principle synthesis acceptance checks

Use `tests/principle-synthesis-cases.md` for four guided dry runs and `tests/scenarios.md` for adversarial cases 53–64. A structural contract check is possible by inspecting the repo routing, skill, and template text; **it does not prove the reasoning skill has been executed successfully**. A meaningful behavioral check must use actual accessible original evidence, produce a candidate disposition, and verify that repeated AI reports do not create false source independence or unsupported knowledge promotion.

Record the topic/source boundary, candidate disposition, independent source families, evidence limitations, artifact/index write status, and whether each expected behavior passed. Never label an unperformed scenario PASS.


## Research and synthesis evaluations

Use tests/research-synthesis-evals.json for five realistic cases. Resolve real source artifacts from the supplied input or Drive; keep that corpus out of GitHub. Synthetic packets are in tests/fixtures.

For each case, start a fresh task session with the pinned repo, prompt, input artifacts and separate output directory. Do not expose assertions, diagnoses, expected answers or proposed fixes to the task agent. Grade afterward with concrete artifact locators. Compare against the previous skill version or a no-skill control using the same input. Record manual semantic results separately from deterministic checks, source-access limits and excluded writes/publication. Repeat selected cases before claiming reliability. These JSON cases are not an automatic semantic CI runner.

Run `python tests/check_skills.py` (PyYAML required) as well as the existing structural marker check. Neither executable check certifies research reasoning or live connector reliability.

Run validator regression cases with python -m unittest discover -s tests -p test_skill_validation.py. Keep semantic results in a dated test-run record with exact source boundaries and whether results were observed or simulated.

## Native document formatting regression

Run `node --test tests/test_native_text_ranges.mjs` (Node 22+) before native Docs branding work. CI runs the same checks. They verify UTF-16 endpoints and detect a smaller trailing character; they do not replace actual Drive content/style read-back or rendered-page inspection.
