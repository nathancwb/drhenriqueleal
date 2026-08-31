# -*- coding: utf-8 -*-
import json

with open("assets/js/blog-data.js", "r", encoding="utf-8") as f:
    js_content = f.read()

# Parse JSON from blog-data.js
json_str = js_content.split("window.BLOG_POSTS = ")[1].rstrip(";\n")
posts = json.loads(json_str)

MONTHS = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"]
def format_date_pt(d_str):
    y, m, d = d_str.split("-")
    return f"{int(d)} de {MONTHS[int(m)-1]} de {y}"

# Generate cards for all 20 posts
cards_html = ""
for p in posts:
    cards_html += f"""
                <a href="{p['slug']}.html" class="blog-card" data-category="{p['category']}">
                    <div class="blog-card-img-wrap">
                        <img src="{p['cover']}" alt="{p['title']}" class="blog-card-img" loading="lazy">
                        <span class="blog-card-badge">{p['category']}</span>
                    </div>
                    <div class="blog-card-body">
                        <div class="blog-card-meta">
                            <span>{format_date_pt(p['date'])}</span> · <span>{p['readingMinutes']} min</span>
                        </div>
                        <h3 class="blog-card-title">{p['title']}</h3>
                        <p class="blog-card-excerpt">{p['excerpt']}</p>
                        <div class="blog-card-footer">
                            <span class="read-more-link">Ler artigo completo ↗</span>
                        </div>
                    </div>
                </a>
    """

blog_html = f"""<!DOCTYPE html>
<html lang="pt-BR">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <link rel="stylesheet" href="assets/css/style.css?v=11.0">
    <link rel="icon" type="image/png" href="assets/img/favicon.png?v=3">
    <link rel="apple-touch-icon" href="assets/img/favicon.png?v=3">
    <title>Blog & Artigos Clínicos | Dr. Henrique Leal Rosa em Curitiba</title>
    <meta name="description" content="Artigos educativos sobre Harmonização Facial, Botox, Fios de PDO, Bioestimuladores e Estética Avançada em Curitiba com o Dr. Henrique Leal Rosa.">
    <link rel="canonical" href="https://drhenriqueleal.com.br/blog.html">
    
    <style>
        .blog-hero {{
            padding: 150px 0 35px;
            background: #FAFBFD;
            text-align: center;
            border-bottom: 1px solid rgba(27, 58, 92, 0.06);
        }}
        .blog-hero-label {{
            font-size: 0.82rem;
            font-weight: 700;
            letter-spacing: 0.15em;
            text-transform: uppercase;
            color: var(--color-accent);
            display: block;
            margin-bottom: 12px;
        }}
        .blog-hero-title {{
            font-family: var(--font-heading);
            font-size: clamp(2.2rem, 4vw, 3.4rem);
            color: var(--color-primary);
            margin-bottom: 14px;
            font-weight: 700;
        }}
        .blog-hero-desc {{
            font-size: 1.1rem;
            color: #64748B;
            max-width: 680px;
            margin: 0 auto 30px;
            line-height: 1.7;
        }}
        
        .blog-filter-bar {{
            display: flex;
            gap: 8px;
            justify-content: center;
            flex-wrap: wrap;
            margin-bottom: 30px;
            padding: 0 10px;
        }}
        .blog-filter-btn {{
            background: #FFFFFF;
            color: #475569;
            border: 1px solid rgba(27, 58, 92, 0.12);
            padding: 7px 16px;
            border-radius: 30px;
            font-size: 0.82rem;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.25s ease;
        }}
        .blog-filter-btn:hover, .blog-filter-btn.active {{
            background: var(--color-primary);
            color: #FFFFFF;
            border-color: var(--color-primary);
            box-shadow: 0 4px 14px rgba(27, 58, 92, 0.15);
        }}
        
        .blog-grid {{
            display: grid;
            grid-template-columns: repeat(3, 1fr);
            gap: 26px;
            margin-bottom: 60px;
        }}
        .blog-card {{
            background: #FFFFFF;
            border-radius: 18px;
            border: 1px solid rgba(27, 58, 92, 0.08);
            overflow: hidden;
            display: flex;
            flex-direction: column;
            box-shadow: 0 6px 20px rgba(27, 58, 92, 0.04);
            text-decoration: none;
            color: inherit;
            transition: transform 0.3s ease, box-shadow 0.3s ease;
        }}
        .blog-card:hover {{
            transform: translateY(-5px);
            box-shadow: 0 16px 36px rgba(27, 58, 92, 0.09);
        }}
        .blog-card-img-wrap {{
            width: 100%;
            height: 190px;
            overflow: hidden;
            position: relative;
        }}
        .blog-card-img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.5s ease;
        }}
        .blog-card:hover .blog-card-img {{
            transform: scale(1.06);
        }}
        .blog-card-badge {{
            position: absolute;
            top: 12px;
            left: 12px;
            background: rgba(15, 40, 71, 0.85);
            backdrop-filter: blur(4px);
            color: #FFFFFF;
            font-size: 0.72rem;
            font-weight: 700;
            text-transform: uppercase;
            letter-spacing: 0.06em;
            padding: 4px 10px;
            border-radius: 20px;
        }}
        
        .blog-card-body {{
            padding: 22px 20px;
            display: flex;
            flex-direction: column;
            flex-grow: 1;
        }}
        .blog-card-meta {{
            font-size: 0.78rem;
            color: #94A3B8;
            font-weight: 500;
            margin-bottom: 8px;
        }}
        .blog-card-title {{
            font-family: var(--font-heading);
            font-size: 1.18rem;
            color: var(--color-primary);
            line-height: 1.35;
            margin: 0 0 10px 0;
            font-weight: 700;
        }}
        .blog-card-excerpt {{
            font-size: 0.88rem;
            color: #64748B;
            line-height: 1.6;
            margin-bottom: 16px;
            display: -webkit-box;
            -webkit-line-clamp: 3;
            -webkit-box-orient: vertical;
            overflow: hidden;
        }}
        .blog-card-footer {{
            margin-top: auto;
            padding-top: 12px;
            border-top: 1px solid rgba(27, 58, 92, 0.06);
            display: flex;
            justify-content: flex-end;
            align-items: center;
        }}
        .read-more-link {{
            font-size: 0.82rem;
            font-weight: 700;
            color: var(--color-accent);
            display: inline-flex;
            align-items: center;
            gap: 4px;
            transition: transform 0.2s ease;
        }}
        .blog-card:hover .read-more-link {{
            transform: translateX(3px);
        }}
        
        .blog-cta-box {{
            background: linear-gradient(135deg, #0F2847 0%, #1B3A5C 100%);
            border-radius: 24px;
            padding: 50px 40px;
            text-align: center;
            color: #FFFFFF;
            margin-bottom: 70px;
        }}
        .blog-cta-title {{
            font-family: var(--font-heading);
            font-size: clamp(1.8rem, 3vw, 2.4rem);
            margin-bottom: 14px;
            color: #FFFFFF;
        }}
        .blog-cta-text {{
            font-size: 1.05rem;
            color: rgba(255, 255, 255, 0.88);
            max-width: 600px;
            margin: 0 auto 28px;
            line-height: 1.6;
        }}
        
        @media (max-width: 992px) {{
            .blog-grid {{ grid-template-columns: repeat(2, 1fr); }}
        }}
        @media (max-width: 640px) {{
            .blog-grid {{ grid-template-columns: 1fr; }}
            .blog-hero {{ padding: 130px 0 25px; }}
            .blog-card-body {{ padding: 18px 16px; }}
        }}
    </style>
</head>

<body>

    <!-- ==================== HEADER ==================== -->
    <header class="header" id="header">
        <div class="container">
            <a href="index.html" class="header-logo">
                <img src="assets/img/logo-simbolo.webp" alt="Símbolo Dr. Henrique Leal" class="logo-symbol" id="header-logo-img">
                <img src="assets/img/logo-texto.webp" alt="Dr. Henrique Leal Rosa" class="logo-text">
            </a>
            <nav class="nav-links" id="navLinks">
                <a href="index.html#resultados">Resultados</a>
                <a href="procedimentos.html">Procedimentos</a>
                <a href="sobre.html">Dr. Henrique</a>
                <a href="index.html#localizacao">Consultório</a>
                <a href="index.html#faq">Dúvidas</a>
                <a href="blog.html" style="color: #ffffff; font-weight: 700;">Blog</a>
            </nav>
            <button class="menu-toggle" id="menuToggle" aria-label="Menu">
                <span></span>
                <span></span>
                <span></span>
            </button>
        </div>
    </header>

    <!-- ==================== HERO BLOG ==================== -->
    <section class="blog-hero">
        <div class="container">
            <span class="blog-hero-label">Blog & Artigos Clínicos</span>
            <h1 class="blog-hero-title">Ciência, Estética e Cuidados em Curitiba</h1>
            <p class="blog-hero-desc">
                Orientações práticas, dúvidas frequentes e artigos sobre tratamentos faciais e corporais, com foco em segurança e naturalidade.
            </p>
            
            <!-- Category Filter Bar -->
            <div class="blog-filter-bar" id="categoryFilterBar">
                <button class="blog-filter-btn active" data-category="ALL">Todos os Artigos (20)</button>
                <button class="blog-filter-btn" data-category="Bioestimuladores">Bioestimuladores (2)</button>
                <button class="blog-filter-btn" data-category="Estética Íntima">Estética Íntima (2)</button>
                <button class="blog-filter-btn" data-category="Fios de PDO">Fios de PDO (2)</button>
                <button class="blog-filter-btn" data-category="Harmonização Facial">Harmonização Facial (2)</button>
                <button class="blog-filter-btn" data-category="Ozonioterapia">Ozonioterapia (2)</button>
                <button class="blog-filter-btn" data-category="Preenchimento Labial">Preenchimento Labial (2)</button>
                <button class="blog-filter-btn" data-category="Protocolo Bioforce">Protocolo Bioforce (2)</button>
                <button class="blog-filter-btn" data-category="Rinomodelação">Rinomodelação (2)</button>
                <button class="blog-filter-btn" data-category="Terapia Capilar">Terapia Capilar (2)</button>
                <button class="blog-filter-btn" data-category="Toxina Botulínica">Toxina Botulínica (2)</button>
            </div>
        </div>
    </section>

    <!-- ==================== BLOG POSTS CONTAINER ==================== -->
    <section style="padding: 40px 0 80px; background: #FFFFFF;">
        <div class="container">
            
            <!-- Posts Grid -->
            <div class="blog-grid" id="blogGrid">
{cards_html}
            </div>

            <!-- CTA Box -->
            <div class="blog-cta-box">
                <h2 class="blog-cta-title">Deseja uma avaliação individualizada?</h2>
                <p class="blog-cta-text">
                    O Dr. Henrique Leal atende no Edifício Today's Office (Água Verde, Curitiba), com planejamento anatômico exclusivo para você.
                </p>
                <a href="https://wa.me/5541988577430?text=Ol%C3%A1%2C%20vi%20o%20blog%20e%20gostaria%20de%20agendar%20uma%20avalia%C3%A7%C3%A3o." class="btn btn-primary" target="_blank" rel="noopener">
                    Agendar pelo WhatsApp ↗
                </a>
            </div>

        </div>
    </section>

    <!-- ==================== FOOTER ==================== -->
    <footer class="footer">
        <div class="container">
            <div class="footer-grid">
                <div class="footer-brand">
                    <a href="index.html">
                        <img src="assets/img/logo-sub-colorida.webp" alt="Dr. Henrique Leal Rosa" class="footer-logo" loading="lazy">
                    </a>
                    <p>Harmonização Facial com naturalidade e sofisticação. Curitiba, PR.</p>
                </div>
                <div class="footer-col">
                    <h4>Navegação</h4>
                    <a href="index.html">Início</a>
                    <a href="procedimentos.html">Procedimentos</a>
                    <a href="sobre.html">Dr. Henrique</a>
                    <a href="index.html#localizacao">Consultório</a>
                    <a href="index.html#faq">Dúvidas</a>
                    <a href="blog.html">Blog</a>
                </div>
                <div class="footer-col">
                    <h4>Procedimentos</h4>
                    <a href="fios-de-pdo-curitiba.html">Fios de PDO</a>
                    <a href="botox-curitiba.html">Toxina Botulínica</a>
                    <a href="preenchimento-labial-curitiba.html">Preenchimento</a>
                    <a href="bioestimuladores-de-colageno-curitiba.html">Bioestimuladores</a>
                </div>
                <div class="footer-col">
                    <h4>Contato</h4>
                    <a href="https://wa.me/5541988577430" target="_blank" rel="noopener">WhatsApp</a>
                    <a href="https://maps.google.com/?q=Av.+Rep.+Argentina,+1237+-+Sala+518+-+%C3%81gua+Verde,+Curitiba+-+PR" target="_blank" rel="noopener">Edifício Today's Office · Água Verde</a>
                </div>
            </div>
            <div class="footer-bottom">
                <p>&copy; 2026 Dr. Henrique Leal Rosa. Todos os direitos reservados. CRO-PR 31739 · CRBM-PR 8966.</p>
            </div>
        </div>
    </footer>

    <script src="assets/js/main.js?v=5.0"></script>
    <script>
        document.addEventListener('DOMContentLoaded', function() {{
            const filterBtns = document.querySelectorAll('.blog-filter-btn');
            const cards = document.querySelectorAll('.blog-card');

            filterBtns.forEach(btn => {{
                btn.addEventListener('click', function() {{
                    filterBtns.forEach(b => b.classList.remove('active'));
                    this.classList.add('active');

                    const cat = this.getAttribute('data-category');

                    cards.forEach(card => {{
                        if (cat === 'ALL' || card.getAttribute('data-category') === cat) {{
                            card.style.display = 'flex';
                        }} else {{
                            card.style.display = 'none';
                        }}
                    }});
                }});
            }});
        }});
    </script>
</body>
</html>
"""

with open("blog.html", "w", encoding="utf-8") as f:
    f.write(blog_html)

print("Regenerated refined blog.html with compact card images and balanced grid!")
