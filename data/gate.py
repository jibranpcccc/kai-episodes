"""Full gate for one episode - implements every check in EPISODE-RULES.md."""
import collections, io, os, re, subprocess, sys
from playwright.sync_api import sync_playwright
from PIL import Image, ImageChops

ROOT = r"C:\Users\jibra\Desktop\1\KAI"
name = sys.argv[1] if len(sys.argv) > 1 else "BYTE-01-A"
html = os.path.join(ROOT, name + ".html")

src = open(html, encoding="utf-8").read()
print(f"=== GATE: {name} ===")
fails = []

# --- 1. structure ---
secs = re.findall(r'<section class="scene[^"]*" data-scene="(\d+)">(.*?)</section>', src, re.S)
durs = [(float(a), float(b)) for a, b in re.findall(r"\{s:\s*([0-9.]+),\s*e:\s*([0-9.]+)\}", src)]
longest = max(b - a for a, b in durs)
print(f"windows            : {len(secs)}")
print(f"longest window     : {longest:.1f}s  {'OK' if longest <= 20.5 else 'FAIL'}")
if longest > 20.5: fails.append("window > 20s")

noart = [i + 1 for i, (idx, body) in enumerate(secs) if "<svg" not in body]
print(f"windows w/o drawing: {len(noart)}  {'OK' if not noart else 'FAIL ' + str(noart[:5])}")
if noart: fails.append("window without drawing")

# --- 2. simultaneous reveals ---
stacked = []
for idx, body in secs:
    rail = re.search(r'<div class="rail">(.*?)</div>', body, re.S)
    b2 = body if not rail else body.replace(rail.group(0), "")
    vals = [round(float(v), 1) for v in re.findall(r'data-in="([0-9.]+)"', b2)]
    c = collections.Counter(vals)
    if any(t <= 0.5 and n >= 2 for t, n in c.items()):
        stacked.append(int(idx) + 1)
print(f"stacked reveals    : {len(stacked)}  {'OK' if not stacked else 'FAIL ' + str(stacked[:5])}")
if stacked: fails.append("elements stacked at window start")

# --- 3. runtime / audio / loudness ---
total = max(b for a, b in durs)
print(f"runtime            : {int(total//60)}:{int(total%60):02d}")

# measure the audio actually embedded in the HTML, not a build artifact
import base64, tempfile
_m = re.search(r'vo:\s*"data:audio/mpeg;base64,([A-Za-z0-9+/=]+)"', src)
if _m:
    _td = tempfile.mkdtemp()
    mp3 = os.path.join(_td, "embedded.mp3")
    open(mp3, "wb").write(base64.b64decode(_m.group(1)))
if os.path.exists(mp3):
    out = subprocess.run(["ffmpeg", "-hide_banner", "-nostats", "-i", mp3, "-af",
                          "ebur128=peak=true", "-f", "null", "-"],
                         capture_output=True, text=True, errors="ignore").stderr
    m = re.findall(r"I:\s+(-?[0-9.]+) LUFS", out)
    loud = float(m[-1]) if m else None
    ok = loud is not None and abs(loud + 14) <= 0.8
    print(f"loudness           : {loud} LUFS  {'OK' if ok else 'FAIL'}")
    if not ok: fails.append("loudness off target")

# --- 4. callout dots on artwork ---
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1920, "height": 1080})
    pg.goto("file:///" + html.replace("\\", "/")); pg.wait_for_timeout(700)
    pg.evaluate("""()=>{document.body.classList.add('render');
      const vo=document.getElementById('vo'); window.__T=0;
      Object.defineProperty(vo,'currentTime',{get:()=>window.__T,set:v=>{}});}""")
    sc = pg.evaluate("window.EPISODE.scenes")
    dots_total = dots_bad = clipped = 0
    for i, x in enumerate(sc):
        t = x["s"] + (x["e"] - x["s"]) * 0.85
        pg.evaluate("t=>{window.__T=t;window.renderAt(t);}", t); pg.wait_for_timeout(55)
        d = pg.evaluate("""(i)=>{const s=[...document.querySelectorAll('.scene')][i];
          const ann=s.querySelector('svg.ann');
          let badges=[], box=null;
          if(ann){
            const art=ann.querySelector('svg');
            if(art){const b=art.getBoundingClientRect();
              box={l:b.left,t:b.top,r:b.right,b:b.bottom};}
            badges=[...ann.querySelectorAll('g.badge circle')].map(c=>{
              const r=c.getBoundingClientRect(); return {x:r.x+r.width/2,y:r.y+r.height/2};});
          }
          const sr=document.getElementById('stage').getBoundingClientRect(); let cl=0;
          s.querySelectorAll('*').forEach(el=>{const cs=getComputedStyle(el);
            if(cs.opacity==='0'||cs.display==='none')return;const r=el.getBoundingClientRect();
            if(r.width<2||r.height<2)return;
            if(r.left<sr.left-4||r.right>sr.right+4||r.top<sr.top-4||r.bottom>sr.bottom+4)cl++;});
          return {badges, box, cl};}""", i)
        if d["cl"]: clipped += 1
        if d["badges"]:
            box = d["box"]
            for q in d["badges"]:
                dots_total += 1
                if not box or not (box["l"] - 4 <= q["x"] <= box["r"] + 4 and
                                   box["t"] - 4 <= q["y"] <= box["b"] + 4):
                    dots_bad += 1
    b.close()

print(f"callout dots       : {dots_total} checked, {dots_bad} off artwork  "
      f"{'OK' if dots_bad == 0 else 'FAIL'}")
if dots_bad: fails.append("callout dot off artwork")
print(f"clipped windows    : {clipped}  {'OK' if clipped == 0 else 'FAIL'}")
if clipped: fails.append("clipped elements")

# --- 5. colours: every var(--x) must be defined ---
defined = set(re.findall(r"--([a-z0-9-]+)\s*:", src))
used = set(re.findall(r"var\(--([a-z0-9-]+)", src))
missing = sorted(used - defined)
print(f"undefined colours  : {len(missing)}  {'OK' if not missing else 'FAIL ' + str(missing)}")
if missing: fails.append("undefined colour vars")

# --- 6. motion: something must actually change between frames ---
import io as _io
with sync_playwright() as p:
    b = p.chromium.launch(); pg = b.new_page(viewport={"width": 1920, "height": 1080})
    pg.goto("file:///" + html.replace("\\", "/")); pg.wait_for_timeout(600)
    pg.evaluate("""()=>{document.body.classList.add('render');
      const vo=document.getElementById('vo'); window.__T=0;
      Object.defineProperty(vo,'currentTime',{get:()=>window.__T,set:v=>{}});}""")
    sc3 = pg.evaluate("window.EPISODE.scenes")
    moved = []
    for i, x in enumerate(sc3):
        base = x["s"] + (x["e"] - x["s"]) * 0.5
        shots = []
        for t in (base, base + 1.0):
            pg.evaluate("t=>{window.__T=t;window.renderAt(t);}", t); pg.wait_for_timeout(70)
            shots.append(Image.open(_io.BytesIO(pg.screenshot())).convert("RGB"))
        d = ImageChops.difference(shots[0], shots[1]).convert("L")
        if sum(d.getdata()) / (d.width * d.height) > 0.08:
            moved.append(i + 1)
    b.close()

print(f"windows with motion : {len(moved)}/{len(sc3)}  "
      f"{'OK' if len(moved) >= len(sc3) * 0.6 else 'FAIL (too static)'}")
if len(moved) < len(sc3) * 0.6: fails.append("too few windows animate")

print()
print("RESULT:", "PASS" if not fails else "FAIL -> " + "; ".join(fails))
