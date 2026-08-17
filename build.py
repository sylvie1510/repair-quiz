# -*- coding: utf-8 -*-
"""בונה את index.html עם הפונטים מוטמעים base64."""
import base64, os
HOME = os.path.expanduser("~")
HERE = os.path.dirname(os.path.abspath(__file__))

def font(name):
    with open(os.path.join(HOME, "Library", "Fonts", name), "rb") as f:
        return "data:font/otf;base64," + base64.b64encode(f.read()).decode()

src = open(os.path.join(HERE, "src", "quiz.template.html"), encoding="utf-8").read()
out = (src.replace("__FONT_LIGHT__", font("Polin-Light.otf"))
          .replace("__FONT_BLACK__", font("Polin-Black.otf")))
assert "__FONT_" not in out
open(os.path.join(HERE, "index.html"), "w", encoding="utf-8").write(out)
print("index.html", round(len(out)/1024), "KB")
