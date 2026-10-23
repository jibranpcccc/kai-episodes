p=r"C:\Users\jibra\Desktop\1\KAI\data\make_episodes.py"
s=open(p,encoding="utf-8").read()
reps=[
 ("align-items:center;justify-content:center;gap:40px;padding:0 120px}}",
  "align-items:center;justify-content:center;gap:64px;padding:0 120px}}"),
 (".stat .u{{font-family:var(--mono);font-size:17px;font-weight:700;letter-spacing:.22em;",
  ".stat .u{{font-family:var(--mono);font-size:19px;font-weight:700;letter-spacing:.20em;"),
 (".col{{display:flex;flex-direction:column;gap:26px;width:1100px}}",
  ".col{{display:flex;flex-direction:column;gap:26px;width:1240px}}"),
 ("""  .node--sel{{border-color:var(--blue);box-shadow:0 0 0 3px rgba(4,94,239,.35);
              background:rgba(4,94,239,.08)}}""",
  """  .node--sel{{border-color:var(--blue);box-shadow:0 0 0 3px rgba(4,94,239,.35);
              background:rgba(4,94,239,.08)}}
  /* scale the chart furniture up to reference density */
  .bar{{height:66px}}
  .bar .bar__track{{height:44px}}
  .bar .bar__lab{{width:210px;font-size:19px}}
  .bar .bar__val{{width:155px;font-size:28px}}
  .prod__frame{{width:252px;height:196px}}
  .prod__cap{{font-size:17px;letter-spacing:.18em}}"""),
 # ep02 hook: bigger numbers, more air
 ('<div style="display:flex;align-items:flex-end;gap:70px">','<div style="display:flex;align-items:flex-end;gap:96px">'),
 ('<div class="n wt" style="font-size:150px" data-in="@paid@">$1,600</div>',
  '<div class="n wt" style="font-size:168px" data-in="@paid@">$1,600</div>'),
 ('<div class="n red" style="font-size:150px" data-in="@bill@">$412</div>',
  '<div class="n red" style="font-size:168px" data-in="@bill@">$412</div>'),
 # ep03 hook: separate the two numbers
 ('<div style="display:flex;align-items:flex-end;gap:110px">','<div style="display:flex;align-items:flex-end;gap:170px">'),
]
for a,b in reps:
    if a not in s: print("NOT FOUND:", a[:70])
    s=s.replace(a,b)
open(p,"w",encoding="utf-8").write(s)
print("patched")
