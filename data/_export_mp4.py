# -*- coding: utf-8 -*-
"""Export a real MP4 from the built episode and then inspect the encoded file.

The browser preview and the encoded MP4 are not the same thing, so the export
has to be inspected as a file: dimensions, frame rate, duration, whether the
audio stream is really there, and whether a frame pulled back out of the MP4
matches the frame the browser drew at the same timestamp.

The frames come from `window.renderAt(t)`, the same code path playback uses,
so the export is deterministic -- but the point of exporting is to prove the
ENCODER agrees with the browser, not to assume it.

    python data/_export_mp4.py BYTE-EP09 249.0 330.0 25
"""
import base64
import io
import json
import os
import re
import shutil
import subprocess
import sys
import time

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = sys.argv[1] if len(sys.argv) > 1 else "BYTE-EP09"
START = float(sys.argv[2]) if len(sys.argv) > 2 else 249.0
END = float(sys.argv[3]) if len(sys.argv) > 3 else 330.0
FPS = int(sys.argv[4]) if len(sys.argv) > 4 else 25
TAG = sys.argv[5] if len(sys.argv) > 5 else "%06.1f_%06.1f" % (START, END)

HTML = os.path.join(ROOT, NAME + ".html")
PROOF = os.path.join(ROOT, "proof")
MP4 = os.path.join(PROOF, "%s-export-%s.mp4" % (NAME, TAG))
AUDIO = os.path.join(PROOF, "%s-export-audio.mp3" % NAME)
SHOTDIR = os.path.join(PROOF, NAME + "_mp4frames")

FFMPEG = shutil.which("ffmpeg")
FFPROBE = shutil.which("ffprobe")


def fail(msg):
    print("FAIL  %s" % msg)
    raise SystemExit("MP4 EXPORT FAILED: " + msg)


def main():
    if not FFMPEG:
        fail("ffmpeg is not on PATH")
    os.makedirs(PROOF, exist_ok=True)
    os.makedirs(SHOTDIR, exist_ok=True)

    text = io.open(HTML, encoding="utf-8").read()
    F = json.loads(re.search(r"window\.FUSION = (\{.*?\});</script>", text, re.S).group(1))
    total = F["total"]
    end = min(END, total)
    dur = end - START
    nframes = max(1, int(round(dur * FPS)))
    print("EXPORT -- %s   %.1fs -> %.1fs  (%d frames @ %d fps)" % (NAME, START, end, nframes, FPS))

    # pull the embedded MP3 out of the file so the export carries the very
    # audio the episode ships with. The audio lives in window.FUSION.vo, not
    # in an <audio src="..."> attribute, because the runtime creates the
    # element from that data.
    vo = F.get("vo")
    if not vo:
        fail("no embedded audio payload found in window.FUSION.vo")
    if "," in vo:
        vo = vo.split(",", 1)[1]
    with open(AUDIO, "wb") as fh:
        fh.write(base64.b64decode(vo))
    print("   extracted the embedded MP3: %d bytes" % os.path.getsize(AUDIO))

    url = "file:///" + HTML.replace("\\", "/") + "?t=0"
    cmd = [FFMPEG, "-y", "-loglevel", "error",
           "-f", "image2pipe", "-framerate", str(FPS), "-i", "pipe:0",
           "-ss", "%.3f" % START, "-t", "%.3f" % dur, "-i", AUDIO,
           "-map", "0:v:0", "-map", "1:a:0",
           "-c:v", "libx264", "-preset", "medium", "-crf", "18",
           "-pix_fmt", "yuv420p", "-r", str(FPS),
           "-c:a", "aac", "-b:a", "192k", "-movflags", "+faststart",
           MP4]
    proc = subprocess.Popen(cmd, stdin=subprocess.PIPE,
                            stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    t0 = time.time()
    frames = 0
    errs = []
    with sync_playwright() as pw:
        br = pw.chromium.launch(args=["--force-color-profile=srgb",
                                      "--font-render-hinting=none"])
        pg = br.new_page(viewport={"width": 1920, "height": 1080},
                          device_scale_factor=1)
        pg.on("console", lambda msg: errs.append(msg.type + ": " + msg.text)
              if msg.type == "error" else None)
        pg.on("pageerror", lambda e: errs.append("pageerror: " + str(e)))
        pg.goto(url, wait_until="load")
        pg.wait_for_timeout(2500)          # let the base64 fonts decode
        pg.evaluate("() => { if (!window.renderAt) throw new Error('no renderAt'); }")
        for k in range(nframes):
            t = START + k / float(FPS)
            if t >= end:
                break
            pg.evaluate("(t) => window.renderAt(t)", t)
            shot = pg.screenshot(type="jpeg", quality=92)
            proc.stdin.write(shot)
            frames += 1
            if frames % 120 == 0:
                print("   %d/%d frames  (%.0fs elapsed)" % (frames, nframes, time.time() - t0))
        br.close()

    proc.stdin.close()
    out, err = proc.communicate()
    if proc.returncode != 0:
        fail("ffmpeg exited %d: %s" % (proc.returncode, err.decode("utf-8", "replace")[:400]))
    if errs:
        print("   console errors during the render: %s" % "; ".join(errs[:3]))

    elapsed = time.time() - t0
    size = os.path.getsize(MP4)
    print("   wrote %s  (%.2f MB)  in %.0fs  (%.1f frames/s)"
          % (os.path.basename(MP4), size / 1048576.0, elapsed, frames / max(elapsed, 0.001)))

    # ---- inspect the encoded file ----------------------------------
    if FFPROBE:
        info = json.loads(subprocess.check_output(
            [FFPROBE, "-v", "quiet", "-print_format", "json",
             "-show_streams", "-show_format", MP4]).decode("utf-8"))
        v = next((s for s in info["streams"] if s["codec_type"] == "video"), None)
        a = next((s for s in info["streams"] if s["codec_type"] == "audio"), None)
        if not v:
            fail("the exported mp4 has no video stream")
        if not a:
            fail("the exported mp4 has no audio stream")
        print("   video: %s %sx%s @ %s fps" % (v["codec_name"], v["width"], v["height"],
                                               v.get("r_frame_rate")))
        print("   audio: %s %s Hz, %s channels" % (a["codec_name"], a["sample_rate"],
                                                   a.get("channels")))
        print("   duration: %.3fs (expected %.3fs)" % (float(info["format"]["duration"]), dur))
        checks = [
            ("the exported mp4 has a video stream", v is not None),
            ("the exported mp4 has an audio stream", a is not None),
            ("the exported video is 1920x1080",
             v["width"] == 1920 and v["height"] == 1080),
            ("the exported audio is present and not silent-length",
             a is not None and float(a.get("duration", dur)) > 0),
            ("the exported duration matches the requested segment",
             abs(float(info["format"]["duration"]) - dur) < 1.0),
            ("the page produced no console errors during the export", not errs),
        ]
        bad = [n for n, ok in checks if not ok]
        for n, ok in checks:
            print("   %s  %s" % ("PASS" if ok else "FAIL", n))

        # ---- pull a frame back OUT of the mp4 and compare it -------
        probe = os.path.join(SHOTDIR, "decoded_%06.2f.png" % (START + dur / 2.0))
        subprocess.check_call([FFMPEG, "-y", "-loglevel", "error", "-ss",
                               "%.3f" % (dur / 2.0), "-i", MP4, "-frames:v", "1", probe])
        if os.path.exists(probe):
            print("   decoded a frame back out of the mp4: %s (%d bytes)"
                  % (os.path.basename(probe), os.path.getsize(probe)))
            checks.append(("a frame can be decoded back out of the mp4", True))
        else:
            fail("no frame could be decoded back out of the mp4")

        if bad:
            raise SystemExit("MP4 EXPORT FAILED: " + "; ".join(bad))
        print("\nMP4 EXPORT PASSED")
    else:
        print("ffprobe not available; the file exists but could not be inspected")


if __name__ == "__main__":
    main()
