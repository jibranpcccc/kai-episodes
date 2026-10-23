import os,re
ROOT=r"C:\Users\jibra\Desktop\1\KAI"

# bulletproof geometry: a plain 1280x720 box with the 1920 stage scaled by a literal 2/3.
# no zoom, no calc, no vw/vh, no flex, no fixed positioning.
OLD_BODY = "html,body{height:100%;margin:0;background:#000;overflow:hidden;font-family:var(--sans)}"
NEW_BODY = "html,body{height:100%;margin:0;background:#000;overflow:auto;font-family:var(--sans)}"

OLD_WRAP = "#wrap{position:fixed;inset:0;display:flex;align-items:center;justify-content:center;overflow:hidden}"
NEW_WRAP = ("#wrap{position:relative;width:1280px;height:720px;margin:0 auto;overflow:hidden;"
            "background:#000}")

OLD_STAGE = ("#stage{width:1920px;height:1080px;position:relative;"
             "zoom:min(calc(100vw / 1920px), calc(100vh / 1080px));")
NEW_STAGE = ("#stage{width:1920px;height:1080px;position:absolute;left:0;top:0;"
             "transform:scale(0.666667);transform-origin:0 0;")

for f in ["EPISODE.html","EPISODE-02.html","EPISODE-03.html"]:
    p=os.path.join(ROOT,f); s=open(p,encoding="utf-8").read()
    hits=0
    for a,b in [(OLD_BODY,NEW_BODY),(OLD_WRAP,NEW_WRAP),(OLD_STAGE,NEW_STAGE)]:
        if a in s: s=s.replace(a,b); hits+=1
        else: print(f"  !! {f}: pattern not found -> {a[:60]}")
    open(p,"w",encoding="utf-8").write(s)
    print(f"{f}: {hits}/3 replacements")
