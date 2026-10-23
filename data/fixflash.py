import re, os
P=r"C:\Users\jibra\Desktop\1\KAI\EPISODE.html"
h=open(P,encoding="utf-8").read()

# 1) scene swap: no fade, so the outgoing frame can never linger
old_css=".scene{position:absolute;inset:0;opacity:0;visibility:hidden;transition:opacity .24s ease}"
new_css=".scene{position:absolute;inset:0;opacity:0;visibility:hidden}"
assert old_css in h, "css not found"
h=h.replace(old_css,new_css)

# 2) scene index: hold the previous scene through the gap instead of falling back to scene 1
old_js="""  // active scene
  let idx=SCENES.findIndex(s=>t>=s.s && t<s.e);
  if(idx<0) idx = t>=SCENES[SCENES.length-1].e ? SCENES.length-1 : 0;"""
new_js="""  // active scene — clamp to the last scene that has started.
  // (findIndex returns -1 inside the 0.25s gap between cuts, which used to
  //  fall back to scene 0 and flash the hook after every slide)
  let idx=0;
  for(let i=0;i<SCENES.length;i++){ if(t>=SCENES[i].s) idx=i; }"""
assert old_js in h, "js not found"
h=h.replace(old_js,new_js)

open(P,"w",encoding="utf-8").write(h)
print("patched: hard cut + gap-safe index")
