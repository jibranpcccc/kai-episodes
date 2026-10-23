import os,subprocess
from PIL import Image
ROOT=r"C:\Users\jibra\Desktop\1\KAI"; chrome=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
for f,tag in [("EPISODE-02.html","ep02"),("EPISODE-03.html","ep03")]:
    src=open(os.path.join(ROOT,f),encoding="utf-8").read()
    # only click Play; nothing else is forced
    inj='<script>setTimeout(function(){var s=document.getElementById("start");if(s)s.click();},200);</script>'
    tmp=os.path.join(ROOT,f"_{tag}_live.html")
    open(tmp,"w",encoding="utf-8").write(src.replace("</body>",inj+"\n</body>"))
    out=os.path.join(ROOT,"proof",f"live_{tag}.png")
    if os.path.exists(out): os.remove(out)
    subprocess.run([chrome,"--headless=new","--disable-gpu","--no-sandbox","--hide-scrollbars",
        "--autoplay-policy=no-user-gesture-required","--force-device-scale-factor=1",
        "--window-size=1280,720","--virtual-time-budget=9000",
        f"--screenshot={out}","file:///"+tmp.replace("\\","/")],capture_output=True)
    os.remove(tmp)
    if not os.path.exists(out): print(f,"NO SCREENSHOT"); continue
    im=Image.open(out).convert("RGB"); px=im.load(); W,H=im.size
    bright=sum(1 for y in range(0,H,2) for x in range(0,W,2) if sum(px[x,y])>330)
    print(f"{f:18} live playback -> {W}x{H} bright={bright:5d} {'CONTENT VISIBLE' if bright>400 else 'STILL BLANK'}")
