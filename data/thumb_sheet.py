import csv, os
from PIL import Image, ImageDraw, ImageFont

ROOT=r"C:\Users\jibra\Desktop\1\KAI"
rows=list(csv.DictReader(open(ROOT+r"\data\videos_ranked.csv",encoding="utf-8")))
rows.sort(key=lambda r:int(r["rank"]))

def font(sz):
    for n in ["seguisb.ttf","arialbd.ttf","segoeui.ttf","arial.ttf"]:
        try: return ImageFont.truetype(n,sz)
        except: pass
    return ImageFont.load_default()

def sheet(items, cols, tw, path, title):
    th=int(tw*9/16); pad=8; cap=44
    rowsn=(len(items)+cols-1)//cols
    W=cols*(tw+pad)+pad; H=rowsn*(th+cap+pad)+pad+40
    canvas=Image.new("RGB",(W,H),(18,18,22)); d=ImageDraw.Draw(canvas)
    d.text((pad,10),title,font=font(24),fill=(255,255,255))
    for i,(vid,label,txt) in enumerate(items):
        p=os.path.join(ROOT,"thumbs",vid+".jpg")
        if not os.path.exists(p): continue
        im=Image.open(p).convert("RGB").resize((tw,th),Image.LANCZOS)
        x=pad+(i%cols)*(tw+pad); y=40+pad+(i//cols)*(th+cap+pad)
        canvas.paste(im,(x,y))
        d.text((x+4,y+th+4),label,font=font(15),fill=(120,255,180))
        d.text((x+4,y+th+22),txt[:int(tw/6.2)],font=font(13),fill=(210,210,210))
    canvas.save(path,quality=90)
    print("wrote",path,canvas.size)

top=[(r["id"],f"#{r['rank']} {int(r['views']):,}",r["title"]) for r in rows[:12]]
sheet(top,4,440,ROOT+r"\data\sheet_thumbs_top.jpg","TOP 12 THUMBNAILS BY VIEWS  (@kaiexplainsYT)")

mid=[r for r in rows if 60<=int(r["rank"])<=71]
sheet([(r["id"],f"#{r['rank']} {int(r['views']):,}",r["title"]) for r in mid],4,440,ROOT+r"\data\sheet_thumbs_mid.jpg","RANKS 60-71 (typical performers) ")
