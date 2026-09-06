"""Fresh bounded falsification tests; imports no manuscript implementation.

This does NOT certify all stretches or the full size-thirty enumeration.
"""
from collections import Counter
from functools import lru_cache
from pathlib import Path
import json
import time
import lrcalc

ROOT = Path(__file__).resolve().parent

@lru_cache(None)
def parts(total, height=6, ceiling=12):
    if total == 0:
        return ((),)
    if height == 0:
        return ()
    return tuple((a,) + rest for a in range(1, min(total, ceiling) + 1)
                 for rest in parts(total-a, height-1, a))

def trim(p):
    return tuple(x for x in p if x)

def pad(p, n):
    return p + (0,)*(n-len(p))

def contained(p, l):
    return len(p) <= len(l) and all(a <= b for a, b in zip(p, l))

@lru_cache(None)
def lr(tup, stretch=1):
    return int(lrcalc.lrcoef(*(tuple(stretch*x for x in p) for p in tup)))

def direct_tableaux(tup):
    l, m, v = tup
    if sum(l) != sum(m)+sum(v) or not contained(m, l):
        return 0
    m = pad(m, len(l))
    cells = [(j, c) for j in range(len(l)) for c in range(l[j], m[j], -1)]
    cells_set = set(cells)
    used = [0]*len(v)
    filling = {}
    def rec(k):
        if k == len(cells):
            return int(tuple(used) == v)
        j, c = cells[k]
        lo = filling.get((j-1, c), 0)+1 if (j-1, c) in cells_set else 1
        hi = filling.get((j, c+1), len(v))
        ans = 0
        for label in range(lo, hi+1):
            i = label-1
            if used[i] == v[i] or (i and used[i] >= used[i-1]):
                continue
            used[i] += 1
            filling[j, c] = label
            ans += rec(k+1)
            used[i] -= 1
            del filling[j, c]
        return ans
    return rec(0)

def smaller(p, k, a=1):
    return trim(tuple(x-a*(j < k) for j, x in enumerate(p)))

def main():
    started = time.monotonic()
    counts = Counter()
    examples = {}
    def check(rule, source, target, params):
        for t in (1, 2, 3):
            assert lr(source, t) == lr(target, t), (rule, source, target, params, t)
            counts[rule + '_stretch_equalities'] += 1
        counts[rule + '_instances'] += 1
        key = rule + ('_zero' if lr(source) == 0 else '_positive')
        examples.setdefault(key, {'source': source, 'target': target, 'params': params,
                                  'values': [lr(source,t) for t in (1,2,3)]})
    for total in range(1, 13):
        for l in parts(total):
            n = len(l)
            lp = pad(l, n+1)
            for msum in range(total+1):
                for m in parts(msum):
                    if not contained(m,l):
                        continue
                    for v in parts(total-msum):
                        if not contained(v,l):
                            continue
                        source = l,m,v
                        counts['balanced_contained_triples'] += 1
                        base = lr(source)
                        if total <= 8:
                            assert direct_tableaux(source) == base, source
                            counts['independent_direct_tableau_counts'] += 1
                        mp,vp = pad(m,n+1),pad(v,n+1)
                        for k in range(1,n):
                            qk = sum(mp[:k])+sum(vp[:k])-sum(lp[:k])
                            if qk < 0:
                                continue
                            amax = min(lp[k-1]-lp[k], mp[k-1]-mp[k]-min(qk,lp[k]-mp[k]))
                            for a in range(1,amax+1):
                                target = smaller(l,k,a),smaller(m,k,a),v
                                check('strengthened',source,target,{'k':k,'a':a,'qk':qk})
                        for p in range(1,n):
                            for q in range(1,n-p+1):
                                r = p+q
                                amax = min(mp[p-1]-mp[p],vp[q-1]-vp[q],
                                           lp[r-1]-max(lp[r],mp[p]+vp[q]))
                                for a in range(1,amax+1):
                                    target=smaller(l,r,a),smaller(m,p,a),smaller(v,q,a)
                                    check('rectangular',source,target,{'p':p,'q':q,'a':a,'r_equals_n':r==n})
                                    if r==n: counts['rectangular_final_row_instances'] += 1
                                    if q==1: counts['rectangular_q1_instances'] += 1
                                good_gaps = mp[p-1]>mp[p] and vp[q-1]>vp[q] and lp[r-1]>lp[r]
                                margin = mp[p-1]+vp[q-1]-lp[0]-lp[r]
                                if good_gaps and margin>=1:
                                    target=smaller(l,r),smaller(m,p),smaller(v,q)
                                    check('second',source,target,{'p':p,'q':q,'margin':margin})
                                    if not contained(target[1],target[0]) or not contained(target[2],target[0]):
                                        counts['second_noncontained_targets'] += 1
                                        examples.setdefault('second_noncontained', {'source':source,'target':target,'params':{'p':p,'q':q},'values':[lr(source,t) for t in (1,2,3)]})
                                # Exact counterexample to deleting the +1 hypothesis.
                                if good_gaps and margin==0 and 'second_weakened_counterexample' not in examples:
                                    target=smaller(l,r),smaller(m,p),smaller(v,q)
                                    if lr(source)!=lr(target):
                                        examples['second_weakened_counterexample']={'source':source,'target':target,'params':{'p':p,'q':q},'source_values':[lr(source,t) for t in (1,2,3)],'target_values':[lr(target,t) for t in (1,2,3)]}
                        if base and mp[n-1]==vp[n-1]==0:
                            A,B=mp[:n],vp[:n]
                            L,h,u,w=lp[0],lp[n-1],mp[0],vp[0]
                            C=tuple(L-x for x in reversed(lp[:n]))
                            def complement(a,width):
                                return trim(tuple(width-x for x in reversed(a)))
                            for dual in (False,True):
                                X=(A,B,C)
                                width=L
                                if dual:
                                    X=tuple(pad(complement(a,a[0]),n) for a in X)
                                    width=u+w-h
                                for i in range(3):
                                    others=[trim(X[j]) for j in range(3) if j!=i]
                                    target=(complement(X[i],width),*others)
                                    assert all(x>=0 for x in target[0]), target
                                    assert sum(target[0])==sum(target[1])+sum(target[2]),target
                                    check('six',source,target,{'dual':dual,'choice':i})
        print(json.dumps({'completed_outer_size':total,'counts':dict(counts)}),flush=True)
    output={'scope':{'outer_size_at_most':12,'length_at_most':6,'stretches':[1,2,3],
                     'direct_tableau_outer_size_at_most':8},'counts':dict(counts),
            'examples':examples,'elapsed_seconds':time.monotonic()-started,
            'scope_limit':'Exact bounded falsification only; no all-stretch or full-box proof claimed.'}
    (ROOT/'exact_boundary_results.json').write_text(json.dumps(output,indent=2)+'\n')
    print(json.dumps(output,indent=2))

if __name__ == '__main__':
    main()
