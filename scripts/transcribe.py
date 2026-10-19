#!/usr/bin/env python3
"""
Word-level transcription for episodes whose voiceover is a human recording.

Produces the same information the edge-tts word boundaries give us:
a list of (start_seconds, word) so cue times can be snapped to words.

Usage:
    python scripts/transcribe.py audio/my_take.mp3

Writes  audio/my_take.words.json = [[t, "word"], ...]
"""
import json
import sys
from pathlib import Path


def main() -> int:
    if len(sys.argv) < 2:
        print("usage: transcribe.py <audio file>", file=sys.stderr)
        return 2
    src = Path(sys.argv[1])
    if not src.exists():
        print(f"not found: {src}", file=sys.stderr)
        return 2

    from faster_whisper import WhisperModel

    # 'small' is a good CPU compromise; 'base' is ~2x faster and still fine
    model = WhisperModel("small", device="cpu", compute_type="int8")
    segments, info = model.transcribe(
        str(src), word_timestamps=True, vad_filter=True, language="en"
    )

    words = []
    for seg in segments:
        for w in seg.words or []:
            words.append([round(w.start, 3), w.word.strip()])

    out = src.with_suffix(".words.json")
    out.write_text(json.dumps(words, indent=0), encoding="utf-8")
    print(f"{len(words)} words -> {out}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
