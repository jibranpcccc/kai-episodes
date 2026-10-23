import re
p=r"C:\Users\jibra\Desktop\1\KAI\data\make_episodes.py"
s=open(p,encoding="utf-8").read()

s=s.replace("GAP   = 0.25","GAP   = 0.25\nTAIL  = 0.7   # hold the end card")

# create + append the tail silence inside render_vo
s=s.replace("""    open(os.path.join(vo_dir,"l.txt"),"w").write("\\n".join(lst))""",
"""    tail = os.path.join(vo_dir,"t.wav")
    subprocess.run(["ffmpeg","-y","-hide_banner","-loglevel","error","-f","lavfi",
                    "-i","anullsrc=r=44100:cl=mono","-t",str(TAIL),"-c:a","pcm_s16le", tail], check=True)
    lst.append(f"file '{(vo_dir+'/t.wav').replace(chr(92),'/')}'")
    open(os.path.join(vo_dir,"l.txt"),"w").write("\\n".join(lst))""")

s=s.replace("    total = sum(d) + GAP*(len(d)-1)","    total = sum(d) + GAP*(len(d)-1) + TAIL")
open(p,"w",encoding="utf-8").write(s)
print("patched tail", "TAIL" in s, s.count("t.wav"))
