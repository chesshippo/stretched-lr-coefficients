# Audit evidence and reproduction scope

- [FINAL_AUDIT.md](FINAL_AUDIT.md): combined findings, all21 normalized claims,
  software assumptions, licensing and limited novelty assessment.
- [paper_audit/audit_report.md](paper_audit/audit_report.md): fresh mathematical
  reading and independently authored bounded/symbolic falsification tests.
- [computational_audit/COMPUTATIONAL_AUDIT.md](computational_audit/COMPUTATIONAL_AUDIT.md):
  complete strict certificate inventory and adversarial witnesses.
- [licensing_audit/REPORT.md](licensing_audit/REPORT.md): original163-file-instance
  license/attribution audit; the new addendum corrects its identified error.
- [FRESH_EVIDENCE.md](FRESH_EVIDENCE.md): separate full raw asset, exact identity
  and portable engine-free verification commands.

The reports are retained as written, with their date and bounded scope. A
development report that says a later complete run was pending is historical
evidence; it is not a contradiction of the separately dated final COMPLETE
receipts. The new final report adjudicates the original findings without
rewriting them. The raw supplement includes the portable validator, its tests
and exact raw execution evidence.

The original seven-stage mathematical replay is the root reproduce.py command
and was exercised on macOS. Its frozen path handling is suitable for macOS/Linux;
native Windows full-replay support is not claimed. The new
code/unpack_frozen_packet.py helper and raw-supplement validator use portable
standard-library interfaces and do not execute the frozen verifier. Native
Windows was not available for testing, so portability rests on those interfaces
and the independent source review rather than an observed Windows run.

## Repeat the strict inventory

After reconstructing the frozen packet, install the main pinned audit
requirements and run from the main release (choose new external output paths):

    python3 -B audit/code/strict_corpus_audit.py --packet ../stretched-lr-inspection/packet --output ../strict-inventory inventory
    python3 -B audit/code/strict_corpus_audit.py --packet ../stretched-lr-inspection/packet --output ../strict-final-cover finalcover

Both inventory and finalcover are needed for the complete strict certificate
audit. An individual mode's success does not establish the whole paper or
replace the seven-stage replay/full raw-polynomial verification. The code pins
and checks every frozen input byte before executing any packet code. Its16
mathematical audit function bodies are unchanged from the independent original;
only safe input/output routing and startup integrity checks were added.

The other original research-audit programs are preserved for inspection and
may require their recorded directory layout, installed arithmetic dependencies
or a disposable working copy. Some write result files next to themselves. Do
not run such tests in an immutable release you intend to keep hash-identical.
The portable raw validator writes only its selected external temporary catalog
and stdout result; its hostile test suite should run from a disposable copy.

AUDIT_MATERIALS.json records exact copied bytes. Referenced downloaded research
papers are not redistributed; their primary URLs and hashes remain in source
logs. No provider requests, private model conversations, engine binaries,
installed packages, credentials or repository history are included.
