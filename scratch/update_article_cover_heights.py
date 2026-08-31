# -*- coding: utf-8 -*-
import re

with open("scratch/generate_blog_drhenrique_brand.py", "r", encoding="utf-8") as f:
    content = f.read()

# Replace .article-cover-wrap CSS with compact height
old_css = """.article-cover-wrap {
            width: 100%;
            height: 420px;
            border-radius: 20px;
            overflow: hidden;
            margin-bottom: 40px;
            box-shadow: 0 12px 36px rgba(27, 58, 92, 0.09);
        }"""

new_css = """.article-cover-wrap {
            width: 100%;
            max-width: 680px;
            height: 280px;
            border-radius: 16px;
            overflow: hidden;
            margin: 0 auto 35px auto;
            box-shadow: 0 8px 24px rgba(27, 58, 92, 0.07);
        }"""

content = content.replace(old_css, new_css)

# Also update figure img wrap
old_fig = """.article-figure-img-wrap {
            width: 100%;
            height: 380px;
            border-radius: 16px;
            overflow: hidden;
            box-shadow: 0 8px 26px rgba(27, 58, 92, 0.07);
        }"""

new_fig = """.article-figure-img-wrap {
            width: 100%;
            max-width: 680px;
            height: 260px;
            border-radius: 14px;
            overflow: hidden;
            margin: 0 auto;
            box-shadow: 0 6px 20px rgba(27, 58, 92, 0.06);
        }"""

content = content.replace(old_fig, new_fig)

# Ensure nav has Blog as the last item
old_nav = """<nav class="nav-links" id="navLinks">
                <a href="index.html#resultados">Resultados</a>
                <a href="procedimentos.html">Procedimentos</a>
                <a href="sobre.html">Dr. Henrique</a>
                <a href="blog.html" style="color: #ffffff; font-weight: 700;">Blog</a>
                <a href="index.html#localizacao">Consultório</a>
                <a href="index.html#faq">Dúvidas</a>
            </nav>"""

new_nav = """<nav class="nav-links" id="navLinks">
                <a href="index.html#resultados">Resultados</a>
                <a href="procedimentos.html">Procedimentos</a>
                <a href="sobre.html">Dr. Henrique</a>
                <a href="index.html#localizacao">Consultório</a>
                <a href="index.html#faq">Dúvidas</a>
                <a href="blog.html" style="color: #ffffff; font-weight: 700;">Blog</a>
            </nav>"""

content = content.replace(old_nav, new_nav)

with open("scratch/generate_blog_drhenrique_brand.py", "w", encoding="utf-8") as f:
    f.write(content)

print("Updated generator script with compact image sizes and Blog at the end of the menu!")
