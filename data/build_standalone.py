import re, os, base64, shutil

ROOT = r"C:\Users\jibra\Desktop\1\KAI"

kai   = open(os.path.join(ROOT,"core","kai.css"),encoding="utf-8").read()
pcss  = open(os.path.join(ROOT,"core","player.css"),encoding="utf-8").read()
pjs   = open(os.path.join(ROOT,"core","player.js"),encoding="utf-8").read()

# fonts are in core/fonts — rewrite so an inlined stylesheet still finds them
kai = kai.replace('url("fonts/', 'url("core/fonts/')

FALLBACK = """
/* ---- no-JS safety net: never show a blank page ---- */
.no-js #start{display:none!important}
.no-js .scene:first-of-type{opacity:1!important;visibility:visible!important}
.no-js [data-in]{opacity:1!important;transform:none!important}
.no-js .grow{width:var(--w)!important}
"""

NOJS_BOOT = '<script>document.documentElement.classList.remove("no-js");</script>'

def no_jsify(html):
    html = html.replace('<html lang="en">', '<html lang="en" class="no-js">', 1)
    html = re.sub(r'(<body[^>]*>)', r'\1\n' + NOJS_BOOT, html, count=1)
    return html

# ------------------------------------------------------------------ EP 01
src = open(os.path.join(ROOT,"EPISODE.html"),encoding="utf-8").read()
out = src.replace('<link rel="stylesheet" href="core/kai.css">', '<style>\n'+kai+'\n'+FALLBACK+'\n</style>', 1)
out = no_jsify(out)
open(os.path.join(ROOT,"EPISODE.html"),"w",encoding="utf-8").write(out)
print("EPISODE.html          inlined, self-contained")

# ------------------------------------------------------------- EP 02 / 03
for ep, dst, vo in [("ep02","EPISODE-02.html","audio/ep02_vo.mp3"),
                    ("ep03","EPISODE-03.html","audio/ep03_vo.mp3")]:
    p = os.path.join(ROOT,"episodes",ep,"index.html")
    s = open(p,encoding="utf-8").read()

    title   = re.search(r"<title>(.*?)</title>", s, re.S).group(1)
    epstyle = re.search(r"<style>(.*?)</style>", s, re.S).group(1)
    body    = re.search(r"<body>(.*?)<script>", s, re.S).group(1).strip()
    epjs    = re.search(r"<script>(.*?)</script>", s, re.S).group(1)

    epjs = epjs.replace("../../audio/", "audio/")

    # embed the voiceover so there is no external file to go stale or be cached
    apath = os.path.join(ROOT, vo.replace("/", os.sep))
    b64 = base64.b64encode(open(apath, "rb").read()).decode()
    epjs = epjs.replace('vo: "audio/vo.mp3"',
                        'vo: "data:audio/mpeg;base64,' + b64 + '"')
    print(f"   embedded voiceover {os.path.basename(apath)} ({len(b64)//1024} KB base64)")

    html = f"""<!DOCTYPE html>
<html lang="en" class="no-js">
<head>
<meta charset="utf-8">
<title>{title}</title>
<style>
{kai}
{pcss}
{epstyle}
{FALLBACK}
</style>
</head>
<body>
{NOJS_BOOT}
{body}
<script>
{epjs}
</script>
<script>
{pjs}
</script>
</body>
</html>
"""
    open(os.path.join(ROOT,dst),"w",encoding="utf-8").write(html)
    print(f"{dst:22} inlined, self-contained  ({len(html)//1024} KB)")

# clean up the now-redundant nested folder
shutil.rmtree(os.path.join(ROOT,"episodes"), ignore_errors=True)
print("removed episodes/ folder (audio copied to audio/)")
