import os, subprocess
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
src=open(os.path.join(ROOT,"EPISODE.html"),encoding="utf-8").read()
chrome=r"C:\Program Files\Google\Chrome\Application\chrome.exe"
shots=[
 (0,"s1",".strike{width:112%!important}"),
 (1,"s2",".seg-w{width:58%!important}.seg-k{width:42%!important}"),
 (2,"s3",".seg-w{width:58%!important}.seg-k{width:42%!important}.spill-pour{height:86px!important}"),
 (3,"s4","#needle{transform:translateX(-50%) rotate(-82.8deg)!important}"),
 (4,"s5",""),
 (5,"s6",".hfill{width:var(--w)!important}"),
 (6,"s7",""),
]
for n,name,extra in shots:
    dbg=src.replace("</style>",
        "#start{display:none!important}"
        ".scene{opacity:1!important;visibility:visible!important}"
        "[data-in]{opacity:1!important;transform:none!important}"
        f".scene:not([data-scene=\"{n}\"]){{display:none!important}}"
        + extra + "</style>",1)
    if n==3: dbg=dbg.replace('<span class="gnum" id="toknum">40</span>','<span class="gnum" id="toknum">4</span>')
    if n==1: dbg=dbg.replace('<span class="n" id="ctxnum">1K</span>','<span class="n" id="ctxnum">32K</span>')
    p=os.path.join(ROOT,f"_dbg_{name}.html")   # ROOT so core/kai.css resolves
    open(p,"w",encoding="utf-8").write(dbg)
    out=os.path.join(ROOT,"proof",f"frame_{name}.png")
    if os.path.exists(out): os.remove(out)
    subprocess.run([chrome,"--headless=new","--disable-gpu","--no-sandbox","--hide-scrollbars",
                    "--force-device-scale-factor=1","--window-size=1920,1080",
                    f"--screenshot={out}","file:///"+p.replace("\\","/")],capture_output=True)
    os.remove(p)
    print(name,"ok" if os.path.exists(out) else "FAIL")
