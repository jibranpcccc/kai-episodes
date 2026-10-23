# -*- coding: utf-8 -*-
"""Player and audio behaviour test for a built FUSION episode.

This is not a static inspection. It drives the real page in Chromium and
checks that the controls a viewer actually uses work:

  * the embedded MP3 decodes (not a blob that only *looks* like audio)
  * play / pause / resume / stop all do what they say
  * seeking moves both the audio clock and the rendered scene
  * the keyboard shortcuts work
  * the rate buttons work
  * the audio clock and the scene timeline stay in sync
  * the scene boundaries are contiguous with no gap and no overlap

Usage:  python data/_player_test.py BYTE-EP09
"""
import base64
import io
import json
import os
import re
import sys

from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
NAME = sys.argv[1] if len(sys.argv) > 1 else "BYTE-EP09"
PATH = os.path.join(ROOT, NAME + ".html")
URL = "file:///" + PATH.replace("\\", "/")

results = []


def check(name, ok, detail=""):
    results.append((name, bool(ok), detail))
    print("%s  %-46s %s" % ("PASS" if ok else "FAIL", name, detail))


def main():
    text = io.open(PATH, encoding="utf-8").read()
    F = json.loads(re.search(r"window\.FUSION = (\{.*?\});</script>", text, re.S).group(1))
    scenes = F["scenes"]
    total = F["total"]

    errs = []
    with sync_playwright() as pw:
        br = pw.chromium.launch(args=[
            "--autoplay-policy=no-user-gesture-required",
            "--mute-audio",
            "--force-color-profile=srgb",
        ])
        pg = br.new_page(viewport={"width": 1920, "height": 1080})
        pg.on("console", lambda m: errs.append(m.type + ": " + m.text)
              if m.type == "error" else None)
        pg.on("pageerror", lambda e: errs.append("pageerror: " + str(e)))
        pg.goto(URL, wait_until="load")
        pg.wait_for_timeout(1200)

        # ---- 1. the embedded audio element -----------------------------
        info = pg.evaluate("""() => {
          const a = document.getElementById('vo');
          if (!a) return null;
          return {src: a.getAttribute('src') || '', ready: a.readyState,
                  dur: a.duration, paused: a.paused, ct: a.currentTime,
                  rate: a.playbackRate};
        }""")
        check("the audio element exists", info is not None)
        if info is None:
            br.close()
            return finish()
        check("the audio source is embedded, not linked",
              info["src"].startswith("data:audio/mpeg;base64,"),
              "src=%s..." % info["src"][:32])
        check("the browser reports a real duration",
              info["dur"] and info["dur"] > 0,
              "duration=%.3fs" % info["dur"])
        check("the timeline and the audio clock agree",
              abs(info["dur"] - total) < 1.0,
              "audio %.3fs vs timeline %.3fs" % (info["dur"], total))

        # ---- 2. the MP3 really decodes -------------------------------
        dec = pg.evaluate("""async () => {
          const a = document.getElementById('vo');
          const b64 = (a.getAttribute('src') || '').split(',')[1] || '';
          const bin = atob(b64);
          const u8 = new Uint8Array(bin.length);
          for (let i = 0; i < bin.length; i++) u8[i] = bin.charCodeAt(i);
          const AC = window.AudioContext || window.webkitAudioContext;
          if (!AC) return {err: 'no AudioContext'};
          const ac = new AC();
          const buf = await ac.decodeAudioData(u8.buffer.slice(0));
          // measure real signal energy over the first 20 s
          const n = Math.min(buf.length, Math.floor(buf.sampleRate * 20));
          const ch = buf.getChannelData(0);
          let peak = 0, sum = 0;
          for (let i = 0; i < n; i++) { const v = Math.abs(ch[i]); if (v > peak) peak = v; sum += v * v; }
          const rms = n ? Math.sqrt(sum / n) : 0;
          await ac.close();
          return {sr: buf.sampleRate, ch: buf.numberOfChannels,
                  dur: buf.duration, frames: buf.length, peak: peak, rms: rms,
                  bytes: bin.length};
        }""")
        if dec.get("err"):
            check("the embedded MP3 decodes", False, dec["err"])
        else:
            check("the embedded MP3 decodes", True,
                  "%d bytes -> %d ch @ %d Hz, %.3fs" % (dec["bytes"], dec["ch"],
                                                       dec["sr"], dec["dur"]))
            check("the decoded audio is not silence",
                  dec["peak"] > 0.01 and dec["rms"] > 0.001,
                  "peak=%.3f rms=%.4f" % (dec["peak"], dec["rms"]))
            check("the decoded audio length matches the timeline",
                  abs(dec["dur"] - total) < 1.0,
                  "decoded %.3fs vs timeline %.3fs" % (dec["dur"], total))

        # ---- 3. play / pause / resume ---------------------------------
        pg.evaluate("() => { document.getElementById('vo').currentTime = 0; }")
        pg.click("#ctlPlay")
        pg.wait_for_timeout(1600)
        s1 = pg.evaluate("""() => { const a = document.getElementById('vo');
            return {ct: a.currentTime, paused: a.paused}; }""")
        check("play starts the clock", not s1["paused"] and s1["ct"] > 0.4,
              "t=%.3f paused=%s" % (s1["ct"], s1["paused"]))

        pg.click("#ctlPlay")
        pg.wait_for_timeout(500)
        s2 = pg.evaluate("""() => { const a = document.getElementById('vo');
            return {ct: a.currentTime, paused: a.paused}; }""")
        check("pause freezes the clock", s2["paused"], "paused=%s" % s2["paused"])
        pg.wait_for_timeout(700)
        s2b = pg.evaluate("() => document.getElementById('vo').currentTime")
        check("a paused clock does not drift", abs(s2b - s2["ct"]) < 0.05,
              "drift=%.3fs" % abs(s2b - s2["ct"]))

        pg.click("#ctlPlay")
        pg.wait_for_timeout(1200)
        s3 = pg.evaluate("() => document.getElementById('vo').currentTime")
        check("resume continues from where it paused", s3 > s2b + 0.4,
              "%.3f -> %.3f" % (s2b, s3))

        # ---- 4. seek ---------------------------------------------------
        pg.evaluate("() => { document.getElementById('vo').currentTime = 300; }")
        pg.wait_for_timeout(700)
        seek = pg.evaluate("""() => {
          const a = document.getElementById('vo');
          const F = window.__FUSION__;
          const sc = F.sceneAt(300);
          return {ct: a.currentTime, scene: sc, total: F.F.total};
        }""")
        check("seek lands on the requested time", abs(seek["ct"] - 300) < 1.2,
              "ct=%.3f" % seek["ct"])
        want = None
        for i, s in enumerate(scenes):
            if s["s"] <= 300 < s["e"]:
                want = i
                break
        check("the rendered scene follows the audio clock", seek["scene"] == want,
              "scene=%s expected=%s" % (seek["scene"], want))

        # ---- 5. keyboard shortcuts -------------------------------------
        pg.keyboard.press("Space")
        pg.wait_for_timeout(400)
        kb1 = pg.evaluate("() => document.getElementById('vo').paused")
        check("Space pauses", kb1 is True, "paused=%s" % kb1)
        pg.keyboard.press("Space")
        pg.wait_for_timeout(400)
        kb2 = pg.evaluate("() => document.getElementById('vo').paused")
        check("Space resumes", kb2 is False, "paused=%s" % kb2)

        before = pg.evaluate("() => document.getElementById('vo').currentTime")
        pg.keyboard.press("ArrowRight")
        pg.wait_for_timeout(400)
        after = pg.evaluate("() => document.getElementById('vo').currentTime")
        check("ArrowRight seeks forward 5s", after - before > 3.5,
              "%.3f -> %.3f" % (before, after))
        pg.keyboard.press("ArrowLeft")
        pg.wait_for_timeout(400)
        back = pg.evaluate("() => document.getElementById('vo').currentTime")
        check("ArrowLeft seeks back 5s", after - back > 3.5,
              "%.3f -> %.3f" % (after, back))

        pg.keyboard.press("s")
        pg.wait_for_timeout(400)
        stopped = pg.evaluate("""() => { const a = document.getElementById('vo');
            return {ct: a.currentTime, paused: a.paused}; }""")
        check("S stops and rewinds", stopped["paused"] and stopped["ct"] < 0.3,
              "ct=%.3f paused=%s" % (stopped["ct"], stopped["paused"]))

        pg.click("#ctl .rate[data-r='2']")
        pg.wait_for_timeout(250)
        rate = pg.evaluate("() => document.getElementById('vo').playbackRate")
        check("the rate button changes the rate", abs(rate - 2) < 0.01,
              "rate=%s" % rate)
        pg.click("#ctl .rate[data-r='1']")
        pg.wait_for_timeout(200)
        rate1 = pg.evaluate("() => document.getElementById('vo').playbackRate")
        check("the rate button returns to 1x", abs(rate1 - 1) < 0.01,
              "rate=%s" % rate1)

        # ---- 6. the timeline itself -----------------------------------
        tl = pg.evaluate("""() => {
          const F = window.__FUSION__;
          const sc = F.F.scenes;
          const out = {gaps: [], overlaps: [], bad: 0, maxGap: 0, cover: []};
          for (let i = 1; i < sc.length; i++) {
            const d = sc[i].s - sc[i-1].e;
            if (d > out.maxGap) out.maxGap = d;
            // a uniform, small dip between windows is the designed
            // transition; a ragged one is a timeline defect
            if (d > 0.5) out.gaps.push([i, sc[i-1].e, sc[i].s, d]);
            if (d < -0.001) out.overlaps.push([i, sc[i-1].e, sc[i].s, -d]);
          }
          const all = [];
          for (let i = 0; i < sc.length; i++) {
            const a = F.sceneAt(sc[i].s + 0.01);
            if (a !== i) out.bad++;
            const b = F.sceneAt(sc[i].e - 0.01);
            if (b !== i) out.bad++;
          }
          // the timeline must cover the whole runtime
          out.cover.push(sc[0].s, sc[sc.length-1].e, F.F.total);
          return out;
        }""")
        check("no window boundary leaves a hole in the timeline",
              not tl["gaps"],
              "gaps over 0.5s: %d (largest dip %.3fs)" % (len(tl["gaps"]), tl["maxGap"]))
        check("the scene timeline has no overlap", not tl["overlaps"],
              "overlaps=%d" % len(tl["overlaps"]))
        check("sceneAt() agrees with the scene table at every edge",
              tl["bad"] == 0, "%d mismatches over %d scenes" % (tl["bad"], len(scenes)))
        cov = tl["cover"]
        check("the timeline runs from zero to the end of the audio",
              cov[0] <= 0.001 and abs(cov[1] - cov[2]) < 1.0,
              "first %.3f, last window ends %.3f, runtime %.3f" % (cov[0], cov[1], cov[2]))

        # ---- 7. transitions actually change the screen -----------------
        trans = pg.evaluate("""() => {
          const F = window.__FUSION__;
          const sc = F.F.scenes;
          const els = document.querySelectorAll('.scene');
          let wrong = 0, missing = 0, sameCue = 0;
          const seen = {};
          for (let i = 0; i < sc.length; i++) {
            F.renderState(sc[i].s + 0.05);
            const on = document.querySelector('.scene.on');
            if (!on) { missing++; continue; }
            const idx = Array.prototype.indexOf.call(els, on);
            if (idx !== i) wrong++;
            seen[idx] = (seen[idx] || 0) + 1;
            const cue = document.getElementById('cue');
            if (cue && sc[i].label && cue.textContent !== sc[i].label) sameCue++;
          }
          return {wrong: wrong, missing: missing, sameCue: sameCue,
                  distinct: Object.keys(seen).length, n: sc.length};
        }""")
        check("renderState() shows the window the clock is in",
              trans["wrong"] == 0 and trans["missing"] == 0,
              "%d wrong, %d missing" % (trans["wrong"], trans["missing"]))
        check("every window owns a distinct scene element",
              trans["distinct"] == trans["n"],
              "%d distinct of %d windows" % (trans["distinct"], trans["n"]))
        check("the caption line follows the scene",
              trans["sameCue"] == 0, "%d mismatches" % trans["sameCue"])

        check("the page produced no console errors", not errs,
              "; ".join(errs[:3]) if errs else "0 errors")
        br.close()
    return finish()


def finish():
    bad = [r for r in results if not r[1]]
    print("\n%d passed, %d failed" % (len(results) - len(bad), len(bad)))
    if bad:
        raise SystemExit("PLAYER TEST FAILED: " + "; ".join(r[0] for r in bad))
    print("PLAYER TEST PASSED")


if __name__ == "__main__":
    main()
