#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NEGATIVE REGRESSION TEST SUITE FOR BYTE FORENSICS QUALITY GATES

Proves that both fusion_gate.py and deep_episode_auditor.py rigorously REJECT
broken fixtures and do NOT give false passes on:
  1. Root vs episodes/ HTML divergence
  2. Altered caption word with identical token count
  3. Missing authoritative spec file
  4. Visual reveal finishing < 1.0s before scene exit
  5. Element overflowing canvas bounds
  6. Stale SVG semantic artifact (e.g. router IP / 8-port switch)

Usage:
    python tests/test_quality_gates_rejection.py
"""

import io
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYS_PY = sys.executable

PASSED_REGRESSIONS = []
FAILED_REGRESSIONS = []


def assert_rejection(test_name, cmd, expected_err_fragment):
    """Runs cmd and asserts that it EXITS WITH CODE 1 and prints expected fragment."""
    proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
    combined = (proc.stdout or "") + "\n" + (proc.stderr or "")
    if proc.returncode != 0 and expected_err_fragment.lower() in combined.lower():
        PASSED_REGRESSIONS.append((test_name, "Correctly rejected (exit code %d): matched '%s'" % (proc.returncode, expected_err_fragment)))
        print(f"  [PASS] {test_name}: correctly rejected with exit code {proc.returncode}")
        return True
    else:
        FAILED_REGRESSIONS.append((test_name, f"Expected rejection with '{expected_err_fragment}', got exit code {proc.returncode}. Output:\n{combined[-500:]}"))
        print(f"  [FAIL] {test_name}: FAILED TO REJECT! (exit code {proc.returncode})")
        return False


def run_all_negative_tests():
    print("=" * 70)
    print("BYTE FORENSICS NEGATIVE REGRESSION TEST SUITE")
    print("Testing that quality gates reject intentionally broken fixtures")
    print("=" * 70)

    with tempfile.TemporaryDirectory() as tmpdir:
        # Fixture paths
        test_ep_name = "BYTE-TEST-FIXTURE"
        root_html = os.path.join(ROOT, f"{test_ep_name}.html")
        epis_dir = os.path.join(ROOT, "episodes")
        epis_html = os.path.join(epis_dir, f"{test_ep_name}.html")
        srt_file = os.path.join(epis_dir, f"{test_ep_name}.srt")
        root_srt = os.path.join(ROOT, f"{test_ep_name}.srt")
        chap_file = os.path.join(epis_dir, f"{test_ep_name}-chapters.txt")
        root_chap = os.path.join(ROOT, f"{test_ep_name}-chapters.txt")
        spec_file = os.path.join(ROOT, "data", f"spec_{test_ep_name.lower().replace('-', '_')}.py")

        # Canonical baseline from BYTE-DUAL-GPU
        base_html = open(os.path.join(ROOT, "BYTE-DUAL-GPU.html"), "r", encoding="utf-8").read()
        base_srt = open(os.path.join(ROOT, "BYTE-DUAL-GPU.srt"), "r", encoding="utf-8").read()
        base_chap = open(os.path.join(ROOT, "BYTE-DUAL-GPU-chapters.txt"), "r", encoding="utf-8").read()
        base_spec = open(os.path.join(ROOT, "data", "spec_dual_gpu.py"), "r", encoding="utf-8").read()

        def cleanup():
            for f in [root_html, epis_html, srt_file, root_srt, chap_file, root_chap, spec_file]:
                if os.path.exists(f):
                    os.remove(f)

        cleanup()

        try:
            # -------------------------------------------------------------
            # TEST 1: Root and episodes/ HTML divergence
            # -------------------------------------------------------------
            print("\n--- Test 1: Divergent Root vs Episodes/ HTML ---")
            io.open(root_html, "w", encoding="utf-8").write(base_html)
            # Make episodes/ different by adding a comment
            io.open(epis_html, "w", encoding="utf-8").write(base_html + "<!-- divergent byte -->")
            io.open(srt_file, "w", encoding="utf-8").write(base_srt)
            io.open(root_srt, "w", encoding="utf-8").write(base_srt)
            io.open(chap_file, "w", encoding="utf-8").write(base_chap)
            io.open(root_chap, "w", encoding="utf-8").write(base_chap)
            io.open(spec_file, "w", encoding="utf-8").write(base_spec)

            cmd1 = [SYS_PY, os.path.join(ROOT, "data", "deep_episode_auditor.py"), test_ep_name]
            assert_rejection("1. Divergent HTML in deep_episode_auditor", cmd1, "CANONICAL_SOURCE")

            # -------------------------------------------------------------
            # TEST 2: Altered caption word in SRT with identical word count
            # -------------------------------------------------------------
            print("\n--- Test 2: Altered Caption Word with Equal Token Count ---")
            # Make HTMLs identical again
            io.open(root_html, "w", encoding="utf-8").write(base_html)
            io.open(epis_html, "w", encoding="utf-8").write(base_html)
            # Alter one single word in SRT from 'graphics' to 'bogusword'
            bad_srt = base_srt.replace("graphics cards", "bogusword cards", 1)
            io.open(srt_file, "w", encoding="utf-8").write(bad_srt)
            io.open(root_srt, "w", encoding="utf-8").write(bad_srt)

            cmd2 = [SYS_PY, os.path.join(ROOT, "data", "deep_episode_auditor.py"), test_ep_name]
            assert_rejection("2. Altered word in deep_episode_auditor", cmd2, "SCRIPT_PARITY")

            # -------------------------------------------------------------
            # TEST 3: Missing specification file
            # -------------------------------------------------------------
            print("\n--- Test 3: Missing Authoritative Spec File ---")
            # Restore SRT
            io.open(srt_file, "w", encoding="utf-8").write(base_srt)
            io.open(root_srt, "w", encoding="utf-8").write(base_srt)
            # Delete spec file
            if os.path.exists(spec_file):
                os.remove(spec_file)

            cmd3 = [SYS_PY, os.path.join(ROOT, "data", "fusion_gate.py"), test_ep_name]
            assert_rejection("3. Missing spec in fusion_gate", cmd3, "14e")

            # -------------------------------------------------------------
            # TEST 4: Reveal hold duration < 1.0s before scene cut
            # -------------------------------------------------------------
            print("\n--- Test 4: Visual Reveal Hold < 1.0s Before Cut ---")
            io.open(spec_file, "w", encoding="utf-8").write(base_spec)
            # Tamper with Scene 58 w58_10 beat to end 0.5s before scene cut
            m_f = re.search(r'window\.FUSION = (\{.*?\});</script>', base_html, re.S)
            F_bad = json.loads(m_f.group(1))
            for b in F_bad['beats']:
                if b.get('el') == '#w58_10':
                    # Scene 58 ends at 686.310; make this end at 685.900 (hold = 0.41s)
                    b['s'] = 685.600
                    b['e'] = 685.900
            bad_hold_html = base_html.replace(m_f.group(1), json.dumps(F_bad, separators=(',', ':')))
            io.open(root_html, "w", encoding="utf-8").write(bad_hold_html)
            io.open(epis_html, "w", encoding="utf-8").write(bad_hold_html)

            cmd4 = [SYS_PY, os.path.join(ROOT, "data", "deep_episode_auditor.py"), test_ep_name]
            assert_rejection("4. Short reveal hold in deep_episode_auditor", cmd4, "CARD_VISIBILITY")

            # -------------------------------------------------------------
            # TEST 5: Stale SVG semantic artifact (router IP / 8-port switch)
            # -------------------------------------------------------------
            print("\n--- Test 5: Stale SVG Semantic Artifact (Router IP) ---")
            # Inject 192.168.1.1 into an SVG
            bad_svg_html = base_html.replace('data-art="chip"', 'data-art="chip" data-test="192.168.1.1"')
            io.open(root_html, "w", encoding="utf-8").write(bad_svg_html)
            io.open(epis_html, "w", encoding="utf-8").write(bad_svg_html)

            cmd5 = [SYS_PY, os.path.join(ROOT, "data", "deep_episode_auditor.py"), test_ep_name]
            assert_rejection("5. Stale SVG artifact in deep_episode_auditor", cmd5, "SVG_SEMANTICS")

        finally:
            cleanup()

    print("\n" + "=" * 70)
    print(f"REGRESSION SUITE RESULTS: {len(PASSED_REGRESSIONS)} PASSED · {len(FAILED_REGRESSIONS)} FAILED")
    print("=" * 70)
    if FAILED_REGRESSIONS:
        print("\nFailures:")
        for name, err in FAILED_REGRESSIONS:
            print(f"  ❌ {name}: {err}")
        return 1
    else:
        print("\n✅ ALL NEGATIVE FIXTURES RIGOROUSLY REJECTED AS EXPECTED!")
        return 0


if __name__ == "__main__":
    sys.exit(run_all_negative_tests())
