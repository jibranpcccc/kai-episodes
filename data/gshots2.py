import os,subprocess
from PIL import Image
ROOT=r"C:\Users\jibra\Desktop\1\KAI"; CHROME=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
def build(T):
    return ("<style>*{transition:none!important;animation:none!important}</style>"
            "<script>setTimeout(function(){var vo=document.getElementById('vo');"
            "try{vo.play=function(){return Promise.resolve();};}catch(e){}"
            f"try{{Object.defineProperty(vo,'currentTime',{{get:function(){{return {T};}},set:function(){{}}}});}}catch(e){{}}"
            "document.getElementById('start').click();},200);</script>")
for f,tag,T in [("EPISODE-02.html","ep02",24.0),("EPISODE-03.html","ep03ring",16.6),("EPISODE-03.html","ep03spark",21.2)]:
    src=open(os.path.join(ROOT,f),encoding="utf-8").read()
    tmp=os.path.join(ROOT,f"_{tag}.html"); open(tmp,"w",encoding="utf-8").write(src.replace("</body>",build(T)+"\n</body>"))
    out=os.path.join(ROOT,"proof",f"g_{tag}.png")
    if os.path.exists(out): os.remove(out)
    subprocess.run([CHROME,"--headless=new","--disable-gpu","--no-sandbox","--hide-scrollbars",
        "--force-device-scale-factor=1","--window-size=1280,720","--virtual-time-budget=3000",
        f"--screenshot={out}","file:///"+tmp.replace("\\","/")],capture_output=True)
    os.remove(tmp)
    im=Image.open(out).convert("RGB"); px=im.load(); W,H=im.size
    b=sum(1 for y in range(0,H,2) for x in range(0,W,2) if sum(px[x,y])>330)
    print(f"{tag:10} t={T:5.1f}s bright={b:5d}")
