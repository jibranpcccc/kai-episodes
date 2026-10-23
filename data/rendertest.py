import os,re,subprocess
from PIL import Image
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
chrome=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
def lit(path):
    im=Image.open(path).convert("RGB"); px=im.load(); n=0
    for y in range(0,im.height,3):
        for x in range(0,im.width,3):
            r,g,b=px[x,y]
            if r+g+b>40: n+=1
    return n
for f in ["EPISODE.html","EPISODE-02.html","EPISODE-03.html"]:
    src=open(os.path.join(ROOT,f),encoding="utf-8").read()
    # with JS
    out1=os.path.join(ROOT,"proof",f"t_{f}.png")
    subprocess.run([chrome,"--headless=new","--disable-gpu","--no-sandbox","--hide-scrollbars",
      "--force-device-scale-factor=1","--window-size=1200,800","--virtual-time-budget=2500",
      f"--screenshot={out1}","file:///"+os.path.join(ROOT,f).replace("\\","/")],capture_output=True)
    # without JS: strip every <script> block
    nojs=re.sub(r"<script[^>]*>.*?</script>","",src,flags=re.S)
    tmp=os.path.join(ROOT,"_nojs.html"); open(tmp,"w",encoding="utf-8").write(nojs)
    out2=os.path.join(ROOT,"proof",f"t_nojs_{f}.png")
    subprocess.run([chrome,"--headless=new","--disable-gpu","--no-sandbox","--hide-scrollbars",
      "--force-device-scale-factor=1","--window-size=1200,800",
      f"--screenshot={out2}","file:///"+tmp.replace("\\","/")],capture_output=True)
    os.remove(tmp)
    a=lit(out1); b=lit(out2)
    print(f"{f:18} with JS: {a:6d} lit   no JS: {b:6d} lit   -> {'OK' if a>500 and b>500 else 'BLANK!'}")
