import os,re
ROOT=r"C:\Users\jibra\Desktop\1\KAI"

WRAP_OLD = "#wrap{position:fixed;inset:0;overflow:hidden}"
WRAP_NEW = ("#wrap{position:fixed;inset:0;display:flex;align-items:center;justify-content:center;"
            "overflow:hidden}")
STAGE_OLD = "#stage{width:1920px;height:1080px;position:absolute;left:0;top:0;transform-origin:0 0;"
STAGE_NEW = ("#stage{width:1920px;height:1080px;position:relative;"
             "zoom:min(calc(100vw / 1920px), calc(100vh / 1080px));")

FIT_OLD_A = """  const fit = () => {
    const k = Math.min(innerWidth / 1920, innerHeight / 1080);
    stage.style.transformOrigin = '0 0';
    stage.style.left = Math.max(0, (innerWidth  - 1920 * k) / 2) + 'px';
    stage.style.top  = Math.max(0, (innerHeight - 1080 * k) / 2) + 'px';
    stage.style.transform = 'scale(' + k + ')';
  };"""
FIT_NEW_A = "  const fit = () => {};   /* scaling is pure CSS now */"

FIT_OLD_B = """function fit(){
  const k=Math.min(innerWidth/1920, innerHeight/1080);
  stage.style.transformOrigin='0 0';
  stage.style.left=Math.max(0,(innerWidth -1920*k)/2)+'px';
  stage.style.top =Math.max(0,(innerHeight-1080*k)/2)+'px';
  stage.style.transform='scale('+k+')';
}"""
FIT_NEW_B = "function fit(){}   /* scaling is pure CSS now */"

# core files (for future builds)
for f in ["core/player.css","core/player.js"]:
    p=os.path.join(ROOT,f); s=open(p,encoding="utf-8").read()
    s=s.replace(WRAP_OLD,WRAP_NEW).replace(STAGE_OLD,STAGE_NEW).replace(FIT_OLD_A,FIT_NEW_A)
    open(p,"w",encoding="utf-8").write(s)

for f in ["EPISODE.html","EPISODE-02.html","EPISODE-03.html"]:
    p=os.path.join(ROOT,f); s=open(p,encoding="utf-8").read()
    n=0
    for a,b in [(WRAP_OLD,WRAP_NEW),(STAGE_OLD,STAGE_NEW),(FIT_OLD_A,FIT_NEW_A),(FIT_OLD_B,FIT_NEW_B)]:
        if a in s: s=s.replace(a,b); n+=1
    open(p,"w",encoding="utf-8").write(s)
    print(f"{f}: {n}/4 substitutions")
