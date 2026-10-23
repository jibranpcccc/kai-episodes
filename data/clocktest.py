import os,subprocess
from PIL import Image
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
CHROME=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
FIREFOX=r"C:\Program Files\Mozilla Firefox\firefox.exe"
PROF=os.path.join(os.environ["TEMP"],"ffqa_profile")

HARNESS = """<script>
setTimeout(function(){
  var vo=document.getElementById('vo');
  try{ vo.play=function(){return Promise.resolve();}; }catch(e){}
  var T=0;
  try{ Object.defineProperty(vo,'currentTime',{get:function(){return T;},set:function(v){T=v;}}); }catch(e){}
  setInterval(function(){ T+=0.05; }, 40);
  var s=document.getElementById('start'); if(s) s.click();
},250);
</script>"""

def bright(p):
    im=Image.open(p).convert("RGB"); px=im.load(); W,H=im.size
    return sum(1 for y in range(0,H,2) for x in range(0,W,2) if sum(px[x,y])>330)

for f,tag in [("EPISODE-02.html","ep02"),("EPISODE-03.html","ep03")]:
    src=open(os.path.join(ROOT,f),encoding="utf-8").read()
    tmp=os.path.join(ROOT,f"_{tag}_clock.html")
    open(tmp,"w",encoding="utf-8").write(src.replace("</body>",HARNESS+"\n</body>"))
    url="file:///"+tmp.replace("\\","/")

    out1=os.path.join(ROOT,"proof",f"clock_chrome_{tag}.png")
    for p in [out1]:
        if os.path.exists(p): os.remove(p)
    subprocess.run([CHROME,"--headless=new","--disable-gpu","--no-sandbox","--hide-scrollbars",
        "--force-device-scale-factor=1","--window-size=1280,720","--virtual-time-budget=4000",
        f"--screenshot={out1}",url],capture_output=True)

    out2=os.path.join(ROOT,"proof",f"clock_ff_{tag}.png")
    if os.path.exists(out2): os.remove(out2)
    p=subprocess.Popen([FIREFOX,"--headless","--no-remote","--profile",PROF,
        "--window-size=1280,720","--screenshot",out2,url],
        stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
    try: p.wait(timeout=45)
    except subprocess.TimeoutExpired: p.kill()

    os.remove(tmp)
    c = bright(out1) if os.path.exists(out1) else -1
    ff= bright(out2) if os.path.exists(out2) else -1
    print(f"{f:18} CHROME bright={c:5d}  FIREFOX bright={ff:5d}   "
          f"{'BOTH OK' if c>400 and ff>400 else 'PROBLEM'}")
