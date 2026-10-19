#!/usr/bin/env python3
"""Offline synthetic regression probes; prints reported decisions, not semantic findings."""
from copy import deepcopy
import importlib.util
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[4]
spec = importlib.util.spec_from_file_location('existing_improvement_tests', ROOT/'tests/test_skill_improvement.py')
tests = importlib.util.module_from_spec(spec)
spec.loader.exec_module(tests)
import sys
if len(sys.argv) == 2:
    variant_spec = importlib.util.spec_from_file_location('variant_loop', sys.argv[1])
    variant = importlib.util.module_from_spec(variant_spec)
    variant_spec.loader.exec_module(variant)
    tests.loop = variant
loop = tests.loop


def scenario(name, probe):
    t = tests.ImprovementTests()
    t.setUp()
    try:
        return {'probe': name, **probe(t)}
    finally:
        t.doCleanups()


def duplicate_holdout(t):
    e = t.evaluation()
    e['cases'][1]['input'] = deepcopy(e['cases'][0]['input'])
    try:
        result = loop.compare(t.m, 'batch-01', e, t.root)
        return {'accepted': True, 'decision': result['decision'], 'same_input_hash': True}
    except ValueError as exc:
        return {'accepted': False, 'error': str(exc), 'same_input_hash': True}


def same_candidate_second_iteration(t):
    e = t.evaluation()
    first = loop.compare(t.m, 'batch-01', e, t.root)
    second = deepcopy(e)
    second['evaluation_id'] = 'eval-02'
    result = loop.compare(t.m, 'batch-01', second, t.root)
    return {'first_decision': first['decision'], 'second_decision': result['decision'],
            'budget_exceeded': result['reasons']['budget_exceeded'],
            'same_candidate_hash': e['candidate']['sha256'] == second['candidate']['sha256'],
            'total_reported_iterations': e['usage']['iterations'] + second['usage']['iterations'],
            'limit_iterations': t.c['max_iterations']}


def experimental_symlink(t):
    e = t.evaluation()
    production = t.root/'skills/example/SKILL.md'
    production.parent.mkdir(parents=True)
    production.write_text('production candidate')
    candidate = t.root/e['candidate']['path']
    candidate.unlink()
    candidate.symlink_to(production)
    e['candidate']['sha256'] = loop.file_hash(candidate)
    try:
        result = loop.compare(t.m, 'batch-01', e, t.root)
        return {'accepted': True, 'decision': result['decision'], 'canonical_candidate_under_skills': True}
    except ValueError as exc:
        return {'accepted': False, 'error': str(exc), 'canonical_candidate_under_skills': True}


def unreviewed_failure_status(t):
    r = deepcopy(t.r)
    r['run_id'] = 'new-attempt'
    r['cycle_id'] = 'new-cycle'
    loop.collect(t.m, r)
    key = next(iter(t.m['backlog']))
    review = {'review_artifact': t.artifact('engineering/review.md', 'Synthetic original-run review only'),
              'issues': {key: {'cause': 'tool', 'status': 'NO_CHANGE'}}}
    loop.finish(t.m, 'batch-01', review, t.root)
    return {'issue_status_after_original_batch_closed': t.m['backlog'][key]['status'],
            'new_run_was_in_closed_batch': r['run_id'] in t.m['batches']['batch-01']['run_ids'],
            'new_run_is_in_issue_history': r['run_id'] in t.m['backlog'][key]['run_ids']}


def prior_failed_candidate(t):
    # A valid configurable limit makes this probe applicable to the original script too.
    t.m['batches']['batch-01']['limits']['max_candidates'] = 2
    e = t.evaluation()
    e['cases'][0]['gates']['citations'][1] = 'FAIL'
    first = loop.compare(t.m, 'batch-01', e, t.root)
    second = deepcopy(e)
    second['evaluation_id'] = 'eval-02'
    second['cases'][0]['gates']['citations'][1] = 'PASS'
    result = loop.compare(t.m, 'batch-01', second, t.root)
    return {'first_decision': first['decision'], 'second_decision': result['decision'],
            'same_candidate_hash': e['candidate']['sha256'] == second['candidate']['sha256'],
            'same_case_inputs': [c['input'] for c in e['cases']] == [c['input'] for c in second['cases']],
            'prior_candidate_gate_failure_still_stored': first['reasons']['hard_gate_failed']}


def excluded_no_patch_lifecycle(t):
    memory = loop.empty_memory()
    for index in range(3):
        record = deepcopy(t.r)
        record['run_id'] = f'excluded-run-{index}'
        record['cycle_id'] = f'excluded-cycle-{index}'
        record['skills'][0]['outcome'] = 'EXCLUDED_BY_USER'
        record['skills'][0]['observations'][0].update(result='EXCLUDED', severity='info')
        loop.collect(memory, record)
    batch = loop.prepare_batch(memory, 'excluded-review', t.c)
    review = {'review_artifact': t.artifact('engineering/excluded-review.md',
              'Synthetic no-patch review: publication explicitly excluded in all three cycles.'), 'issues': {}}
    first = loop.finish(memory, 'excluded-review', review, t.root)
    repeat = loop.finish(memory, 'excluded-review', review, t.root)
    next_batch = loop.prepare_batch(memory, 'later-review', t.c)
    return {'selected_runs': len(batch['run_ids']), 'issue_count': len(memory['backlog']),
            'first_finish': first['status'], 'repeat_finish': repeat['status'],
            'next_batch': next_batch['status'], 'preserved_run_count': len(memory['runs'])}


if __name__ == '__main__':
    print(json.dumps({'scope': 'offline synthetic code probes only', 'results': [
        scenario('duplicate_replay_held_out_input', duplicate_holdout),
        scenario('same_candidate_second_iteration', same_candidate_second_iteration),
        scenario('experimental_symlink_into_skills', experimental_symlink),
        scenario('new_failure_inherits_old_review_disposition', unreviewed_failure_status),
        scenario('prior_failed_unchanged_candidate_recommended', prior_failed_candidate),
        scenario('fresh_excluded_no_patch_lifecycle', excluded_no_patch_lifecycle),
    ]}, indent=2))
