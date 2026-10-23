p=r"C:\Users\jibra\Desktop\1\KAI\data\make_episodes.py"
s=open(p,encoding="utf-8").read().replace("\r\n","\n")
s=s.replace(".ruler{{position:absolute;left:50%;transform:translateX(-50%);bottom:64px;",
            ".ruler{{position:absolute;left:50%;transform:translateX(-50%);bottom:158px;")
s=s.replace(".spark{{position:absolute;left:50%;transform:translateX(-50%);bottom:52px;",
            ".spark{{position:absolute;left:50%;transform:translateX(-50%);bottom:72px;")
open(p,"w",encoding="utf-8",newline="\n").write(s)
print("ruler raised to bottom:158px, spark raised")
