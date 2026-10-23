import re,os,base64
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
p=os.path.join(ROOT,"data","build_standalone.py")
s=open(p,encoding="utf-8").read()

old = '''    epjs = epjs.replace("../../audio/", "audio/")
    epjs = epjs.replace('vo: "audio/vo.mp3"', 'vo: "%s"' % vo)'''
new = '''    epjs = epjs.replace("../../audio/", "audio/")

    # embed the voiceover so there is no external file to go stale or be cached
    apath = os.path.join(ROOT, vo.replace("/", os.sep))
    b64 = base64.b64encode(open(apath, "rb").read()).decode()
    epjs = epjs.replace('vo: "audio/vo.mp3"',
                        'vo: "data:audio/mpeg;base64,' + b64 + '"')
    print(f"   embedded voiceover {os.path.basename(apath)} ({len(b64)//1024} KB base64)")'''
assert old in s, "vo replacement block not found"
s = s.replace(old, new)
if "import base64" not in s:
    s = s.replace("import re, os", "import re, os, base64", 1)
open(p,"w",encoding="utf-8").write(s)
print("build_standalone will embed the audio")
