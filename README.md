# KAI — episode renderer

Renders the episode HTML files to MP4 **on GitHub's machines**. Nothing runs on your laptop
except `git push`.

## What's here

```
episodes/            self-contained episode pages (voiceover embedded as base64)
  core/fonts/        the six typefaces the pages reference
scripts/render.py    headless Chromium -> PNG frames -> ffmpeg -> MP4
scripts/transcribe.py  optional: word timings from a human voiceover (faster-whisper)
.github/workflows/render.yml   the CI job
```

Each episode page exposes `window.renderAt(t)`, which paints the frame at exactly `t` seconds.
The renderer walks the clock frame by frame, so the output is deterministic — no real-time
screen capture, no dropped frames, no drift.

## Push it

```bash
cd repo
git init
git add .
git commit -m "episode renderer"
git branch -M main
git remote add origin https://github.com/YOURNAME/YOURREPO.git
git push -u origin main
```

Make the repo **public** — that's what makes Actions unlimited and free.
(Push needs a GitHub personal access token as the password, or use GitHub Desktop.)

## Get the video

1. Repo → **Actions** tab → the `render` run starts automatically.
2. Wait ~8–15 minutes (two episodes at 30 fps on a 2-core runner).
3. Open the finished run → **Artifacts** → download `videos`.
4. Unzip → `EPISODE-02.mp4`, `EPISODE-03.mp4` — 1920×1080, H.264, AAC.

To re-render without a code change: **Actions → render → Run workflow**.
You can override `fps` (default 30) and render a single episode via `only`
(e.g. `EPISODE-02`).

## Free-tier facts

| | |
|---|---|
| Cost | **$0** on a public repo (unlimited minutes) |
| Runner | 2 vCPU, 7 GB RAM, no GPU |
| Job limit | 6 hours (we use ~15 min) |
| Artifacts | kept 30 days, set in the workflow |
| Catch | scheduled runs pause after 60 days of repo inactivity — a manual run restarts them |

## How the audio stays in sync

The voiceover is embedded in the HTML as a base64 data URI, and the cue times were measured
from **that same audio**. `render.py` decodes the audio back out of the page and muxes it in,
so the MP4 cannot drift from the cues — there is only one audio source.

## Adding an episode

Drop a new self-contained episode HTML into `episodes/` (and its `core/fonts` reference still
resolves). Commit. The workflow picks up every `*.html` in that folder.

## Whisper

`transcribe.py` is for when you record your own voice. It produces word-level timings with
`faster-whisper`, which can then replace the edge-tts word boundaries in the cue map.
It is not needed for the current edge-tts episodes.
