import re

with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# 1. Global prevention of horizontal scroll
if "html, body {" in css:
    css = css.replace("html, body {", "html, body {\n    overflow-x: hidden;\n    max-width: 100vw;\n    width: 100%;")
else:
    css = "html, body {\n    overflow-x: hidden;\n    max-width: 100vw;\n    width: 100%;\n}\n" + css

# 2. Fix cert-swiper overflow
css = css.replace("overflow: visible;\n    position: relative;\n}", "overflow: hidden;\n    position: relative;\n    max-width: min(380px, 90vw);\n}")

with open("assets/css/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Applied global overflow protection and cert-swiper fix!")
