#!/usr/bin/env python3
"""
Render the episode HTML files to MP4 on a headless Chromium.

Each episode is a single self-contained HTML file with:
  * the voiceover embedded as a base64 data URI
  * window.renderAt(t)  -> paints the frame at exactly t seconds
  * window.EPISODE.total -> duration

We step the clock frame by frame, screenshot, then mux the embedded
audio back on with ffmpeg. Because the audio comes out of the same file
that produced the cue times, sync is exact by construction.
"""
import base64
import os
import re
import subprocess
import sys
from pathlib import Path

from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent
EPISODES = ROOT / "episodes"
OUT = ROOT / "out"
WORK = ROOT / "out" / "_frames"

FPS = int(os.environ.get("FPS", "30"))
ONLY = (os.environ.get("ONLY") or "").strip()
RES = (os.environ.get("RES") or "1440p").lower()

W, H = 1920, 1080


def extract_audio(html: str, dst: Path) -> bool:
    m = re.search(r"data:audio/mpeg;base64,([A-Za-z0-9+/=\s]+)", html)
    if not m:
        return False
    dst.write_bytes(base64.b64decode(re.sub(r"\s+", "", m.group(1))))
    return True


def render_one(page, html_path: Path) -> Path:
    name = html_path.stem
    frames_dir = WORK / name
    if frames_dir.exists():
        for f in frames_dir.iterdir():
            f.unlink()
    frames_dir.mkdir(parents=True, exist_ok=True)

    html = html_path.read_text(encoding="utf-8")
    vo = frames_dir / "vo.mp3"
    has_audio = extract_audio(html, vo)
    print(f"[{name}] embedded audio: {'yes' if has_audio else 'NO'}")

    # ?t=0 puts the player into render mode (hides HUD/controls, unscales the stage);
    # we also set the class explicitly in case the query string is dropped.
    page.goto(html_path.resolve().as_uri() + "?t=0")
    page.wait_for_function("!!((window.EPISODE || window.FUSION) && window.renderAt)", timeout=60000)
    page.evaluate("document.body.classList.add('render')")
    page.evaluate("async () => { if (document.fonts && document.fonts.ready) await document.fonts.ready; }")
    page.wait_for_timeout(300)          # let layout and webfonts fully settle
    assert page.evaluate("document.body.classList.contains('render')"), "render mode not applied"

    total = float(page.evaluate("(window.EPISODE || window.FUSION).total"))
    n = max(1, int(round(total * FPS)))
    print(f"[{name}] {total:.2f}s -> {n} frames at {FPS}fps")

    for i in range(n):
        t = i / FPS
        page.evaluate(f"window.renderAt({t})")
        page.screenshot(
            path=str(frames_dir / f"f{i:05d}.jpg"),
            type="jpeg",
            quality=95,
        )
        if i % 150 == 0:
            print(f"   frame {i}/{n}")

    mp4 = OUT / f"{name}.mp4"
    cmd = [
        "ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
        "-framerate", str(FPS),
        "-i", str(frames_dir / "f%05d.jpg"),
    ]
    if has_audio:
        cmd += ["-i", str(vo)]

    # 1440p High-Fidelity Lanczos Scaling & Bitrate Target
    if RES == "1440p":
        vf_scale = "scale=2560:1440:flags=lanczos,unsharp=5:5:0.3:5:5:0.0"
        bitrate_opts = ["-b:v", "14M", "-maxrate", "18M", "-bufsize", "28M"]
    else:
        vf_scale = "null"
        bitrate_opts = []

    if has_audio:
        filter_complex = f"[0:v]{vf_scale}[vout];[1:a]apad=whole_dur={total:.3f}[aout]"
        cmd += [
            "-filter_complex", filter_complex,
            "-map", "[vout]", "-map", "[aout]",
            "-c:a", "aac", "-b:a", "384k",
        ]
    else:
        if vf_scale != "null":
            cmd += ["-vf", vf_scale]

    cmd += [
        "-c:v", "libx264", "-preset", "medium", "-crf", "16",
        *bitrate_opts,
        "-pix_fmt", "yuv420p", "-movflags", "+faststart",
        str(mp4),
    ]
    subprocess.run(cmd, check=True)
    print(f"[{name}] wrote {mp4} ({mp4.stat().st_size/1e6:.1f} MB)")

    # Post-render stream and duration integrity probe
    try:
        import json as _json
        probe = subprocess.run([
            "ffprobe", "-v", "error", "-show_entries", "format=duration:stream=codec_type,width,height",
            "-of", "json", str(mp4)
        ], capture_output=True, text=True)
        info = _json.loads(probe.stdout)
        v_stream = next((s for s in info.get("streams", []) if s.get("codec_type") == "video"), None)
        a_stream = next((s for s in info.get("streams", []) if s.get("codec_type") == "audio"), None)
        dur_mp4 = float(info.get("format", {}).get("duration", 0))
        assert v_stream is not None, "Rendered MP4 has no video stream!"
        if has_audio:
            assert a_stream is not None, "Rendered MP4 has no audio stream!"
        assert abs(dur_mp4 - total) <= 0.20, f"MP4 duration {dur_mp4:.2f}s drifts from expected {total:.2f}s!"
        print(f"[{name}] MP4 verified: {v_stream.get('width')}x{v_stream.get('height')}, duration={dur_mp4:.2f}s, audio={'yes' if a_stream else 'no'}")
    except Exception as e:
        print(f"[{name}] Note: MP4 probe: {e}")

    return mp4


def main() -> int:
    OUT.mkdir(parents=True, exist_ok=True)
    files = sorted(EPISODES.glob("*.html"))
    if ONLY:
        files = [f for f in files if f.stem.lower() == ONLY.lower() or f.name.lower() == ONLY.lower()]
    if not files:
        print("no episode HTML found in episodes/", file=sys.stderr)
        return 1

    with sync_playwright() as p:
        try:
            browser = p.chromium.launch(args=["--force-device-scale-factor=1"])
        except Exception:
            # fall back to a system Chrome (handy locally; CI installs chromium)
            browser = p.chromium.launch(channel="chrome",
                                        args=["--force-device-scale-factor=1"])
        if RES == "1440p":
            page = browser.new_page(viewport={"width": 2560, "height": 1440},
                                    device_scale_factor=1.333333)
        else:
            page = browser.new_page(viewport={"width": W, "height": H},
                                    device_scale_factor=1)
        for f in files:
            render_one(page, f)
        browser.close()

    print("\ndone:", ", ".join(x.name for x in sorted(OUT.glob("*.mp4"))))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
