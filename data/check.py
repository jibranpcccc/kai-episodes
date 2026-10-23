import re, os, subprocess
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
html=open(os.path.join(ROOT,"EPISODE.html"),encoding="utf-8").read()
blocks=re.findall(r"<script>(.*?)</script>", html, re.S)
print("script blocks:", len(blocks))
js="\n".join(blocks)
p=os.path.join(ROOT,"data","_check.js")
open(p,"w",encoding="utf-8").write(js)
r=subprocess.run(["node","--check",p],capture_output=True,text=True)
print("node --check:", "PASS" if r.returncode==0 else "FAIL")
if r.returncode: print(r.stderr[:900])
# asset references
import glob
for m in re.findall(r'(?:href|src)="([^"]+)"', html):
    if m.startswith("http"): continue
    ok=os.path.exists(os.path.join(ROOT,m.replace("/",os.sep)))
    print(("  OK   " if ok else "  MISS ")+m)
