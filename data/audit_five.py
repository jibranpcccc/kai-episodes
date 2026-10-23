"""Audit rendered episodes: duration vs HTML, blank frames at scene cuts, cut timing."""
import json, os, re, subprocess, sys

ROOT = r"C:\Users\jibra\Desktop\1\KAI"


def yavg_series(path, fps=4):
    """per-frame luma average at `fps` samples per second"""
    out = subprocess.run(
        ["ffmpeg", "-hide_banner", "-nostats", "-i", path,
         "-vf", f"fps={fps},signalstats,metadata=print:key=lavfi.signalstats.YAVG",
         "-f", "null", "-"],
        capture_output=True, text=True, errors="ignore").stderr
    vals, t = [], 0.0
    for line in out.splitlines():
        m = re.search(r"pts_time:([0-9.]+)", line)
        if m:
            t = float(m.group(1))
        m = re.search(r"YAVG=([0-9.]+)", line)
        if m:
            vals.append((t, float(m.group(1))))
    return vals


def duration(path):
    return float(subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration",
                                 "-of", "csv=p=0", path], capture_output=True, text=True).stdout)


def has_audio(path):
    o = subprocess.run(["ffprobe", "-v", "error", "-select_streams", "a",
                        "-show_entries", "stream=codec_name", "-of", "csv=p=0", path],
                       capture_output=True, text=True).stdout.strip()
    return bool(o)


def audit(name):
    html = os.path.join(ROOT, name + ".html")
    mp4 = os.path.join(ROOT, "videos_cloud", name, name + ".mp4")
    if not (os.path.exists(html) and os.path.exists(mp4)):
        return {"name": name, "error": "missing file"}

    src = open(html, encoding="utf-8").read()
    scenes = [(float(a), float(b)) for a, b in re.findall(r"\{s:\s*([0-9.]+),\s*e:\s*([0-9.]+)\}", src)]
    total = float(re.search(r"total:\s*([0-9.]+)", src).group(1))
    dur = duration(mp4)
    s = yavg_series(mp4)

    if not s:
        return {"name": name, "error": "no luma data"}

    med = sorted(v for _, v in s)[len(s) // 2]

    def at(t):
        return min(s, key=lambda kv: abs(kv[0] - t))[1]

    # blank check: 0.6s after each scene start should have content
    blanks = []
    for a, b in scenes:
        if a + 0.6 > dur:
            continue
        y = at(a + 0.6)
        if y < med * 0.80:
            blanks.append((round(a, 1), round(y, 1)))

    # cut check: luma should change measurably across a scene boundary
    dead_cuts = []
    for a, b in scenes[1:]:
        before = at(a - 0.4)
        after = at(a + 0.7)
        if abs(after - before) < 0.4:
            dead_cuts.append(round(a, 1))

    return {"name": name, "dur": dur, "total": total, "audio": has_audio(mp4),
            "median": med, "blanks": blanks, "dead_cuts": dead_cuts,
            "scenes": len(scenes)}


rows = []
for n in ["BYTE-03", "BYTE-04", "BYTE-05", "BYTE-06", "BYTE-07"]:
    rows.append(audit(n))

print(f"{'episode':10} {'video':>7} {'html':>7} {'audio':>6} {'scenes':>6}  verdict")
print("-" * 78)
bad = 0
for r in rows:
    if r.get("error"):
        print(f"{r['name']:10} ERROR {r['error']}")
        bad += 1
        continue
    drift = abs(r["dur"] - r["total"])
    ok = (drift < 0.6 and r["audio"] and not r["blanks"] and not r["dead_cuts"])
    if not ok:
        bad += 1
    print(f"{r['name']:10} {r['dur']:7.1f} {r['total']:7.1f} {str(r['audio']):>6} "
          f"{r['scenes']:6}  {'OK' if ok else 'CHECK'}")
    if r["blanks"]:
        print(f"    blank at scene start: {r['blanks'][:6]}")
    if r["dead_cuts"]:
        print(f"    no visible change across cut: {r['dead_cuts'][:6]}")
    if drift >= 0.6:
        print(f"    duration drift {drift:.2f}s")

print(f"\n{bad} of {len(rows)} need attention")
