import re,os,subprocess
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
html=open(os.path.join(ROOT,"EPISODE.html"),encoding="utf-8").read()
js="\n".join(re.findall(r"<script>(.*?)</script>", html, re.S))
p=os.path.join(ROOT,"data","_c.js"); open(p,"w",encoding="utf-8").write(js)
r=subprocess.run(["node","--check",p],capture_output=True,text=True)
print("node --check:", "PASS" if r.returncode==0 else "FAIL\n"+r.stderr[:400]); os.remove(p)
# count cues actually wired
print("data-in cues :", len(re.findall(r'data-in="', html)))
print("JS thresholds:", len(re.findall(r"!fired\.has\('", html)))
print("SFX cues     :", len(re.findall(r"\{t:[0-9.]+, f:'", html)))
print("wipes        :", re.search(r"const WIPES = \[[0-9., ]+\];",html).group(0))
print("TOTAL        :", re.search(r"const TOTAL = [0-9.]+;",html).group(0))
for m in re.findall(r'(?:href|src)="([^"]+)"', html):
    if not m.startswith("http"):
        print(("  OK   " if os.path.exists(os.path.join(ROOT,m.replace("/",os.sep))) else "  MISS ")+m)
