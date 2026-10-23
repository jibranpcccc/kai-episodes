import os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
p=os.path.join(ROOT,"core","player.css")
s=open(p,encoding="utf-8").read()
s=s.replace("body.render [data-in]{opacity:1}\n","")
open(p,"w",encoding="utf-8").write(s)

p=os.path.join(ROOT,"core","player.js")
s=open(p,encoding="utf-8").read()
old="  if (new URLSearchParams(location.search).has('t')) document.body.classList.add('render');"
new=("  const _q = new URLSearchParams(location.search);\n"
     "  if (_q.has('t')) { document.body.classList.add('render'); }\n")
assert old in s
s=s.replace(old,new)
# call it once everything is defined
anchor="\n  startEl.addEventListener('click'"
assert anchor in s
call = """
  if (_q.has('t')) {
    const _t = parseFloat(_q.get('t')) || 0;
    requestAnimationFrame(() => window.renderAt(_t));
  }
"""
s=s.replace(anchor, call + anchor, 1)
open(p,"w",encoding="utf-8").write(s)
print("auto-render on ?t= added")
