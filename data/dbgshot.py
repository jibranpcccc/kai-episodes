import os,subprocess
from PIL import Image
ROOT=r"C:\Users\jibra\Desktop\1\KAI"; CHROME=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
h=("<style>*{transition:none!important}</style><script>setTimeout(function(){"
   "var vo=document.getElementById('vo');vo.play=()=>Promise.resolve();"
   "var t=70;Object.defineProperty(vo,'currentTime',{get:()=>t,set:v=>{}});"
   "window.renderAt(70);document.getElementById('start').click();},250);</script>")
src=open(os.path.join(ROOT,"BYTE-02.html"),encoding="utf-8").read()
tmp=os.path.join(ROOT,"_dbg.html"); open(tmp,"w",encoding="utf-8").write(src.replace("</body>",h+"\n</body>"))
out=os.path.join(ROOT,"proof","debug_overlay.png")
if os.path.exists(out): os.remove(out)
subprocess.run([CHROME,"--headless=new","--disable-gpu","--no-sandbox","--hide-scrollbars",
    "--force-device-scale-factor=1","--window-size=1280,720","--virtual-time-budget=2500",
    f"--screenshot={out}","file:///"+tmp.replace("\\","/")+"?debug=1"],capture_output=True)
os.remove(tmp)
im=Image.open(out).convert("RGB")
print("debug overlay screenshot:", im.size)
