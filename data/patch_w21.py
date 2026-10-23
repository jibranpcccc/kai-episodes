# -*- coding: utf-8 -*-
with open(r"C:\Users\jibra\Desktop\1\KAI\data\build_spec_structured_outputs.py", "r", encoding="utf-8") as f:
    text = f.read()

old_w21 = '''    note_head="THE THREE INDEPENDENT EVALUATIONS",
    note_items=[
        dict(t="ACCURACY: COMPLIANT FORMAT DOES NOT PREVENT FACTUAL ERRORS",
             at="three success stories require three tests"),
        dict(t="SPEED: A FAST ENGINE MAY REJECT MANY COMPLEX SCHEMAS",
             at="fast engine may support fewer schemas"),
        dict(t="SUPPORT: ACCEPTED SCHEMAS MAY DROP UNSUPPORTED RULES",
             at="accepted schema may contain rules the engine does not enforce"),
    ],'''

new_w21 = '''    note_head="THREE INDEPENDENT EVALUATIONS",
    note_items=[
        dict(t="ACCURACY: COMPLIANT OUTPUT CAN STILL BE FACTUALLY FALSE",
             at="three success stories require three tests"),
        dict(t="SPEED: A FAST ENGINE MAY REJECT COMPLEX SCHEMAS",
             at="fast engine may support fewer schemas"),
        dict(t="SUPPORT: ACCEPTED SCHEMAS MAY SILENTLY DROP RULES",
             at="accepted schema may contain rules the engine does not enforce"),
    ],'''

text = text.replace(old_w21, new_w21)

with open(r"C:\Users\jibra\Desktop\1\KAI\data\build_spec_structured_outputs.py", "w", encoding="utf-8") as f:
    f.write(text)

print("Updated Win 21 note items")
