from PIL import Image
im=Image.open(r"C:\Users\jibra\Desktop\1\KAI\proof\ep02_page.png").convert("RGB")
print("size",im.size)
cols=im.getcolors(1<<20)
cols.sort(reverse=True)
print("top colours:",[(c, f"#{r:02X}{g:02X}{b:02X}") for c,(r,g,b) in cols[:5]])
