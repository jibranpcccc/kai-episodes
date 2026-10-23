import re
p=r"C:\Users\jibra\Desktop\1\KAI\data\make_episodes.py"
s=open(p,encoding="utf-8").read()
print("CRLF present:", "\r\n" in s)
s=s.replace("\r\n","\n")
open(p,"w",encoding="utf-8",newline="\n").write(s)
print("normalised to LF")
