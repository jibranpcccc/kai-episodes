p=r"C:\Users\jibra\Desktop\1\KAI\data\make_episodes.py"
lines=open(p,encoding="utf-8").read().replace("\r\n","\n").split("\n")
for i,l in enumerate(lines):
    if l.strip()=="return d" :
        lines[i]="    return d, WORDS"
        print(f"fixed line {i+1}")
        break
src="\n".join(lines)
assert "boundary=\"WordBoundary\"" in src, "word capture missing!"
assert "WORDS.append" in src, "WORDS append missing!"
open(p,"w",encoding="utf-8",newline="\n").write(src)
print("ok")
