with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Add universal section containment and mobile precision rules
rock_solid_rules = """
/* ==========================================================================
   ROCK-SOLID MOBILE RESPONSIVENESS & OVERFLOW CONTAINMENT
   ========================================================================== */

html {
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

*, *::before, *::after {
    box-sizing: border-box !important;
}

section,
.section,
.hero,
.footer,
.cta-section,
.container {
    max-width: 100% !important;
    box-sizing: border-box !important;
}

/* Diferenciais Section Containment */
#diferenciais,
#diferenciais .container,
.diferenciais-layout,
.diferenciais-cards,
.diferenciais-image {
    overflow: hidden !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
}

/* Sobre / Authority Section Containment */
#sobre,
#sobre .container,
.about-authority-editorial,
.authority-editorial-media,
.authority-editorial-frame,
.authority-editorial-content {
    overflow: hidden !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
}

.authority-editorial-frame img {
    max-width: 100% !important;
    height: auto !important;
}

/* Footer Containment & Logo Resizing */
.footer,
.footer .container,
.footer-grid,
.footer-brand {
    overflow: hidden !important;
    max-width: 100% !important;
    box-sizing: border-box !important;
}

.footer-brand .footer-logo-link {
    display: inline-flex !important;
    align-items: center !important;
    gap: 12px !important;
    max-width: 100% !important;
}

.footer-brand .footer-logo-link img:nth-child(1) {
    height: 42px !important;
    width: auto !important;
    flex-shrink: 0 !important;
}

.footer-brand .footer-logo-link img:nth-child(2) {
    height: 32px !important;
    max-width: calc(100% - 60px) !important;
    width: auto !important;
    object-fit: contain !important;
}

@media (max-width: 768px) {
    .container {
        padding-left: 16px !important;
        padding-right: 16px !important;
    }

    .cert-swiper {
        width: 100% !important;
        max-width: 290px !important;
        margin: 0 auto !important;
        overflow: hidden !important;
        border-radius: 20px !important;
    }

    .cert-swiper .swiper-slide {
        width: 290px !important;
        max-width: 100% !important;
        height: 340px !important;
        border-radius: 20px !important;
    }

    .footer-brand .footer-logo-link img:nth-child(1) {
        height: 36px !important;
    }

    .footer-brand .footer-logo-link img:nth-child(2) {
        height: 26px !important;
        max-width: 190px !important;
    }
}
"""

css += "\n" + rock_solid_rules

with open("assets/css/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Applied rock-solid responsive rules!")
