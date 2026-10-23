p=r"C:\Users\jibra\Desktop\1\KAI\data\wordsync.py"
s=open(p,encoding="utf-8").read()
old=r"cue_t\[tok\] = max\(starts\[i\]+0\.10, min\(est, starts\[i\]\+d\[i\]-0\.15\)\n"
new=r"cue_t\[tok\] = max\(starts\[i\]\+0\.10, min\(est, starts\[i\]\+d\[i\]-0\.15\)\n"
assert old in s, "pattern line not found in patcher"
s=s.replace(old,new)
open(p,"w",encoding="utf-8").write(s)
print("escaped the literal +")
