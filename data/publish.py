import re,os
p=r"C:\Users\jibra\Desktop\1\KAI\data\make_episodes.py"
s=open(p,encoding="utf-8").read().replace("\r\n","\n")

# 1) keep only the 0.04s of lead silence that silenceremove actually keeps
s=s.replace("WORDS.append((t, [(max(0.0, x - lead), w) for x, w in ws]))",
            "WORDS.append((t, [(max(0.0, x - lead + 0.04), w) for x, w in ws]))")

# 2) publish the master audio to the exact file the HTML will load, in the SAME build
anchor = '''    open(os.path.join(folder,"index.html"),"w",encoding="utf-8").write(html)'''
assert anchor in s, "html write anchor not found"
publish = '''    # publish the master audio next to the page it belongs to, and prove they match
    import shutil as _sh
    master = os.path.join(folder, "audio", "vo.mp3")
    pub = os.path.join(ROOT, "audio", spec["id"] + "_vo.mp3")
    os.makedirs(os.path.dirname(pub), exist_ok=True)
    _sh.copyfile(master, pub)
    ad = dur(pub)
    assert abs(ad - total) < 0.08, f"{spec['id']}: audio {ad:.2f}s vs cue timeline {total:.2f}s"
    print(f"   audio published: {pub}  {ad:.2f}s  (cue timeline {total:.2f}s, drift {ad-total:+.3f}s)")
'''
s=s.replace(anchor, publish + anchor, 1)
open(p,"w",encoding="utf-8",newline="\n").write(s)
print("build now publishes audio + asserts the match")
