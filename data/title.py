import re, os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"; P=os.path.join(ROOT,"EPISODE.html")
h=open(P,encoding="utf-8").read()
h=re.sub(r"<title>.*?</title>","<title>The VRAM Lie — 43s episode (HTML cut)</title>",h)
h=re.sub(r'<div id="tc">[^<]+</div>','<div id="tc">0.0 / 42.7</div>',h)
open(P,"w",encoding="utf-8").write(h)
print("title/tc:", re.search(r"<title>.*?</title>",h).group(0),
      "|", re.search(r'<div id="tc">[^<]+</div>',h).group(0))
print("overlay:", re.search(r'Episode 01[^<]+',h).group(0))
