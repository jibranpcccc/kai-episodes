doc = r"""# EPISODE 01 — "The VRAM Lie"

**Runtime 42.7s · 7 scenes · faceless · 1080p · voice: en-US-AndrewNeural (+8%)**

Rebuilt from a 51.2s first cut after the voice changed from the Windows desktop synth to a
Microsoft neural voice. Trimming the silence shaved 8.5s — no dead air remains.

---

## The script

| # | In | VO (spoken) | On screen | Sound |
|---|---|---|---|---|
| 1 | **0:00.0** | "Everyone buying a GPU for local AI is measuring the wrong number." | `LOCAL AI · VRAM · 2026` chip. **24 GB** builds, `≠`, then a red **24 GB** struck through. | — |
| 2 | **0:04.1** | "Twenty-four gigabytes of VRAM doesn't run a twenty-four gigabyte model. The weights are only half. The other half is the KV cache — and it grows with every token of context." | One bar splits: **Weights 14 GB** (white, fixed) then **KV cache 10 GB** (azure). Context counter rolls `1K → 32K`. | tick @ 8.4, tick @ 9.8 |
| 3 | **0:14.3** | "A twenty-four gig model at thirty-two K context needs six more gigabytes. So the card that fits it, doesn't." | Yellow **+6 GB** tape. A red pour line drops out of the bar into a dashed **System RAM** box. | ticks @ 14.4 / 17.7 / 18.9 |
| 4 | **0:20.6** | "It spills into system RAM, at a tenth of the speed. Forty tokens a second becomes four." | Needle sweeps hard left; number counts **40 → 4** in red. | **whoosh** @ 20.4 |
| 5 | **0:25.9** | "Sixteen gigs: comfortable at eight K. Twenty-four: fine at thirty-two K. Forty-eight: real work." | Ranked rows land one at a time — `#1 16 GB`, `#2 24 GB`, `#3 48 GB` (selected, blue + crop-marks). | thud @ 26.0, ticks @ 28.5 / 30.8 |
| 6 | **0:32.4** | "Above seventy B, you're not buying VRAM. You're buying bandwidth." | **VRAM 14 GB** (short, azure) vs **Bandwidth 960 GB/s** (long, yellow). Tape: *you're buying bandwidth.* | ticks @ 32.5 / 35.2 |
| 7 | **0:36.2** | "So stop asking how many gigabytes. Ask how many tokens per second you need — and buy the smallest card that still holds your context." | Line 1, line 2, then the verdict tape **BUY THE SMALLEST CARD THAT HOLDS YOUR CONTEXT**. Faint `<yourchannel>`. | **whoosh** @ 35.9, thud @ 40.3 |

**132 words** across 42.7s — 185 wpm overall, 192 wpm of actual speech. Brisk, deliberate.

---

## Voice

`en-US-AndrewNeural` at `rate:+8%`. Seven segments, each rendered separately, then **silence-trimmed**
at both ends (`silenceremove` + `areverse`) and joined with a fixed **0.25s** gap.

| seg | 1 | 2 | 3 | 4 | 5 | 6 | 7 | total |
|---|---|---|---|---|---|---|---|---|
| trimmed | 3.85 | 9.96 | 6.08 | 4.99 | 6.23 | 3.56 | 6.54 | **41.22s** |

---

## Sync verification

Phrase onsets measured with `silencedetect` on the decoded `vo.mp3`. Every anchored cue:

| Cue | Fires | Phrase onset | Δ |
|---|---|---|---|
| Weights bar | 8.41 | 8.41 | 0.00 |
| KV cache bar | 9.84 | 9.84 | 0.00 |
| Context counter | 12.02 | 12.02 | 0.00 |
| Needle 40→4 | 23.75 | 23.75 | 0.00 |
| Spill pour | 18.87 | 18.86 | +0.01 |
| Row #2 24 GB | 28.50 | 28.50 | 0.00 |
| Row #3 48 GB | 30.81 | 30.81 | 0.00 |
| Bandwidth bar | 35.16 | 35.16 | 0.00 |
| Line 2 | 38.19 | 38.19 | 0.00 |
| Verdict tape | 40.32 | 40.32 | 0.00 |

**Worst anchored deviation: 0.10 s** (2–3 frames). The remaining cues are decorative or deliberate
follow-ons (the +6 GB tape sits mid-phrase, the RAM box lands 0.34 s after the pour).

**Colour wipes:** 0.62 s each, full cover at 46 % (0.285 s in).
Wipe 1 covers at **20.640 s**, wipe 2 at **36.170 s** — both exactly on the cut, error **0.000 s**.

---

## Files

```
EPISODE.html          open in Chrome/Edge, click PLAY
audio/vo.mp3          42.72s · Andrew · trimmed
audio/tick|whoosh|thud.mp3
audio/vo_david_backup.mp3   the original robotic cut, kept for comparison
core/kai.css          the design system
```

**To change voice:** edit `VOICE` / `RATE` in `data/revoice.py`, re-run it, then re-run
`data/rebuild2.py`. Both cue maps are derived from the audio, not guessed.
"""
open(r"C:\Users\jibra\Desktop\1\KAI\EPISODE_SCRIPT.md","w",encoding="utf-8").write(doc)
print("EPISODE_SCRIPT.md rewritten:",len(doc),"chars")
