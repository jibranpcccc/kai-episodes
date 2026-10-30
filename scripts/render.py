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
import json
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
        m = re.search(r"""const\s+AUDIO_B64\s*=\s*(?:/\*.*?\*/)?\s*["']([A-Za-z0-9+/=\s]+)["']""", html)
    if not m:
        return False
    dst.write_bytes(base64.b64decode(re.sub(r"\s+", "", m.group(1))))
    return True


def verify_rendered_mp4(mp4: Path, total: float, expected_res: str = "1440p", has_audio: bool = True):
    """
    Strict post-render stream, dimension, frame rate, duration, and decode integrity verification.
    Raises ValueError or RuntimeError on ANY defect (hard failure).
    """
    target_w, target_h = (2560, 1440) if expected_res == "1440p" else (1920, 1080)
    
    probe = subprocess.run([
        "ffprobe", "-v", "error",
        "-show_entries", "format=duration:stream=codec_type,codec_name,width,height,r_frame_rate,channels,channel_layout",
        "-of", "json", str(mp4)
    ], capture_output=True, text=True)
    if probe.returncode != 0:
        raise RuntimeError(f"ffprobe failed to probe {mp4.name}: {probe.stderr.strip()}")
    
    info = json.loads(probe.stdout)
    v_stream = next((s for s in info.get("streams", []) if s.get("codec_type") == "video"), None)
    a_stream = next((s for s in info.get("streams", []) if s.get("codec_type") == "audio"), None)
    
    # 1. Video stream verification
    if v_stream is None:
        raise ValueError(f"CRITICAL RENDER DEFECT: {mp4.name} contains NO video stream!")
    
    v_codec = v_stream.get("codec_name")
    if not v_codec or v_codec not in ("h264", "hevc", "av1", "vp9"):
        raise ValueError(f"CRITICAL RENDER DEFECT: {mp4.name} invalid or missing video codec: '{v_codec}'!")
        
    actual_w = v_stream.get("width")
    actual_h = v_stream.get("height")
    if actual_w != target_w or actual_h != target_h:
        raise ValueError(
            f"CRITICAL RENDER DEFECT: {mp4.name} resolution is {actual_w}x{actual_h}, "
            f"expected exact {target_w}x{target_h} ({expected_res})!"
        )
    
    r_fps_str = v_stream.get("r_frame_rate", "0/1")
    try:
        num, den = map(float, r_fps_str.split("/"))
        actual_fps = num / den if den != 0 else 0.0
    except Exception:
        actual_fps = 0.0
    if abs(actual_fps - FPS) > 0.5:
        raise ValueError(f"CRITICAL RENDER DEFECT: {mp4.name} frame rate is {actual_fps:.2f}fps, expected {FPS}fps!")
    
    # 2. Audio stream verification
    if has_audio:
        if a_stream is None:
            raise ValueError(f"CRITICAL RENDER DEFECT: {mp4.name} contains NO audio stream when narration audio was required!")
        a_codec = a_stream.get("codec_name")
        if not a_codec or a_codec not in ("aac", "mp3", "opus", "flac"):
            raise ValueError(f"CRITICAL RENDER DEFECT: {mp4.name} invalid audio codec: '{a_codec}' (expected aac/mp3/opus)!")
        channels = int(a_stream.get("channels", 0))
        if channels < 1:
            raise ValueError(f"CRITICAL RENDER DEFECT: {mp4.name} has invalid audio channel count ({channels})!")
        layout = a_stream.get("channel_layout") or ("mono" if channels == 1 else "stereo" if channels == 2 else f"{channels}ch")
        audio_desc = f"{a_codec} ({layout}, {channels}ch)"
    else:
        audio_desc = "none (no audio track required)"
    
    # 3. Duration & Drift Check
    dur_mp4 = float(info.get("format", {}).get("duration", 0))
    if abs(dur_mp4 - total) > 0.20:
        raise ValueError(
            f"CRITICAL RENDER DEFECT: {mp4.name} duration {dur_mp4:.2f}s drifts from "
            f"expected cue timeline {total:.2f}s by {abs(dur_mp4 - total):.2f}s (> 0.20s threshold)!"
        )
    
    # 4. Bitstream decoding pass via ffmpeg null sink
    decode_check = subprocess.run([
        "ffmpeg", "-v", "error", "-i", str(mp4), "-f", "null", "-"
    ], capture_output=True, text=True)
    if decode_check.returncode != 0 or decode_check.stderr.strip():
        raise RuntimeError(f"CRITICAL RENDER DEFECT: {mp4.name} failed bitstream decoding: {decode_check.stderr.strip()}")
    
    print(f"[{mp4.stem}] MP4 VERIFIED: {v_codec} {actual_w}x{actual_h} @ {actual_fps:.1f}fps, audio: {audio_desc}, duration={dur_mp4:.2f}s")


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
    page.evaluate("""() => {
        document.body.classList.add('render');
        const style = document.createElement('style');
        style.id = 'pure-clean-render-canvas-override';
        style.textContent = `
            #ctl, #boot, #bar, #tc, #wm, #rail, #ticks, .src, .kicker, .kicker-line,
            .boot__mark, [id*="ctl"], [id*="tc"], [class*="src"], #hud, #cue, #start {
                display: none !important;
                visibility: hidden !important;
                opacity: 0 !important;
                pointer-events: none !important;
            }
        `;
        document.head.appendChild(style);
    }""")
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
        vf_scale = "unsharp=5:5:0.3:5:5:0.0"
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

    # Mandatory Hard Post-Render Verification
    verify_rendered_mp4(mp4, total, RES, has_audio)
    print(f"[{name}] wrote and verified {mp4} ({mp4.stat().st_size/1e6:.1f} MB)")

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
        
        # Exact 1920x1080 CSS viewport. For 1440p, device_scale_factor=4/3 (1.3333333333333333)
        # generates exact 2560x1440 physical pixel screenshots without black letterbox borders.
        if RES == "1440p":
            page = browser.new_page(viewport={"width": 1920, "height": 1080},
                                    device_scale_factor=4 / 3)
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
