import os,subprocess
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
chrome=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
src=open(os.path.join(ROOT,"episodes","ep02","index.html"),encoding="utf-8").read()
inj="""<script>
document.getElementById('start').style.display='none';
['hud','tc','cue'].forEach(function(i){var e=document.getElementById(i); if(e)e.style.display='none';});
var S=document.querySelectorAll('.scene')[3];
S.classList.add('active');
S.querySelectorAll('[data-in]').forEach(function(e){e.classList.add('on');});
S.querySelectorAll('.grow').forEach(function(e){e.classList.add('on');});
</script>"""
p=os.path.join(ROOT,"episodes","ep02","_qa_fit.html")
open(p,"w",encoding="utf-8").write(src.replace("</body>",inj+"\n</body>"))
out=os.path.join(ROOT,"proof","scene_fit_1200x800.png")
subprocess.run([chrome,"--headless=new","--disable-gpu","--no-sandbox","--hide-scrollbars",
  "--force-device-scale-factor=1","--window-size=1200,800",f"--screenshot={out}",
  "file:///"+p.replace("\\","/")],capture_output=True)
os.remove(p)
print("ok" if os.path.exists(out) else "FAIL")
