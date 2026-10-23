import re,os,subprocess
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
html=open(os.path.join(ROOT,"EPISODE.html"),encoding="utf-8").read()
js="\n".join(re.findall(r"<script>(.*?)</script>", html, re.S))
p=os.path.join(ROOT,"data","_c.js"); open(p,"w",encoding="utf-8").write(js)
r=subprocess.run(["node","--check",p],capture_output=True,text=True)
print("node --check:", "PASS" if r.returncode==0 else "FAIL\n"+r.stderr[:500]); os.remove(p)
print("SCENES block:")
print(re.search(r"const SCENES = \[.*?\];",html,re.S).group(0))
print("TOTAL:", re.search(r"const TOTAL = [0-9.]+;",html).group(0))
