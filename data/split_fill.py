"""Split long scenes so no window runs longer than ~18s, and fill the frame."""
import pathlib, re

SPLITTER = '''

def split_scenes(spec, max_s=18.0, wps=2.7):
    """Break any scene longer than max_s into shorter windows.

    Items (rows/bars/table rows/chips) travel with the sentence that mentions
    them, so cue phrases keep matching and sync is preserved.
    """
    out = []
    for sc in spec["scenes"]:
        vo = sc["vo"].strip()
        words = len(vo.split()) or 1
        est = words / wps
        parts = [p for p in re.split(r"(?<=[.!?])\\s+", vo) if p.strip()]
        if est <= max_s * 1.15 or len(parts) < 2:
            out.append(sc)
            continue

        target = int(words * (max_s / est))
        chunks, cur, curw = [], [], 0
        for p in parts:
            w = len(p.split())
            if cur and curw + w > target:
                chunks.append(" ".join(cur)); cur, curw = [p], w
            else:
                cur.append(p); curw += w
        if cur:
            chunks.append(" ".join(cur))
        if len(chunks) < 2:
            out.append(sc)
            continue

        cues = dict(sc.get("cues", {}))
        buckets = [{} for _ in chunks]
        for k, ph in cues.items():
            for ci, c in enumerate(chunks):
                if ph.lower() in c.lower():
                    buckets[ci][k] = ph
                    break
            else:
                buckets[0][k] = ph

        # split list items across chunks by where their cue phrase lives
        items = sc.get("items")
        chips = sc.get("chips")
        per_chunk_items = None
        per_chunk_chips = None
        if items:
            per_chunk_items = [[] for _ in chunks]
            for idx, it in enumerate(items):
                ph = cues.get(str(idx), "")
                placed = False
                for ci, c in enumerate(chunks):
                    if ph and ph.lower() in c.lower():
                        per_chunk_items[ci].append(it); placed = True; break
                if not placed:
                    per_chunk_items[0].append(it)
            per_chunk_items = [x or items for x in per_chunk_items]
        if chips:
            per_chunk_chips = [[] for _ in chunks]
            for idx, ch in enumerate(chips):
                ph = cues.get(str(idx), "")
                for ci, c in enumerate(chunks):
                    if ph and ph.lower() in c.lower():
                        per_chunk_chips[ci].append(ch); break
                else:
                    per_chunk_chips[0].append(ch)
            per_chunk_chips = [x or chips for x in per_chunk_chips]

        for ci, c in enumerate(chunks):
            new = dict(sc)
            new["vo"] = c
            new["cues"] = buckets[ci]
            if per_chunk_items is not None:
                new["items"] = per_chunk_items[ci]
            if per_chunk_chips is not None:
                new["chips"] = per_chunk_chips[ci]
            out.append(new)
    spec["scenes"] = out
    return spec

'''

def main():
    p = pathlib.Path(r"C:\Users\jibra\Desktop\1\KAI\data\generate.py")
    s = p.read_text(encoding="utf-8")

    if "def split_scenes(" not in s:
        s = s.replace("def hero(i", SPLITTER + "\ndef hero(i", 1)

    # call it right after the spec is loaded
    old = '    name = spec.get("name", "EPISODE")'
    new = '    spec = split_scenes(spec)\n    name = spec.get("name", "EPISODE")'
    assert old in s
    s = s.replace(old, new, 1)

    # fill the frame: bigger art, wider rows, larger type
    s = s.replace("  .hero--h{{width:470px}}", "  .hero--h{{width:560px}}")
    s = s.replace("  .hero--v{{width:560px;margin-bottom:8px}}", "  .hero--v{{width:640px;margin-bottom:10px}}")
    s = s.replace("  .hero svg{{width:100%!important;height:auto!important;display:block;max-height:290px}}",
                  "  .hero svg{{width:100%!important;height:auto!important;display:block;max-height:330px}}")
    s = s.replace("  .col{{display:flex;flex-direction:column;gap:14px;width:1120px}}",
                  "  .col{{display:flex;flex-direction:column;gap:16px;width:1400px}}")
    s = s.replace("  .bf-row{{gap:26px;min-height:92px}}", "  .bf-row{{gap:26px;min-height:112px}}")
    s = s.replace("  .bf-row__k{{font-size:26px!important}}", "  .bf-row__k{{font-size:30px!important}}")
    s = s.replace("  .bf-row__v{{font-size:30px!important}}", "  .bf-row__v{{font-size:34px!important}}")
    s = s.replace("  .ctr{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:26px;padding:0 90px}}",
                  "  .ctr{{position:absolute;inset:0;display:flex;flex-direction:column;align-items:center;justify-content:center;gap:22px;padding:0 70px;transform:scale(1.06)}}")

    p.write_text(s, encoding="utf-8")
    print("splitter installed; frame scaled up")


if __name__ == "__main__":
    main()
