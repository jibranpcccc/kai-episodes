# -*- coding: utf-8 -*-
"""PRODUCE — one command from an angle id to a verified episode.

    python data/_produce.py VRAM-001              one episode, end to end
    python data/_produce.py --batch 10            ten episodes, end to end
    python data/_produce.py --list                what is available

For each angle this runs, in order:

  1. data/make_spec.py <ID>          write data/spec_gen_<ID>.py
  2. data/fusion_build.py            edge-tts, scheduler, captions, loudness, HTML
  3. data/fusion_gate.py             30 checks against the built file
  4. data/_recheck.py                26 checks against the three deliverable files
  5. data/_check_open.py             5 checks: no empty opening, no early ink,
                                     no needle outside its dial

and prints one line per episode. The writing inside the episode - the argument
that ties the facts together - is still the human part; everything else is
this script.
"""
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(HERE)
PY = sys.executable
DATA = os.path.join(ROOT, "data")


def run(cmd, label, env=None):
    """Run a step. Returns (ok, tail, seconds)."""
    t0 = time.time()
    e = dict(os.environ, PYTHONIOENCODING="utf-8")
    if env:
        e.update(env)
    p = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, env=e)
    dt = time.time() - t0
    tail = [l for l in (p.stdout or "").splitlines() if l.strip()]
    tail += [l for l in (p.stderr or "").splitlines() if l.strip()]
    ok = (p.returncode == 0)
    return ok, tail, dt


def produce(angle_id):
    """One angle, start to finish. Returns a one-line verdict."""
    spec_mod = "spec_gen_%s" % angle_id
    name = "BYTE-GEN-%s" % angle_id
    steps = []

    ok, tail, dt = run([PY, os.path.join(DATA, "make_spec.py"), angle_id], "spec")
    steps.append(("spec", ok, dt))
    if not ok:
        return "%-12s SPEC FAILED  (%.1fs)  %s" % (
            angle_id, dt, tail[-1] if tail else "")

    ok, tail, dt = run([PY, os.path.join(DATA, "fusion_build.py")],
                       "build", env={"FUSION_SPEC": spec_mod})
    steps.append(("build", ok, dt))
    if not ok:
        return "%-12s BUILD FAILED (%.1fs)  %s" % (
            angle_id, dt, tail[-1] if tail else "")

    ok, tail, dt = run([PY, os.path.join(DATA, "fusion_gate.py"), name, spec_mod],
                       "gate")
    steps.append(("gate", ok, dt))
    gate_line = next((l for l in reversed(tail) if "passed" in l), "")

    ok2, tail2, dt2 = run([PY, os.path.join(DATA, "_recheck.py"), name, spec_mod],
                          "recheck")
    steps.append(("recheck", ok2, dt2))
    re_line = next((l for l in reversed(tail2) if "RECHECK" in l), "")

    ok3, tail3, dt3 = run([PY, os.path.join(DATA, "_check_open.py"), name],
                          "open")
    steps.append(("open", ok3, dt3))
    op_line = next((l for l in reversed(tail3) if "CHECKS" in l), "")

    good = ok and ok2 and ok3
    total = sum(s[2] for s in steps)
    return ("%-12s %s  %-42s %-26s %-22s  %6.1fs" % (
        angle_id,
        "PASS" if good else "FAIL",
        gate_line.strip() or "gate: no summary",
        re_line.strip() or "recheck: no summary",
        op_line.strip() or "open: no summary",
        total))


def main():
    args = sys.argv[1:]
    if not args or args[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if args[0] == "--list":
        p = subprocess.run([PY, os.path.join(DATA, "make_spec.py"), "--list"],
                           cwd=ROOT, capture_output=True, text=True)
        print(p.stdout)
        return 0
    if args[0] == "--batch":
        n = int(args[1]) if len(args) > 1 else 10
        p = subprocess.run([PY, os.path.join(DATA, "make_spec.py"), "--list"],
                           cwd=ROOT, capture_output=True, text=True)
        ids = [l.split()[0] for l in p.stdout.splitlines()
               if l.strip() and l.split()[0].count("-") == 1
               and l.split()[0][0].isalpha()]
        ids = ids[:n]
    else:
        ids = args

    print("angle       result  gate                              "
          "recheck                        open                     time")
    t0 = time.time()
    for aid in ids:
        print(produce(aid), flush=True)
    print("\n%d episode(s) in %.1f s total" % (len(ids), time.time() - t0))
    return 0


if __name__ == "__main__":
    sys.exit(main())
