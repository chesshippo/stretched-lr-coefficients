"""Small synthetic ZIP/gate tests. No actual raw corpus or arithmetic engines.

The completed-audit prerequisite is mocked for ZIP-level tests. These fixtures
are deliberately not evidence of any full mathematical computation.
"""
import ast
from contextlib import ExitStack
from copy import deepcopy
from hashlib import sha256
import importlib.util
import json
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import patch
import warnings
import zipfile

sys.dont_write_bytecode=True
HERE=Path(__file__).resolve().parent
AUDIT=HERE.parents[2]
PUB=AUDIT.parent/'20260906T123424Z_exhaustive_release'

def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path);m=importlib.util.module_from_spec(spec);spec.loader.exec_module(m);return m
old=module('current_gate',PUB/'build_tools/fresh_evidence_gate.py')
g=module('proposed_gate',HERE/'proposed/fresh_evidence_gate.py')

def byte_pin(value):return {'bytes':len(value),'sha256':sha256(value).hexdigest()}
def encoded(value):return (json.dumps(value,indent=2,sort_keys=True)+'\n').encode()

class GateTests(unittest.TestCase):
    def setUp(self):
        self.stack=ExitStack();self.addCleanup(self.stack.close)
        self.base=Path(self.stack.enter_context(tempfile.TemporaryDirectory(prefix='mock_',dir=HERE)))
        self.pub=self.base/'pub';self.audit=self.base/'audit';self.public=self.pub/'release_additions'
        (self.public/'audit').mkdir(parents=True);(self.audit/'full_regeneration').mkdir(parents=True)
        (self.pub/g.SUPPLEMENT).mkdir()
        self.config={'source_archive_sha256':g.ARCHIVE_SHA}
        self.producer={'identity':{'wrapper_sha256':g.WRAPPER_SHA}}
        self.portable={'status':'COMPLETE','verified_cases':g.TOTAL}
        (self.audit/'portable_full_validation.json').write_bytes(encoded(self.portable))
        (self.audit/'full_regeneration/complete.json').write_bytes(encoded(self.producer))
        for n in ('audit/FRESH_EVIDENCE.md','audit/FINAL_AUDIT.md','ARCHIVAL_ERRATA.md'):
            (self.public/n).write_text('Synthetic fixture; not proof evidence. '*8)
        self.payload={n:('Synthetic fixture '+n+'\n').encode() for n in
                      ['raw/identity.json','raw/batch-00000.json','raw/batch-00000.jsonl.gz',
                       'catalog/catalog.sqlite','catalog/catalog.json','catalog/binding.json','catalog/engines.json',
                       'validator/validate_raw_supplement.py','producer/parallel_regenerate.py','tools/unpack_frozen_packet.py',
                       'LICENSE','LICENSES/CC-BY-4.0.txt']}
        self.payload['raw/complete.json']=(self.audit/'full_regeneration/complete.json').read_bytes()
        self.payload['validation/portable-complete.json']=(self.audit/'portable_full_validation.json').read_bytes()
        for n in ('README.md','LICENSING.md','NOTICE','THIRD_PARTY_NOTICES.md'):
            self.payload[n]=('Synthetic fixture; not proof evidence. '*8).encode()
        self.expected={n:byte_pin(b) for n,b in self.payload.items() if '/' in n or n=='LICENSE'}
        (self.public/'audit/code').mkdir()
        (self.public/'audit/code/unpack_frozen_packet.py').write_bytes(self.payload['tools/unpack_frozen_packet.py'])
        self.build()

    def build(self,payload=None,embedded_manifest=None,alter_stream=None,extra=None,duplicate=False,symlink=False,bad_sums=False):
        payload=self.payload if payload is None else payload
        manifest={'schema':'complete-raw-polynomial-supplement-v1','status':'COMPLETE','polynomials':g.TOTAL,
                  'rational_monomial_coefficients':g.COEFFICIENTS,'source_archive_sha256':g.ARCHIVE_SHA,
                  'validator_sha256':g.VALIDATOR_SHA,'identity':self.producer['identity'],
                  'files':{n:byte_pin(b) for n,b in payload.items()}}
        mbytes=encoded(manifest);self.manifest=mbytes
        path=self.pub/g.SUPPLEMENT/'MANIFEST.json';path.write_bytes(mbytes)
        pins=dict(manifest['files'],**{'MANIFEST.json':byte_pin(mbytes)})
        sums=''.join(f"{p['sha256']}  {n}\n" for n,p in sorted(pins.items(),key=lambda item:Path(item[0]).parts)).encode()
        asset=self.pub/(g.SUPPLEMENT+'.zip')
        with warnings.catch_warnings():
            warnings.simplefilter('ignore',UserWarning)
            with zipfile.ZipFile(asset,'w') as z:
                for n,b in payload.items():
                    if alter_stream and n==alter_stream:b+=b'changed within ZIP'
                    info=zipfile.ZipInfo(g.SUPPLEMENT+'/'+n)
                    if symlink and n=='raw/identity.json':info.create_system=3;info.external_attr=(stat.S_IFLNK|0o777)<<16
                    z.writestr(info,b)
                z.writestr(g.SUPPLEMENT+'/MANIFEST.json',mbytes if embedded_manifest is None else embedded_manifest)
                z.writestr(g.SUPPLEMENT+'/SHA256SUMS',b'wrong' if bad_sums else sums)
                if extra:z.writestr(extra,b'extra')
                if duplicate:z.writestr(g.SUPPLEMENT+'/raw/identity.json',payload['raw/identity.json'])
        self.evidence={'status':'COMPLETE','polynomials':g.TOTAL,'rational_monomial_coefficients':g.COEFFICIENTS,
            'portable_validation':g.pin(self.audit/'portable_full_validation.json'),
            'producer_completion':g.pin(self.audit/'full_regeneration/complete.json'),
            'identity':self.producer['identity'],'validator_sha256':g.VALIDATOR_SHA,
            'source_archive_sha256':g.ARCHIVE_SHA,'full_latte':False,'full_lean':False,
            'all_zip_members_byte_verified':True,'asset':{'filename':asset.name,**g.pin(asset)},
            'supplement_manifest':g.pin(path),'files':len(payload)+2}
        (self.public/'audit/FRESH_EVIDENCE.json').write_bytes(encoded(self.evidence))
        return asset

    def invoke(self,target=g):
        with patch.object(target,'require_completed_audit',return_value=(self.config,self.audit,self.producer,self.portable)):
            if target is g:
                with patch.object(g,'expected_payload_pins',return_value=self.expected),patch.object(g,'verify_migration',return_value={}):
                    return target.require_fresh_evidence(self.pub,self.base,self.public)
            return target.require_fresh_evidence(self.pub,self.base,self.public)

    def rejects(self,pattern=None):
        with self.assertRaisesRegex((ValueError,zipfile.BadZipFile),pattern or '.'):
            self.invoke()

    def test_genuine_synthetic_zip_passes(self):self.assertEqual(self.invoke()['status'],'COMPLETE')
    def test_old_gate_accepts_rehashed_unrelated_zip(self):
        asset=self.pub/(g.SUPPLEMENT+'.zip')
        with zipfile.ZipFile(asset,'w') as z:z.writestr('unrelated.txt','no evidence')
        self.evidence['asset'].update(g.pin(asset));(self.public/'audit/FRESH_EVIDENCE.json').write_bytes(encoded(self.evidence))
        self.assertEqual(self.invoke(old)['status'],'COMPLETE')
        self.rejects('ZIP member')
    def test_wrong_embedded_manifest(self):self.build(embedded_manifest=b'{}');self.rejects('embedded manifest')
    def test_rehashed_wrong_raw_payload(self):
        p=dict(self.payload);p['raw/batch-00000.jsonl.gz']=b'wrong raw';self.build(p);self.rejects('differs from verified audit')
    def test_rehashed_wrong_catalog_payload(self):
        p=dict(self.payload);p['catalog/binding.json']=b'wrong binding';self.build(p);self.rejects('differs from verified audit')
    def test_rehashed_wrong_validator(self):
        p=dict(self.payload);p['validator/validate_raw_supplement.py']=b'wrong code';self.build(p);self.rejects('differs from verified audit')
    def test_rehashed_wrong_producer(self):
        p=dict(self.payload);p['producer/parallel_regenerate.py']=b'wrong code';self.build(p);self.rejects('differs from verified audit')
    def test_rehashed_wrong_portable_result(self):
        p=dict(self.payload);p['validation/portable-complete.json']=b'wrong result';self.build(p);self.rejects('differs from verified audit')
    def test_rehashed_wrong_extractor(self):
        p=dict(self.payload);p['tools/unpack_frozen_packet.py']=b'wrong tool';self.build(p);self.rejects('differs from verified audit')
    def test_extra_member(self):self.build(extra=g.SUPPLEMENT+'/extra');self.rejects('ZIP member')
    def test_duplicate_member(self):self.build(duplicate=True);self.rejects('ZIP member')
    def test_traversal_member(self):self.build(extra='../escape');self.rejects('ZIP member')
    def test_symlink_member(self):self.build(symlink=True);self.rejects('Nonregular')
    def test_corrupt_bytes_inside_zip(self):self.build(alter_stream='raw/identity.json');self.rejects('member size')
    def test_bad_checksum_file(self):self.build(bad_sums=True);self.rejects('SHA256SUMS')
    def test_component_order_checksum_accepted(self):
        p=dict(self.payload);p['validator/review.md']=b'review';p['validator/review/REPORT.md']=b'long review'
        for n in ('validator/review.md','validator/review/REPORT.md'):self.expected[n]=byte_pin(p[n])
        self.build(p);self.assertEqual(self.invoke()['status'],'COMPLETE')
    def test_wrong_public_extractor(self):
        (self.public/'audit/code/unpack_frozen_packet.py').write_bytes(b'changed')
        self.rejects('Public extractor differs')
    def test_rehashed_wrong_license(self):
        p=dict(self.payload);p['LICENSE']=b'wrong license';self.build(p);self.rejects('differs from verified audit')
    def test_missing_catalog_member(self):
        p=dict(self.payload);del p['catalog/catalog.json'];self.build(p);self.rejects('missing or differs')
    def test_extra_raw_namespace_member(self):
        p=dict(self.payload);p['raw/extra.json']=b'raw extra';self.build(p);self.rejects('source-bound payload')
    def test_bounded_manifest(self):
        m=json.loads(self.manifest);m['status']='BOUNDED_VALIDATION';b=encoded(m)
        with self.assertRaisesRegex(ValueError,'identity/scope'):
            g.verify_supplement_zip(self.pub/(g.SUPPLEMENT+'.zip'),b,self.expected,self.config,self.producer,self.evidence)
    def test_duplicate_json_fields(self):
        with self.assertRaisesRegex(ValueError,'Duplicate JSON'):g.strict_json('{"status":"FAIL","status":"COMPLETE"}')

class MigrationTests(unittest.TestCase):
    def test_migration_links_and_mutations(self):
        with tempfile.TemporaryDirectory(prefix='migration_',dir=HERE) as t,patch.object(g,'MIGRATED_CASES',128):
            a=Path(t);(a/'full_regeneration').mkdir();new={'wrapper_sha256':g.WRAPPER_SHA,'batch_size':128}
            oldid=dict(new,wrapper_sha256=g.PRE_MAXIMAL_SHA)
            previous={'status':'PASS','count':128,'identity':oldid,'raw_sha256':'1'*64,'batch_index':0}
            previous_bytes=(json.dumps(previous,indent=2)+'\n').encode()
            origin={'wrapper_sha256':g.PRE_MAXIMAL_SHA,'metadata_sha256':sha256(previous_bytes).hexdigest(),
                    'raw_sha256':'1'*64,'correction':'Accept the literal maximal-dimension annotation only at full ambient dimension'}
            current=dict(previous,identity=new,revalidated_from=origin)
            path=a/'full_regeneration/batch-00000.json';path.write_bytes((json.dumps(current,indent=2)+'\n').encode())
            portable={'verified_batches':[{'batch_index':0,'cases':128,'metadata_sha256':g.digest(path),'raw_sha256':'1'*64}]}
            report={'status':'MIGRATED_READY_TO_RESUME','all_core_regeneration_complete':False,'migrated_cases':128,
                    'new_identity':new,'old_identity':oldid,'batches':[{'batch':0,'cases':128,'origin':origin,'new_metadata_sha256':g.digest(path)}]}
            rp=a/'maximal_label_migration.json';rp.write_bytes(encoded(report))
            self.assertEqual(g.verify_migration(a,{'identity':new},portable)['migrated_cases'],128)
            reordered={'batch_size':128,'wrapper_sha256':g.WRAPPER_SHA}
            self.assertEqual(g.verify_migration(a,{'identity':reordered},portable)['migrated_cases'],128)
            variants=[]
            for field,value in [('migrated_cases',256),('all_core_regeneration_complete',True)]:
                x=deepcopy(report);x[field]=value;variants.append(x)
            x=deepcopy(report);x['batches'][0]['new_metadata_sha256']='2'*64;variants.append(x)
            x=deepcopy(report);x['batches'][0]['origin']['raw_sha256']='2'*64;variants.append(x)
            x=deepcopy(report);x['batches'][0]['origin']['metadata_sha256']='2'*64;variants.append(x)
            x=deepcopy(report);x['batches'].append(x['batches'][0]);variants.append(x)
            for x in variants:
                rp.write_bytes(encoded(x))
                with self.assertRaises(ValueError):g.verify_migration(a,{'identity':new},portable)
            # Rehash every new object consistently: the old metadata hash must
            # still equal the bytes reconstructed under the pinned old writer.
            current['revalidated_from']['metadata_sha256']='2'*64
            path.write_bytes((json.dumps(current,indent=2)+'\n').encode())
            portable['verified_batches'][0]['metadata_sha256']=g.digest(path)
            report['batches'][0]['new_metadata_sha256']=g.digest(path)
            rp.write_bytes(encoded(report))
            with self.assertRaisesRegex(ValueError,'historical metadata hash cannot be reconstructed'):
                g.verify_migration(a,{'identity':new},portable)

class CompletionTests(unittest.TestCase):
    def run_case(self,mutation=None,missing_portable=False):
        with tempfile.TemporaryDirectory(prefix='completion_',dir=HERE) as t:
            root=Path(t);pub=root/'pub';pub.mkdir();raw=root/'audit/full_regeneration';raw.mkdir(parents=True)
            (pub/'build_config.json').write_bytes(encoded({'audit_run':'audit','source_archive_sha256':g.ARCHIVE_SHA}))
            producer={'status':'COMPLETE','all_core_regeneration_complete':True,'verified_cases':g.TOTAL,'total':g.TOTAL,'full_latte':False}
            portable=deepcopy(producer)
            if mutation:mutation(producer,portable)
            (raw/'complete.json').write_bytes(encoded(producer))
            if not missing_portable:(root/'audit/portable_full_validation.json').write_bytes(encoded(portable))
            return g.require_completed_audit(pub,root)
    def test_portable_bounded_rejected(self):
        with self.assertRaisesRegex(ValueError,'must be COMPLETE'):
            self.run_case(lambda p,v:v.update(status='BOUNDED_VALIDATION',all_core_regeneration_complete=False))
    def test_producer_bounded_rejected(self):
        with self.assertRaisesRegex(ValueError,'must be COMPLETE'):
            self.run_case(lambda p,v:p.update(status='BOUNDED_VALIDATION',all_core_regeneration_complete=False))
    def test_false_complete_count_512_rejected(self):
        with self.assertRaisesRegex(ValueError,'exact full corpus'):
            self.run_case(lambda p,v:v.update(verified_cases=512))
    def test_float_complete_count_rejected(self):
        with self.assertRaisesRegex(ValueError,'exact full corpus'):
            self.run_case(lambda p,v:v.update(verified_cases=float(g.TOTAL)))
    def test_missing_portable_rejected(self):
        with self.assertRaises(FileNotFoundError):self.run_case(missing_portable=True)

class StartupTests(unittest.TestCase):
    def test_new_strict_rejects_before_packet_code_executes(self):
        with tempfile.TemporaryDirectory(prefix='startup_',dir=HERE) as t:
            base=Path(t);packet=base/'packet';packet.mkdir()
            (packet/'MANIFEST.json').write_bytes((AUDIT/'replay/packet/MANIFEST.json').read_bytes())
            marker=base/'ran'
            (packet/'verify.py').write_text('from pathlib import Path\nPath('+repr(str(marker))+').write_text("bad")\n')
            strict=PUB/'release_additions/audit/code/strict_corpus_audit.py'
            result=subprocess.run([sys.executable,'-I','-B',str(strict),'--packet',str(packet),'--output',str(base/'out'),'inventory'],capture_output=True,text=True,timeout=20)
            self.assertNotEqual(result.returncode,0);self.assertIn('missing or extra files',result.stderr);self.assertFalse(marker.exists())
    def test_optimized_gate_rejects_before_any_input_read(self):
        code="import importlib.util;from pathlib import Path;s=importlib.util.spec_from_file_location('g',"+repr(str(HERE/'proposed/fresh_evidence_gate.py'))+");g=importlib.util.module_from_spec(s);s.loader.exec_module(g);g.require_completed_audit(Path('/nonexistent'),Path('/nonexistent'))"
        result=subprocess.run([sys.executable,'-I','-OO','-B','-c',code],capture_output=True,text=True,timeout=20)
        self.assertNotEqual(result.returncode,0);self.assertIn('assertions enabled',result.stderr)
    def test_math_functions_unchanged(self):
        def defs(p):return {n.name:ast.dump(n,include_attributes=False) for n in ast.parse(p.read_text()).body if isinstance(n,ast.FunctionDef)}
        self.assertEqual(defs(AUDIT/'computational_audit/adversarial_checks.py'),defs(PUB/'release_additions/audit/code/strict_corpus_audit.py'))

if __name__=='__main__':
    suite=unittest.defaultTestLoader.loadTestsFromModule(sys.modules[__name__])
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    out={'status':'PASS' if result.wasSuccessful() else 'FAIL','tests':result.testsRun,'failures':len(result.failures),'errors':len(result.errors),
         'synthetic_zip_fixtures_not_proof_evidence':True,'complete_audit_prerequisite_mocked_for_zip_tests':True,
         'actual_full_gate_run':False,'engines_run':False,
         'original_gate_sha256':g.digest(PUB/'build_tools/fresh_evidence_gate.py'),
         'proposed_gate_sha256':g.digest(HERE/'proposed/fresh_evidence_gate.py')}
    (HERE/'test_result.json').write_text(json.dumps(out,indent=2)+'\n')
    raise SystemExit(0 if result.wasSuccessful() else 1)
