import os,subprocess,re
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
CHROME=r"C:\Program Files\Google\Chrome\Application\chrome.exe"

HARNESS = """<script>
(function(){
  var log=[];
  try{
    var vo=document.getElementById('vo');
    try{ vo.play=function(){return Promise.resolve();}; log.push('play-stubbed'); }catch(e){ log.push('play-stub-FAIL'); }
    var T=0;
    try{ Object.defineProperty(vo,'currentTime',{get:function(){return T;},set:function(v){T=v;}}); log.push('clock-ok'); }
    catch(e){ log.push('clock-FAIL:'+e.name); }
    document.getElementById('start').click();
    // advance the clock in steps that virtual time will chew through
    var n=0;
    var iv=setInterval(function(){ T+=0.25; n++; if(n>200) clearInterval(iv); }, 20);
    setTimeout(function(){
      var on=document.querySelectorAll('[data-in].on').length;
      var act=document.querySelectorAll('.scene.active').length;
      var tot=document.querySelectorAll('[data-in]').length;
      document.title='RESULT on='+on+'/'+tot+' active='+act+' t='+T.toFixed(1)+' '+log.join(',');
    }, 1500);
  }catch(e){ document.title='RESULT error='+e.message; }
})();
</script>"""

for f,tag in [("EPISODE-02.html","ep02"),("EPISODE-03.html","ep03")]:
    src=open(os.path.join(ROOT,f),encoding="utf-8").read()
    tmp=os.path.join(ROOT,f"_{tag}_dom.html")
    open(tmp,"w",encoding="utf-8").write(src.replace("</body>",HARNESS+"\n</body>"))
    r=subprocess.run([CHROME,"--headless=new","--disable-gpu","--no-sandbox",
        "--virtual-time-budget=6000","--dump-dom","file:///"+tmp.replace("\\","/")],
        capture_output=True,text=True,encoding="utf-8",errors="ignore")
    os.remove(tmp)
    m=re.search(r"<title>(RESULT[^<]*)</title>", r.stdout or "")
    print(f"{f:18} {m.group(1) if m else 'NO RESULT (title unchanged)'}")
