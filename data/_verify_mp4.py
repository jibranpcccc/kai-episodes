# -*- coding: utf-8 -*-
"""Check the exported MP4 against the browser and against the episode audio.

Two things are proved here, and neither is assumed:

1. VIDEO ROUND-TRIP. A frame is decoded back OUT of the exported MP4 at a given
   second, and the browser is asked to render the same moment of the episode.
   The two images are compared pixel by pixel. If the encoder changed anything
   -- or if the MP4 timeline were offset from the episode timeline -- the
   difference would not be near-zero.

2. AUDIO OFFSET. The MP4's audio stream is decoded, and its per-second energy
   envelope is correlated against the episode's own embedded MP3, sliced at the
   offset the export was asked for. A mis-set -ss shows up immediately as a
   broken correlation.

    python data/_verify_mp4.py BYTE-EP09 249.0 345.0 526.0 580.0
"""
import base64
import io
import json
import os
import re
import subprocess
import sys

import numpy as np
from PIL import Image
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = sys.argv[1] if len(sys.argv) > 1 else "BYTE-EP09"
A0, A1 = float(sys.argv[2]), float(sys.argv[3])   # segment A in episode seconds
B0, B1 = float(sys.argv[4]), float(sys.argv[5])   # segment B in episode seconds
PROOF = os.path.join(ROOT, "proof")
MP4 = os.path.join(PROOF, "BYTE-EP09-export-representative.mp4")
WORK = os.path.join(PROOF, "mp4verify")
FFMPEG = "ffmpeg"

results = []


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print("%s  %-52s %s" % ("PASS" if ok else "FAIL", name, detail))


def envelope(path, start=0.0, dur=None, ss=None):
    """1-second RMS envelope of a media file, as a numpy array."""
    cmd = [FFMPEG, "-v", "quiet"]
    if ss is not None:
        cmd += ["-ss", "%.3f" % ss]
    cmd += ["-i", path]
    if dur is not None:
        cmd += ["-t", "%.3f" % dur]
    cmd += ["-ac", "1", "-ar", "8000", "-f", "s16le", "-"]
    raw = subprocess.check_output(cmd)
    a = np.frombuffer(raw, dtype=np.int16).astype(np.float64)
    n = 8000
    usable = (len(a) // n) * n
    return np.sqrt((a[:usable].reshape(-1, n) ** 2).mean(axis=1) / (32768.0 ** 2))


def main():
    os.makedirs(WORK, exist_ok=True)
    html = os.path.join(ROOT, NAME + ".html")
    text = io.open(html, encoding="utf-8").read()
    F = json.loads(re.search(r"window\.FUSION = (\{.*?\});</script>", text, re.S).group(1))
    vo = F["vo"]
    if "," in vo:
        vo = vo.split(",", 1)[1]
    ep_audio = os.path.join(WORK, "episode.mp3")
    with open(ep_audio, "wb") as fh:
        fh.write(base64.b64decode(vo))

    # ---- 1. video round-trip ------------------------------------------
    # (mp4 second, episode second) pairs: segment A is 0..(A1-A0) in the mp4,
    # segment B starts at (A1-A0) in the mp4.
    segA_len = A1 - A0
    pairs = [
        (segA_len * 0.25, A0 + (A1 - A0) * 0.25),
        (segA_len * 0.75, A0 + (A1 - A0) * 0.75),
        (segA_len + (B1 - B0) * 0.35, B0 + (B1 - B0) * 0.35),
        (segA_len + (B1 - B0) * 0.80, B0 + (B1 - B0) * 0.80),
    ]
    url = "file:///" + html.replace("\\", "/")
    diffs = []
    with sync_playwright() as pw:
        br = pw.chromium.launch(args=["--force-color-profile=srgb",
                                      "--font-render-hinting=none"])
        pg = br.new_page(viewport={"width": 1920, "height": 1080},
                          device_scale_factor=1)
        for k, (mps, eps) in enumerate(pairs):
            dec = os.path.join(WORK, "decoded_%02d.png" % k)
            subprocess.check_call([FFMPEG, "-y", "-loglevel", "error", "-ss",
                                   "%.3f" % mps, "-i", MP4, "-frames:v", "1", dec])
            pg.goto(url + "?t=%.2f" % eps, wait_until="load")
            pg.wait_for_timeout(700)
            shot = os.path.join(WORK, "browser_%02d.png" % k)
            pg.screenshot(path=shot)
            a = np.asarray(Image.open(dec).convert("RGB"), dtype=np.int16)
            b = np.asarray(Image.open(shot).convert("RGB"), dtype=np.int16)
            if a.shape != b.shape:
                diffs.append((mps, eps, 255.0))
                continue
            d = float(np.abs(a - b).mean())
            diffs.append((mps, eps, d))
        br.close()

    worst = max(d[2] for d in diffs)
    for mps, eps, d in diffs:
        print("   mp4 %7.2fs  vs  episode %7.2fs   mean abs pixel difference %.3f"
              % (mps, eps, d))
    check("the decoded MP4 frame matches the browser render", worst < 12.0,
          "worst mean difference %.3f / 255" % worst)

    # ---- 2. audio offset ----------------------------------------------
    mp4_env = envelope(MP4)
    a_env = envelope(ep_audio, ss=A0, dur=A1 - A0)
    b_env = envelope(ep_audio, ss=B0, dur=B1 - B0)

    def corr(x, y):
        n = min(len(x), len(y))
        x, y = x[:n], y[:n]
        if n < 5:
            return 0.0
        x = x - x.mean()
        y = y - y.mean()
        d = np.sqrt((x * x).sum() * (y * y).sum())
        return float((x * y).sum() / d) if d else 0.0

    # the mp4 audio is the two segments back to back
    joined = np.concatenate([a_env, b_env])
    r = corr(mp4_env[:len(joined)], joined)
    check("the MP4 audio is the episode audio at the right offset", r > 0.90,
          "envelope correlation %.4f (%d s compared)" % (r, len(joined)))

    # a deliberate mis-offset must NOT correlate -- proves the check has teeth
    wrong = corr(mp4_env[:len(joined)], np.concatenate([a_env[8:], b_env[8:]]))
    check("the same check rejects a deliberately mis-offset slice", wrong < 0.90,
          "mis-offset correlation %.4f" % wrong)

    print("\n%d passed, %d failed"
          % (sum(1 for r in results if r[1]), sum(1 for r in results if not r[1])))
    if any(not r[1] for r in results):
        raise SystemExit("MP4 VERIFICATION FAILED")


if __name__ == "__main__":
    main()
