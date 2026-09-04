with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# 1. Update html, body
html_body_rule = """html {
    overflow-x: hidden !important;
    max-width: 100% !important;
    width: 100% !important;
}

body {
    overflow-x: hidden !important;
    max-width: 100vw !important;
    width: 100% !important;
    position: relative !important;
}
"""

if "html {" in css:
    import re
    css = re.sub(r'html\s*\{[^}]*\}', '', css)
if "body {" in css:
    css = re.sub(r'body\s*\{', 'body {\n    overflow-x: hidden;\n    max-width: 100vw;\n    width: 100%;\n', css, count=1)

css = html_body_rule + css

# 2. Fix marquee containers to clip cleanly
css = css.replace(".ba-marquee-container {\n    overflow: hidden;\n    width: 100%;", ".ba-marquee-container {\n    overflow: hidden !important;\n    overflow-x: clip !important;\n    width: 100% !important;\n    max-width: 100vw !important;")

# 3. Add mobile animation safety and layout safety
mobile_safety = """
/* Mobile Overflow & Layout Safety Fixes */
@media (max-width: 768px) {
    html, body {
        overflow-x: hidden !important;
        width: 100% !important;
        max-width: 100vw !important;
    }

    .fade-in-right,
    .fade-in-left {
        transform: translateY(20px) scale(0.98) !important;
    }
    .fade-in-right.visible,
    .fade-in-left.visible {
        transform: translateY(0) scale(1) !important;
    }

    .container {
        padding-left: 16px !important;
        padding-right: 16px !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
    }

    .diferenciais-layout {
        display: flex !important;
        flex-direction: column !important;
        gap: 30px !important;
        width: 100% !important;
        max-width: 100% !important;
    }

    .diferenciais-cards {
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
    }

    .diff-card {
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
    }

    .diferenciais-image {
        width: 100% !important;
        max-width: 100% !important;
        box-sizing: border-box !important;
    }

    .cert-swiper {
        width: 100% !important;
        max-width: min(340px, calc(100vw - 32px)) !important;
        margin: 0 auto !important;
        overflow: hidden !important;
        border-radius: 20px !important;
    }

    .cert-swiper .swiper-slide {
        width: 100% !important;
        max-width: 100% !important;
        height: 380px !important;
        border-radius: 20px !important;
    }

    .ba-marquee-container {
        overflow: hidden !important;
        overflow-x: clip !important;
        max-width: 100vw !important;
        width: 100% !important;
    }
}
"""

css += mobile_safety

with open("assets/css/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Applied full mobile safety CSS!")
