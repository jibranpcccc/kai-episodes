"""Hardware illustration library + rotating hero stack.

Each scene shows a stack of hardware drawings; one becomes visible at a time,
timed to real spoken-word positions, so a NEW drawing appears every ~1.5 s.
"""
import pathlib, re

ART_EXTRA = r'''
ART["ram"] = (
    '<svg viewBox="0 0 420 130" class="art">'
    '<rect x="8" y="26" width="404" height="76" rx="6" class="s"/>'
    '<rect x="24" y="40" width="52" height="48" rx="3" class="s t"/>'
    '<rect x="86" y="40" width="52" height="48" rx="3" class="s t"/>'
    '<rect x="148" y="40" width="52" height="48" rx="3" class="s t"/>'
    '<rect x="210" y="40" width="52" height="48" rx="3" class="s t"/>'
    '<rect x="272" y="40" width="52" height="48" rx="3" class="s t"/>'
    '<rect x="334" y="40" width="52" height="48" rx="3" class="fl pulse"/>'
    '<path d="M20 102v16M52 102v16M84 102v16M116 102v16M148 102v16M180 102v16'
    'M212 102v16M244 102v16M276 102v16M308 102v16M340 102v16M372 102v16" class="s t"/>'
    '</svg>')

ART["ssd"] = (
    '<svg viewBox="0 0 420 150" class="art">'
    '<rect x="20" y="30" width="380" height="90" rx="8" class="s"/>'
    '<rect x="40" y="52" width="150" height="46" rx="4" class="s t"/>'
    '<rect x="206" y="52" width="60" height="46" rx="4" class="fy pulse"/>'
    '<rect x="280" y="52" width="60" height="46" rx="4" class="s t"/>'
    '<rect x="380" y="66" width="18" height="34" rx="2" class="fl"/>'
    '</svg>')

ART["cpu"] = (
    '<svg viewBox="0 0 260 260" class="art">'
    '<rect x="46" y="46" width="168" height="168" rx="8" class="s"/>'
    '<rect x="86" y="86" width="88" height="88" rx="4" class="s t"/>'
    '<g class="spin"><rect x="106" y="106" width="48" height="48" rx="4" class="fl pulse"/></g>'
    '<g class="s t"><path d="M70 46V16M100 46V16M130 46V16M160 46V16M190 46V16"/>'
    '<path d="M70 214v30M100 214v30M130 214v30M160 214v30M190 214v30"/>'
    '<path d="M46 70H16M46 100H16M46 130H16M46 160H16M46 190H16"/>'
    '<path d="M214 70h30M214 100h30M214 130h30M214 160h30M214 190h30"/></g>'
    '</svg>')

ART["board"] = (
    '<svg viewBox="0 0 440 240" class="art">'
    '<rect x="10" y="12" width="420" height="216" rx="8" class="s"/>'
    '<rect x="34" y="40" width="120" height="120" rx="4" class="s t"/>'
    '<g class="spin"><rect x="74" y="80" width="40" height="40" rx="3" class="fl pulse"/></g>'
    '<rect x="176" y="36" width="200" height="16" rx="3" class="s t"/>'
    '<rect x="176" y="66" width="200" height="16" rx="3" class="s t"/>'
    '<rect x="176" y="96" width="200" height="16" rx="3" class="fy"/>'
    '<rect x="176" y="132" width="120" height="70" rx="4" class="s t"/>'
    '<rect x="312" y="132" width="64" height="70" rx="4" class="s t"/>'
    '</svg>')

ART["psu"] = (
    '<svg viewBox="0 0 400 180" class="art">'
    '<rect x="16" y="26" width="368" height="128" rx="8" class="s"/>'
    '<g class="spin"><circle cx="120" cy="90" r="46" class="s t"/>'
    '<path d="M120 52a38 38 0 0 1 0 76" class="blade"/>'
    '<path d="M120 128a38 38 0 0 1 0-76" class="blade dim"/></g>'
    '<rect x="220" y="52" width="140" height="20" rx="3" class="s t"/>'
    '<rect x="220" y="86" width="140" height="20" rx="3" class="s t"/>'
    '<rect x="220" y="118" width="90" height="18" rx="3" class="fy"/>'
    '</svg>')

ART["cooler"] = (
    '<svg viewBox="0 0 320 320" class="art">'
    '<g class="spin"><circle cx="160" cy="160" r="120" class="s"/>'
    '<path d="M160 62a98 98 0 0 1 0 196" class="blade"/>'
    '<path d="M160 258a98 98 0 0 1 0-196" class="blade dim"/></g>'
    '<circle cx="160" cy="160" r="34" class="s t"/>'
    '<circle cx="160" cy="160" r="14" class="fl pulse"/>'
    '</svg>')

ART["slot"] = (
    '<svg viewBox="0 0 440 140" class="art">'
    '<rect x="12" y="34" width="416" height="72" rx="6" class="s"/>'
    '<rect x="28" y="52" width="384" height="36" rx="4" class="s t"/>'
    '<g class="fy"><rect x="44" y="60" width="20" height="20"/><rect x="76" y="60" width="20" height="20"/>'
    '<rect x="108" y="60" width="20" height="20"/><rect x="140" y="60" width="20" height="20"/></g>'
    '<rect x="300" y="60" width="20" height="20" class="fl"/>'
    '</svg>')

ORDER = ["gpu", "ram", "cpu", "ssd", "board", "cooler", "psu", "slot", "chip", "laptop"]
'''

def main():
    p = pathlib.Path(r"C:\Users\jibra\Desktop\1\KAI\data\generate.py")
    s = p.read_text(encoding="utf-8")

    # 1) append the hardware library just before the COLOUR map
    anchor = "COLOUR = {"
    assert anchor in s
    s = s.replace(anchor, ART_EXTRA + "\n" + anchor, 1)

    # 2) hero becomes a stack of drawings, revealed one at a time
    old_hero = '''def hero(i, cls):
    key = BG_ORDER[i % len(BG_ORDER)]
    return f\'<figure class="hero {cls}">{ART[key]}</figure>\''''
    new_hero = '''def hero(i, cls, k=6):
    """a stack of hardware drawings; band0..band{k-1} reveal one at a time"""
    keys = [ORDER[(i * 3 + j) % len(ORDER)] for j in range(k)]
    figs = "".join(f\'<figure data-in="@band{j}@">{ART[key]}</figure>\'
                   for j, key in enumerate(keys))
    return f\'<div class="hero {cls}">{figs}</div>\''''
    assert old_hero in s
    s = s.replace(old_hero, new_hero, 1)

    # 3) band times: K evenly spaced spoken words per scene
    old_cue = '''    devs = sorted(abs(cue[k] - WORD[k]) for k in WORD if k in cue)'''
    new_cue = '''    # hardware stack: one new drawing per ~1.4s, each on a real spoken word
    BAND = {}
    for i, sc in enumerate(spec["scenes"]):
        ws = [w[0] for w in words[i]] or [0.0]
        K = 6
        picks = [ws[min(len(ws) - 1, int((j + 1) * len(ws) / (K + 1)))] for j in range(K)]
        for j, t in enumerate(picks):
            BAND[(i, j)] = starts[i] + t

    devs = sorted(abs(cue[k] - WORD[k]) for k in WORD if k in cue)'''
    assert old_cue in s
    s = s.replace(old_cue, new_cue, 1)

    # 4) resolve @bandN@ tokens
    old_sub = '''            if key == "cap":
                return \'data-in="0.15"\' '''
    new_sub = '''            if key == "cap":
                return \'data-in="0.15"\'
            if key.startswith("band"):
                j = int(key[4:])
                return \'data-in="%.2f"\' % (BAND[(i, j)] - starts[i])
            '''
    if old_sub in s:
        s = s.replace(old_sub, new_sub, 1)
    else:
        # fallback: insert right after the def sub line
        s = s.replace('''            key = m.group(1)
            if key == "cap":''', '''            key = m.group(1)
            if key.startswith("band"):
                j = int(key[4:])
                return \'data-in="%.2f"\' % (BAND[(i, j)] - starts[i])
            if key == "cap":''', 1)

    # 5) CSS for the stack
    s = s.replace("  .hero{{flex:0 0 auto;animation:bob 7s ease-in-out infinite;margin:0}}",
"""  .hero{{flex:0 0 auto;margin:0;position:relative}}
  .hero figure{{position:absolute;inset:0;opacity:0;transition:opacity .22s ease}}
  .hero figure.on{{opacity:1}}
  .hero svg{{width:100%;height:auto}}""")
    s = s.replace("  .hero--h{{width:380px}}", "  .hero--h{{width:400px;height:250px}}")
    s = s.replace("  .hero--v{{width:290px;margin-bottom:4px}}", "  .hero--v{{width:330px;height:210px;margin-bottom:6px}}")

    p.write_text(s, encoding="utf-8")
    print("hardware stack installed: 10 drawings, 6 per scene, one every ~1.4s")


if __name__ == "__main__":
    main()
