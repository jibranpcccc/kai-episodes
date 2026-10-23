# -*- coding: utf-8 -*-
with open(r"C:\Users\jibra\Desktop\1\KAI\core\fusion.css", "r", encoding="utf-8") as f:
    css = f.read()

target_css = ".note__left{display:flex;flex-direction:column;gap:26px;align-items:flex-start;justify-content:center}"
rep_css = target_css + "\n.note__art{height:100%;display:flex;flex-direction:column;justify-content:center}"

if target_css in css and ".note__art{height:100%" not in css:
    css = css.replace(target_css, rep_css)
    with open(r"C:\Users\jibra\Desktop\1\KAI\core\fusion.css", "w", encoding="utf-8") as f:
        f.write(css)
    print("Updated fusion.css")
else:
    print("fusion.css already has note__art or target not found")

# Now update fusion_build.py for snappier animation settling to fix static %
with open(r"C:\Users\jibra\Desktop\1\KAI\data\fusion_build.py", "r", encoding="utf-8") as f:
    py = f.read()

# Replace push and draw duration in artpanel:
py = py.replace('win.beat(svgid, "draw", at, dur=2000, ease="draw", sdur=1200)',
                'win.beat(svgid, "draw", at, dur=1400, ease="draw", sdur=900)')
py = py.replace('win.beat(inner, "push", at, dur=2000, ease="push", **{"from": 0.962, "to": 1.0})',
                'win.beat(inner, "push", at, dur=1400, ease="push", **{"from": 0.962, "to": 1.0})')

# Replace fdur and cdur in bars, rows, rails:
py = py.replace('fdur=950', 'fdur=650')
py = py.replace('cdur=950', 'cdur=650')
py = py.replace('cdur=900', 'cdur=650')

with open(r"C:\Users\jibra\Desktop\1\KAI\data\fusion_build.py", "w", encoding="utf-8") as f:
    f.write(py)
print("Updated fusion_build.py animation settling durations")
