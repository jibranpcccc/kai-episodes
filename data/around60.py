import os,subprocess
from PIL import Image
ROOT=r"C:\Users\jibra\Desktop\1\KAI"; CHROME=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
def build(T):
    return ("<style>*{transition:none!important;animation:none!important}</style>"
            "<script>setTimeout(function(){var vo=document.getElementById('vo');"
            "try{vo.play=function(){return Promise.resolve();};}catch(e){}"
            f"try{{Object.defineProperty(vo,'currentTime',{{get:function(){{return {T};}},set:function(){{}}}});}}catch(e){{}}"
            f"window.renderAt({T});document.getElementById('start').click();}},250);</script>")
src=open(os.path.join(ROOT,"BYTE-02.html"),encoding="utf-8").read()
for T in [52,54,56,58,60,62,64,66,68]:
    tmp=os.path.join(ROOT,"_z.html"); open(tmp,"w",encoding="utf-8").write(src.replace("</body>",build(T)+"\n</body>"))
    out=os.path.join(ROOT,"proof",f"t{T}.png")
    if os.path.exists(out): os.remove(out)
    subprocess.run([CHROME,"--headless=new","--disable-gpu","--no-sandbox","--hide-scrollbars",
        "--force-device-scale-factor=1","--window-size=1280,720","--virtual-time-budget=2500",
        f"--screenshot={out}","file:///"+tmp.replace("\\","/")],capture_output=True)
    im=Image.open(out).convert("RGB"); px=im.load(); W,H=im.size
    b=sum(1 for y in range(0,H,3) for x in range(0,W,3) if sum(px[x,y])>330)
    print(f"  t={T:3}s  bright={b:5d}  {'BLANK' if b<200 else 'ok'}")
os.remove(tmp)
