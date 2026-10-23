import glob, os
from PIL import Image
ROOT=r"C:\Users\jibra\Desktop\1\KAI"
n=0
for f in glob.glob(os.path.join(ROOT,"thumbs","*.jpg")):
    try:
        im=Image.open(f)
        if im.format!="JPEG":
            im.convert("RGB").save(f,"JPEG",quality=92); n+=1
    except Exception as e:
        print("ERR",f,e)
print("converted:",n)
