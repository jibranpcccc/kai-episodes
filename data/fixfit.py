import re,os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"

# ---------- 1. player.css : stop grid-centering an oversized element ----------
p=os.path.join(ROOT,"core","player.css")
s=open(p,encoding="utf-8").read()
s=s.replace("#wrap{position:fixed;inset:0;display:grid;place-items:center}",
            "#wrap{position:fixed;inset:0;overflow:hidden}")
s=s.replace("#stage{width:1920px;height:1080px;position:relative;transform-origin:center center;",
            "#stage{width:1920px;height:1080px;position:absolute;left:0;top:0;transform-origin:0 0;")
open(p,"w",encoding="utf-8").write(s)
print("player.css patched")

# ---------- 2. player.js : position the stage explicitly ----------
p=os.path.join(ROOT,"core","player.js")
s=open(p,encoding="utf-8").read()
old="""  const fit = () => {
    const k = Math.min(innerWidth / 1920, innerHeight / 1080);
    stage.style.transform = 'scale(' + k + ')';
  };"""
new="""  const fit = () => {
    const k = Math.min(innerWidth / 1920, innerHeight / 1080);
    stage.style.transformOrigin = '0 0';
    stage.style.left = Math.max(0, (innerWidth  - 1920 * k) / 2) + 'px';
    stage.style.top  = Math.max(0, (innerHeight - 1080 * k) / 2) + 'px';
    stage.style.transform = 'scale(' + k + ')';
  };"""
assert old in s, "player.js fit not found"
s=s.replace(old,new)
open(p,"w",encoding="utf-8").write(s)
print("player.js patched")

# ---------- 3. EPISODE.html : same bug in the inline copy ----------
p=os.path.join(ROOT,"EPISODE.html")
s=open(p,encoding="utf-8").read()
s=s.replace("#wrap{position:fixed;inset:0;display:grid;place-items:center}",
            "#wrap{position:fixed;inset:0;overflow:hidden}")
s=s.replace("#stage{width:1920px;height:1080px;position:relative;transform-origin:center center;",
            "#stage{width:1920px;height:1080px;position:absolute;left:0;top:0;transform-origin:0 0;")
old2="""function fit(){
  const s=Math.min(innerWidth/1920, innerHeight/1080);
  stage.style.transform='scale('+s+')';
}"""
new2="""function fit(){
  const k=Math.min(innerWidth/1920, innerHeight/1080);
  stage.style.transformOrigin='0 0';
  stage.style.left=Math.max(0,(innerWidth -1920*k)/2)+'px';
  stage.style.top =Math.max(0,(innerHeight-1080*k)/2)+'px';
  stage.style.transform='scale('+k+')';
}"""
assert old2 in s, "EPISODE fit not found"
s=s.replace(old2,new2)
open(p,"w",encoding="utf-8").write(s)
print("EPISODE.html patched")
