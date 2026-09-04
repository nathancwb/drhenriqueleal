with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Let's inspect where .cert-swiper is defined
import re

# Ensure html and body are completely locked against horizontal scroll
css = re.sub(r'html\s*\{[^}]*\}', '', css)
css = re.sub(r'body\s*\{[^}]*\}', '', css, count=1)

base_reset = """html {
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
}
"""

css = base_reset + css

# Clean cert-swiper base
css = re.sub(r'\.cert-swiper\s*\{[^}]*\}', '''.cert-swiper {
    width: 100%;
    max-width: 320px;
    margin: 0 auto;
    padding-bottom: 30px;
    overflow: hidden !important;
    position: relative;
}''', css)

# Clean cert-swiper slide
css = re.sub(r'\.cert-swiper\s*\.swiper-slide\s*\{[^}]*\}', '''.cert-swiper .swiper-slide {
    display: flex;
    position: relative;
    justify-content: center;
    background: #FFFFFF;
    border-radius: 20px;
    box-shadow: 0 12px 30px rgba(27, 58, 92, 0.12);
    border: 1px solid rgba(27, 58, 92, 0.08);
    overflow: hidden;
    height: 380px;
    max-width: 100%;
}''', css)

with open("assets/css/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Updated cert-swiper and base styles!")
