p=r"C:\Users\jibra\Desktop\1\KAI\repo\scripts\render.py"
s=open(p,encoding="utf-8").read()
old='        browser = p.chromium.launch(args=["--force-device-scale-factor=1"])'
new='''        try:
            browser = p.chromium.launch(args=["--force-device-scale-factor=1"])
        except Exception:
            # fall back to a system Chrome (handy locally; CI installs chromium)
            browser = p.chromium.launch(channel="chrome",
                                        args=["--force-device-scale-factor=1"])'''
assert old in s
s=s.replace(old,new)
open(p,"w",encoding="utf-8").write(s)
print("chromium fallback added")
