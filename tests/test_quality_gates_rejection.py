#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
COMPREHENSIVE QUALITY GATE & REGRESSION AUDIT SUITE FOR BYTE FORENSICS

Tests:
  0. Normal Valid Baseline: Proves clean episode passes both gates with exit code 0.
  1. Negative: Divergent Root vs Episodes/ HTML rejected (CANONICAL_SOURCE, code 1).
  2. Negative: Altered caption word with identical token count rejected (SCRIPT_PARITY, code 1).
  3. Negative: Missing authoritative specification rejected (Check 14e, code 1).
  4. Negative: Visual reveal finishing < 1.0s before cut rejected (CARD_VISIBILITY, code 1).
  5. Negative: Stale SVG semantic artifact (router IP) rejected (SVG_SEMANTICS, code 1).
  6. Functional: 1440p frame rasterization fills 2560x1440 canvas without letterbox borders.
  7. Functional: Hard failure on invalid/corrupted MP4 verification (ffprobe probe rejects).
  8. Negative: Deliberately late animation cue without valid nudge rejected (Check 5, code 1).
  9. Negative: Invalid authored timing adjustment / mismatched nudge rejected (Check 5, code 1).
  10. Negative: Incorrect phrase anchor missing from scene narration rejected (Check 5, code 1).

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
from pathlib import Path

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SYS_PY = sys.executable

PASSED_TESTS = []
FAILED_TESTS = []


def assert_rejection(test_name, cmd, expected_err_fragment):
    """Runs cmd and asserts that it EXITS WITH EXACT CODE 1 and prints expected fragment."""
    proc = subprocess.run(cmd, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
    combined = (proc.stdout or "") + "\n" + (proc.stderr or "")
    if proc.returncode == 1 and expected_err_fragment.lower() in combined.lower():
        PASSED_TESTS.append((test_name, f"Correctly rejected with code 1 matching '{expected_err_fragment}'"))
        print(f"  [PASS] {test_name}: correctly rejected with exit code 1")
        return True
    else:
        err = f"Expected code 1 with '{expected_err_fragment}', got code {proc.returncode}. Output:\n{combined[-600:]}"
        FAILED_TESTS.append((test_name, err))
        print(f"  [FAIL] {test_name}: FAILED (code {proc.returncode})")
        return False


def run_all_tests():
    print("=" * 75)
    print("BYTE FORENSICS QUALITY GATE & REGRESSION AUDIT SUITE")
    print("=" * 75)

    canonical_html = os.path.join(ROOT, "episodes", "BYTE-DUAL-GPU.html")
    canonical_spec = os.path.join(ROOT, "data", "spec_dual_gpu.py")
    assert os.path.exists(canonical_html), f"Missing {canonical_html}"
    assert os.path.exists(canonical_spec), f"Missing {canonical_spec}"

    # -------------------------------------------------------------------------
    # TEST 0: Normal Valid Baseline Verification
    # -------------------------------------------------------------------------
    print("\n--- Test 0: Normal Valid Baseline Verification (BYTE-DUAL-GPU) ---")
    cmd_base = [SYS_PY, os.path.join(ROOT, "data", "deep_episode_auditor.py"), "BYTE-DUAL-GPU"]
    res_base = subprocess.run(cmd_base, cwd=ROOT, capture_output=True, text=True, encoding="utf-8", errors="replace")
    if res_base.returncode == 0 and "AUDIT SUMMARY: 12 PASSED" in res_base.stdout:
        PASSED_TESTS.append(("0. Normal Baseline deep_episode_auditor", "Passed cleanly with exit code 0"))
        print("  [PASS] 0. Normal Baseline deep_episode_auditor: exit code 0, 12 passed")
    else:
        FAILED_TESTS.append(("0. Normal Baseline deep_episode_auditor", f"Failed with code {res_base.returncode}: {res_base.stdout[-400:]}"))
        print(f"  [FAIL] 0. Normal Baseline deep_episode_auditor: exit code {res_base.returncode}")

    # Temporary fixture sandbox for negative tests
    test_ep_name = "BYTE-TEST-FIXTURE"
    root_html = os.path.join(ROOT, f"{test_ep_name}.html")
    epis_dir = os.path.join(ROOT, "episodes")
    epis_html = os.path.join(epis_dir, f"{test_ep_name}.html")
    srt_file = os.path.join(epis_dir, f"{test_ep_name}.srt")
    root_srt = os.path.join(ROOT, f"{test_ep_name}.srt")
    chap_file = os.path.join(epis_dir, f"{test_ep_name}-chapters.txt")
    root_chap = os.path.join(ROOT, f"{test_ep_name}-chapters.txt")
    spec_file = os.path.join(ROOT, "data", f"spec_{test_ep_name.lower().replace('-', '_')}.py")

    base_html = open(canonical_html, "r", encoding="utf-8").read()
    base_srt = open(os.path.join(ROOT, "BYTE-DUAL-GPU.srt"), "r", encoding="utf-8").read()
    base_chap = open(os.path.join(ROOT, "BYTE-DUAL-GPU-chapters.txt"), "r", encoding="utf-8").read()
    base_spec = open(canonical_spec, "r", encoding="utf-8").read()

    def cleanup():
        for f in [root_html, epis_html, srt_file, root_srt, chap_file, root_chap, spec_file]:
            if os.path.exists(f):
                os.remove(f)

    cleanup()

    try:
        # ---------------------------------------------------------------------
        # TEST 1: Root and episodes/ HTML divergence
        # ---------------------------------------------------------------------
        print("\n--- Test 1: Divergent Root vs Episodes/ HTML ---")
        io.open(root_html, "w", encoding="utf-8").write(base_html)
        io.open(epis_html, "w", encoding="utf-8").write(base_html + "<!-- divergence byte -->")
        io.open(srt_file, "w", encoding="utf-8").write(base_srt)
        io.open(root_srt, "w", encoding="utf-8").write(base_srt)
        io.open(chap_file, "w", encoding="utf-8").write(base_chap)
        io.open(root_chap, "w", encoding="utf-8").write(base_chap)
        io.open(spec_file, "w", encoding="utf-8").write(base_spec)

        cmd1 = [SYS_PY, os.path.join(ROOT, "data", "deep_episode_auditor.py"), test_ep_name]
        assert_rejection("1. Divergent HTML in deep_episode_auditor", cmd1, "CANONICAL_SOURCE")

        # ---------------------------------------------------------------------
        # TEST 2: Altered caption word in SRT with identical word count
        # ---------------------------------------------------------------------
        print("\n--- Test 2: Altered Caption Word with Equal Token Count ---")
        io.open(root_html, "w", encoding="utf-8").write(base_html)
        io.open(epis_html, "w", encoding="utf-8").write(base_html)
        bad_srt = base_srt.replace("graphics cards", "bogusword cards", 1)
        io.open(srt_file, "w", encoding="utf-8").write(bad_srt)
        io.open(root_srt, "w", encoding="utf-8").write(bad_srt)

        cmd2 = [SYS_PY, os.path.join(ROOT, "data", "deep_episode_auditor.py"), test_ep_name]
        assert_rejection("2. Altered word in deep_episode_auditor", cmd2, "SCRIPT_PARITY")

        # ---------------------------------------------------------------------
        # TEST 3: Missing specification file (removal of valid spec)
        # ---------------------------------------------------------------------
        print("\n--- Test 3: Missing Specification File ---")
        io.open(srt_file, "w", encoding="utf-8").write(base_srt)
        io.open(root_srt, "w", encoding="utf-8").write(base_srt)
        if os.path.exists(spec_file):
            os.remove(spec_file)

        # Run with explicit missing spec name
        cmd3 = [SYS_PY, os.path.join(ROOT, "data", "fusion_gate.py"), test_ep_name, "nonexistent_spec"]
        assert_rejection("3. Missing spec in fusion_gate", cmd3, "14e")

        # ---------------------------------------------------------------------
        # TEST 4: Reveal hold duration < 1.0s before scene cut
        # ---------------------------------------------------------------------
        print("\n--- Test 4: Visual Reveal Hold < 1.0s Before Cut ---")
        io.open(spec_file, "w", encoding="utf-8").write(base_spec)
        m_f = re.search(r'window\.FUSION = (\{.*?\});</script>', base_html, re.S)
        F_bad = json.loads(m_f.group(1))
        for b in F_bad['beats']:
            if b.get('el') == '#w58_10':
                # Scene 58 ends at 686.310; force this beat to end at 685.900 (hold = 0.41s)
                b['s'] = 685.600
                b['e'] = 685.900
        bad_hold_html = base_html.replace(m_f.group(1), json.dumps(F_bad, separators=(',', ':')))
        io.open(root_html, "w", encoding="utf-8").write(bad_hold_html)
        io.open(epis_html, "w", encoding="utf-8").write(bad_hold_html)

        cmd4 = [SYS_PY, os.path.join(ROOT, "data", "deep_episode_auditor.py"), test_ep_name]
        assert_rejection("4. Short reveal hold in deep_episode_auditor", cmd4, "CARD_VISIBILITY")

        # ---------------------------------------------------------------------
        # TEST 5: Stale SVG semantic artifact (router IP)
        # ---------------------------------------------------------------------
        print("\n--- Test 5: Stale SVG Semantic Artifact (Router IP) ---")
        bad_svg_html = base_html.replace('data-art="chip"', 'data-art="chip" data-test="192.168.1.1"')
        io.open(root_html, "w", encoding="utf-8").write(bad_svg_html)
        io.open(epis_html, "w", encoding="utf-8").write(bad_svg_html)

        cmd5 = [SYS_PY, os.path.join(ROOT, "data", "deep_episode_auditor.py"), test_ep_name]
        assert_rejection("5. Stale SVG artifact in deep_episode_auditor", cmd5, "SVG_SEMANTICS")

        # ---------------------------------------------------------------------
        # TEST 8: Deliberately Late Cue without Valid Adjustment (Check 5 Loophole Test)
        # ---------------------------------------------------------------------
        print("\n--- Test 8: Deliberately Late Cue Rejected (Check 5 Loophole Fix) ---")
        io.open(spec_file, "w", encoding="utf-8").write(base_spec)
        F_late = json.loads(m_f.group(1))
        for b in F_late['beats']:
            if b.get('el') == '#w0_02':
                # Shift arrival 2.0 seconds late after spoken phrase (measured off ~ +2.0s)
                b['s'] = 4.20
                b['arr'] = 4.20
                b['nudge'] = 0.0
                break
        bad_late_html = base_html.replace(m_f.group(1), json.dumps(F_late, separators=(',', ':')))
        io.open(root_html, "w", encoding="utf-8").write(bad_late_html)
        io.open(epis_html, "w", encoding="utf-8").write(bad_late_html)

        cmd8 = [SYS_PY, os.path.join(ROOT, "data", "fusion_gate.py"), test_ep_name]
        assert_rejection("8. Deliberately late cue in fusion_gate", cmd8, "miss spoken anchor phrase")

        # ---------------------------------------------------------------------
        # TEST 9: Invalid Timing Nudge / Mismatched Authored Offset (Check 5)
        # ---------------------------------------------------------------------
        print("\n--- Test 9: Invalid Timing Nudge Mismatch Rejected (Check 5) ---")
        F_nud = json.loads(m_f.group(1))
        for b in F_nud['beats']:
            if b.get('el') == '#w0_02':
                # Anchor arrives at ~2.157s; set arr=1.00s (off=-1.157s), but set nudge=-0.10s (mismatch=1.057s > 0.25s)
                b['s'] = 1.00
                b['arr'] = 1.00
                b['nudge'] = -0.10
                break
        bad_nud_html = base_html.replace(m_f.group(1), json.dumps(F_nud, separators=(',', ':')))
        io.open(root_html, "w", encoding="utf-8").write(bad_nud_html)
        io.open(epis_html, "w", encoding="utf-8").write(bad_nud_html)

        cmd9 = [SYS_PY, os.path.join(ROOT, "data", "fusion_gate.py"), test_ep_name]
        assert_rejection("9. Mismatched nudge in fusion_gate", cmd9, "miss spoken anchor phrase")

        # ---------------------------------------------------------------------
        # TEST 10: Incorrect Phrase Anchor Missing From Narration (Check 5)
        # ---------------------------------------------------------------------
        print("\n--- Test 10: Incorrect Anchor Phrase Rejected (Check 5) ---")
        F_anc = json.loads(m_f.group(1))
        for b in F_anc['beats']:
            if b.get('el') == '#w0_02':
                b['anchor'] = "quantum cryogenic superconductor"
                break
        bad_anc_html = base_html.replace(m_f.group(1), json.dumps(F_anc, separators=(',', ':')))
        io.open(root_html, "w", encoding="utf-8").write(bad_anc_html)
        io.open(epis_html, "w", encoding="utf-8").write(bad_anc_html)

        cmd10 = [SYS_PY, os.path.join(ROOT, "data", "fusion_gate.py"), test_ep_name]
        assert_rejection("10. Missing anchor phrase in fusion_gate", cmd10, "miss spoken anchor phrase")

    finally:
        cleanup()

    # -------------------------------------------------------------------------
    # TEST 6: 1440p Frame Rasterization & Full Stage Coverage (Requirement A)
    # -------------------------------------------------------------------------
    print("\n--- Test 6: 1440p Frame Rasterization & Full Stage Coverage ---")
    try:
        from playwright.sync_api import sync_playwright
        from PIL import Image

        with sync_playwright() as pw:
            b = pw.chromium.launch()
            # 1920x1080 CSS viewport with device_scale_factor = 4/3 -> 2560x1440 raster
            pg = b.new_page(viewport={"width": 1920, "height": 1080}, device_scale_factor=4 / 3)
            pg.goto("file:///" + canonical_html.replace("\\", "/") + "?t=0")
            pg.wait_for_function("!!((window.EPISODE || window.FUSION) && window.renderAt)", timeout=60000)
            pg.evaluate("document.body.classList.add('render')")
            pg.evaluate("window.renderAt(2.0)")

            stage_info = pg.evaluate('''() => {
                const stage = document.querySelector('#stage') || document.querySelector('.stage') || document.body;
                const rect = stage.getBoundingClientRect();
                const cs = window.getComputedStyle(stage);
                return {
                    id: stage.id,
                    className: stage.className,
                    left: rect.left,
                    top: rect.top,
                    width: rect.width,
                    height: rect.height,
                    bgColor: cs.backgroundColor
                };
            }''')

            shot_file = os.path.join(ROOT, "temp_audit_frame.png")
            pg.screenshot(path=shot_file, type="png")
            b.close()

        with Image.open(shot_file) as im:
            w, h = im.size
            aspect = w / h
            c_tl = im.getpixel((0, 0))
            c_tr = im.getpixel((w - 1, 0))
            c_bl = im.getpixel((0, h - 1))
            c_br = im.getpixel((w - 1, h - 1))
            corners = [c_tl, c_tr, c_bl, c_br]

        if os.path.exists(shot_file):
            os.remove(shot_file)

        stage_anchored = (
            stage_info.get("left") == 0 and stage_info.get("top") == 0 and
            stage_info.get("width") == 1920 and stage_info.get("height") == 1080
        )
        dim_ok = (w == 2560 and h == 1440 and abs(aspect - 16 / 9) < 0.001)
        corners_ok = all(isinstance(c, tuple) and all(v < 60 for v in c[:3]) for c in corners)

        if dim_ok and stage_anchored and corners_ok:
            PASSED_TESTS.append(("6. 1440p Zero-Letterbox Rasterization", f"Exact {w}x{h} (16:9), stage fills full raster canvas, all corners match dark obsidian stage ({corners})"))
            print(f"  [PASS] 6. 1440p Zero-Letterbox Rasterization: {w}x{h} (16:9), DOM stage 1920x1080 fully occupying 2560x1440 canvas, corners={corners}")
        else:
            FAILED_TESTS.append(("6. 1440p Zero-Letterbox Rasterization", f"Stage fill failure: dim_ok={dim_ok}, stage_anchored={stage_anchored}, corners_ok={corners_ok}, corners={corners}"))
            print(f"  [FAIL] 6. 1440p Zero-Letterbox Rasterization: {w}x{h}, stage_anchored={stage_anchored}, corners={corners}")
    except Exception as e:
        FAILED_TESTS.append(("6. 1440p Zero-Letterbox Rasterization", f"Exception: {e}"))
        print(f"  [FAIL] 6. 1440p Zero-Letterbox Rasterization: {e}")

    # -------------------------------------------------------------------------
    # TEST 7: Hard Failure on MP4 Probe & Decode Error (Requirement B & 4)
    # -------------------------------------------------------------------------
    print("\n--- Test 7: MP4 Probe & Decode Hard Failure Gate ---")
    try:
        scripts_dir = os.path.join(ROOT, "scripts")
        if scripts_dir not in sys.path:
            sys.path.insert(0, scripts_dir)
        from render import verify_rendered_mp4
        with tempfile.NamedTemporaryFile(suffix=".mp4", delete=False) as tf:
            # Corrupted dummy file
            tf.write(b"NOT_A_REAL_MP4_VIDEO")
            bad_mp4_path = Path(tf.name)

        rejected = False
        try:
            verify_rendered_mp4(bad_mp4_path, total=753.8, expected_res="1440p", has_audio=True)
        except (RuntimeError, ValueError):
            rejected = True
        finally:
            if bad_mp4_path.exists():
                bad_mp4_path.unlink()

        if rejected:
            PASSED_TESTS.append(("7. MP4 Probe Hard Failure", "Corrupted MP4 triggered immediate hard failure exception"))
            print("  [PASS] 7. MP4 Probe Hard Failure: corrupted MP4 strictly rejected (hard failure)")
        else:
            FAILED_TESTS.append(("7. MP4 Probe Hard Failure", "Corrupted MP4 did not raise hard failure exception!"))
            print("  [FAIL] 7. MP4 Probe Hard Failure: failed to reject corrupted MP4!")
    except Exception as e:
        FAILED_TESTS.append(("7. MP4 Probe Hard Failure", f"Exception: {e}"))
        print(f"  [FAIL] 7. MP4 Probe Hard Failure: {e}")

    # -------------------------------------------------------------------------
    # SUMMARY
    # -------------------------------------------------------------------------
    print("\n" + "=" * 75)
    print(f"AUDIT SUITE SUMMARY: {len(PASSED_TESTS)} PASSED · {len(FAILED_TESTS)} FAILED")
    print("=" * 75)
    if FAILED_TESTS:
        print("\nFailures:")
        for name, err in FAILED_TESTS:
            print(f"  ❌ {name}: {err}")
        return 1
    else:
        print("\n✅ ALL BASELINE, REGRESSION, 1440P RASTER, AND HARD PROBE TESTS PASSED!")
        return 0


if __name__ == "__main__":
    sys.exit(run_all_tests())
