"""Strict saved metadata/cross-check consistency supplement; no engine calls."""
from collections import Counter
from fractions import Fraction
import json
from pathlib import Path
import re
import time

HERE=Path(__file__).resolve().parent
OLD=HERE/'archive/problems/stretched-lr-coefficients/runs/20260905T173132Z'
start=time.monotonic();counts=Counter()
def check(p):
    co=[Fraction(x) for x in p['coefficients']]
    assert all(type(x) is str and re.fullmatch(r'-?\d+(?:/[1-9]\d*)?',x) for x in p['coefficients'])
    for k in ('n','degree','degree_bound','hive_variables','normaliz_vertices','triangulation_size'):
        assert type(p[k]) is int and p[k]>=0,(k,p[k])
    assert p['normaliz_vertices']>0
    assert p['min_coefficient']==str(min(co))
    assert p['min_coefficient_index']==min(range(len(co)),key=lambda i:co[i])
    interior=list(range(1,len(co)-1)) or [0]
    i=min(interior,key=lambda i:co[i])
    assert p['min_interior_coefficient']==str(co[i]) and p['min_interior_index']==i
    assert p['leading_coefficient']==str(co[-1])
    assert all(type(x) is int and x>=0 for x in p['values'])
    cross=p['cross_checks']
    for t in (1,2,3):
        name=f'lrcalc_t{t}'
        if name in cross:assert type(cross[name]) is int and cross[name]==p['values'][t]
        else:assert t>1 and name+'_skipped' in cross and p['values'][t]>2000000
    if 'lr_tableau_dp_t1' in cross:assert type(cross['lr_tableau_dp_t1']) is int and cross['lr_tableau_dp_t1']==p['c']
    if p['latte_crosscheck']=='full':
        assert 'latte' in p['engines'] and cross['latte_values_t0_to']==p['degree_bound']+2
    counts['computed_records_checked']+=1
for band,journal in [('small','small_minimum_signs/results.jsonl'),('large','conditional_scan/results.jsonl')]:
    for line in (OLD/journal).open():
        rec=json.loads(line)
        if rec['status']=='COMPUTED':check(rec['polynomial']);counts[band]+=1
check(json.loads((OLD/'hard_case_current_source.json').read_text())['polynomial']);counts['recovery']=1
report={'status':'PASS','counts':dict(counts),'strict_coefficient_text_engine_metadata_and_cross_checks':True,'elapsed_s':time.monotonic()-start}
(HERE/'metadata_supplement.json').write_text(json.dumps(report,indent=2)+'\n');print(json.dumps(report))
