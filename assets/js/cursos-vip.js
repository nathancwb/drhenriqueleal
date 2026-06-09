// ==========================================================================
// DR. HENRIQUE LEAL — LANDING PAGE DE CURSOS VIP (SCROLLYTELLING ENGINE)
// Motor JavaScript de Rolagem de Alta Performance e Baixo Consumo de Processador
// ==========================================================================

document.addEventListener('DOMContentLoaded', () => {

    // --- Splash Screen Integration ---
    const splashScreen = document.getElementById('splash-screen');
    const splashLogo = document.getElementById('splash-logo');

    if (splashScreen && splashLogo) {
        const splashPlayed = sessionStorage.getItem('splashPlayedCursos');

        if (!splashPlayed) {
            sessionStorage.setItem('splashPlayedCursos', 'true');
            document.body.classList.add('splash-active');

            const startSplash = () => {
                setTimeout(() => {
                    // Zoom slightly and fade out smoothly in the center
                    splashLogo.style.transform = 'scale(0.85)';
                    splashLogo.style.opacity = '0';
                    splashLogo.style.transition = 'transform 0.8s cubic-bezier(0.25, 1, 0.5, 1), opacity 0.8s ease';

                    setTimeout(() => {
                        splashScreen.classList.add('fade-out');
                        setTimeout(() => {
                            splashScreen.remove();
                            document.body.classList.remove('splash-active');
                        }, 600);
                    }, 800);
                }, 1500);
            };

            if (splashLogo.complete) {
                startSplash();
            } else {
                splashLogo.addEventListener('load', startSplash);
            }
        } else {
            splashScreen.remove();
            document.body.classList.remove('splash-active');
        }
    } else {
        document.body.classList.remove('splash-active');
    }

    // --- FAQ Accordions (lp-static-info) ---
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        if (question) {
            question.addEventListener('click', () => {
                const isActive = item.classList.contains('active');
                faqItems.forEach(i => i.classList.remove('active'));
                if (!isActive) {
                    item.classList.add('active');
                }
            });
        }
    });

    // --- Mentoria Selection Shortcut Form Binding (Garantir Minha Vaga CTA) ---
    const selectMentoriaBtns = document.querySelectorAll('.select-mentoria-btn');
    const procedureSelect = document.getElementById('c-procedure');

    selectMentoriaBtns.forEach(btn => {
        btn.addEventListener('click', (e) => {
            e.preventDefault();
            const mentoriaValue = btn.getAttribute('data-mentoria');
            if (procedureSelect && mentoriaValue) {
                procedureSelect.value = mentoriaValue;
            }

            // Scroll to Candidatura block smoothly
            const candidaturaBlock = document.getElementById('block-candidatura');
            if (candidaturaBlock) {
                const headerEl = document.querySelector('.header');
                const headerHeight = headerEl ? headerEl.offsetHeight : 0;
                window.scrollTo({
                    top: candidaturaBlock.offsetTop + 10 - headerHeight,
                    behavior: 'smooth'
                });
            }
        });
    });

    // --- SCROLLYTELLING INTERACTIVE ENGINE ---
    // Only runs interactive stickies on desktop (widths > 992px)
    const isDesktop = () => window.innerWidth > 992;

    // --- 3 Pilares Metodologia Scroll Utilities (immersive-web skill) ---
    const blockProgress = (id) => {
        const el = document.getElementById(id);
        if (!el) return 0;
        const h = el.offsetHeight - window.innerHeight;
        if (h <= 0) return 0;
        return Math.max(0, Math.min(1, -el.getBoundingClientRect().top / h));
    };
    const easeOut3 = (t) => 1 - Math.pow(1 - t, 3);
    const clamp01 = (v, a, b) => Math.max(0, Math.min(1, (v - a) / (b - a)));

    const doB4 = (p) => {
        const b4lbl = document.getElementById('b4-lbl');
        const b4h   = document.getElementById('b4-h');
        const b4ln  = document.getElementById('b4-line');
        const b4lw  = document.getElementById('b4-lw');
        const b4p0  = document.getElementById('b4p0');
        const b4p1  = document.getElementById('b4p1');
        const b4p2  = document.getElementById('b4p2');

        if (!b4lbl || !b4h || !b4ln || !b4lw || !b4p0 || !b4p1 || !b4p2) return;

        // Título aparece
        const hp = easeOut3(clamp01(p, 0, 0.14));
        b4lbl.style.opacity = hp * 0.7;
        b4h.style.opacity   = hp;
        b4h.style.transform = `translateY(${(1 - hp) * 20}px)`;

        // Linha dourada cresce verticalmente
        const lp = easeOut3(clamp01(p, 0.13, 0.64));
        b4ln.style.height = (lp * b4lw.offsetHeight) + 'px';

        // Pilares revelam-se em sequência
        const e0 = easeOut3(clamp01(p, 0.18, 0.38));
        b4p0.style.opacity   = e0;
        b4p0.style.transform = `translateX(${(1 - e0) * -60}px)`;

        const e1 = easeOut3(clamp01(p, 0.34, 0.54));
        b4p1.style.opacity   = e1;
        b4p1.style.transform = `translateX(${(1 - e1) * 60}px) translateY(80px)`;

        const e2 = easeOut3(clamp01(p, 0.50, 0.70));
        b4p2.style.opacity   = e2;
        b4p2.style.transform = `translateX(${(1 - e2) * 60}px)`;
    };

    const handleScrollytellingEngine = () => {
        const scrollY = window.scrollY;
        const viewportHeight = window.innerHeight;

        // Skip viewport math on mobile/tablet and reset all style opacities
        if (!isDesktop()) {
            const heroBlock = document.getElementById('block-hero');
            const heroSticky = heroBlock ? heroBlock.querySelector('.scrolly-sticky') : null;
            if (heroSticky) heroSticky.style.opacity = 1;

            const publicoBlock = document.getElementById('block-publico');
            const publicoSticky = publicoBlock ? publicoBlock.querySelector('.scrolly-sticky') : null;
            if (publicoSticky) publicoSticky.style.opacity = 1;

            const mentoriasBlock = document.getElementById('block-mentorias');
            if (mentoriasBlock) mentoriasBlock.style.opacity = 1;

            const b4vp = document.getElementById('b4-vp');
            if (b4vp) b4vp.style.opacity = 1;

            const candidaturaBlock = document.getElementById('block-candidatura');
            const candidaturaSticky = candidaturaBlock ? candidaturaBlock.querySelector('.scrolly-sticky') : null;
            if (candidaturaSticky) candidaturaSticky.style.opacity = 1;

            return;
        }

        // ==================== BLOCO 1: HERO PARALLAX & ZOOM & FADES ====================
        const heroBlock = document.getElementById('block-hero');
        const heroBg = document.querySelector('.hero-parallax-bg');
        const phase1 = document.getElementById('hero-phase-1');
        const phase2 = document.getElementById('hero-phase-2');

        if (heroBlock && heroBg && phase1 && phase2) {
            const rect = heroBlock.getBoundingClientRect();
            const blockHeight = heroBlock.offsetHeight;
            const percent = Math.min(Math.max(-rect.top / (blockHeight - viewportHeight), 0), 1);

            // Bind Zoom
            heroBg.style.transform = `scale(${1 + percent * 0.08})`;

            // Cinematic fade-out of the entire Hero sticky container as it exits
            const heroSticky = heroBlock.querySelector('.scrolly-sticky');
            if (heroSticky) {
                const exitProgress = Math.max(0, Math.min(1, rect.bottom / (viewportHeight * 0.8)));
                heroSticky.style.opacity = exitProgress;
            }

            // Phase Transitions
            if (percent < 0.45) {
                phase1.classList.add('active');
                phase2.classList.remove('active');
                phase1.style.opacity = Math.max(1 - (percent * 2.2), 0);
                phase1.style.pointerEvents = 'auto';
                
                phase2.style.opacity = 0;
                phase2.style.pointerEvents = 'none';
            } else {
                phase1.classList.remove('active');
                phase2.classList.add('active');
                
                phase1.style.opacity = 0;
                phase1.style.pointerEvents = 'none';
                
                phase2.style.opacity = Math.min((percent - 0.45) * 2.2, 1);
                phase2.style.pointerEvents = 'auto';
            }
        }

        // ==================== BLOCO 2: PÚBLICO-ALVO (HORIZONTAL SLIDING CAROUSEL) ====================
        const publicoBlock = document.getElementById('block-publico');
        const publicoTrack = document.getElementById('publico-track');

        if (publicoBlock && publicoTrack) {
            const rect = publicoBlock.getBoundingClientRect();
            const blockHeight = publicoBlock.offsetHeight;
            const percent = Math.min(Math.max(-rect.top / (blockHeight - viewportHeight), 0), 1);

            if (isDesktop()) {
                // Calculate sliding percentage (from 0% to -98vw since each card is 45vw and gap is 4vw)
                const cardWidth = 45;
                const gap = 4;
                const numCards = 3;
                const travelDistance = (numCards - 1) * (cardWidth + gap); // 98vw
                const translateX = percent * -travelDistance;
                publicoTrack.style.transform = `translate3d(${translateX}vw, 0, 0)`;

                // Smooth cross-fade on entry and exit based on bounding rect
                const publicoSticky = publicoBlock.querySelector('.scrolly-sticky');
                if (publicoSticky) {
                    const entryProgress = Math.max(0, Math.min(1, (viewportHeight - rect.top) / (viewportHeight * 0.35)));
                    const exitProgress = Math.max(0, Math.min(1, rect.bottom / (viewportHeight * 0.8)));
                    publicoSticky.style.opacity = Math.min(entryProgress, exitProgress);
                }
            }
        }

        // ==================== BLOCO 3: MENTORIAS (PHOTO CROSS-FADES) ====================
        const mentoriasBlock = document.getElementById('block-mentorias');
        if (mentoriasBlock) {
            const cards = mentoriasBlock.querySelectorAll('.reveal-card-trigger');
            const centerOfViewport = viewportHeight / 2;
            
            // Smooth fade-in on entry and fade-out on exit specifically for the sticky left image column
            const rect = mentoriasBlock.getBoundingClientRect();
            const stickyLeft = mentoriasBlock.querySelector('.scrolly-sticky-left');
            if (stickyLeft) {
                if (isDesktop()) {
                    // Fade in over the first 40% of entry
                    const entryProgress = Math.max(0, Math.min(1, (viewportHeight - rect.top) / (viewportHeight * 0.4)));
                    // Fade out ONLY after unpinning and scrolling up (when rect.bottom goes from viewportHeight * 0.45 to 0)
                    const exitProgress = Math.max(0, Math.min(1, rect.bottom / (viewportHeight * 0.45)));
                    stickyLeft.style.opacity = Math.min(entryProgress, exitProgress);
                } else {
                    stickyLeft.style.opacity = 1;
                }
            }
            
            let closestCard = null;
            let minDistance = Infinity;

            cards.forEach(card => {
                const rect = card.getBoundingClientRect();
                const cardCenter = rect.top + rect.height / 2;
                const distance = Math.abs(cardCenter - centerOfViewport);

                if (distance < minDistance) {
                    minDistance = distance;
                    closestCard = card;
                }
            });

            cards.forEach(card => {
                const cardIndex = card.getAttribute('data-mentoria-index');

                // O card mais próximo do centro é ativado e ganha opacidade 1
                if (card === closestCard && minDistance < viewportHeight * 0.7) {
                    card.classList.add('active');

                    // Swaps active photo in column 1 dynamically
                    const activePhoto = document.getElementById(`mentoria-img-${cardIndex}`);
                    const activeBlur = document.getElementById(`ambient-blur-${cardIndex}`);
                    if (activePhoto) {
                        document.querySelectorAll('.scrolly-image-swap').forEach(img => img.classList.remove('active'));
                        activePhoto.classList.add('active');
                    }
                    if (activeBlur) {
                        document.querySelectorAll('.ambient-blur-img').forEach(img => img.classList.remove('active'));
                        activeBlur.classList.add('active');
                    }
                } else {
                    card.classList.remove('active');
                }
            });
        }

        // ==================== BLOCO 4: METODOLOGIA ====================
        const b4Block = document.getElementById('b4');
        const b4vp = document.getElementById('b4-vp');
        if (b4Block && b4vp) {
            if (isDesktop()) {
                const rect = b4Block.getBoundingClientRect();
                const entryProgress = Math.max(0, Math.min(1, (viewportHeight - rect.top) / (viewportHeight * 0.35)));
                const exitProgress = Math.max(0, Math.min(1, rect.bottom / (viewportHeight * 0.8)));
                b4vp.style.opacity = Math.min(entryProgress, exitProgress);
                
                // Run internal pillar progression animations
                doB4(blockProgress('b4'));
            }
        }

        // ==================== BLOCO 5: TIMELINE & CANDIDATURA REVEAL ====================
        const candidaturaBlock = document.getElementById('block-candidatura');
        const infoPanel = document.getElementById('candidatura-info-panel');
        const formPanel = document.getElementById('candidatura-form-panel');

        if (candidaturaBlock && infoPanel && formPanel) {
            const rect = candidaturaBlock.getBoundingClientRect();
            const blockHeight = candidaturaBlock.offsetHeight;
            const percent = Math.min(Math.max(-rect.top / (blockHeight - viewportHeight), 0), 1);

            if (isDesktop()) {
                // Smooth fade-in on entry and fade-out on exit using bounding rect
                const sticky = candidaturaBlock.querySelector('.scrolly-sticky');
                if (sticky) {
                    const entryProgress = Math.max(0, Math.min(1, (viewportHeight - rect.top) / (viewportHeight * 0.35)));
                    const exitProgress = Math.max(0, Math.min(1, rect.bottom / (viewportHeight * 0.8)));
                    sticky.style.opacity = Math.min(entryProgress, exitProgress);
                }
            }

            if (rect.top < viewportHeight - 120) {
                infoPanel.classList.add('revealed');
                formPanel.classList.add('revealed');
            }
        }
    };



    // --- Register global scroll listeners ---
    window.addEventListener('scroll', handleScrollytellingEngine, { passive: true });
    window.addEventListener('resize', handleScrollytellingEngine, { passive: true });
    
    // Initial run
    handleScrollytellingEngine();

    // ==========================================================================
    // IMMERSIVE WEB SKILL — INTEGRATION & LUXURY MICRO-ANIMATIONS LOGIC
    // ==========================================================================



    // --- 2. Ambient Particles System (immersive-web skill) ---
    const createParticlesField = (containerId, count = 25) => {
        const container = document.getElementById(containerId);
        if (!container) return;

        for (let i = 0; i < count; i++) {
            const p = document.createElement('div');
            p.className = 'lp-particle';

            // Random size (2px to 6px)
            const size = Math.random() * 4 + 2;
            // Random horizontal starting position (0% to 100%)
            const left = Math.random() * 100;
            // Random duration (12s to 24s)
            const dur = Math.random() * 12 + 12;
            // Random delay so particles don't all rise at once
            const delay = Math.random() * -24;
            // Random drift amplitude (-40px to +40px)
            const drift = Math.random() * 80 - 40;

            p.style.left = `${left}%`;
            p.style.width = `${size}px`;
            p.style.height = `${size}px`;
            p.style.animationDuration = `${dur}s`;
            p.style.animationDelay = `${delay}s`;
            p.style.setProperty('--drift', `${drift}px`);

            // Apply different shades of luxury gold/white color
            const colors = ['rgba(197, 164, 126, 0.3)', 'rgba(255, 255, 255, 0.25)', 'rgba(42, 125, 225, 0.15)'];
            p.style.backgroundColor = colors[Math.floor(Math.random() * colors.length)];

            container.appendChild(p);
        }
    };
    createParticlesField('hero-particles', 30);

    // --- 3. Magnetic Snapping Physics (immersive-web skill) ---
    const magneticBtns = document.querySelectorAll('.magnetic');
    magneticBtns.forEach(btn => {
        btn.addEventListener('mousemove', (e) => {
            const rect = btn.getBoundingClientRect();
            // Calculate distance between cursor and center of button
            const centerX = rect.left + rect.width / 2;
            const centerY = rect.top + rect.height / 2;
            
            // Safe physical pull weight
            const deltaX = (e.clientX - centerX) * 0.32;
            const deltaY = (e.clientY - centerY) * 0.32;

            btn.style.transform = `translate(${deltaX}px, ${deltaY}px)`;
        });

        btn.addEventListener('mouseleave', () => {
            // Snap back beautifully using custom cubic bezier
            btn.style.transform = 'translate(0px, 0px)';
            btn.style.transition = 'transform 0.45s cubic-bezier(0.25, 1.35, 0.5, 1.2)';
            setTimeout(() => {
                btn.style.transition = '';
            }, 450);
        });
    });

    // --- 4. 3D Perspective Tilt on Hover (immersive-web skill) ---
    const tiltCards = document.querySelectorAll('.card-3d');
    tiltCards.forEach(card => {
        card.addEventListener('mousemove', (e) => {
            const rect = card.getBoundingClientRect();
            // Normalize cursor position within the card boundaries (-0.5 to +0.5)
            const normalizedX = (e.clientX - rect.left) / rect.width - 0.5;
            const normalizedY = (e.clientY - rect.top) / rect.height - 0.5;

            // Rotate on Y axis based on mouse X, and X axis based on mouse Y
            const rotateY = (normalizedX * 16).toFixed(2);
            const rotateX = (-normalizedY * 16).toFixed(2);

            card.style.transform = `rotateY(${rotateY}deg) rotateX(${rotateX}deg)`;
        });

        card.addEventListener('mouseleave', () => {
            // Restore native rotation
            card.style.transform = 'rotateY(0deg) rotateX(0deg)';
        });
    });

    // --- Mobile Tabs Selector for Mentorias ---
    const tabBtns = document.querySelectorAll('.mentoria-tab-btn');
    const mentoriaCards = document.querySelectorAll('.lp-mentoria-detail-card');

    tabBtns.forEach(btn => {
        btn.addEventListener('click', () => {
            const targetTab = btn.getAttribute('data-tab');

            // Toggle active buttons
            tabBtns.forEach(b => b.classList.remove('active'));
            btn.classList.add('active');

            // Toggle active cards
            mentoriaCards.forEach(card => {
                const cardIndex = card.getAttribute('data-mentoria-index');
                if (cardIndex === targetTab) {
                    card.classList.add('mobile-active');
                    // Reset opacity for smooth transition
                    card.style.opacity = '0';
                    card.offsetHeight; // Force browser repaint reflow
                    card.style.opacity = '1';
                } else {
                    card.classList.remove('mobile-active');
                }
            });
        });
    });

});

