with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

footer_and_about_fix = """
/* Mobile Strict Containment & Overflow Immunity */
@media (max-width: 768px) {
    html, body {
        overflow-x: hidden !important;
        width: 100% !important;
        max-width: 100vw !important;
    }

    *, *::before, *::after {
        box-sizing: border-box !important;
    }

    .container {
        width: 100% !important;
        max-width: 100% !important;
        padding-left: 16px !important;
        padding-right: 16px !important;
        overflow: hidden !important;
    }

    /* Hero */
    .hero,
    .hero-content,
    .hero-social-proof {
        max-width: 100% !important;
        overflow: hidden !important;
    }

    /* Diferenciais & Certificate */
    #diferenciais,
    #diferenciais .container,
    .diferenciais-layout,
    .diferenciais-cards,
    .diferenciais-image {
        max-width: 100% !important;
        width: 100% !important;
        overflow: hidden !important;
    }

    .cert-swiper {
        width: 100% !important;
        max-width: 280px !important;
        margin: 0 auto !important;
        overflow: hidden !important;
    }

    .cert-swiper .swiper-slide {
        width: 280px !important;
        max-width: 100% !important;
        height: 330px !important;
    }

    /* Sobre / Authority */
    #sobre,
    #sobre .container,
    .about-authority-editorial,
    .authority-editorial-media,
    .authority-editorial-frame,
    .authority-editorial-content {
        max-width: 100% !important;
        width: 100% !important;
        overflow: hidden !important;
    }

    .authority-editorial-frame img {
        max-width: 100% !important;
        height: auto !important;
    }

    /* Footer Logo Mobile Scaling */
    .footer-brand .footer-logo-link {
        display: inline-flex !important;
        align-items: center !important;
        gap: 10px !important;
        max-width: 100% !important;
    }

    .footer-brand .footer-logo-link img:nth-child(1) {
        height: 38px !important;
        width: auto !important;
    }

    .footer-brand .footer-logo-link img:nth-child(2) {
        height: 30px !important;
        max-width: 200px !important;
        width: auto !important;
    }

    /* Marquee overflow shield */
    .ba-marquee-container {
        overflow: hidden !important;
        overflow-x: clip !important;
        width: 100% !important;
        max-width: 100vw !important;
    }
}
"""

css += footer_and_about_fix

with open("assets/css/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Applied strict mobile containment fixes!")
