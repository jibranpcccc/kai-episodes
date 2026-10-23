import os,subprocess
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
chrome=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
JOBS=[("ep02",[0,2,3,4]),("ep03",[0,1,2,3])]
for ep,scenes in JOBS:
    src=open(os.path.join(ROOT,"episodes",ep,"index.html"),encoding="utf-8").read()
    for n in scenes:
        inj=f"""<script>
document.getElementById('start').style.display='none';
['hud','tc','cue'].forEach(function(i){{var e=document.getElementById(i); if(e)e.style.display='none';}});
var S=document.querySelectorAll('.scene')[{n}];
S.classList.add('active');
S.querySelectorAll('[data-in]').forEach(function(e){{e.classList.add('on');}});
S.querySelectorAll('.grow').forEach(function(e){{e.classList.add('on');}});
</script>"""
        dbg=src.replace("</body>", inj+"\n</body>")
        p=os.path.join(ROOT,"episodes",ep,f"_qa{n}.html")
        open(p,"w",encoding="utf-8").write(dbg)
        out=os.path.join(ROOT,"proof",f"{ep}_s{n}.png")
        if os.path.exists(out): os.remove(out)
        subprocess.run([chrome,"--headless=new","--disable-gpu","--no-sandbox","--hide-scrollbars",
                        "--force-device-scale-factor=1","--window-size=1920,1080",
                        f"--screenshot={out}","file:///"+p.replace("\\","/")],capture_output=True)
        os.remove(p)
        print(ep,n,"ok" if os.path.exists(out) else "FAIL")
