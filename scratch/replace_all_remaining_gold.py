import re

# 1. index.html
with open("index.html", "r", encoding="utf-8") as f:
    content = f.read()
content = content.replace("#c5a47e", "#2A7DE1")
with open("index.html", "w", encoding="utf-8") as f:
    f.write(content)

# 2. assets/css/style.css
with open("assets/css/style.css", "r", encoding="utf-8") as f:
    content = f.read()
content = content.replace("#c5a47e", "#2A7DE1")
content = content.replace("rgba(197, 164, 126, 0.3)", "rgba(42, 125, 225, 0.3)")
content = content.replace("rgba(212, 175, 55, 0.4)", "rgba(42, 125, 225, 0.4)")
content = content.replace("rgba(212, 175, 55, 0.3)", "rgba(42, 125, 225, 0.3)")
content = content.replace("rgba(212, 175, 55, 0.22)", "rgba(42, 125, 225, 0.15)")
with open("assets/css/style.css", "w", encoding="utf-8") as f:
    f.write(content)

# 3. assets/js/main.js
with open("assets/js/main.js", "r", encoding="utf-8") as f:
    content = f.read()
content = content.replace("#D4AF37", "#2A7DE1")
content = content.replace("rgba(212, 175, 55, 0.1)", "rgba(42, 125, 225, 0.15)")
with open("assets/js/main.js", "w", encoding="utf-8") as f:
    f.write(content)

print("Replaced all gold occurrences in index.html, style.css, and main.js!")
