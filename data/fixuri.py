p=r"C:\Users\jibra\Desktop\1\KAI\repo\scripts\render.py"
s=open(p,encoding="utf-8").read()
old='    page.goto("file://" + str(html_path).replace("\\\\", "/"))'
new='    page.goto(html_path.resolve().as_uri())'
assert old in s, "goto line not found"
s=s.replace(old,new)
open(p,"w",encoding="utf-8").write(s)
print("file URI fixed")
