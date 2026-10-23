p=r"C:\Users\jibra\Desktop\1\KAI\data\make_episodes.py"
s=open(p,encoding="utf-8").read().replace("\r\n","\n")
# transforms on [data-in] elements get overridden by .on{transform:none} — use margins
s=s.replace(".ruler{{position:absolute;left:50%;transform:translateX(-50%);bottom:158px;width:1100px;height:74px}}",
            ".ruler{{position:absolute;left:0;right:0;margin:0 auto;bottom:158px;width:1100px;height:74px}}")
s=s.replace(".spark{{position:absolute;left:50%;transform:translateX(-50%);bottom:72px;width:520px;height:220px}}",
            ".spark{{position:absolute;left:0;right:0;margin:0 auto;bottom:72px;width:520px;height:220px}}")
s=s.replace(".ring{{position:absolute;right:120px;top:50%;transform:translateY(-50%);width:200px;height:200px}}",
            ".ring{{position:absolute;right:120px;top:50%;margin-top:-100px;width:200px;height:200px}}")
open(p,"w",encoding="utf-8",newline="\n").write(s)
print("centred with margins (no transform)")
