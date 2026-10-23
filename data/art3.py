import os,subprocess
from PIL import Image
ROOT=r"C:\Users\jibra\Desktop\1\KAI"; CHROME=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
def build(T):
    return ("<style>*{transition:none!important}</style><script>setTimeout(function(){"
      "var vo=document.getElementById('vo');vo.play=()=>Promise.resolve();"
      f"Object.defineProperty(vo,'currentTime',{{get:()=>{T},set:v=>{{}}}});"
      f"window.renderAt({T});document.getElementById('start').click();}},250);</script>")
src=open(os.path.join(ROOT,"BYTE-02.html"),encoding="utf-8").read()
for T,tag in [(17,"gpu"),(48,"chip"),(300,"two")]:
    tmp=os.path.join(ROOT,"_c.html"); open(tmp,"w",encoding="utf-8").write(src.replace("</body>",build(T)+"\n</body>"))
    out=os.path.join(ROOT,"proof",f"art3_{tag}.png")
    if os.path.exists(out): os.remove(out)
    subprocess.run([CHROME,"--headless=new","--disable-gpu","--no-sandbox","--hide-scrollbars",
      "--force-device-scale-factor=1","--window-size=1280,720","--virtual-time-budget=3000",
      f"--screenshot={out}","file:///"+tmp.replace("\\","/")],capture_output=True)
    print(tag, "ok")
os.remove(tmp)
