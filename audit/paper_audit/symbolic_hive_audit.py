"""Exact symbolic verification of manuscript coordinate and slack identities."""
from pathlib import Path
import json
import sympy as s

ROOT = Path(__file__).resolve().parent
counts = {'ranks': [], 'equalities': 0, 'rectangle_slack_equalities': 0}

def eq(a, b=0):
    assert s.expand(a-b) == 0, s.expand(a-b)
    counts['equalities'] += 1

for n in range(1, 8):
    mu = (0,) + s.symbols(f'm1:{n+1}')
    nu = (0,) + s.symbols(f'v1:{n+1}')
    ll = s.symbols(f'l1:{n}')
    la = (0,) + ll + (sum(mu)+sum(nu)-sum(ll),)
    h = {}
    for a in range(n+1):
        for b in range(n+1-a):
            if b == 0: value = sum(mu[:a+1])
            elif a == 0: value = sum(la[:b+1])
            elif a+b == n: value = sum(mu)+sum(nu[:b+1])
            else: value = s.Symbol(f'h{a}_{b}')
            h[a,b] = value
    def F(b,j):
        return h[j-min(b,j),min(b,j)]
    x = {(r,k):s.expand(F(k,r)-F(k-1,r)-F(k,r-1)+F(k-1,r-1))
         for r in range(1,n+1) for k in range(1,n+1)}
    def S(j,i):
        return sum(x[r,i] for r in range(1,j+1))
    def y(j,b):
        return mu[j]+sum(x[j,k] for k in range(1,b+1))
    def L(j,i): return S(j-1,i)-S(j,i+1)
    def C(j,b): return y(j-1,b-1)-y(j,b)
    for r in range(1,n+1):
        eq(sum(x[r,k] for k in range(1,n+1)),la[r]-mu[r])
        for k in range(r+1,n+1): eq(x[r,k])
    for k in range(1,n+1): eq(S(n,k),nu[k])
    for a,b in h:
        eq(h[a,b],sum(mu[:a+b+1])+sum(x[r,k] for r in range(1,a+b+1) for k in range(1,b+1)))
        ss=a+b
        if (a+1,b+1) in h:
            eq(h[a+1,b]+h[a,b+1]-h[a,b]-h[a+1,b+1],C(ss+2,b+1))
        if (a,b+1) in h and (a+1,b-1) in h:
            eq(h[a,b]+h[a+1,b]-h[a,b+1]-h[a+1,b-1],L(ss+1,b))
        if (a+1,b) in h and (a-1,b+1) in h:
            eq(h[a,b]+h[a,b+1]-h[a+1,b]-h[a-1,b+1],x[ss+1,b+1])
    eq(x[n,n],nu[n])
    for r in range(1,n):eq(L(r+1,r),x[r,r]-x[r+1,r+1])
    for j in range(1,n+1):
        for i in range(j,n):eq(L(j,i))
    for j in range(2,n+1):
        for b in range(j,n+1):eq(C(j,b),la[j-1]-la[j])
    # Rectangular changes are identities on the entire unconstrained array space.
    a=s.Symbol('a')
    xx={(j,i):s.Symbol(f'x{j}_{i}') for j in range(1,n+1) for i in range(1,n+1)}
    for p in range(1,n):
        for q in range(1,n-p+1):
            r=p+q
            delta={(p+i,i): -a for i in range(1,q+1)}
            for j in range(1,n+1):
                for i in range(1,n):
                    change=sum(delta.get((z,i),0) for z in range(1,j))-sum(delta.get((z,i+1),0) for z in range(1,j+1))
                    eq(change,-a if i==q and j>=r+1 else 0)
                    counts['rectangle_slack_equalities']+=1
            for j in range(2,n+1):
                for b in range(1,n+1):
                    change=-a*int(j-1<=p)+a*int(j<=p)+sum(delta.get((j-1,i),0) for i in range(1,b))-sum(delta.get((j,i),0) for i in range(1,b+1))
                    eq(change,-a if j==r+1 and b>=q+1 else 0)
                    counts['rectangle_slack_equalities']+=1
    counts['ranks'].append(n)
(ROOT/'symbolic_hive_results.json').write_text(json.dumps(counts,indent=2)+'\n')
print(json.dumps(counts,indent=2))
