"""Bounded publication-gate probes; no arithmetic engines or corpus inventory.

All writes are private fixtures beside this script. Isolated AST fragments are
explicitly identified: they do not claim an actual complete build was executed.
"""
from pathlib import Path
from hashlib import sha256
import ast
import json
import subprocess
import sys
import tempfile

sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
AUDIT=HERE.parents[1]
PUB=AUDIT.parent/'20260906T123424Z_exhaustive_release'
ORIGINAL=HERE.parent/'adversarial_checks.py'
STRICT=PUB/'release_additions/audit/code/strict_corpus_audit.py'

def source(path):return path.read_text()
def pinned(path):return {'path':str(path),'sha256':sha256(path.read_bytes()).hexdigest()}
def selected_main(path,predicate):
    node=next(n for n in ast.parse(source(path)).body if isinstance(n,ast.FunctionDef) and n.name=='main')
    return [n for n in node.body if predicate(n)]
def execute(nodes,namespace,optimize=0):
    exec(compile(ast.Module(body=nodes,type_ignores=[]),'<isolated production statements>','exec',optimize=optimize),namespace)

def main():
    result={'scope':'Bounded code/gate probes, not an actual publication or full corpus run',
            'engines_executed':False,'sources':{n:pinned(p) for n,p in
                [('builder',PUB/'build_tools/build_release.py'),('sealer',PUB/'build_tools/seal_release.py'),
                 ('strict',STRICT),('original',ORIGINAL)]},'probes':{}}
    with tempfile.TemporaryDirectory(prefix='fixtures_',dir=HERE) as t:
        fixture=Path(t);fakepub=fixture/'pub';fakepub.mkdir()
        raw=fixture/'audit/full_regeneration';raw.mkdir(parents=True)
        report=fakepub/'release_additions/audit/FINAL_AUDIT.md';report.parent.mkdir(parents=True)
        report.write_text('Synthetic placeholder, not an audit.\n')
        (raw/'complete.json').write_text(json.dumps({'status':'COMPLETE','all_core_regeneration_complete':True,
                                                   'verified_cases':358952,'total':358952}))
        names={'audit_root','regeneration'}
        def gate(n):
            return ((isinstance(n,ast.Assign) and isinstance(n.targets[0],ast.Name) and n.targets[0].id in names)
                    or (isinstance(n,ast.If) and ('regeneration[' in ast.unparse(n.test)
                                                or 'FINAL_AUDIT.md' in ast.unparse(n.test))))
        nodes=selected_main(PUB/'build_tools/build_release.py',gate)
        execute(nodes,{'ROOT':fixture,'HERE':fakepub,'config':{'audit_run':'audit'},'json':json})
        result['probes']['producer_summary_without_raw_or_portable']=dict(
            gate_accepted=True,raw_cases_present=0,portable_receipt_present=False,
            asset_present=False,final_audit_is_placeholder=True,production_statements=len(nodes))

        assertions=selected_main(PUB/'build_tools/seal_release.py',lambda n:
                                  isinstance(n,ast.Assert) and 'full[' in ast.unparse(n.test))
        invalid={'status':'BOUNDED_VALIDATION','all_core_regeneration_complete':False,'verified_cases':128,'total':358952}
        outcomes={}
        for opt in (0,2):
            try:execute(assertions,{'full':invalid},optimize=opt);outcomes[str(opt)]='accepted'
            except AssertionError:outcomes[str(opt)]='rejected'
        result['probes']['sealer_complete_assertions_under_optimization']=outcomes

        old=fixture/'old';root=fixture/'release'
        for p in (old,root):(p/'evidence/parts').mkdir(parents=True)
        text=json.dumps({'parts':[{'path':'evidence/parts/evidence.zip.part-000','sha256':sha256(b'good').hexdigest()}]})
        for p in (old,root):(p/'evidence/PARTS.json').write_text(text)
        (old/'evidence/parts/evidence.zip.part-000').write_bytes(b'good')
        (root/'evidence/parts/evidence.zip.part-000').write_bytes(b'corrupted')
        nodes=selected_main(PUB/'build_tools/seal_release.py',lambda n:
                            isinstance(n,ast.Assert) and 'PARTS.json' in ast.unparse(n.test))
        # Original OLD layout has a nested stretched-lr-full-proof directory.
        (fixture/'old-wrapper').mkdir();old.rename(fixture/'old-wrapper/stretched-lr-full-proof')
        execute(nodes,{'root':root,'OLD':fixture/'old-wrapper'})
        result['probes']['evidence_manifest_equality_with_changed_part']=dict(gate_accepted=True,part_changed=True,
            caveat='This tests the exact isolated part-preservation assertion, not an entire seal.')

        packet=fixture/'packet';packet.mkdir()
        (packet/'MANIFEST.json').write_bytes((AUDIT/'replay/packet/MANIFEST.json').read_bytes())
        (packet/'verify.py').write_text('from pathlib import Path\nimport sys\np=Path(sys.argv[sys.argv.index("--output")+1])\np.with_name("untrusted_verifier_executed.txt").write_text("executed before file integrity verification")\n')
        out=fixture/'strict-output'
        call=subprocess.run([sys.executable,'-I','-B',str(STRICT),'--packet',str(packet),'--output',str(out),'inventory'],
                            capture_output=True,text=True,timeout=20)
        marker=out/'untrusted_verifier_executed.txt'
        result['probes']['strict_startup_executes_unverified_packet_verifier']=dict(
            untrusted_code_executed=marker.is_file(),returncode=call.returncode,
            stdout=call.stdout,stderr=call.stderr,
            caveat='Deliberately incomplete synthetic packet; it fails after the unverified verifier has already executed. No inventory ran.')

    olddefs={n.name:ast.dump(n,include_attributes=False) for n in ast.parse(source(ORIGINAL)).body if isinstance(n,ast.FunctionDef)}
    newdefs={n.name:ast.dump(n,include_attributes=False) for n in ast.parse(source(STRICT)).body if isinstance(n,ast.FunctionDef)}
    result['function_body_comparison']={'same_names':olddefs.keys()==newdefs.keys(),
        'functions_compared':len(olddefs),'all_unchanged':olddefs==newdefs,
        'changed_names':[n for n in olddefs if olddefs[n]!=newdefs.get(n)]}
    (HERE/'bounded_probe_results.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result,indent=2))

if __name__=='__main__':main()
