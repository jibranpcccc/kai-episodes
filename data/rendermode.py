import re,os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"

# ---------- player.css : render-mode chrome ----------
p=os.path.join(ROOT,"core","player.css")
s=open(p,encoding="utf-8").read()
if "body.render" not in s:
    s += """
/* ---------- deterministic render mode (?t=SECONDS) ---------- */
body.render{overflow:hidden;background:#000}
body.render #wrap{width:1920px;height:1080px;margin:0}
body.render #stage{transform:none}
body.render #hud,body.render #tc,body.render #cue,body.render #start{display:none!important}
body.render [data-in],body.render .grow,body.render #wipe{transition:none!important;animation:none!important}
body.render [data-in]{opacity:1}
"""
open(p,"w",encoding="utf-8").write(s)
print("player.css: render mode added")

# ---------- player.js : window.renderAt(t) ----------
p=os.path.join(ROOT,"core","player.js")
s=open(p,encoding="utf-8").read()
if "window.renderAt" not in s:
    hook = """
  /* ---------- deterministic frame renderer (used by CI) ---------- */
  if (new URLSearchParams(location.search).has('t')) document.body.classList.add('render');

  window.renderAt = function (t) {
    let idx = 0;
    for (let i = 0; i < SCENES.length; i++) if (t >= SCENES[i].s) idx = i;
    scenesEl.forEach((sc, k) => sc.classList.toggle('active', k === idx));
    const sc = SCENES[idx], rel = t - sc.s, el = scenesEl[idx];
    if (!el) return;
    el.querySelectorAll('[data-in]').forEach(n => {
      const d = parseFloat(n.dataset.in);
      if (!isFinite(d) || rel >= d) n.classList.add('on');
      else n.classList.remove('on');
    });
    document.getElementById('start').classList.add('hide');
  };
"""
    s = s.replace("\n  startEl.addEventListener('click'", hook + "\n  startEl.addEventListener('click'", 1)
open(p,"w",encoding="utf-8").write(s)
print("player.js: window.renderAt added")
