import re, os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
h=open(os.path.join(ROOT,"EPISODE.html"),encoding="utf-8").read()
starts={0:0.00,1:4.35,2:16.07,3:23.74,4:29.96,5:36.98,6:42.77}
vals={}
for n in range(7):
    m=re.search(r'<section class="scene" data-scene="%d">(.*?)</section>'%n, h, re.S)
    vals[n]=[float(x) for x in re.findall(r'data-in="([0-9.]+)"', m.group(1))]

# (scene, index, label, phrase onset in the audio)
T=[(1,1,"Weights bar fills","The weights are only half.",9.03),
   (1,2,"KV cache bar fills","the other half is the KV cache",11.00),
   (1,3,"Context counter rolls","grows with every token",12.89),
   (2,1,"+6 GB tape","needs six more gigabytes",18.60),
   (2,2,"System RAM box","So the card that fits it",20.79),
   (3,0,"'Tokens per second' caption","It spills into system RAM",23.84),
   (3,1,"'Spilled to RAM' caption","a tenth of the speed",26.20),
   (4,0,"Table caption","Sixteen gigs",30.06),
   (4,1,"Row #1 16 GB","Sixteen gigs",30.06),
   (4,2,"Row #2 24 GB","Twenty-four: fine",31.28),
   (4,3,"Row #3 48 GB","Forty-eight: real work",33.37),
   (5,3,"Bandwidth bar + tape","You're buying bandwidth",40.66),
   (6,0,"Line 1","Stop asking",42.88),
   (6,1,"Line 2","Ask how many tokens",45.60),
   (6,2,"Verdict tape","buy the smallest card",47.93)]

print(f"{'cue':34} {'phrase onset':>12} {'cue time':>9} {'delta':>8}")
print("-"*68)
worst=0
for sc,idx,lab,phrase,onset in T:
    t=starts[sc]+vals[sc][idx]
    d=t-onset
    worst=max(worst,abs(d))
    flag="" if abs(d)<=0.30 else ("  <-- LATE" if d>0 else "  <-- EARLY")
    print(f"{lab:34} {onset:12.2f} {t:9.2f} {d:+8.2f}{flag}")
print("-"*68)
print(f"worst deviation: {worst:.2f}s   (<=0.30s = imperceptible)")

# needle sweep is driven in JS, check it separately
ndl=re.search(r"rel>=([0-9.]+) && !fired.has\('ndl'\)",h).group(1)
print(f"needle sweep cue: {starts[3]+float(ndl):.2f}s  vs 'Forty tokens a second' @ 27.07s  "
      f"({starts[3]+float(ndl)-27.07:+.2f}s)")
pour=re.search(r"rel>=([0-9.]+) && !fired.has\('pour'\)",h).group(1)
print(f"spill pour cue  : {starts[2]+float(pour):.2f}s  vs 'So the card that fits it' @ 20.79s  "
      f"({starts[2]+float(pour)-20.79:+.2f}s)")

# wipes
w=[float(x) for x in re.search(r"const WIPES = \[(.*?)\]",h).group(1).split(",")]
print("\nWIPE / CUT ALIGNMENT  (wipe reaches full cover at start+0.285s)")
for wi,cut in zip(w,[23.74,42.77]):
    print(f"  wipe {wi:.2f}s -> full cover {wi+0.285:.2f}s   cut at {cut:.2f}s   delta {wi+0.285-cut:+.3f}s")
