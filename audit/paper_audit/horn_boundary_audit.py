"""Independent finite construction of subset tests and bounded factor checks."""
from itertools import combinations, product
from pathlib import Path
from collections import Counter
import json
from exact_boundary_audit import parts, contained, lr, pad, trim

root=Path(__file__).resolve().parent
catalog={}
counts=Counter()
examples={}
def tau(I): return trim(tuple(i-j for j,i in reversed(tuple(enumerate(I,1)))))
for n in range(2,8):
    catalog[n]=[]
    for r in range(1,n):
        subsets=tuple(combinations(range(1,n+1),r))
        for I,J,K in product(subsets,repeat=3):
            ti,tj,tk=tau(I),tau(J),tau(K)
            if sum(tk)!=sum(ti)+sum(tj): continue
            counts['balanced_subset_tests']+=1
            if lr((tk,ti,tj))==1: catalog[n].append((I,J,K))
    assert len(catalog[n])=={2:3,3:12,4:41,5:142,6:521,7:2042}[n]
for total in range(1,11):
    for la in parts(total,5):
        n=len(la)
        if n<2:continue
        for msum in range(total+1):
            for mu in parts(msum,5):
                if not contained(mu,la):continue
                for nu in parts(total-msum,5):
                    if not contained(nu,la):continue
                    source=la,mu,nu
                    if lr(source)==0:continue
                    counts['positive_sources']+=1
                    l,m,v=pad(la,n),pad(mu,n),pad(nu,n)
                    for I,J,K in catalog[n]:
                        select=lambda p,Q:trim(tuple(p[i-1] for i in Q))
                        comp=lambda Q:tuple(i for i in range(1,n+1) if i not in Q)
                        f1=select(l,K),select(m,I),select(v,J)
                        if sum(f1[0])!=sum(f1[1])+sum(f1[2]):continue
                        f2=select(l,comp(K)),select(m,comp(I)),select(v,comp(J))
                        assert 0<sum(f1[0])<total and 0<sum(f2[0])<total
                        for t in (1,2,3):
                            assert lr(source,t)==lr(f1,t)*lr(f2,t),(source,I,J,K,t)
                            counts['stretch_factor_equalities']+=1
                        counts['factorizations']+=1
                        examples.setdefault('first',{'source':source,'I':I,'J':J,'K':K,'factors':[f1,f2]})
output={'catalog_counts':{n:len(v) for n,v in catalog.items()},'scope':{'outer_size_at_most':10,'length_at_most':5,'stretches':[1,2,3]},'counts':dict(counts),'examples':examples,'limit':'Bounded falsification and exact catalog counts, not a proof of all Horn instances or all stretches.'}
(root/'horn_boundary_results.json').write_text(json.dumps(output,indent=2)+'\n')
print(json.dumps(output,indent=2))
