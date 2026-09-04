with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

import re

# Extract @import statements
imports = re.findall(r'@import\s+url\([^)]+\);', css)
css_without_imports = re.sub(r'@import\s+url\([^)]+\);', '', css)

# Clean multiple html, body definitions
css_clean = re.sub(r'html\s*\{[^}]*\}', '', css_without_imports)
css_clean = re.sub(r'body\s*\{[^}]*\}', '', css_clean)
css_clean = re.sub(r'html,\s*body\s*\{[^}]*\}', '', css_clean)

final_css = "\n".join(imports) + "\n\n" + """html {
    overflow-x: hidden !important;
    max-width: 100vw !important;
    width: 100% !important;
}

body {
    overflow-x: hidden !important;
    max-width: 100vw !important;
    width: 100% !important;
    position: relative !important;
    margin: 0;
    padding: 0;
    font-family: var(--font-body);
    color: var(--color-text);
    background-color: var(--color-bg);
    line-height: 1.7;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
}

*, *::before, *::after {
    box-sizing: border-box !important;
}
""" + css_clean

with open("assets/css/style.css", "w", encoding="utf-8") as f:
    f.write(final_css)

# Also update index.html to v=11.0
with open("index.html", "r", encoding="utf-8") as f:
    html = f.read()

html = re.sub(r'style\.css\?v=[^"]+', 'style.css?v=11.0', html)

with open("index.html", "w", encoding="utf-8") as f:
    f.write(html)

print("Cleaned CSS order and updated index.html to v=11.0!")
