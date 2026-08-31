# -*- coding: utf-8 -*-
import glob, re

footer_brand_block = """<div class="footer-brand">
                    <a href="index.html" class="footer-logo-link" style="display: inline-flex; align-items: center; gap: 14px; margin-bottom: 18px; text-decoration: none;">
                        <img src="assets/img/logo-simbolo.webp" alt="Símbolo Dr. Henrique Leal" style="height: 52px; width: auto; filter: brightness(0) invert(1); opacity: 0.95;">
                        <img src="assets/img/logo-texto.webp" alt="Dr. Henrique Leal Rosa" style="height: 42px; width: auto; filter: brightness(0) invert(1); opacity: 0.95;">
                    </a>
                    <p>Harmonização Facial com naturalidade e sofisticação. Curitiba, PR.</p>
                </div>"""

for fn in glob.glob("*.html"):
    with open(fn, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace footer brand block
    content = re.sub(r'<div class="footer-brand">[\s\S]*?<p>Harmonização Facial com naturalidade e sofisticação\. Curitiba, PR\.</p>\s*</div>', footer_brand_block, content)
    
    with open(fn, "w", encoding="utf-8") as f:
        f.write(content)

print("Updated all HTML footers with prominent horizontal logo + symbol!")
