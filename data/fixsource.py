import re,os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"

# ---------- core/player.css : the ONE place layout lives ----------
p=os.path.join(ROOT,"core","player.css")
s=open(p,encoding="utf-8").read()
s=s.replace("html,body{height:100%;margin:0;background:#000;overflow:hidden;font-family:var(--sans)}",
            "html,body{height:100%;margin:0;background:#000;overflow:auto;font-family:var(--sans)}")
s=re.sub(r"#wrap\{[^}]*\}",
         "#wrap{position:relative;width:1280px;height:720px;margin:0 auto;overflow:hidden;background:#000}", s)
s=re.sub(r"#stage\{[^}]*\}",
         "#stage{width:1920px;height:1080px;position:absolute;left:0;top:0;"
         "transform:scale(0.666667);transform-origin:0 0;"
         "background:var(--black);overflow:hidden;color:var(--white);font-family:var(--mono)}", s)
if "@media (min-width:1600px)" not in s:
    s += ("\n/* bigger box on big screens - fixed numbers only, no calc division */\n"
          "@media (min-width:1600px) and (min-height:940px){\n"
          "  #wrap{width:1600px;height:900px}\n"
          "  #wrap #stage{transform:scale(0.833333)}\n"
          "}\n")
open(p,"w",encoding="utf-8").write(s)
print("player.css: fixed-size layout written to source")

# ---------- core/player.js : never hide the page if audio cannot start ----------
p=os.path.join(ROOT,"core","player.js")
s=open(p,encoding="utf-8").read()
old="""  function begin() {
    reset();
    startEl.classList.add('hide');
    audio.currentTime = 0;
    audio.play().then(() => { playing = true; loop(); })
         .catch(() => { cueEl.textContent = 'AUDIO BLOCKED — click again'; });
  }"""
new="""  function begin() {
    reset();
    startEl.classList.add('hide');
    audio.currentTime = 0;
    const p = audio.play();
    if (p && p.then) {
      p.then(() => { playing = true; loop(); })
       .catch(() => { startEl.classList.remove('hide');
                      startEl.querySelector('.meta').textContent = 'CLICK AGAIN TO START AUDIO'; });
    } else { playing = true; loop(); }
  }"""
assert old in s, "begin() not found"
s=s.replace(old,new)
open(p,"w",encoding="utf-8").write(s)
print("player.js: playback failure no longer blanks the page")
