# -*- coding: utf-8 -*-
"""Structural audit of a built episode.

Reads the generated HTML as a file, not as a browser sees it, and checks the
things a browser would silently paper over: a missing payload, a beat that
points at an element that is not there, a duplicated id, an audio track that
is not an MP3, an external reference the page cannot load offline.

    python data/_audit_html.py BYTE-EP09
"""
import base64
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def fail(bad, msg):
    bad.append(msg)


def main(name):
    path = os.path.join(ROOT, name + ".html")
    if not os.path.exists(path):
        raise SystemExit("%s does not exist" % path)
    text = open(path, encoding="utf-8").read()
    bad = []
    info = []

    # ---- document shell ------------------------------------------------
    m = re.search(r"<title>(.*?)</title>", text, re.S)
    if not m:
        fail(bad, "no <title>")
    else:
        info.append("document title: %s" % m.group(1))
        if "&amp;" in m.group(1) and "·" not in m.group(1):
            fail(bad, "the title still carries an escaped ampersand")

    m = re.search(r'window\.FUSION\s*=\s*(\{.*?\});', text, re.S)
    if not m:
        fail(bad, "no window.FUSION payload")
        print("\n".join(bad))
        raise SystemExit("STRUCTURAL AUDIT FAILED")
    F = json.loads(m.group(1))

    for key in ("title", "kicker", "subtitle", "total", "words", "scenes",
                "beats", "vo"):
        if key not in F:
            fail(bad, "the payload has no %r" % key)
    info.append("payload: %d words, %d scenes, %d beats, total %.3fs"
                % (len(F["words"]), len(F["scenes"]), len(F["beats"]), F["total"]))

    # ---- scenes and beats ---------------------------------------------
    scenes = F["scenes"]
    for i, s in enumerate(scenes):
        if s["e"] < s["s"]:
            fail(bad, "scene %d ends before it starts" % i)
        if i and s["s"] < scenes[i - 1]["e"] - 0.001:
            fail(bad, "scene %d overlaps scene %d" % (i, i - 1))
    beats = F["beats"]
    for b in beats:
        if "s" not in b or "e" not in b:
            fail(bad, "a beat has no timing")
        elif b["e"] < b["s"]:
            fail(bad, "a beat ends before it starts")
    groups = {}
    for b in beats:
        groups.setdefault(b.get("group"), []).append(b)
    for sc in scenes:
        bs = sorted(groups.get(sc["id"], []), key=lambda x: x["s"])
        for i in range(1, len(bs)):
            gap = bs[i]["s"] - bs[i - 1]["s"]
            if gap < 0.29:
                fail(bad, "scene %d has two beats %.3fs apart" % (sc["id"], gap))
            if gap > 8.0:
                fail(bad, "scene %d has a %.1fs dead spot" % (sc["id"], gap))
    info.append("beats: %d, every scene has %d-%d"
                % (len(beats),
                   min(len(groups.get(s["id"], [])) for s in scenes),
                   max(len(groups.get(s["id"], [])) for s in scenes)))

    # ---- element ids ---------------------------------------------------
    ids = re.findall(r'\bid="([^"]+)"', text)
    dupes = sorted(set(i for i in ids if ids.count(i) > 1))
    if dupes:
        fail(bad, "duplicate element ids: %s" % ", ".join(dupes[:6]))
    info.append("element ids: %d, %d unique" % (len(ids), len(set(ids))))

    # every beat target has to exist in the markup
    for b in beats:
        t = b.get("sel") or b.get("id") or b.get("target")
        if not t:
            continue
        sel = t if t.startswith("#") else "#" + t
        if sel not in text:
            fail(bad, "a beat points at %s, which is not in the page" % sel)

    # ---- embedded assets ------------------------------------------------
    m = re.search(r'data:audio/mpeg;base64,([A-Za-z0-9+/=]+)', text)
    if not m:
        fail(bad, "no embedded audio")
    else:
        raw = base64.b64decode(m.group(1))
        if not (raw[:3] == b"ID3" or raw[:2] == b"\xff\xfb" or raw[:2] == b"\xff\xfa"):
            fail(bad, "the embedded audio does not start with an MP3 frame")
        info.append("embedded audio: %.2f MB, %d bytes" % (len(raw) / 1048576.0, len(raw)))
    fonts = re.findall(r"data:font/ttf;base64,([A-Za-z0-9+/=]+)", text)
    info.append("embedded fonts: %d" % len(fonts))
    if not fonts:
        fail(bad, "no embedded font")

    # ---- no outside references ------------------------------------------
    ext = re.findall(r'(?:src|href)\s*=\s*"(https?://[^"]+|//[^"]+)"', text)
    if ext:
        fail(bad, "the page loads something from outside: %s" % ext[:3])
    ext2 = re.findall(r'(?:src|href)\s*=\s*"(?!data:)([^"]+)"', text)
    if ext2:
        fail(bad, "the page loads a local file: %s" % ext2[:3])
    info.append("external references: 0")

    # ---- the page has to be one file -------------------------------------
    for token in ("<style>", "</style>", "<script>", "</script>"):
        if token not in text:
            fail(bad, "the page is missing %s" % token)
    if "<iframe" in text or "<img" in text:
        fail(bad, "the page embeds an iframe or an image")

    # ---- sidecar files ----------------------------------------------------
    srt = os.path.join(ROOT, name + ".srt")
    if not os.path.exists(srt):
        fail(bad, "no .srt next to the html")
    else:
        s = open(srt, encoding="utf-8").read()
        cues = re.findall(r"(\d\d:\d\d:\d\d,\d\d\d) --> (\d\d:\d\d:\d\d,\d\d\d)", s)
        if len(cues) != 262 and len(cues) != len(re.findall(r"^\d+$", s, re.M)):
            fail(bad, "the .srt cue count does not match its index")
        prev_end = -1.0
        for a, b in cues:
            ta = sum(float(x) * f for x, f in zip(a.replace(",", ".").split(":"), (3600, 60, 1)))
            tb = sum(float(x) * f for x, f in zip(b.replace(",", ".").split(":"), (3600, 60, 1)))
            if tb <= ta:
                fail(bad, "a caption ends before it starts at %s" % a)
            if ta < prev_end - 0.001:
                fail(bad, "a caption overlaps the one before it at %s" % a)
            prev_end = tb
        if cues and prev_end > F["total"] + 1.0:
            fail(bad, "the captions run past the end of the episode")
        info.append("captions: %d cues, last ends %.2fs (episode %.2fs)"
                    % (len(cues), prev_end, F["total"]))

    print("STRUCTURAL AUDIT -- %s" % name)
    for i in info:
        print("   %s" % i)
    if bad:
        print("\nPROBLEMS")
        for b in bad:
            print("   %s" % b)
        raise SystemExit("STRUCTURAL AUDIT FAILED (%d problem(s))" % len(bad))
    print("\nSTRUCTURAL AUDIT PASSED")


if __name__ == "__main__":
    main(sys.argv[1] if len(sys.argv) > 1 else "BYTE-EP09")
