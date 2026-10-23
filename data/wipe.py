import os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
p=os.path.join(ROOT,"core","player.js")
s=open(p,encoding="utf-8").read()
anchor="    document.getElementById('start').classList.add('hide');\n  };"
assert anchor in s, "renderAt tail not found"
wipe = """    document.getElementById('start').classList.add('hide');
    // colour wipe: replay it analytically so renders match playback
    const wp = (E.wipes || []).find(w => t >= w && t <= w + 0.62);
    if (wp) {
      const pr = (t - wp) / 0.62;
      wipeEl.style.display = 'flex';
      wipeEl.style.transform = 'translateX(' + (-103 + pr * 206) + '%)';
    } else {
      wipeEl.style.display = 'none';
    }
  };"""
s=s.replace(anchor,wipe,1)
open(p,"w",encoding="utf-8").write(s)
print("wipe rendering added to renderAt")
