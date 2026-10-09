# Tests

The tests here are scenario/behavior checks for the assistant's operating system. They are not unit tests for a software package.

A future automation layer can convert these into executable evaluations. For now, use `tests/scenarios.md` during meaningful architecture or skill changes.

## Principle synthesis acceptance checks

Use `tests/principle-synthesis-cases.md` for four guided dry runs and `tests/scenarios.md` for adversarial cases 53–64. A structural contract check is possible by inspecting the repo routing, skill, and template text; **it does not prove the reasoning skill has been executed successfully**. A meaningful behavioral check must use actual accessible original evidence, produce a candidate disposition, and verify that repeated AI reports do not create false source independence or unsupported knowledge promotion.

Record the topic/source boundary, candidate disposition, independent source families, evidence limitations, artifact/index write status, and whether each expected behavior passed. Never label an unperformed scenario PASS.
