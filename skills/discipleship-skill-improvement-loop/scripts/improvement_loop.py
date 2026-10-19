#!/usr/bin/env python3
"""Local evidence ledger and conservative paired-evaluation gate; no network or model calls."""
import argparse
from contextlib import contextmanager
from copy import deepcopy
import hashlib
import json
import math
import os
from pathlib import Path
import re
import tempfile

ROOT = Path(__file__).resolve().parents[3]
DIMENSIONS = ('instruction_adherence', 'research_accuracy', 'citation_reliability',
              'completeness', 'practical_usefulness', 'evidence_quality', 'synthesis_quality',
              'workflow_reliability', 'interruption_recovery', 'efficiency', 'governance')
GATES = ('evidence', 'citations', 'mission', 'safeguarding', 'approval', 'privacy', 'purpose')
CAUSES = ('instructions', 'conflict', 'tool', 'routing', 'verification', 'handoff',
          'context', 'stop_condition', 'model', 'external_data', 'unknown')
STATES = ('COMPLETED', 'BLOCKED', 'INTERRUPTED', 'EXCLUDED_BY_USER', 'UNKNOWN')
CODES = DIMENSIONS + ('tool_unavailable', 'external_data_unavailable', 'hook_failure')


def require(ok, message):
    if not ok:
        raise ValueError(message)


def obj(value, keys):
    require(isinstance(value, dict) and set(value) == set(keys), 'invalid or extra fields')


def token(value):
    require(isinstance(value, str) and re.fullmatch(r'[A-Za-z0-9][A-Za-z0-9_.:-]{0,119}', value),
            'expected opaque token, not narrative or personal data')
    return value


def sha(value):
    require(isinstance(value, str) and re.fullmatch(r'[a-f0-9]{64}', value), 'expected SHA-256')
    return value


def digest(value):
    return hashlib.sha256(json.dumps(value, sort_keys=True, separators=(',', ':')).encode()).hexdigest()


def file_hash(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def read(path):
    return json.loads(Path(path).read_text())


def finite_number(value):
    return type(value) in (int, float) and math.isfinite(value) and value >= 0


def config_check(c):
    obj(c, ('batch_cycles', 'max_cycles_per_batch', 'max_candidates', 'max_iterations',
            'max_retries', 'max_seconds', 'max_cost_usd'))
    require(all(finite_number(x) for x in c.values()), 'invalid resource limit')
    require(all(type(c[k]) is int for k in c if k != 'max_cost_usd'), 'integer limits required')
    require(c['batch_cycles'] > 0 and c['max_cycles_per_batch'] >= c['batch_cycles']
            and c['max_candidates'] > 0 and c['max_iterations'] > 0 and c['max_seconds'] > 0,
            'non-positive or inconsistent limit')


def validate_record(r):
    obj(r, ('schema_version', 'run_id', 'cycle_id', 'origin', 'research_status',
            'privacy_reviewed', 'skills'))
    require(type(r['schema_version']) is int and r['schema_version'] == 1, 'schema version')
    token(r['run_id']); token(r['cycle_id'])
    require(r['origin'] in ('research', 'fixture', 'historical_review', 'improvement'), 'origin')
    require(r['research_status'] in STATES, 'research status')
    require(r['privacy_reviewed'] is True, 'privacy review required')
    require(isinstance(r['skills'], list) and r['skills'], 'skills required')
    names = set()
    for s in r['skills']:
        obj(s, ('name', 'version_sha256', 'outcome', 'retries', 'observations'))
        token(s['name']); sha(s['version_sha256'])
        require(s['name'] not in names, 'duplicate skill'); names.add(s['name'])
        require(s['outcome'] in STATES, 'skill outcome')
        require(type(s['retries']) is int and s['retries'] >= 0, 'retry count')
        require(isinstance(s['observations'], list), 'observations must be list')
        for o in s['observations']:
            obj(o, ('code', 'result', 'severity', 'artifact_sha256', 'locator'))
            require(o['code'] in CODES, 'observation code')
            require(o['result'] in ('PASS', 'FAIL', 'UNKNOWN', 'EXCLUDED'), 'observation result')
            require(o['severity'] in ('info', 'minor', 'major', 'critical'), 'severity')
            sha(o['artifact_sha256']); token(o['locator'])
            require(o['result'] != 'EXCLUDED' or o['severity'] == 'info', 'exclusion is not failure')


def empty_memory():
    return {'schema_version': 1, 'runs': {}, 'backlog': {}, 'batches': {}, 'comparisons': {}}


def collect(m, r):
    validate_record(r)
    if r['origin'] == 'improvement':
        return {'status': 'SKIPPED_RECURSION'}
    rid = r['run_id']
    if rid in m['runs']:
        require(m['runs'][rid] == r, 'run ID conflict; preserve original, use new attempt ID')
        return {'status': 'NO_CHANGE', 'run_id': rid}
    m['runs'][rid] = deepcopy(r)
    for s in r['skills']:
        for o in s['observations']:
            if o['result'] not in ('FAIL', 'UNKNOWN'):
                continue
            key = s['name'] + ':' + o['code']
            issue = m['backlog'].setdefault(key, {'run_ids': [], 'root_cause': 'unknown',
                                                 'status': 'OPEN', 'reviews': []})
            if rid not in issue['run_ids']:
                issue['run_ids'].append(rid)
    return {'status': 'COLLECTED', 'run_id': rid}


def prepare_batch(m, bid, c):
    token(bid)
    if bid in m['batches']:
        return m['batches'][bid]
    require(not any(b['status'] == 'IN_PROGRESS' for b in m['batches'].values()),
            'resume existing active batch first')
    reviewed = {r for b in m['batches'].values() if b['status'] == 'COMPLETED' for r in b['run_ids']}
    pending = [r for rid, r in m['runs'].items() if rid not in reviewed]
    cycles = list(dict.fromkeys(r['cycle_id'] for r in pending))
    critical = [r['cycle_id'] for r in pending for s in r['skills'] for o in s['observations']
                if o['result'] == 'FAIL' and o['severity'] == 'critical']
    if len(cycles) < c['batch_cycles'] and not critical:
        return {'status': 'NOT_DUE', 'pending_cycles': len(cycles)}
    # Critical cycles first, even if they arrived beyond the normal batch cap.
    selected = list(dict.fromkeys(critical + cycles))[:c['max_cycles_per_batch']]
    batch = {'status': 'IN_PROGRESS', 'run_ids': [r['run_id'] for r in pending
                                                if r['cycle_id'] in selected],
             'trigger': 'CRITICAL' if critical else 'BATCH', 'limits': dict(c),
             'comparison_ids': [], 'finish': None}
    m['batches'][bid] = batch
    return batch


def artifact(a, root):
    obj(a, ('path', 'sha256'))
    sha(a['sha256'])
    p = Path(a['path'])
    require(not p.is_absolute() and '..' not in p.parts, 'artifact must be repository relative')
    resolved = (root / p).resolve()
    require(resolved.is_relative_to(root.resolve()), 'artifact escaped repository')
    require(resolved.is_file() and file_hash(resolved) == a['sha256'], 'artifact hash mismatch')
    return resolved.relative_to(root.resolve()).as_posix()


def validate_eval(e, root):
    obj(e, ('evaluation_id', 'author', 'evaluator', 'privacy_reviewed', 'baseline', 'candidate',
            'proposal', 'cases', 'usage', 'method'))
    token(e['evaluation_id']); token(e['author']); token(e['evaluator'])
    require(e['privacy_reviewed'] is True, 'privacy review required')
    require(e['method'] in ('behavioral', 'static', 'simulation'), 'evaluation method')
    for key in ('baseline', 'candidate', 'proposal'):
        path = artifact(e[key], root)
        if key in ('candidate', 'proposal'):
            require(path.startswith('engineering/skill-improvement/experiments/'),
                    'candidate/proposal must stay experimental')
    require(e['baseline']['sha256'] != e['candidate']['sha256'], 'no candidate change')
    require(isinstance(e['cases'], list) and e['cases'], 'paired cases required')
    ids = set()
    input_splits = {}
    for case in e['cases']:
        obj(case, ('id', 'split', 'input', 'baseline_output', 'candidate_output', 'scores', 'gates'))
        token(case['id']); require(case['id'] not in ids, 'duplicate case'); ids.add(case['id'])
        require(case['split'] in ('replay', 'held_out'), 'case split')
        for key in ('input', 'baseline_output', 'candidate_output'):
            artifact(case[key], root)
        input_sha = case['input']['sha256']
        previous_split = input_splits.setdefault(input_sha, case['split'])
        require(previous_split == case['split'], 'replay and held-out inputs must differ')
        obj(case['scores'], DIMENSIONS)
        for pair in case['scores'].values():
            require(isinstance(pair, list) and len(pair) == 2 and all(
                v is None or type(v) is int and 0 <= v <= 4 for v in pair), 'invalid paired score')
        obj(case['gates'], GATES)
        for pair in case['gates'].values():
            require(isinstance(pair, list) and len(pair) == 2
                    and all(v in ('PASS', 'FAIL', 'UNKNOWN') for v in pair), 'invalid gate')
    obj(e['usage'], ('seconds', 'cost_usd', 'iterations', 'retries'))
    require(all(finite_number(v) for v in e['usage'].values()), 'invalid usage')
    require(all(type(e['usage'][k]) is int for k in ('iterations', 'retries')), 'integer counts required')
    require(e['usage']['iterations'] > 0, 'iteration required')


def compare(m, bid, e, root):
    validate_eval(e, root)
    require(bid in m['batches'], 'batch missing')
    b = m['batches'][bid]
    eid = e['evaluation_id']
    if eid in m['comparisons']:
        old = m['comparisons'][eid]
        require(old['input_digest'] == digest(e) and old['batch_id'] == bid, 'evaluation ID conflict')
        return old
    require(b['status'] == 'IN_PROGRESS', 'batch already closed')
    prior = [m['comparisons'][i] for i in b['comparison_ids']]
    same_candidate = [p for p in prior if p['evaluation']['candidate']['sha256'] == e['candidate']['sha256']]
    def contract(packet):
        return {'baseline': packet['baseline']['sha256'], 'proposal': packet['proposal']['sha256'],
                'cases': sorted((t['id'], t['split'], t['input']['sha256']) for t in packet['cases'])}
    require(all(contract(p['evaluation']) == contract(e) for p in same_candidate),
            'frozen candidate evaluation contract changed')
    prior_rejection = any(p['decision'] == 'REJECT' for p in same_candidate)
    # These are acceptance limits. The caller must reserve resources before external work.
    limits = b['limits']
    candidates = {p['evaluation']['candidate']['sha256'] for p in prior}
    candidates.add(e['candidate']['sha256'])
    exceeded = len(candidates) > limits['max_candidates']
    for metric, limit in (('seconds', 'max_seconds'), ('cost_usd', 'max_cost_usd'),
                          ('iterations', 'max_iterations'), ('retries', 'max_retries')):
        exceeded |= sum(p['usage'][metric] for p in prior) + e['usage'][metric] > limits[limit]
    cases = e['cases']
    regression = any(p[1] < p[0] for t in cases for p in t['scores'].values() if None not in p)
    gate_fail = any(p[1] == 'FAIL' for t in cases for p in t['gates'].values())
    unknown = any(None in p for t in cases for p in t['scores'].values()) or any(
        'UNKNOWN' in p for t in cases for p in t['gates'].values())
    improved = any(p[1] > p[0] for t in cases for p in t['scores'].values() if None not in p)
    independent = e['author'] != e['evaluator']
    coverage = {t['split'] for t in cases} == {'replay', 'held_out'}
    if exceeded or regression or gate_fail or prior_rejection:
        decision = 'REJECT'
    elif unknown or not independent or not coverage or e['method'] != 'behavioral' or not improved:
        decision = 'INCONCLUSIVE'
    else:
        decision = 'RECOMMEND_REVIEW'
    result = {'batch_id': bid, 'input_digest': digest(e), 'decision': decision,
              'usage': deepcopy(e['usage']), 'evaluation': deepcopy(e),
              'reasons': {'budget_exceeded': bool(exceeded), 'regression': regression,
                          'hard_gate_failed': gate_fail, 'prior_candidate_rejection': prior_rejection, 'unknown': unknown,
                          'independent_evaluator_reported': independent,
                          'replay_and_held_out': coverage, 'strict_improvement': improved}}
    m['comparisons'][eid] = result
    b['comparison_ids'].append(eid)
    return result


def finish(m, bid, review, root):
    obj(review, ('review_artifact', 'issues'))
    artifact(review['review_artifact'], root)
    require(bid in m['batches'], 'batch missing')
    b = m['batches'][bid]
    if b['status'] == 'COMPLETED':
        require(b['finish'] == review, 'finished batch conflict')
        return {'status': 'NO_CHANGE'}
    relevant = {s['name'] + ':' + o['code'] for rid in b['run_ids'] for s in m['runs'][rid]['skills']
                for o in s['observations'] if o['result'] in ('FAIL', 'UNKNOWN')}
    obj(review['issues'], relevant)
    for key, issue in review['issues'].items():
        obj(issue, ('cause', 'status'))
        require(issue['cause'] in CAUSES, 'root cause')
        require(issue['status'] in ('OPEN', 'DEFERRED', 'PROPOSED', 'NO_CHANGE'), 'issue disposition')
    for key, issue in review['issues'].items():
        entry = m['backlog'][key]
        entry.setdefault('reviews', []).append({'batch_id': bid, 'run_ids': list(b['run_ids']),
                                                'cause': issue['cause'], 'status': issue['status']})
        covered = {rid for item in entry['reviews'] for rid in item['run_ids']}
        pending = set(entry['run_ids']) - covered
        entry['root_cause'] = 'unknown' if pending else issue['cause']
        entry['status'] = 'OPEN' if pending else issue['status']
    b['status'] = 'COMPLETED'; b['finish'] = deepcopy(review)
    return {'status': 'COMPLETED', 'batch_id': bid}


@contextmanager
def locked(path):
    path.parent.mkdir(parents=True, exist_ok=True)
    lock = path.with_suffix(path.suffix + '.lock')
    # Persistent lock files + flock release on crash avoid unsafe stale-lock deletion.
    import fcntl
    with lock.open('a') as handle:
        try:
            fcntl.flock(handle, fcntl.LOCK_EX | fcntl.LOCK_NB)
        except BlockingIOError:
            raise ValueError('another writer active; retry later') from None
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def atomic_write(path, value):
    fd, name = tempfile.mkstemp(dir=path.parent, prefix=path.name + '.', suffix='.tmp')
    try:
        with os.fdopen(fd, 'w') as f:
            json.dump(value, f, indent=2, sort_keys=True, allow_nan=False)
            f.write('\n'); f.flush(); os.fsync(f.fileno())
        os.replace(name, path)
    finally:
        if os.path.exists(name):
            os.unlink(name)


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--root', type=Path, default=ROOT)
    p.add_argument('--memory', type=Path, default=Path('engineering/skill-improvement/memory.json'))
    p.add_argument('--config', type=Path, default=Path('config/skill-improvement.json'))
    p.add_argument('command', choices=('collect', 'batch', 'compare', 'finish', 'status'))
    p.add_argument('--input', type=Path)
    p.add_argument('--batch-id')
    args = p.parse_args()
    root = args.root.resolve()
    memory = args.memory if args.memory.is_absolute() else root / args.memory
    config_path = args.config if args.config.is_absolute() else root / args.config
    try:
        c = read(config_path); config_check(c)
        with locked(memory):
            m = read(memory) if memory.exists() else empty_memory()
            require(m['schema_version'] == 1, 'unsupported memory version')
            before = digest(m)
            if args.command == 'status':
                result = m
            elif args.command == 'batch':
                require(args.batch_id is not None, '--batch-id required')
                result = prepare_batch(m, args.batch_id, c)
            else:
                require(args.input is not None, '--input required')
                value = read(args.input)
                if args.command == 'collect':
                    result = collect(m, value)
                else:
                    require(args.batch_id is not None, '--batch-id required')
                    result = compare(m, args.batch_id, value, root) if args.command == 'compare' else finish(
                        m, args.batch_id, value, root)
            if digest(m) != before:
                atomic_write(memory, m)
        print(json.dumps(result, indent=2, allow_nan=False))
        return 0
    except (ValueError, OSError, KeyError, TypeError) as exc:
        print(json.dumps({'status': 'ERROR', 'error': str(exc)}))
        return 2


if __name__ == '__main__':
    raise SystemExit(main())
