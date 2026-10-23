import re
p=r"C:\Users\jibra\Desktop\1\KAI\data\make_episodes.py"
s=open(p,encoding="utf-8").read().replace("\r\n","\n")

# 1. fix the phrase so it matches the spoken line
s=s.replace("'row3':'Run it round'", "'row3':'Run it flat out'")

# 2. a phrase that is not in the script must fail loudly, never silently snap to 0
old = '''    p = text.lower().find(phrase.lower())
    if p < 0:
        return words[0][0] if words else 0.0'''
new = '''    p = text.lower().find(phrase.lower())
    if p < 0:
        raise ValueError(f"cue phrase not found in script: {phrase!r}")'''
assert old in s, "phrase_time fallback not found"
s=s.replace(old,new)
open(p,"w",encoding="utf-8",newline="\n").write(s)
print("cue fixed + phrase matching now strict")
