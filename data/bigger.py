import os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
OLD='#wrap{position:relative;width:1280px;height:720px;margin:0 auto;overflow:hidden;background:#000}'
NEW=('#wrap{position:relative;width:1280px;height:720px;margin:0 auto;overflow:hidden;background:#000}\n'
     '/* bigger box on big screens - fixed numbers only, no calc division */\n'
     '@media (min-width:1600px) and (min-height:940px){\n'
     '  #wrap{width:1600px;height:900px}\n'
     '  #wrap #stage{transform:scale(0.833333)}\n'
     '}')
for f in ["EPISODE.html","EPISODE-02.html","EPISODE-03.html"]:
    p=os.path.join(ROOT,f); s=open(p,encoding="utf-8").read()
    if OLD not in s: print("MISS",f); continue
    s=s.replace(OLD,NEW,1)
    open(p,"w",encoding="utf-8").write(s)
    print(f"{f}: responsive box added")
