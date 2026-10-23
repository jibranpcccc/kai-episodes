import os,subprocess
from PIL import Image, ImageDraw, ImageFont
ROOT=r"C:\Users\jibra\Desktop\1\KAI"; CHROME=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
def build(T):
    return ("<style>*{transition:none!important}</style>"
            "<script>setTimeout(function(){var vo=document.getElementById('vo');"
            "try{vo.play=function(){return Promise.resolve();};}catch(e){}"
            f"try{{Object.defineProperty(vo,'currentTime',{{get:function(){{return {T};}},set:function(){{}}}});}}catch(e){{}}"
            f"window.renderAt({T});document.getElementById('start').click();}},250);</script>")
src=open(os.path.join(ROOT,"BYTE-02.html"),encoding="utf-8").read()
shots=[(17,"hook-art"),(48,"hook2-chip"),(80,"rule-chip"),(105,"file-bars"),(128,"cache-grid"),(185,"vram-gpu"),(240,"prefill-arrow"),(300,"speed-gpu"),(370,"twocard"),(415,"close-chip")]
tiles=[]
for T,tag in shots:
    tmp=os.path.join(ROOT,f"_a_{tag}.html"); open(tmp,"w",encoding="utf-8").write(src.replace("</body>",build(T)+"\n</body>"))
    out=os.path.join(ROOT,"proof",f"art_{tag}.png")
    if os.path.exists(out): os.remove(out)
    subprocess.run([CHROME,"--headless=new","--disable-gpu","--no-sandbox","--hide-scrollbars",
        "--force-device-scale-factor=1","--window-size=1280,720","--virtual-time-budget=3000",
        f"--screenshot={out}","file:///"+tmp.replace("\\","/")],capture_output=True)
    os.remove(tmp)
    if os.path.exists(out):
        im=Image.open(out).convert("RGB"); px=im.load(); W,H=im.size
        b=sum(1 for y in range(0,H,3) for x in range(0,W,3) if sum(px[x,y])>330)
        tiles.append((f"{T}s {tag}", im.resize((620,349),Image.LANCZOS), b))
def f(s):
    for n in ["seguisb.ttf","arialbd.ttf"]:
        try: return ImageFont.truetype(n,s)
        except: pass
    return ImageFont.load_default()
cols=2; rows=(len(tiles)+1)//2
c=Image.new("RGB",(cols*626+6, rows*(349+24)+6),(22,22,26)); d=ImageDraw.Draw(c)
for i,(lab,im,b) in enumerate(tiles):
    x=3+(i%cols)*626; y=3+(i//cols)*(349+24)
    c.paste(im,(x,y+20)); d.text((x+4,y+3),lab,font=f(12),fill=(120,255,180))
c.save(os.path.join(ROOT,"proof","byte2_art.jpg"),quality=88)
print("ok", c.size)
