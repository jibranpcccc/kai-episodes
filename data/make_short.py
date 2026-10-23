"""Derive a vertical 1080x1920 Short from an already-built episode.

    python data/make_short.py BYTE-02.html --scenes 2 --out BYTE-02-SHORT.html

Takes the first N scenes, trims the embedded voiceover to their end, reflows the
layout into a vertical column, and re-embeds everything so the file stands alone.
"""
import argparse, base64, os, re, subprocess, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

VERTICAL_CSS = """
  /* ---------- 9:16 reflow ---------- */
  #wrap, body.render #wrap{width:1080px!important;height:1920px!important;margin:0!important}
  #stage, body.render #stage{width:1080px!important;height:1920px!important;
        transform:none!important;transform-origin:top left}
  .ctr{padding:0 64px;gap:38px}
  .col{width:100%!important;gap:18px!important}
  .split,.split.wide{flex-direction:column!important;width:100%!important;
        gap:34px!important;justify-content:center!important}
  .side{gap:44px!important}
  .float{width:min(78%,640px)!important}
  .big{font-size:210px!important}
  .u{font-size:86px!important}
  .bf-row{width:100%!important;min-height:86px;padding:16px 24px!important}
  .bf-row__k{font-size:26px!important}
  .bf-row__v{font-size:30px!important}
  .bf-bar{width:100%!important}
  .bf-bar__lab{width:190px!important;font-size:16px!important}
  .bf-bar__val{width:170px!important;font-size:26px!important}
  .chip{font-size:17px!important;padding:10px 14px!important}
  .bf-tape{font-size:26px!important;padding:12px 20px!important}
  .bf-big{font-size:58px!important;text-align:center}
  .rail{bottom:110px}
  #hud,#tc,#cue{font-size:14px!important}
"""

FIT_JS = """
<script>
/* preview only: scale the 1080x1920 stage to fit the window */
(function(){
  var wrap = document.getElementById('wrap');
  function fit(){
    if (document.body.classList.contains('render')) { wrap.style.transform='none'; return; }
    var k = Math.min(innerWidth/1080, innerHeight/1920);
    wrap.style.transformOrigin = 'top center';
    wrap.style.transform = 'scale(' + k + ')';
    wrap.style.marginLeft = 'auto';
    wrap.style.marginRight = 'auto';
  }
  addEventListener('resize', fit); fit();
})();
</script>
"""


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("html")
    ap.add_argument("--scenes", type=int, default=2)
    ap.add_argument("--out", required=True)
    a = ap.parse_args()

    src_path = a.html if os.path.isabs(a.html) else os.path.join(ROOT, a.html)
    html = open(src_path, encoding="utf-8").read()

    scenes = [(float(m[0]), float(m[1])) for m in
              re.findall(r"\{s:\s*([0-9.]+),\s*e:\s*([0-9.]+)\}", html)]
    if len(scenes) < a.scenes:
        sys.exit(f"only {len(scenes)} scenes in {src_path}")
    keep = scenes[:a.scenes]
    end = keep[-1][1] + 0.4
    print(f"keeping {a.scenes} scene(s), 0.00 -> {end:.2f}s")

    # trim the embedded voiceover
    m = re.search(r'vo:\s*"data:audio/mpeg;base64,([A-Za-z0-9+/=]+)"', html)
    if not m:
        sys.exit("no embedded audio found")
    audio = base64.b64decode(m.group(1))
    with tempfile.TemporaryDirectory() as td:
        i = os.path.join(td, "in.mp3"); o = os.path.join(td, "out.mp3")
        open(i, "wb").write(audio)
        subprocess.run(["ffmpeg", "-y", "-hide_banner", "-loglevel", "error",
                        "-i", i, "-t", f"{end:.2f}", "-c:a", "libmp3lame",
                        "-b:a", "128k", o], check=True)
        short_b64 = base64.b64encode(open(o, "rb").read()).decode()

    # keep only the sections we want
    sections = re.findall(r'<section class="scene" data-scene="\d+">.*?</section>', html, re.S)
    if len(sections) < a.scenes:
        sys.exit("section count mismatch")
    kept = sections[:a.scenes]
    for k, s in enumerate(kept):
        kept[k] = re.sub(r'data-scene="\d+"', f'data-scene="{k}"', s, count=1)

    scenes_js = ",\n  ".join(f"{{s:{s:5.2f},  e:{e:5.2f}}}" for s, e in keep)

    def grab(key, default="[]"):
        mm = re.search(key + r":\s*(\[[^\]]*\])", html, re.S)
        return mm.group(1) if mm else default

    wipes = ", ".join(f"{w:.3f}" for w in (scenes[1][0] - 0.285,) if w > 0)

    out = re.sub(r'<section class="scene" data-scene="\d+">.*?</section>', "", html, flags=re.S)
    out = out.replace("</style>", VERTICAL_CSS + "\n</style>", 1)
    out = out.replace('<div id="wrap"><div id="stage">',
                      '<div id="wrap"><div id="stage">\n' + "\n".join(kept) + "\n", 1)
    out = re.sub(r'vo:\s*"data:audio/mpeg;base64,[A-Za-z0-9+/=]+"',
                 f'vo: "data:audio/mpeg;base64,{short_b64}"', out, count=1)
    out = re.sub(r"scenes:\s*\[[^\]]*\]", "scenes: [\n  " + scenes_js + "\n  ]", out, count=1)
    out = re.sub(r"total:\s*[0-9.]+", f"total: {end:.2f}", out, count=1)
    out = re.sub(r"wipes:\s*\[[^\]]*\]", f"wipes: [{wipes}]", out, count=1)
    out = re.sub(r"labels:\s*\[[^\]]*\]", "labels: ['HOOK','30B VS 27B']", out, count=1)
    out = out.replace("</body>", FIT_JS + "\n</body>", 1)
    out = out.replace("<title>", "<title>SHORT · ")

    dst = a.out if os.path.isabs(a.out) else os.path.join(ROOT, a.out)
    open(dst, "w", encoding="utf-8").write(out)
    print(f"wrote {dst}  ({len(out)//1024} KB, {end:.1f}s, 1080x1920)")


if __name__ == "__main__":
    main()
