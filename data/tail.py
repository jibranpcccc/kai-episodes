from PIL import Image
im=Image.open(r"C:\Users\jibra\Desktop\1\KAI\proof\report_tall.png")
print("tall:",im.size)
bot=im.crop((0, im.height-5200, im.width, im.height))
w=760; h=int(bot.height*w/bot.width)
bot.resize((w,h),Image.LANCZOS).save(r"C:\Users\jibra\Desktop\1\KAI\proof\report_tail.jpg",quality=90)
print("tail:",(w,h))
