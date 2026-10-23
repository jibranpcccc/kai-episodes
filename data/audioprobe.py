import os,subprocess,re
ROOT=r"C:\Users\jibra\Desktop\1\KAI"; CHROME=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
PROBE = """<script>
var el=document.getElementById('vo');
function report(v){ document.title='AUDIO '+v; }
el.addEventListener('loadedmetadata',function(){ report('ok dur='+el.duration.toFixed(3)); });
el.addEventListener('error',function(){ report('ERROR code='+(el.error&&el.error.code)); });
setTimeout(function(){ if(!/AUDIO/.test(document.title)) report('timeout rs='+el.readyState+' dur='+el.duration); },2500);
</script>"""
for f in ["EPISODE-02.html","EPISODE-03.html"]:
    src=open(os.path.join(ROOT,f),encoding="utf-8").read()
    tmp=os.path.join(ROOT,"_probe.html"); open(tmp,"w",encoding="utf-8").write(src.replace("</body>",PROBE+"\n</body>"))
    r=subprocess.run([CHROME,"--headless=new","--disable-gpu","--no-sandbox",
        "--virtual-time-budget=6000","--dump-dom","file:///"+tmp.replace("\\","/")],
        capture_output=True,text=True,encoding="utf-8",errors="ignore")
    os.remove(tmp)
    m=re.search(r"<title>(AUDIO[^<]*)</title>", r.stdout or "")
    print(f"  {f:18} {m.group(1) if m else 'no result'}")

h=open(os.path.join(ROOT,"EPISODE.html"),encoding="utf-8").read()
print("\nEPISODE.html  size", len(h)//1024, "KB")
print("  boot scripts :", h.count("classList.remove(\"no-js\")"))
print("  fallback css :", h.count("no-JS safety net"))
print("  style blocks :", h.count("<style>"))
