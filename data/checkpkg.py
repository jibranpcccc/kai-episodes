import importlib
for m in ["numpy","cv2","PIL","scipy","sklearn","pandas","pytesseract"]:
    try:
        mod = importlib.import_module(m)
        print(f"{m:12} OK  {getattr(mod,'__version__','?')}")
    except Exception as e:
        print(f"{m:12} MISSING ({type(e).__name__})")
