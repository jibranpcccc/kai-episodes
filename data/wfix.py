p=r"C:\Users\jibra\Desktop\1\KAI\repo\scripts\render.py"
s=open(p,encoding="utf-8").read()
s=s.replace('page.wait_for_function("window.EPISODE && window.renderAt", timeout=30000)',
            'page.wait_for_function("!!(window.EPISODE && window.renderAt)", timeout=60000)')
open(p,"w",encoding="utf-8").write(s)
print("wait condition is now boolean")
