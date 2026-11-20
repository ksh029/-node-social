# 안드로이드 런처 아이콘을 www/icons 이미지로 교체
import os
from PIL import Image
res = "android/app/src/main/res"
fg = Image.open("www/icons/maskable-512.png").convert("RGBA")
full = Image.open("www/icons/icon-512.png").convert("RGBA")
legacy = {"mdpi":48,"hdpi":72,"xhdpi":96,"xxhdpi":144,"xxxhdpi":192}
foreg  = {"mdpi":108,"hdpi":162,"xhdpi":216,"xxhdpi":324,"xxxhdpi":432}
for d in legacy:
    p = f"{res}/mipmap-{d}"
    if not os.path.isdir(p): continue
    for n in ("ic_launcher.png","ic_launcher_round.png"):
        full.resize((legacy[d],)*2, Image.LANCZOS).save(f"{p}/{n}")
    fg.resize((foreg[d],)*2, Image.LANCZOS).save(f"{p}/ic_launcher_foreground.png")
bg = f"{res}/values/ic_launcher_background.xml"
with open(bg,"w") as f:
    f.write('<?xml version="1.0" encoding="utf-8"?>\n<resources>\n    <color name="ic_launcher_background">#1D2026</color>\n</resources>\n')
