# Copyright (C) 2026 Maseeh Ghodsi, for rights held in original contributions.
# SPDX-License-Identifier: GPL-3.0-or-later
"""Fresh bounded adversarial audit. All source inputs are from the frozen ZIP.

No assertion here turns sparse values into an identity. Synthetic mutations are
kept separate from actual corpus discrepancies. All scratch files stay in HERE.
"""
import ast
from collections import Counter, defaultdict
from copy import deepcopy
from fractions import Fraction
from functools import lru_cache
from itertools import combinations
from hashlib import sha256
import importlib.util
import json
from math import factorial, gcd
from pathlib import Path
import subprocess
import sys
import tempfile
import time

sys.dont_write_bytecode = True
import argparse
if sys.flags.optimize:
    raise RuntimeError('Assertions must be enabled; do not use Python -O.')
parser = argparse.ArgumentParser(description='Independent strict audit of the frozen stretched-LR corpus.')
parser.add_argument('--packet', type=Path, required=True)
parser.add_argument('--output', type=Path, required=True)
parser.add_argument('mode', choices=['inventory', 'finalcover', 'controls', 'extra', 'all'])
arguments = parser.parse_args()
ROOT = arguments.packet.resolve(strict=True)
HERE = arguments.output.resolve()
if HERE == ROOT or ROOT in HERE.parents:
    raise RuntimeError('Output must be outside the frozen packet.')
assert sha256((ROOT / 'MANIFEST.json').read_bytes()).hexdigest() == 'f835cbc7ae315eb181139a812d24c11ee29bd747735311eb510bcd09b0aa56f3'
manifest = json.loads((ROOT / 'MANIFEST.json').read_text())
actual_files = set()
for path in ROOT.rglob('*'):
    if path.is_symlink():
        raise RuntimeError('Symlinks are forbidden in the frozen packet.')
    if path.is_file():
        actual_files.add(path.relative_to(ROOT).as_posix())
if actual_files != set(manifest['files']) | {'MANIFEST.json'}:
    raise RuntimeError('Frozen packet contains missing or extra files.')
for name, pin in manifest['files'].items():
    path = ROOT / name
    if Path(name).is_absolute() or '..' in Path(name).parts:
        raise RuntimeError('Unsafe manifest path.')
    actual_hash = sha256()
    with path.open('rb') as stream:
        for block in iter(lambda: stream.read(1024 * 1024), b''):
            actual_hash.update(block)
    if path.stat().st_size != pin['bytes'] or actual_hash.hexdigest() != pin['sha256']:
        raise RuntimeError('Frozen packet bytes changed: ' + name)
# Execute packet code only after every source byte has been checked locally.
HERE.mkdir(parents=True, exist_ok=False)
assert (ROOT / 'MANIFEST.json').is_file()
subprocess.run([sys.executable, '-B', str(ROOT / 'verify.py'), '--manifest-only',
                '--output', str(HERE / 'integrity.json')], cwd=ROOT, check=True)

OLD = ROOT / 'problems/stretched-lr-coefficients/runs/20260905T173132Z'
VP = ROOT / 'problems/stretched-lr-coefficients/verifier/verify.py'
(HERE / 'scratch').mkdir(exist_ok=True)
tempfile.tempdir = str(HERE / 'scratch')
spec = importlib.util.spec_from_file_location('fresh_adversarial_verifier', VP)
v = importlib.util.module_from_spec(spec)
spec.loader.exec_module(v)

def save(name, value):
    (HERE / name).write_text(json.dumps(value, indent=2, sort_keys=True) + '\n')

def strict_partition(p):
    assert type(p) in (tuple, list)
    assert all(type(x) is int and x >= 0 for x in p)
    assert all(x >= y for x, y in zip(p, p[1:]))
    return tuple(x for x in p if x)

def norm(T):
    assert len(T) == 3
    l, m, u = map(strict_partition, T)
    assert sum(l) == sum(m) + sum(u)
    if (sum(m), m) < (sum(u), u):
        m, u = u, m
    return l, m, u

def key(T):
    return sum(T[0]), len(T[0]), T

def box(T):
    assert max(map(len, T)) <= 7 and sum(T[0]) <= 30

def E_conditions(T, c):
    l, m, u = T
    n = len(l)
    assert 1 <= sum(l) <= 30 and n <= 7 and c >= 3
    assert T == norm(T)
    assert len(m) < n and len(u) < n
    m += (0,) * (n-len(m)); u += (0,) * (n-len(u))
    assert gcd(*l, *m, *u) == 1
    assert all(l[j] > m[j] and l[j] > u[j] for j in range(n))
    for j in range(n-1):
        q = sum(m[:j+1]) + sum(u[:j+1]) - sum(l[:j+1])
        assert q > 0 and m[j] <= l[j+1] and u[j] <= l[j+1]
        if l[j] > l[j+1]:
            assert m[j]-m[j+1] <= min(q, l[j+1]-m[j+1])
            assert u[j]-u[j+1] <= min(q, l[j+1]-u[j+1])
    N, M, U = sum(l), sum(m), sum(u)
    sizes = [N, n*l[0]-M, n*l[0]-U, n*(m[0]+u[0])-N,
             n*(m[0]-l[-1])+U, n*(u[0]-l[-1])+M]
    assert min(sizes) >= N

def independent_edge(e):
    before, after = norm(e['before']), norm(e['after'])
    assert max(map(len, before)) <= 7 and max(map(len, after)) <= 7
    l, m, u = before; n = len(l)
    assert n and all(len(p) <= n and all(x <= l[j] for j, x in enumerate(p)) for p in (m,u))
    m += (0,)*(n-len(m)); u += (0,)*(n-len(u))
    p = e['params']; kind = e['kind']; s = e['scale']
    assert type(s) is int and s > 0
    assert all(type(x) is int for k,x in p.items() if k != 'inner')
    if kind == 'gcd':
        assert s >= 2 and gcd(*l,*m,*u) == s
        target = tuple(tuple(x//s for x in a) for a in (l,m,u))
    else:
        assert s == 1
        if kind == 'full_columns':
            a,b = p['a'],p['b']
            assert a == m[-1] and b == u[-1] and a+b > 0 and l[-1] >= a+b
            target = tuple(x-a-b for x in l),tuple(x-a for x in m),tuple(x-b for x in u)
        elif kind in ('row_deletion','shortening'):
            assert p['inner'] in ('mu','nu')
            a,b = (m,u) if p['inner']=='mu' else (u,m)
            if kind == 'row_deletion':
                j=p['j']-1
                assert 0 <= j < n and l[j] == a[j] > 0
                target=l[:j]+l[j+1:],a[:j]+a[j+1:],b
            else:
                k,z=p['k'],p['a']
                assert 1<=k<n and z>=1
                q=sum(a[:k])+sum(b[:k])-sum(l[:k])
                assert q>=0 and q==p['q'] and p['b']==min(q,l[k]-a[k])
                assert z<=l[k-1]-l[k] and z<=a[k-1]-a[k]-p['b']
                target=tuple(x-z*(j<k) for j,x in enumerate(l)),tuple(x-z*(j<k) for j,x in enumerate(a)),b
        elif kind == 'six_representative':
            assert m[-1]==u[-1]==0
            # Construct directly from the symmetric tensor invariant, independently
            # of the closed formulas in the archived local checker.
            comp=lambda part,width: tuple(width-x for x in reversed(part))
            L=l[0]; C=comp(l,L); A=m; B=u
            stars=[comp(x,x[0]) for x in (A,B,C)]
            K=A[0]+B[0]+C[0]-L
            choices=[(comp(A,L),C,B),(comp(B,L),C,A),
                     (comp(stars[2],K),stars[0],stars[1]),
                     (comp(stars[1],K),stars[0],stars[2]),
                     (comp(stars[0],K),stars[1],stars[2])]
            assert 1<=p['row']<=5
            target=choices[p['row']-1]
        elif kind == 'attempt022_rectangular':
            pp,qq,z=p['p'],p['q'],p['a']; r=pp+qq
            assert pp>=1 and qq>=1 and r<=n and z>=1
            ll=l+(0,);mm=m+(0,);uu=u+(0,)
            assert mm[pp-1]-z>=mm[pp] and uu[qq-1]-z>=uu[qq]
            assert ll[r-1]-z>=max(ll[r],mm[pp]+uu[qq])
            target=tuple(tuple(x-z*(j<k) for j,x in enumerate(part)) for part,k in zip((l,m,u),(r,pp,qq)))
        else:
            raise AssertionError(('unknown rule',kind))
    assert norm(target)==after
    return before,after

def corpus_inventory():
    start=time.monotonic(); domains={}; summaries={}; samples={}; path_examples={}
    for band,name,idxfile,journal in [
        ('small','small_minimum_domain.json','small_minimum_core_indices.json','small_minimum_signs/results.jsonl'),
        ('large','conditional_domain_c_ge3.json','combined_terminal_core_indices.json','conditional_scan/results.jsonl')]:
        rows=json.loads((OLD/name).read_text())
        corelist=json.loads((OLD/idxfile).read_text()); core=set(corelist)
        assert len(core)==len(corelist)
        domainkeys=set(); bysize=Counter()
        for i,r in enumerate(rows):
            T=norm([r[k] for k in ('lambda','mu','nu')])
            assert T not in domainkeys;domainkeys.add(T)
            E_conditions(T,r['c']);bysize[sum(T[0])]+=1
        completed=set(); errors={}; hist=Counter(); dimensions=Counter(); coverage=Counter()
        elapsed=[]; coreelapsed=[]; times=[]; distinct=set(); trailing_lines=0
        raw_sha=sha256();raw_bytes=0
        for raw in (OLD/journal).open('rb'):
            assert raw.endswith(b'\n');raw_sha.update(raw);raw_bytes+=len(raw)
            rec=json.loads(raw); i=rec['index']
            assert type(i) is int and 0<=i<len(rows) and i not in completed and i not in errors
            r=rows[i]; hist[rec['status']]+=1
            elapsed.append(rec['elapsed_s']);times.append(rec['finished_at'])
            if rec['status']=='ERROR':
                assert rec['triple']==r;errors[i]=rec;continue
            assert rec['status']=='COMPUTED'
            completed.add(i);p=rec['polynomial']
            assert [p[k] for k in ('lambda','mu','nu','c')]==[r[k] for k in ('lambda','mu','nu','c')]
            co=tuple(Fraction(x) for x in p['coefficients']);d=len(co)-1
            assert p['degree']==d and p['degree_bound']==(p['n']-1)*(p['n']-2)//2
            assert p['hive_variables']==p['degree_bound'] and p['n']==len(r['lambda'])
            assert co[0]==1 and co[-1]>0 and all(x>=0 for x in co)
            assert sum(co)==r['c'] and not p['negative_indices'] and not p['has_negative']
            assert p['leading_coefficient']==str(co[-1]) and p['min_coefficient']==str(min(co))
            assert len(p['values'])==p['degree_bound']+3
            assert all(v.evaluate(co,t)==n for t,n in enumerate(p['values']))
            assert p.get('cached') is not True
            if i in core:
                coreelapsed.append(rec['elapsed_s']);distinct.add(co)
                dimensions[p['n'],d]+=1
                coverage[p['latte_crosscheck']]+=1
                for t in (1,2,3):
                    coverage[f't{t}_present']+=f'lrcalc_t{t}' in p['cross_checks']
                    coverage[f't{t}_skipped']+=f'lrcalc_t{t}_skipped' in p['cross_checks']
                coverage['dp_present']+='lr_tableau_dp_t1' in p['cross_checks']
                coverage['dp_skipped']+='lr_tableau_dp_t1_skipped' in p['cross_checks']
                if p['n']>=6 and d>=4 and band not in samples:
                    samples[band]=rec
                if p['n']<=5 and 'full' not in samples:
                    samples['full']=rec
        historical=list(errors)
        if band=='large':
            assert historical==[1104809]
            recovery=json.loads((OLD/'hard_case_current_source.json').read_text())
            p=recovery['polynomial']; i=1104809
            assert recovery['status']=='COMPUTED' and recovery['verifier_sha256']==sha256(VP.read_bytes()).hexdigest()
            assert [p[k] for k in ('lambda','mu','nu','c')]==[rows[i][k] for k in ('lambda','mu','nu','c')]
            assert i in core and i not in completed
            assert all(Fraction(x)>=0 for x in p['coefficients'])
            completed.add(i);del errors[i]
        assert not errors and core<=completed
        summaries[band]={'domain_rows':len(rows),'domain_by_size':dict(bysize),'core':len(core),
                         'journal_statuses':dict(hist),'journal_bytes':raw_bytes,'journal_sha256':raw_sha.hexdigest(),
                         'historical_errors':historical,'core_missing_after_resolution':sorted(core-completed),
                         'noncore_computed':len(completed-core),'core_polynomials_distinct_excluding_resolution':len(distinct),
                         'degree_rank_histogram_excluding_resolution':{str(k):n for k,n in sorted(dimensions.items())},
                         'coverage_excluding_resolution':dict(coverage),'earliest_finished_at':min(times),'latest_finished_at':max(times),
                         'sum_record_elapsed_s':sum(elapsed),'core_sum_record_elapsed_s_excluding_resolution':sum(coreelapsed),
                         'core_elapsed_p50_p95_p99_max_s':[sorted(coreelapsed)[min(len(coreelapsed)-1,int(len(coreelapsed)*q))] for q in (.5,.95,.99,1)]}
        domains[band]=rows
        print(json.dumps({'stage':'journal','band':band,'core':len(core),'elapsed_s':time.monotonic()-start}),flush=True)
    rows=domains['large']; stages={}; last_fixed=None
    for name in ('reduction_closure_map_paths.jsonl','general_rectangular_closure_paths.jsonl'):
        seen=set();fixed=set();counts=Counter();maxsize=0;outboxpaths=0;scales=Counter();maxedges=0
        for raw in (OLD/name).open():
            rec=json.loads(raw);i=rec['source_index'];assert type(i) is int and i not in seen;seen.add(i)
            original=norm([rows[i][k] for k in ('lambda','mu','nu')]);current=original;scale=1;outbox=False
            for e in rec['path']:
                before,after=independent_edge(e); assert current==before;current=after;scale*=e['scale']
                counts[e['kind']]+=1;maxsize=max(maxsize,sum(before[0]),sum(after[0]));outbox|=sum(before[0])>30 or sum(after[0])>30
                path_examples.setdefault(e['kind'],e)
            assert current==norm(rec['target']) and scale==rec['scale'] and key(current)<=key(original)
            box(current);scales[scale]+=1;maxedges=max(maxedges,len(rec['path']))
            if current==original:fixed.add(i)
            else:assert key(current)<key(original)
            outboxpaths+=outbox
            if outbox:path_examples.setdefault('out_of_box_path',rec)
        expected=set(range(16153,len(rows))) if name.startswith('reduction_') else set(json.loads((OLD/'horn_core_source_indices.json').read_text()))
        assert seen==expected
        expectedfixed=json.loads((OLD/'reduction_closure_fixed_points.json').read_text())['fixed_source_indices'] if name.startswith('reduction_') else json.loads((OLD/'general_rectangular_closure_fixed_indices.json').read_text())
        assert fixed==set(expectedfixed) and len(fixed)==len(expectedfixed)
        stages[name]={'sources':len(seen),'fixed':len(fixed),'smaller_keys':len(seen-fixed),'edge_counts':dict(counts),
                      'max_intermediate_outer_size':maxsize,'out_of_box_paths':outboxpaths,'max_edges':maxedges,'accumulated_scales':dict(scales)}
        print(json.dumps({'stage':'paths','name':name,'elapsed_s':time.monotonic()-start}),flush=True)
    # Stored small Horn factors are redundant for the original checker; independently
    # compare every stored target/factor to the literal selected-index formula.
    factor_count=0
    for raw in (OLD/'small_minimum_core_exclusions.jsonl').open():
        rec=json.loads(raw)
        if rec['kind']!='ESSENTIAL_HORN':continue
        row=domains['small'][rec['index']];T=[tuple(row[k]) for k in ('lambda','mu','nu')];n=len(T[0]);T=[p+(0,)*(n-len(p)) for p in T]
        fac=rec['facet'];expected=[]
        for complement in (False,True):
            ft=tuple(tuple(x for j,x in enumerate(p) if (j in fac[k])!=complement) for p,k in zip(T,('K','I','J')))
            expected.append(tuple(strict_partition(p) for p in ft))
        assert expected==[tuple(strict_partition(p) for p in ft) for ft in rec['factors']]
        factor_count+=1
    save('corpus_inventory.json',{'journals':summaries,'paths':stages,'literal_small_stored_horn_factors':factor_count,'elapsed_s':time.monotonic()-start})
    save('selected_cases.json',samples);save('selected_edges.json',path_examples)

def array_hive_binding():
    results=[]
    for n in range(1,8):
        coords=[(r,k) for r in range(1,n+1) for k in range(1,r+1)]
        variables=len(coords)+n;checks=0;family_counts=Counter()
        for basis in range(-1,variables):
            x={(r,k):int(i==basis) for i,(r,k) in enumerate(coords)}
            mu=[int(basis==len(coords)+r) for r in range(n)]
            X=lambda r,k:x.get((r,k),0)
            outer=[mu[r-1]+sum(X(r,k) for k in range(1,n+1)) for r in range(1,n+1)]
            nu=[sum(X(r,k) for r in range(1,n+1)) for k in range(1,n+1)]
            F=lambda b,j:sum(mu[:j])+sum(X(r,k) for r in range(1,j+1) for k in range(1,b+1))
            h=lambda a,b:F(b,a+b)
            _,interior,rows=v.hive_system(outer,mu,nu,n=n)
            free=[h(*z) for z in interior]
            actual=[b+sum(c*z for c,z in zip(row,free)) for b,row in rows]
            expected=[]
            for a in range(n+1):
                for b in range(n+1):
                    s=a+b
                    if a+b+2<=n:
                        j=s+2;k=b+1
                        slack=mu[j-2]-mu[j-1]+sum(X(j-1,i) for i in range(1,k))-sum(X(j,i) for i in range(1,k+1))
                        expected.append(slack)
                        if basis==-1:family_counts['columns']+=1
                    if b>=1 and a+b+1<=n:
                        j=s+1;i=b
                        expected.append(sum(X(r,i) for r in range(1,j))-sum(X(r,i+1) for r in range(1,j+1)))
                        if basis==-1:family_counts['lattice']+=1
                    if a>=1 and a+b+1<=n:
                        expected.append(X(s+1,b+1))
                        if basis==-1:family_counts['offdiagonal_nonnegativity']+=1
            assert actual==expected
            # Invert exactly, including k>r support and edge/diagonal entries.
            G=lambda b,j:h(j-min(b,j),min(b,j))
            for r in range(1,n+1):
                for k in range(1,n+1):
                    assert G(k,r)-G(k-1,r)-G(k,r-1)+G(k-1,r-1)==X(r,k)
            checks+=1
        results.append({'rank':n,'array_and_inner_basis_dimension':variables,'basis_plus_zero':checks,'rhombus_counts':dict(family_counts),'all_slack_and_inverse_identities':True})
    save('array_hive_linear_identity.json',results)

def record_mutations():
    samples=json.loads((HERE/'selected_cases.json').read_text());results=[]
    for band in ('small','large'):
        source=OLD/f'audit_{"core" if band=="large" else "small"}_polynomial_records.py'
        tree=ast.parse(source.read_text())
        main=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='main')
        fn=next(x for x in main.body if isinstance(x,ast.FunctionDef) and x.name=='check_polynomial')
        fn=deepcopy(fn);fn.body=[x for x in fn.body if not isinstance(x,ast.Nonlocal)]
        # Hoist the exact archived nested function for isolated mutation testing;
        # replace only its nonlocal declaration with an equivalent global binding.
        fn.body.insert(0,ast.Global(names=['fresh_base_counts','evaluated_polynomial_values']))
        module=ast.fix_missing_locations(ast.Module(body=[fn],type_ignores=[]))
        rec=samples[band];i=rec['index'];p=rec['polynomial'];row={k:p[k] for k in ('lambda','mu','nu','c')}
        env=dict(Fraction=Fraction,factorial=factorial,evaluate=v.evaluate,v=v,rows={i:row},core={i},
                 fresh_base_counts=0,evaluated_polynomial_values=0,distinct={},negative=[],all_sizes=Counter(),
                 core_sizes=Counter(),degree_counts=Counter(),core_distinct=set(),engines=Counter())
        exec(compile(module,str(source),'exec'),env)
        check=env['check_polynomial'];check(i,deepcopy(p))
        q=deepcopy(p); co=list(map(Fraction,q['coefficients']))
        perturb=[0,Fraction(-1,4),Fraction(11,24),Fraction(-1,4),Fraction(1,24)]
        for j,c in enumerate(perturb):co[j]+=c
        assert all(c>=0 for c in co)
        q['coefficients']=list(map(str,co));q['values']=[int(v.evaluate(co,t)) for t in range(len(q['values']))]
        check(i,q)
        assert q['values'][:4]==p['values'][:4] and q['values'][4]==p['values'][4]+1
        results.append({'band':band,'index':i,'mutation':'P + binomial(t,4), all coefficients still nonnegative',
                        'archived_check_accepts':True,'source_checker_sha256':sha256(source.read_bytes()).hexdigest(),
                        'original_coefficients':p['coefficients'],'mutated_coefficients':q['coefficients'],
                        'original_values_t0_to4':p['values'][:5],'mutated_values_t0_to4':q['values'][:5],
                        'meaning':'Saved-value consistency and fresh t=1 cannot identify the full polynomial; immutable archive hashes prevent unnoticed byte substitution.'})
        empty=deepcopy(p);empty['values']=[];check(i,empty)
        fake=deepcopy(p);fake['hive_variables']=-999;fake['normaliz_vertices']=-1;fake['triangulation_size']=-1
        check(i,fake)
        results.append({'band':band,'index':i,'empty_values_accepted':True,'nonsensical_hive_engine_metadata_accepted':True})
        malformed=deepcopy(p);malformed['lambda'][0]+=1
        try:check(i,malformed)
        except AssertionError:rejected=True
        else:rejected=False
        assert rejected
        results.append({'band':band,'index':i,'wrong_source_triple_rejected':rejected})
    save('record_mutations.json',results)

def actual_controls():
    controls=[
        ('negative_coordinate_interval',1,[(2,[1]),(-1,[-1])],['1','1'],None),
        ('period2_interval',1,[(0,[1]),(1,[-2])],None,'period 2'),
        ('period2_point',1,[(-1,[2]),(1,[-2])],None,'period 2'),
        ('full_lattice_diagonal_segment',2,[(0,[1,0]),(2,[-1,0]),(0,[1,-1]),(0,[-1,1])],['1','2'],None),
        ('empty_interval',1,[(-2,[1]),(1,[-1])],[],None),
        ('reeve_m13_negative_linear',3,[(0,[0,0,1]),(0,[13,0,-1]),(0,[0,13,-1]),(13,[-13,-13,1])],['1','-1/6','1','13/6'],None)]
    oldhive=v.hive_system; oldrun=subprocess.run;results=[]
    for name,d,rows,expected,error in controls:
        leaf=HERE/'controls'/name;leaf.mkdir(parents=True,exist_ok=True)
        def retained_run(args,**kwargs):
            ret=oldrun(args,**kwargs)
            for p in Path(kwargs['cwd']).iterdir():
                if p.is_file():(leaf/p.name).write_bytes(p.read_bytes())
            (leaf/'stdout.txt').write_text(ret.stdout or '');(leaf/'stderr.txt').write_text(ret.stderr or '')
            save(str((leaf/'invocation.json').relative_to(HERE)),{'args':args,'returncode':ret.returncode,'timeout':kwargs.get('timeout')})
            return ret
        try:
            v.hive_system=lambda *args,**kwargs:(d+2,list(range(d)),rows)
            subprocess.run=retained_run
            try:
                r=v.ehrhart_polynomial_normaliz([1],[1],[],deadline=v.Deadline(20),threads=1)
                actual=list(map(str,r['coefficients']));assert error is None and actual==expected
                result={'coefficients':actual,'mode':r['mode']}
            except v.EngineError as e:
                assert error is not None and error in str(e)
                result={'expected_rejection':str(e)}
            results.append({'name':name,'result':result,'raw_files':{p.name:sha256(p.read_bytes()).hexdigest() for p in leaf.iterdir() if p.is_file()}})
        finally:v.hive_system=oldhive;subprocess.run=oldrun
    exe=Path(v._find_normaliz())
    save('actual_engine_controls.json',{'controls':results,'executable':str(exe),'sha256':sha256(exe.read_bytes()).hexdigest(),'version':oldrun([str(exe),'--version'],capture_output=True,text=True,check=True).stdout})

@lru_cache(None)
def independent_partitions(N,h,M):
    if N==0:return ((),)
    if h==0:return ()
    return tuple((a,)+p for a in range(1,min(N,M)+1) for p in independent_partitions(N-a,h-1,a))

def cell_lr(outer,mu,nu):
    """Literal cell fillings; no hive, row-array DP, or lrcalc algorithm reused."""
    if sum(outer)!=sum(mu)+sum(nu) or len(mu)>len(outer):return 0
    mu=mu+(0,)*(len(outer)-len(mu))
    if any(a>b for a,b in zip(mu,outer)):return 0
    cells=[(r,c) for r,L in enumerate(outer) for c in range(L,mu[r],-1)]
    used=[0]*len(nu);assigned={}
    def fill(j):
        if j==len(cells):return int(tuple(used)==nu)
        r,c=cells[j];total=0
        for k in range(len(nu)):
            if used[k]>=nu[k] or (k and used[k]>=used[k-1]):continue
            label=k+1
            if (r,c+1) in assigned and label>assigned[r,c+1]:continue
            if (r-1,c) in assigned and label<=assigned[r-1,c]:continue
            assigned[r,c]=label;used[k]+=1;total+=fill(j+1);used[k]-=1;del assigned[r,c]
        return total
    return fill(0)

def partition_and_low_c_controls():
    start=time.monotonic()
    source=OLD/'independent_full_domain_enumeration.py';tree=ast.parse(source.read_text())
    fn=next(x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name=='all_partitions')
    env={};exec(compile(ast.Module(body=[fn],type_ignores=[]),str(source),'exec'),env)
    produced=env['all_partitions']();sizes={}
    for N in range(31):
        expected=set(independent_partitions(N,7,30));actual=produced[N]
        assert expected==set(actual) and len(actual)==len(expected);sizes[N]=len(expected)
    counts=Counter();counts_by_N={}
    for N in range(11):
        local=Counter()
        for outer in produced[N]:
            for M in range((N+1)//2,N+1):
                for mu in produced[M]:
                    for nu in produced[N-M]:
                        if M==N-M and mu<nu:continue
                        independent=cell_lr(outer,mu,nu)
                        actual=v.lr_lrcalc(outer,mu,nu)
                        assert independent==actual,(outer,mu,nu,independent,actual)
                        local['triples']+=1;local[f'base_c_{min(actual,3)}'+('_or_more' if actual>=3 else '')]+=1
                        if actual<=2:
                            for t in (2,3):
                                got=v.lr_lrcalc(*[tuple(t*x for x in p) for p in (outer,mu,nu)])
                                expected=0 if actual==0 else 1 if actual==1 else t+1
                                assert got==expected,(outer,mu,nu,t,got,expected)
                                local['low_c_stretch_controls']+=1
        counts.update(local);counts_by_N[N]=dict(local)
    save('partition_low_c_controls.json',{'partition_set_equality_sizes_0_to30':sizes,'literal_cell_vs_lrcalc_counts':dict(counts),
         'by_outer_size':counts_by_N,'elapsed_s':time.monotonic()-start,
         'scope':'All normalized balanced triples of outer size 0..10 and lengths<=7. Low-c stretches t=2,3 are finite controls, not proofs of the all-stretch theorems.'})

def parser_and_reduction_mutations():
    results=[];source=OLD/'audit_core_certificates.py'
    tree=ast.parse(source.read_text());fns=[x for x in tree.body if isinstance(x,ast.FunctionDef) and x.name in ('canonical','certify')]
    env={'gcd':gcd};exec(compile(ast.Module(body=fns,type_ignores=[]),str(source),'exec'),env)
    certify=env['certify']; canonical=env['canonical']
    malformed=[[3,0,2,1],[2,1],[2,1]]
    accepted=canonical(malformed)
    assert accepted==((3,2,1),(2,1),(2,1))
    try:norm(malformed)
    except AssertionError:strict_reject=True
    else:strict_reject=False
    assert strict_reject
    results.append({'case':'interior zero in malformed partition','archived_canonical_accepts':True,'strict_independent_check_rejects':True})
    e=json.loads((HERE/'selected_edges.json').read_text())['shortening']
    assert e['params']['inner']=='nu'
    bad=deepcopy(e);bad['params']['inner']='unknown-invalid-inner'
    assert certify(bad,v)==certify(e,v)
    results.append({'case':'unknown inner selector','archived_edge_checker_accepts_as_nu':True,'actual_frozen_corpus_has_no_such_selectors':True})
    bad=deepcopy(e);bad['scale']=2
    try:certify(bad,v)
    except AssertionError:rejected=True
    else:rejected=False
    assert rejected
    results.append({'case':'wrong scale on shortening','rejected':True})
    bad=deepcopy(e);bad['kind']='unproved_rule'
    try:certify(bad,v)
    except AssertionError:rejected=True
    else:rejected=False
    assert rejected
    results.append({'case':'unknown reduction rule','rejected':True})
    # This is deliberately false engine output: a single feasible integral point
    # inside an interval is not a certificate that the interval is that point.
    false_point=v._parse_latte_taylor('', 'Ax = b, given as (b|-A):\n========================\n[1 -1]\n\nThe number of lattice points is 1.',0,5,1,[(0,[1]),(2,[-1])])
    assert false_point['values']==[1]*5
    results.append({'case':'fabricated LattE equality x=1 for interval [0,2]','pure_parser_accepts_values':false_point['values'],
                    'actual_values':[1,3,5,7,9],'paired_correct_Normaliz_would_reject':True,
                    'meaning':'Point-mode verifies reported equalities and feasibility, not that all original points satisfy those equalities; this trust boundary is disclosed in frozen source.'})
    for name,stdout,stderr,rc in [
        ('missing_taylor','1\n3t^2\n','',0),('duplicate_taylor','1\n2t^1\n2t^1\n3t^2\n','',0),
        ('nonzero_exit','1\n2t^1\n3t^2\n','',1)]:
        try:v._parse_latte_taylor(stdout,stderr,rc,3,1,[(0,[1]),(2,[-1])])
        except v.EngineError:rejected=True
        else:rejected=False
        assert rejected;results.append({'case':name,'rejected':True})
    save('parser_and_reduction_mutations.json',results)

def horn_and_final_cover():
    start=time.monotonic();catalog=json.loads((OLD/'horn_essential_catalog.json').read_text());catcounts={};celltests=0
    for n in range(2,8):
        expected=set()
        for r in range(1,n):
            choices=list(combinations(range(n),r))
            tau={I:tuple(x for x in reversed(tuple(a-j for j,a in enumerate(I))) if x) for I in choices}
            for I in choices:
                for J in choices:
                    total=sum(tau[I])+sum(tau[J])
                    for K in choices:
                        if sum(tau[K])!=total:continue
                        celltests+=1
                        if cell_lr(tau[K],tau[I],tau[J])==1:expected.add((r,I,J,K))
        actual={(f['r'],tuple(f['I']),tuple(f['J']),tuple(f['K'])) for f in catalog[str(n)]}
        assert actual==expected and len(actual)==len(catalog[str(n)])
        catcounts[n]=len(actual)
    large=json.loads((OLD/'conditional_domain_c_ge3.json').read_text());small=json.loads((OLD/'small_minimum_domain.json').read_text())
    fixed=set(json.loads((OLD/'reduction_closure_fixed_points.json').read_text())['fixed_source_indices'])
    horncore=set(json.loads((OLD/'horn_core_source_indices.json').read_text()))
    boundaries=set();factorcalls=0;counts=Counter()
    def horn_check(T,f,expected_counts):
        nonlocal factorcalls
        l,m,u=T;n=len(l);m+=(0,)*(n-len(m));u+=(0,)*(n-len(u))
        assert sum(l[j] for j in f['K'])==sum(m[j] for j in f['I'])+sum(u[j] for j in f['J'])
        cs=[]
        for complement in (False,True):
            target=norm(tuple(tuple(x for j,x in enumerate(p) if (j in f[k])!=complement) for p,k in zip((l,m,u),('K','I','J'))))
            box(target);assert 0<sum(target[0])<sum(l)
            cs.append(v.lr_lrcalc(*target));factorcalls+=1
        assert cs==expected_counts
        return cs[0]*cs[1]
    for line in (OLD/'horn_core_boundary_certificates.jsonl').open():
        rec=json.loads(line);i=rec['source_index'];assert i in fixed and i not in boundaries;boundaries.add(i)
        r=large[i];T=norm([r[k] for k in ('lambda','mu','nu')]);n=len(T[0]);assert rec['outer_length']==n
        f=catalog[str(n)][rec['facet_index']]
        assert horn_check(T,f,rec['factor_multiplicities'])==r['c'];counts['large_horn']+=1
    assert boundaries.isdisjoint(horncore) and boundaries|horncore==fixed
    rectfixed=set(json.loads((OLD/'general_rectangular_closure_fixed_indices.json').read_text()))
    secondraw=json.loads((OLD/'classical_second_affected_core_indices.json').read_text());second=set(secondraw)
    finalraw=json.loads((OLD/'combined_terminal_core_indices.json').read_text());final=set(finalraw)
    assert len(secondraw)==len(second) and len(finalraw)==len(final)
    # The stored second-rule probe was run on the broader Horn core. Only its
    # intersection with the later rectangular fixed points is a final exclusion.
    assert second<=horncore and final==rectfixed-second
    def shorten_check(T,p,q,a,kind):
        l,m,u=T;n=len(l);m+=(0,)*(n-len(m)+1);u+=(0,)*(n-len(u)+1);l+=(0,)
        r=p+q;assert type(p) is int and type(q) is int and type(a) is int
        assert p>=1 and q>=1 and r<=n and a>=1
        assert m[p-1]-a>=m[p] and u[q-1]-a>=u[q] and l[r-1]-a>=l[r]
        if kind=='RECTANGULAR':assert l[r-1]-a>=m[p]+u[q]
        else:assert kind=='SECOND_REDUCTION' and a==1 and m[p-1]+u[q-1]>=l[0]+l[r]+1
        target=norm(tuple(tuple(x-a*(j<k) for j,x in enumerate(part)) for part,k in zip((l,m,u),(r,p,q))))
        box(target);assert sum(target[0])<sum(T[0])
        return target
    for i in second:
        row=large[i];T=norm([row[k] for k in ('lambda','mu','nu')]);n=len(T[0]);l,m,u=[p+(0,)*(n-len(p)+1) for p in T]
        witnesses=[(p,q) for p in range(1,n) for q in range(1,n+1-p)
                   if m[p-1]>m[p] and u[q-1]>u[q] and l[p+q-1]>l[p+q] and m[p-1]+u[q-1]>=l[0]+l[p+q]+1]
        assert witnesses
        p,q=witnesses[0];target=shorten_check(T,p,q,1,'SECOND_REDUCTION')
        assert v.lr_lrcalc(*target)==row['c'];counts['large_second' if i in rectfixed else 'second_probe_already_excluded_earlier']+=1
    smallraw=json.loads((OLD/'small_minimum_core_indices.json').read_text());smallcore=set(smallraw);assert len(smallcore)==len(smallraw)
    seen=set()
    for line in (OLD/'small_minimum_core_exclusions.jsonl').open():
        rec=json.loads(line);i=rec['index'];assert 0<=i<len(small) and i not in seen and i not in smallcore;seen.add(i)
        row=small[i];T=norm([row[k] for k in ('lambda','mu','nu')])
        if rec['kind']=='ESSENTIAL_HORN':
            f=rec['facet'];assert f in catalog[str(len(T[0]))]
            assert horn_check(T,f,rec['factor_c'])==row['c'];counts['small_horn']+=1
        else:
            target=shorten_check(T,rec['p'],rec['q'],rec['a'],rec['kind'])
            assert norm(rec['target'])==target and v.lr_lrcalc(*target)==row['c'];counts['small_'+rec['kind'].lower()]+=1
    assert seen|smallcore==set(range(len(small)))
    save('horn_and_final_cover.json',{'status':'PASS','cell_count_catalog_sizes':catcounts,'independent_literal_cell_catalog_tests':celltests,
         'counts':dict(counts),'fresh_lrcalc_factor_calls':factorcalls,'small_core':len(smallcore),'large_core':len(final),
         'all_horn_factor_box_size_and_balance_checks':True,'all_final_shortening_premises_and_targets_checked':True,
         'all_partition_cover_unions_disjoint_complete':True,'elapsed_s':time.monotonic()-start})

if __name__=='__main__':
    start=time.monotonic()
    mode=arguments.mode
    if mode in ('inventory','all'):corpus_inventory()
    if mode in ('controls','all'):array_hive_binding();record_mutations();actual_controls()
    if mode in ('extra','all'):partition_and_low_c_controls();parser_and_reduction_mutations()
    if mode in ('finalcover','all'):horn_and_final_cover()
    print(json.dumps({'status':'COMPLETE','mode':mode,'elapsed_s':time.monotonic()-start}),flush=True)
