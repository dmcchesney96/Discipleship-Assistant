"""Behavioral software tests; synthetic packets do not certify LLM or live Drive behavior."""
from copy import deepcopy
import importlib.util
import json
import os
from pathlib import Path
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch

ROOT = Path(__file__).resolve().parents[1]
SCRIPT = ROOT / 'skills/discipleship-skill-improvement-loop/scripts/improvement_loop.py'
spec = importlib.util.spec_from_file_location('improvement_loop', SCRIPT)
loop = importlib.util.module_from_spec(spec)
spec.loader.exec_module(loop)

class ImprovementTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.addCleanup(self.tmp.cleanup)
        self.root = Path(self.tmp.name)
        self.m = loop.empty_memory()
        self.c = loop.read(ROOT / 'config/skill-improvement.json')
        self.r = loop.read(ROOT / 'tests/fixtures/skill-improvement/cycle.json')
        loop.collect(self.m, self.r)
        loop.prepare_batch(self.m, 'batch-01', self.c)

    def artifact(self, name, content):
        path = self.root / name
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(content)
        return {'path': name, 'sha256': loop.file_hash(path)}

    def evaluation(self):
        prefix = 'engineering/skill-improvement/experiments/'
        e = {'evaluation_id': 'eval-01', 'author': 'editor', 'evaluator': 'fresh-reviewer',
             'privacy_reviewed': True, 'baseline': self.artifact(prefix+'baseline.md', 'baseline'),
             'candidate': self.artifact(prefix+'candidate.md', 'candidate'),
             'proposal': self.artifact(prefix+'proposal.md', 'bounded synthetic proposal'),
             'method': 'behavioral', 'cases': [],
             'usage': {'seconds': 1, 'cost_usd': 0, 'iterations': 1, 'retries': 0}}
        for split in ('replay', 'held_out'):
            e['cases'].append({'id': split, 'split': split,
                'input': self.artifact(prefix+split+'.txt', split),
                'baseline_output': self.artifact(prefix+split+'-old.md', 'old output'),
                'candidate_output': self.artifact(prefix+split+'-new.md', 'new output'),
                'scores': {d: [3, 3] for d in loop.DIMENSIONS},
                'gates': {d: ['PASS', 'PASS'] for d in loop.GATES}})
        e['cases'][0]['scores']['completeness'] = [2, 3]
        return e

    def result(self, e):
        return loop.compare(self.m, 'batch-01', e, self.root)['decision']

    def test_exact_collect_repeat_no_mutation(self):
        before = deepcopy(self.m)
        self.assertEqual(loop.collect(self.m, self.r)['status'], 'NO_CHANGE')
        self.assertEqual(before, self.m)

    def test_conflicting_run_preserves_history(self):
        changed = deepcopy(self.r); changed['research_status'] = 'BLOCKED'
        with self.assertRaises(ValueError): loop.collect(self.m, changed)
        self.assertEqual(self.m['runs'][self.r['run_id']]['research_status'], 'COMPLETED')

    def test_extra_text_and_email_rejected(self):
        for field, value in [('raw_transcript', 'private'), ('run_id', 'person@example.com')]:
            r = deepcopy(self.r); r[field] = value
            with self.assertRaises(ValueError): loop.validate_record(r)

    def test_privacy_review_required(self):
        r = deepcopy(self.r); r['privacy_reviewed'] = False
        with self.assertRaises(ValueError): loop.validate_record(r)

    def test_improvement_origin_does_not_recurse(self):
        r = deepcopy(self.r); r['origin'] = 'improvement'; before = deepcopy(self.m)
        self.assertEqual(loop.collect(self.m, r)['status'], 'SKIPPED_RECURSION')
        self.assertEqual(before, self.m)

    def test_excluded_stage_is_not_issue(self):
        r = deepcopy(self.r); r['run_id'] = 'excluded'; o = r['skills'][0]['observations'][0]
        o.update(result='EXCLUDED', severity='info')
        m = loop.empty_memory(); loop.collect(m, r)
        self.assertEqual(m['backlog'], {})
        o['severity'] = 'critical'
        with self.assertRaises(ValueError): loop.validate_record(r)

    def test_threshold_counts_cycles_not_attempts(self):
        m = loop.empty_memory()
        for i in range(3):
            r = deepcopy(self.r); r['run_id'] = f'attempt-{i}'
            r['skills'][0]['observations'] = []; loop.collect(m, r)
        self.assertEqual(loop.prepare_batch(m, 'b', self.c)['status'], 'NOT_DUE')
        for i in range(2):
            r = deepcopy(r); r['cycle_id'] = f'new-cycle-{i}'; r['run_id'] = f'new-run-{i}'
            loop.collect(m, r)
        self.assertEqual(loop.prepare_batch(m, 'b', self.c)['trigger'], 'BATCH')

    def test_critical_bypasses_threshold_and_resume_stable(self):
        b = deepcopy(self.m['batches']['batch-01'])
        self.assertEqual(b['trigger'], 'CRITICAL')
        self.assertEqual(loop.prepare_batch(self.m, 'batch-01', self.c), b)
        with self.assertRaises(ValueError): loop.prepare_batch(self.m, 'other', self.c)

    def test_critical_is_selected_ahead_of_old_backlog(self):
        m = loop.empty_memory(); c = dict(self.c, batch_cycles=1, max_cycles_per_batch=1)
        r = deepcopy(self.r); r['run_id'] = 'old'; r['cycle_id'] = 'old'; r['skills'][0]['observations'] = []
        loop.collect(m, r); loop.collect(m, self.r)
        self.assertEqual(loop.prepare_batch(m, 'b', c)['run_ids'], [self.r['run_id']])

    def test_comparison_recommends_review_without_installing(self):
        e = self.evaluation(); before = (ROOT/'skills/ai-research-verification-integration/SKILL.md').read_bytes()
        self.assertEqual(self.result(e), 'RECOMMEND_REVIEW')
        self.assertEqual(before, (ROOT/'skills/ai-research-verification-integration/SKILL.md').read_bytes())

    def test_regression_rejected_even_with_better_total(self):
        e = self.evaluation(); e['cases'][1]['scores']['citation_reliability'] = [4, 3]
        self.assertEqual(self.result(e), 'REJECT')

    def test_hard_gate_failure_rejected(self):
        for gate in loop.GATES:
            e = self.evaluation(); e['evaluation_id'] = gate
            e['cases'][0]['gates'][gate][1] = 'FAIL'
            m = deepcopy(self.m)
            self.assertEqual(self.result(e), 'REJECT'); self.m = m

    def test_unknown_and_same_evaluator_and_tie_inconclusive(self):
        for mode in ('unknown', 'same', 'tie', 'static', 'simulation', 'no_holdout'):
            e = self.evaluation()
            if mode == 'unknown': e['cases'][0]['scores']['synthesis_quality'] = [None, None]
            if mode == 'same': e['evaluator'] = e['author']
            if mode == 'tie': e['cases'][0]['scores']['completeness'] = [3, 3]
            if mode in ('static', 'simulation'): e['method'] = mode
            if mode == 'no_holdout': e['cases'] = e['cases'][:1]
            m = deepcopy(self.m)
            self.assertEqual(self.result(e), 'INCONCLUSIVE', mode); self.m = m

    def test_source_and_output_tampering_rejected(self):
        for key in ('input', 'baseline_output', 'candidate_output'):
            e = self.evaluation(); (self.root/e['cases'][0][key]['path']).write_text('changed')
            with self.assertRaises(ValueError): self.result(e)

    def test_path_escape_and_production_candidate_rejected(self):
        e = self.evaluation(); e['candidate']['path'] = '../private.md'
        with self.assertRaises(ValueError): self.result(e)
        e = self.evaluation(); e['candidate'] = self.artifact('skills/example/SKILL.md', 'bad')
        with self.assertRaises(ValueError): self.result(e)

    def test_duplicate_evaluation_is_idempotent(self):
        e = self.evaluation(); self.result(e); before = deepcopy(self.m)
        self.result(e); self.assertEqual(before, self.m)
        e['usage']['seconds'] = 2
        with self.assertRaises(ValueError): self.result(e)

    def test_budget_and_candidate_limits(self):
        for key, value in [('seconds', 301), ('cost_usd', 2.01), ('iterations', 3), ('retries', 2)]:
            e = self.evaluation(); e['usage'][key] = value; m = deepcopy(self.m)
            self.assertEqual(self.result(e), 'REJECT'); self.m = m
        e = self.evaluation(); self.result(e); e['evaluation_id'] = 'second'
        self.assertEqual(self.result(e), 'RECOMMEND_REVIEW')
        e['evaluation_id'] = 'third'; e['candidate'] = self.artifact('engineering/skill-improvement/experiments/third.md','different candidate')
        self.assertEqual(self.result(e), 'REJECT')

    def test_holdout_cannot_reuse_replay_bytes(self):
        e = self.evaluation(); e['cases'][1]['input'] = e['cases'][0]['input']
        with self.assertRaisesRegex(ValueError, 'inputs must differ'): self.result(e)

    def test_candidate_symlink_into_production_rejected(self):
        production = self.artifact('skills/example/SKILL.md','candidate')
        symlink = self.root/'engineering/skill-improvement/experiments/linked.md'
        symlink.parent.mkdir(parents=True,exist_ok=True); symlink.symlink_to(self.root/production['path'])
        e = self.evaluation(); e['candidate'] = {'path':str(symlink.relative_to(self.root)), 'sha256':production['sha256']}
        with self.assertRaisesRegex(ValueError, 'stay experimental'): self.result(e)

    def test_rejected_candidate_cannot_erase_failure_with_later_scores(self):
        e = self.evaluation(); e['cases'][0]['gates']['citations'][1] = 'FAIL'
        self.assertEqual(self.result(e),'REJECT')
        e['evaluation_id'] = 'again'; e['cases'][0]['gates']['citations'][1] = 'PASS'
        self.assertEqual(self.result(e),'REJECT')
        self.assertTrue(self.m['comparisons']['again']['reasons']['prior_candidate_rejection'])

    def test_candidate_contract_cannot_swap_cases_or_baseline(self):
        e = self.evaluation(); self.result(e)
        e['evaluation_id'] = 'new-cases'; e['cases'][0]['id'] = 'swapped'
        with self.assertRaisesRegex(ValueError,'contract changed'): self.result(e)
        e = self.evaluation(); e['evaluation_id'] = 'new-baseline'
        e['baseline'] = self.artifact('engineering/baseline2.md','new baseline')
        with self.assertRaisesRegex(ValueError,'contract changed'): self.result(e)

    def test_bad_numbers_and_missing_dimension_rejected(self):
        for value in (-1, float('nan'), float('inf'), True):
            e = self.evaluation(); e['usage']['cost_usd'] = value
            with self.assertRaises(ValueError): self.result(e)
        e = self.evaluation(); del e['cases'][0]['scores']['governance']
        with self.assertRaises(ValueError): self.result(e)

    def test_finish_requires_all_issues_and_preserves_failure(self):
        review = {'review_artifact': self.artifact('engineering/review.md','no change'), 'issues': {}}
        with self.assertRaises(ValueError): loop.finish(self.m, 'batch-01', review, self.root)
        key = next(iter(self.m['backlog']))
        review['issues'][key] = {'cause':'tool','status':'NO_CHANGE'}
        self.assertEqual(loop.finish(self.m,'batch-01',review,self.root)['status'],'COMPLETED')
        self.assertEqual(loop.finish(self.m,'batch-01',review,self.root)['status'],'NO_CHANGE')
        self.assertIn(self.r['run_id'],self.m['runs'])
        self.assertEqual(loop.prepare_batch(self.m,'next',self.c)['status'],'NOT_DUE')

    def test_new_failure_does_not_inherit_previous_batch_disposition(self):
        r = deepcopy(self.r); r['run_id'] = 'later'; r['cycle_id'] = 'later-cycle'
        loop.collect(self.m, r)
        key = next(iter(self.m['backlog']))
        review = {'review_artifact':self.artifact('engineering/review.md','first batch only'),
                  'issues':{key:{'cause':'tool','status':'NO_CHANGE'}}}
        loop.finish(self.m, 'batch-01', review, self.root)
        self.assertEqual(self.m['backlog'][key]['status'], 'OPEN')
        self.assertEqual(self.m['backlog'][key]['root_cause'], 'unknown')
        self.assertNotIn('later',self.m['backlog'][key]['reviews'][0]['run_ids'])
        self.assertEqual(loop.prepare_batch(self.m, 'next', self.c)['run_ids'], ['later'])

    def test_atomic_write_failure_keeps_old_state(self):
        path = self.root/'memory.json'; loop.atomic_write(path, self.m); before = path.read_bytes()
        with patch.object(os, 'replace', side_effect=OSError('injected before replace')):
            with self.assertRaises(OSError): loop.atomic_write(path, {'new':True})
        self.assertEqual(path.read_bytes(),before)
        self.assertEqual(list(self.root.glob('*.tmp')),[])

    def test_second_process_lock_rejected(self):
        path = self.root/'memory.json'
        with loop.locked(path):
            code = "import fcntl,sys; f=open(sys.argv[1],'a'); fcntl.flock(f,fcntl.LOCK_EX|fcntl.LOCK_NB)"
            p = subprocess.run([sys.executable,'-c',code,str(path.with_suffix('.json.lock'))],capture_output=True)
            self.assertNotEqual(p.returncode,0)
        with loop.locked(path): pass

    def test_cli_collect_crash_recovery_repeat_and_bad_input(self):
        path = self.root/'memory.json'
        cmd = [sys.executable,str(SCRIPT),'--root',str(ROOT),'--memory',str(path),'collect','--input',
               str(ROOT/'tests/fixtures/skill-improvement/cycle.json')]
        first = subprocess.run(cmd,capture_output=True,text=True)
        self.assertEqual(first.returncode,0,first.stdout)
        before = path.read_bytes(); repeat = subprocess.run(cmd,capture_output=True,text=True)
        self.assertIn('NO_CHANGE',repeat.stdout); self.assertEqual(before,path.read_bytes())
        bad = self.root/'bad.json'; bad.write_text('{invalid')
        cmd[-1] = str(bad); failed = subprocess.run(cmd,capture_output=True,text=True)
        self.assertEqual(failed.returncode,2); self.assertEqual(before,path.read_bytes())

if __name__ == '__main__': unittest.main()
