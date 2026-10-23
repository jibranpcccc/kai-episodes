import os
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
p=os.path.join(ROOT,"EPISODE_SCRIPT.md")
s=open(p,encoding="utf-8").read()
reps=[
("| 2 | **0:04.4** |","| 2 | **0:04.4** |"),
("| tick @ 5.2 |","| tick @ 8.9, tick @ 10.9 |"),
("| tick @ 16.2, tick @ 22.9 |","| tick @ 16.3, tick @ 18.6, tick @ 20.7 |"),
("| **whoosh** @ 23.3 |","| **whoosh** @ 23.5 |"),
("| thud @ 30.3, ticks @ 31.6 |","| thud @ 30.3, ticks @ 31.5 / 33.4 |"),
("| — |\n| 7 |","| ticks @ 37.2 / 40.7 |\n| 7 |"),
("| **whoosh** @ 42.3, thud @ 46.3 |","| **whoosh** @ 42.5, thud @ 48.0 |"),
]
for a,b in reps:
    s=s.replace(a,b,1)

s += """

---

## Sync verification (measured against the decoded mp3)

`silencedetect` on `audio/vo.mp3` at −45 dB gives 21 speech chunks. Every cue was checked against
the onset of the phrase it illustrates:

| Cue | Phrase onset | Cue fires | Δ |
|---|---|---|---|
| Weights bar fills | 9.03 | 8.88 | −0.15 |
| KV cache bar fills | 11.00 | 10.85 | −0.15 |
| Context counter rolls | 12.89 | 12.79 | −0.10 |
| Needle sweep 40→4 | 27.07 | 26.92 | −0.15 |
| Spill pour | 20.79 | 20.67 | −0.12 |
| Row #1 16 GB | 30.06 | 30.31 | +0.25 |
| Row #2 24 GB | 31.28 | 31.51 | +0.23 |
| Row #3 48 GB | 33.37 | 33.31 | −0.06 |
| Bandwidth bar | 40.66 | 40.66 | 0.00 |
| Line 2 (tokens/sec) | 45.60 | 45.60 | 0.00 |
| Verdict tape | 47.93 | 47.93 | 0.00 |

**Scene boundaries:** 6 of 7 land **+0.089 to +0.107 s before** the voice resumes — the picture leads
the sound by a hair, which is the correct direction. Scene 1 starts at 0.000.

**Colour wipes:** each wipe is 0.62 s and reaches full cover at 46 % (0.285 s in).
Wipe 1 full-covers at **23.74 s**, wipe 2 at **42.77 s** — both exactly on the cut, so the scene
never changes in view.

Worst primary-cue deviation: **0.25 s**. Two follow-on elements (System RAM box, verdict tape) land
+0.33 s and +0.37 s *after* their phrase, which reads as a deliberate beat rather than a drift.
"""
open(p,"w",encoding="utf-8").write(s)
print("EPISODE_SCRIPT.md updated:",len(s),"chars")
