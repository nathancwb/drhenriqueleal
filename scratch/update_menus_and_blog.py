# -*- coding: utf-8 -*-
import glob, re

html_files = glob.glob("*.html")

# Canonical nav on index.html:
index_nav = """<nav class="nav-links" id="navLinks">
                <a href="#resultados">Resultados</a>
                <a href="#procedimentos">Procedimentos</a>
                <a href="#sobre">Dr. Henrique</a>
                <a href="#localizacao">Consultório</a>
                <a href="#faq">Dúvidas</a>
                <a href="blog.html">Blog</a>
            </nav>"""

# Canonical nav on subpages:
subpage_nav = """<nav class="nav-links" id="navLinks">
                <a href="index.html#resultados">Resultados</a>
                <a href="procedimentos.html">Procedimentos</a>
                <a href="sobre.html">Dr. Henrique</a>
                <a href="index.html#localizacao">Consultório</a>
                <a href="index.html#faq">Dúvidas</a>
                <a href="blog.html">Blog</a>
            </nav>"""

for fn in html_files:
    with open(fn, "r", encoding="utf-8") as f:
        content = f.read()
        
    # Replace nav
    if fn == "index.html":
        content = re.sub(r'<nav class="nav-links" id="navLinks">[\s\S]*?</nav>', index_nav, content)
    else:
        # Check if it is blog.html to highlight blog
        if fn == "blog.html":
            cur_sub_nav = """<nav class="nav-links" id="navLinks">
                <a href="index.html#resultados">Resultados</a>
                <a href="procedimentos.html">Procedimentos</a>
                <a href="sobre.html">Dr. Henrique</a>
                <a href="index.html#localizacao">Consultório</a>
                <a href="index.html#faq">Dúvidas</a>
                <a href="blog.html" style="color: #ffffff; font-weight: 700;">Blog</a>
            </nav>"""
            content = re.sub(r'<nav class="nav-links" id="navLinks">[\s\S]*?</nav>', cur_sub_nav, content)
        else:
            content = re.sub(r'<nav class="nav-links" id="navLinks">[\s\S]*?</nav>', subpage_nav, content)
            
    with open(fn, "w", encoding="utf-8") as f:
        f.write(content)

print(f"Updated menus across all {len(html_files)} HTML files with Blog as the last item!")
