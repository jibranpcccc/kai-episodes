from PIL import Image
p=r"C:\Users\jibra\Desktop\1\KAI\proof\report_full.png"
im=Image.open(p); print("full:",im.size)
# downscale to a viewable strip
w=760; h=int(im.height*w/im.width)
im.resize((w,h),Image.LANCZOS).save(r"C:\Users\jibra\Desktop\1\KAI\proof\report_full_small.jpg",quality=88)
print("small:",(w,h))
