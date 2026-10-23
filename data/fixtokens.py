import re,os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"

# 1) generator: match the real token form, and REFUSE to write broken output
p=os.path.join(ROOT,"data","make_episodes.py")
s=open(p,encoding="utf-8").read()
old = """        html = re.sub(r'data-in="@(\\w+)"', lambda m: 'data-in="%s"' % rel(m.group(1)), html)"""
new = """        html = re.sub(r'data-in="@(\\w+)@"', lambda m: 'data-in="%s"' % rel(m.group(1)), html)
        leftover = re.findall(r'data-in="([^"]*)"', html)
        bad = [v for v in leftover if not re.fullmatch(r'[0-9.]+', v)]
        assert not bad, f"UNRESOLVED CUES in {spec['id']}: {bad}" """
assert old in s, "generator pattern not found"
s=s.replace(old,new)
open(p,"w",encoding="utf-8").write(s)
print("generator patched + assertion added")

# 2) engine: a bad cue must never hide content again
p=os.path.join(ROOT,"core","player.js")
s=open(p,encoding="utf-8").read()
old="""    if (el) el.querySelectorAll('[data-in]').forEach(n => {
      if (rel >= parseFloat(n.dataset.in)) n.classList.add('on');
    });"""
new="""    if (el) el.querySelectorAll('[data-in]').forEach(n => {
      const d = parseFloat(n.dataset.in);
      // NaN guard: a malformed cue shows the element instead of hiding it forever
      if (!isFinite(d) || rel >= d) n.classList.add('on');
    });"""
assert old in s, "engine pattern not found"
s=s.replace(old,new)
open(p,"w",encoding="utf-8").write(s)
print("engine patched with NaN guard")
