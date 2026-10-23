p=r"C:\Users\jibra\Desktop\1\KAI\data\make_episodes.py"
s=open(p,encoding="utf-8").read()
reps=[
 # VO: idle is 16h, not 24
 ('It still draws ninety watts, all day, whether you\'re using it or not.',
  'It still draws ninety watts for the other sixteen hours, whether you\'re using it or not.'),
 # VO: corrected middle number
 ('Load only, two hundred and ten dollars. Leave it idling, four hundred and twelve. Run it round the clock, six hundred and thirty one.',
  'Load only, two hundred and ten dollars. Add the idle hours, two hundred and ninety four. Run it flat out round the clock, six hundred and thirty one.'),
 # cue phrase follows the new line
 ("'row2':'Leave it idling'","'row2':'Add the idle hours'"),
 # on-screen numbers
 ('<div class="n red" style="font-size:168px" data-in="@bill@">$412</div>',
  '<div class="n red" style="font-size:168px" data-in="@bill@">$294</div>'),
 ('<span class="row__name">Plus idle</span><span class="row__val">$412</span>',
  '<span class="row__name">Plus idle</span><span class="row__val">$294</span>'),
 ('Idle runs 24 h a day','Idle runs the other 16 h'),
]
for a,b in reps:
    if a not in s: print("NOT FOUND:", a[:60])
    s=s.replace(a,b)
open(p,"w",encoding="utf-8").write(s)
print("patched ep02 numbers")
