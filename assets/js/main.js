// ===================================================
// DR. HENRIQUE LEAL ROSA — Main JavaScript
// ===================================================

document.addEventListener('DOMContentLoaded', () => {

    // --- Splash Screen FLIP Animation ---
    const splashScreen = document.getElementById('splash-screen');
    const splashLogo = document.getElementById('splash-logo');
    const headerLogoImg = document.getElementById('header-logo-img');

    if (splashScreen && splashLogo && headerLogoImg) {
        // Check if splash has already played in this session
        const splashPlayed = sessionStorage.getItem('splashPlayed');

        if (!splashPlayed) {
            // First time: run animation
            sessionStorage.setItem('splashPlayed', 'true');
            document.body.classList.add('splash-active');

            // Wait for logo image to load
            const startSplash = () => {
                // Hold for 1.5 seconds
                setTimeout(() => {
                    // Get positions for FLIP
                    const splashRect = splashLogo.getBoundingClientRect();
                    const headerRect = headerLogoImg.getBoundingClientRect();

                    // Calculate scale ratio
                    const scaleX = headerRect.width / splashRect.width;
                    const scaleY = headerRect.height / splashRect.height;
                    const scale = Math.min(scaleX, scaleY);

                    // Calculate translation (center of splash logo to center of header logo)
                    const splashCenterX = splashRect.left + splashRect.width / 2;
                    const splashCenterY = splashRect.top + splashRect.height / 2;
                    const headerCenterX = headerRect.left + headerRect.width / 2;
                    const headerCenterY = headerRect.top + headerRect.height / 2;

                    const dx = headerCenterX - splashCenterX;
                    const dy = headerCenterY - splashCenterY;

                    // Apply FLIP transform
                    splashLogo.style.transform = `translate(${dx}px, ${dy}px) scale(${scale})`;

                    // After animation, fade out splash
                    setTimeout(() => {
                        splashScreen.classList.add('fade-out');

                        setTimeout(() => {
                            splashScreen.remove();
                            document.body.classList.remove('splash-active');
                        }, 600);
                    }, 1200);
                }, 1500);
            };

            if (splashLogo.complete) {
                startSplash();
            } else {
                splashLogo.addEventListener('load', startSplash);
            }
        } else {
            // Already played: remove splash immediately
            splashScreen.remove();
        }
    }

    // --- Mobile Menu ---
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (menuToggle && navLinks) {
        let backdrop = document.querySelector('.nav-backdrop');
        if (!backdrop) {
            backdrop = document.createElement('div');
            backdrop.className = 'nav-backdrop';
            document.body.appendChild(backdrop);
        }

        const toggleMenu = (open) => {
            const shouldOpen = typeof open === 'boolean' ? open : !navLinks.classList.contains('active');
            menuToggle.classList.toggle('active', shouldOpen);
            navLinks.classList.toggle('active', shouldOpen);
            backdrop.classList.toggle('active', shouldOpen);
            document.body.style.overflow = shouldOpen ? 'hidden' : '';
        };

        menuToggle.addEventListener('click', (e) => {
            e.stopPropagation();
            toggleMenu();
        });

        backdrop.addEventListener('click', () => toggleMenu(false));

        // Close on link click
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => toggleMenu(false));
        });

        // Close on escape key
        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && navLinks.classList.contains('active')) {
                toggleMenu(false);
            }
        });
    }

    // --- Sticky Header ---
    const header = document.querySelector('.header');
    if (header) {
        const handleScroll = () => {
            if (window.scrollY > 60) {
                header.classList.add('scrolled');
            } else {
                header.classList.remove('scrolled');
            }
        };
        window.addEventListener('scroll', handleScroll, { passive: true });
        handleScroll();
    }

    // --- FAQ Accordions ---
    const faqItems = document.querySelectorAll('.faq-item');
    faqItems.forEach(item => {
        const question = item.querySelector('.faq-question');
        if (question) {
            question.addEventListener('click', () => {
                const isActive = item.classList.contains('active');

                // Close all
                faqItems.forEach(i => i.classList.remove('active'));

                // Open clicked (if wasn't active)
                if (!isActive) {
                    item.classList.add('active');
                }
            });
        }
    });

    // --- Cinematic Scroll Motion Engine (IntersectionObserver) ---
    const animatedSelectors = [
        '.fade-in',
        '.fade-in-left',
        '.fade-in-right',
        '.reveal-scale',
        '.reveal-curtain',
        '.section-header',
        '.results-card',
        '.proc-card-simple',
        '.diff-card',
        '.faq-item',
        '.authority-pill',
        '.about-feature-item',
        '.legal-notice-banner'
    ];

    // Assign stagger indices to grid children for cascading entrances
    document.querySelectorAll('.procedures-grid, .results-grid, .differentials-grid, .faq-list, .authority-badges-grid').forEach(grid => {
        Array.from(grid.children).forEach((child, idx) => {
            child.style.setProperty('--stagger-idx', (idx % 6) + 1);
            if (!child.classList.contains('fade-in') && !child.classList.contains('fade-in-left') && !child.classList.contains('fade-in-right')) {
                child.classList.add('fade-in');
            }
        });
    });

    const animatedElements = document.querySelectorAll(animatedSelectors.join(', '));

    if (animatedElements.length > 0 && 'IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.08,
            rootMargin: '0px 0px -30px 0px'
        });

        animatedElements.forEach(el => observer.observe(el));
    } else {
        animatedElements.forEach(el => el.classList.add('visible'));
    }



    // --- Procedures Modal ---
    const procModal = document.getElementById('proc-modal');
    const procCards = document.querySelectorAll('.proc-card-simple');
    const modalTitle = document.getElementById('modal-title');
    const modalBody = document.getElementById('modal-body');
    const modalClose = document.querySelector('.modal-close');
    // Select the CTA button in the modal to update its link dynamically if needed (optional)
    const modalCta = document.querySelector('.modal-cta');

    if (procModal && procCards.length > 0) {

        // Open Modal
        procCards.forEach(card => {
            card.addEventListener('click', () => {
                const category = card.getAttribute('data-category');
                const details = card.getAttribute('data-details');

                if (modalTitle) modalTitle.textContent = category;
                if (modalBody) modalBody.innerHTML = details;

                // Update WhatsApp link text based on category
                if (modalCta) {
                    const message = encodeURIComponent(`Olá, tenho interesse em ${category}.`);
                    modalCta.href = `https://wa.me/5541988577430?text=${message}`;
                }

                procModal.showModal();
                procModal.classList.add('open'); // For CSS transition if needed
                document.body.style.overflow = 'hidden'; // Prevent body scroll
            });
        });

        // Close Modal Function
        const closeModal = () => {
            procModal.close();
            procModal.classList.remove('open');
            document.body.style.overflow = '';
        };

        // Close on button click
        if (modalClose) {
            modalClose.addEventListener('click', closeModal);
        }

        // Close on click outside (backdrop)
        procModal.addEventListener('click', (e) => {
            const rect = procModal.getBoundingClientRect();
            const isInDialog = (rect.top <= e.clientY && e.clientY <= rect.top + rect.height &&
                rect.left <= e.clientX && e.clientX <= rect.left + rect.width);

            // Checking if click is on the backdrop (dialog itself) vs content
            // <dialog> backdrop usually covers the viewport. 
            // If click target is the dialog element itself, it's the backdrop.
            if (e.target === procModal) {
                closeModal();
            }
        });
    }

    // --- Carousels Navigation ---
    const carouselWrappers = document.querySelectorAll('.carousel-wrapper');
    
    carouselWrappers.forEach(wrapper => {
        const carousel = wrapper.querySelector('.depoimentos-carousel, .video-carousel');
        const prevBtn = wrapper.querySelector('.carousel-nav.prev');
        const nextBtn = wrapper.querySelector('.carousel-nav.next');
        
        if (carousel && prevBtn && nextBtn) {
            let autoScrollInterval;
            let isVideoPlaying = false;
            
            // Manual Navigation
            prevBtn.addEventListener('click', () => {
                const scrollAmount = carousel.clientWidth * 0.8;
                carousel.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
                resetAutoScroll();
            });

            nextBtn.addEventListener('click', () => {
                const scrollAmount = carousel.clientWidth * 0.8;
                if (carousel.scrollLeft + carousel.clientWidth >= carousel.scrollWidth - 10) {
                    carousel.scrollTo({ left: 0, behavior: 'smooth' });
                } else {
                    carousel.scrollBy({ left: scrollAmount, behavior: 'smooth' });
                }
                resetAutoScroll();
            });

            // Auto Scroll Function
            const startAutoScroll = () => {
                if (isVideoPlaying) return;
                autoScrollInterval = setInterval(() => {
                    if (isVideoPlaying) return;
                    const scrollAmount = carousel.clientWidth * 0.8;
                    if (carousel.scrollLeft + carousel.clientWidth >= carousel.scrollWidth - 10) {
                        carousel.scrollTo({ left: 0, behavior: 'smooth' });
                    } else {
                        carousel.scrollBy({ left: scrollAmount, behavior: 'smooth' });
                    }
                }, 4000); // Increased time slightly for better readability
            };

            const resetAutoScroll = () => {
                clearInterval(autoScrollInterval);
                startAutoScroll();
            };

            // Pause on hover
            carousel.addEventListener('mouseenter', () => clearInterval(autoScrollInterval));
            carousel.addEventListener('mouseleave', startAutoScroll);

            // Stop auto-scroll if a video is playing inside this carousel
            const videos = carousel.querySelectorAll('video');
            videos.forEach(video => {
                video.addEventListener('play', () => {
                    isVideoPlaying = true;
                    clearInterval(autoScrollInterval);
                });
                video.addEventListener('pause', () => {
                    isVideoPlaying = false;
                    startAutoScroll();
                });
                video.addEventListener('ended', () => {
                    isVideoPlaying = false;
                    startAutoScroll();
                });
            });

            // Start initially
            startAutoScroll();
        }
    });

    // --- Procedures Carousel Auto-Scroll (Gentle Movement) ---
    const procCarousel = document.querySelector('.proc-carousel');
    if (procCarousel) {
        let procAutoScroll;
        const speed = 1; // Pixels per interval
        let direction = 1; // 1 = right, -1 = left
        let isHovered = false;

        const startProcScroll = () => {
            procAutoScroll = setInterval(() => {
                if (isHovered) return;

                // Scroll
                procCarousel.scrollLeft += speed * direction;

                // Bounce at ends
                if (procCarousel.scrollLeft + procCarousel.clientWidth >= procCarousel.scrollWidth - 1) {
                    direction = -1; // Go left
                } else if (procCarousel.scrollLeft <= 0) {
                    direction = 1; // Go right
                }
            }, 50); // smooth tick
        };

        // Only auto-scroll if it's actually scrollable
        if (procCarousel.scrollWidth > procCarousel.clientWidth) {
            // startProcScroll(); // Optional: user requested "mini movement", but continuous scroll might be annoying.
            // Let's do a "nudge" animation instead as it's more subtle.

            setTimeout(() => {
                procCarousel.scrollBy({ left: 30, behavior: 'smooth' });
                setTimeout(() => {
                    procCarousel.scrollBy({ left: -30, behavior: 'smooth' });
                }, 1000);
            }, 2000);
        }

        // For now, I'll stick to the requested "mini movement" as a nudge on load, 
        // OR a very slow drift? User asked for "mini movimentacao".
        // A slow drift is often elegant.

        let driftInterval;
        const startDrift = () => {
            driftInterval = setInterval(() => {
                if (procCarousel.matches(':hover')) return;

                // Drift right slowly
                if (procCarousel.scrollLeft + procCarousel.clientWidth < procCarousel.scrollWidth) {
                    procCarousel.scrollLeft += 0.5;
                } else {
                    // Reset to start if reached end (infinite feel) or bounce?
                    // Let's just stop or bounce.
                    // Simple bounce:
                    if (procCarousel.scrollLeft + procCarousel.clientWidth >= procCarousel.scrollWidth - 1) {
                        procCarousel.scrollTo({ left: 0, behavior: 'smooth' });
                    }
                }
            }, 30);
        };

        // Note: Continuous JS scroll on main thread can be jerky. CSS animation is better but complex with scroll snap.
        // Let's implement the simpler "Nudge" to indicate scrollability, as user said "mini movimentacao".
        // A continuous slow scroll is often annoying for clicking.

        // Implementation: Nudge on load + Interval Nudge
        setInterval(() => {
            if (!procCarousel.matches(':hover')) {
                procCarousel.scrollBy({ left: 10, behavior: 'smooth' });
                setTimeout(() => procCarousel.scrollBy({ left: -10, behavior: 'smooth' }), 500);
            }
        }, 5000);

    }

    // --- Expandable Procedure Cards ---
    const expandCards = document.querySelectorAll('[data-expand-card]');
    if (expandCards.length > 0) {
        expandCards.forEach(card => {
            // Desktop: hover to expand
            card.addEventListener('mouseenter', () => {
                expandCards.forEach(c => c.classList.remove('active'));
                card.classList.add('active');
            });

            // Mobile & Desktop Click Logic
            card.style.cursor = 'pointer';
            card.addEventListener('click', (e) => {
                // If clicked on the actual link, let it happen naturally
                if (e.target.classList.contains('expand-card-link')) {
                    return;
                }
                
                if (window.innerWidth <= 768) {
                    if (!card.classList.contains('active')) {
                        e.preventDefault();
                        expandCards.forEach(c => c.classList.remove('active'));
                        card.classList.add('active');
                    } else {
                        window.location.href = 'procedimentos.html';
                    }
                } else {
                    window.location.href = 'procedimentos.html';
                }
            });
        });
    }

    // --- Procedures Grid Filtering ---
    const filterBtns = document.querySelectorAll('.filter-btn');
    const procItems = document.querySelectorAll('.proc-glass-item');

    if (filterBtns.length > 0 && procItems.length > 0) {
        filterBtns.forEach(btn => {
            btn.addEventListener('click', () => {
                // Remove active class
                filterBtns.forEach(b => b.classList.remove('active'));
                btn.classList.add('active');

                const filterValue = btn.getAttribute('data-filter');

                procItems.forEach(item => {
                    if (filterValue === 'all') {
                        item.classList.remove('hidden');
                    } else {
                        const categories = item.getAttribute('data-category').split(' ');
                        if (categories.includes(filterValue)) {
                            item.classList.remove('hidden');
                        } else {
                            item.classList.add('hidden');
                        }
                    }
                });
            });
        });
    }

    // --- Card Lightbox para Antes e Depois ---
    const cardLightbox = document.getElementById('card-lightbox');
    const cardLightboxBody = document.getElementById('card-lightbox-body');
    const cardLightboxClose = document.querySelector('.card-lightbox-close');

    if (cardLightbox && cardLightboxBody) {
        const baCards = document.querySelectorAll('.ba-card');
        
        const openCardLightbox = (card) => {
            // Clone the card's inner content (procedure name + images)
            cardLightboxBody.innerHTML = '';
            const clone = card.cloneNode(true);
            // Remove the fade-in class to avoid animation conflicts
            clone.classList.remove('fade-in');
            cardLightboxBody.appendChild(clone);
            cardLightbox.classList.add('active');
            document.body.style.overflow = 'hidden';
        };

        const closeCardLightbox = () => {
            cardLightbox.classList.remove('active');
            document.body.style.overflow = '';
            setTimeout(() => { cardLightboxBody.innerHTML = ''; }, 300);
        };

        baCards.forEach(card => {
            card.style.cursor = 'pointer';

            // Mobile: touchstart/touchend to detect taps vs scrolls
            let touchStartX = 0;
            let touchStartY = 0;
            let touchStartTime = 0;

            card.addEventListener('touchstart', (e) => {
                touchStartX = e.touches[0].clientX;
                touchStartY = e.touches[0].clientY;
                touchStartTime = Date.now();
            }, { passive: true });

            card.addEventListener('touchend', (e) => {
                const touch = e.changedTouches[0];
                const dx = Math.abs(touch.clientX - touchStartX);
                const dy = Math.abs(touch.clientY - touchStartY);
                const dt = Date.now() - touchStartTime;

                // Only open if it was a tap (small movement, quick touch)
                if (dx < 15 && dy < 15 && dt < 400) {
                    e.preventDefault();
                    openCardLightbox(card);
                }
            });

            // Desktop: normal click
            card.addEventListener('click', () => {
                if (window.innerWidth > 768) {
                    openCardLightbox(card);
                }
            });
        });

        // Close handlers
        if (cardLightboxClose) {
            cardLightboxClose.addEventListener('click', closeCardLightbox);
        }

        cardLightbox.addEventListener('click', (e) => {
            if (e.target === cardLightbox) {
                closeCardLightbox();
            }
        });

        document.addEventListener('keydown', (e) => {
            if (e.key === 'Escape' && cardLightbox.classList.contains('active')) {
                closeCardLightbox();
            }
        });
    }

    // --- Dynamic Watermark Injection & Anti-Copy Protection ---
    
    // Inject watermark overlay divs into all before/after images
    const injectWatermarks = () => {
        const containers = document.querySelectorAll('.ba-image');
        containers.forEach(container => {
            if (!container.querySelector('.watermark-overlay')) {
                const overlay = document.createElement('div');
                overlay.className = 'watermark-overlay';
                container.appendChild(overlay);
            }
        });
    };
    
    // Inject immediately on load
    injectWatermarks();
    
    // Re-run inject when lightbox dynamic content is loaded/updated
    if (cardLightbox) {
        const observer = new MutationObserver(() => {
            injectWatermarks();
        });
        observer.observe(cardLightboxBody, { childList: true, subtree: true });
    }

    // Disable right-click context menu on protected images/overlays
    document.addEventListener('contextmenu', (e) => {
        const isProtected = e.target.classList.contains('watermark-overlay') || 
                            e.target.closest('.ba-image') || 
                            e.target.closest('.ba-card');
        if (isProtected) {
            e.preventDefault();
            showCopyrightToast();
        }
    });

    // Prevent dragging on images
    document.addEventListener('dragstart', (e) => {
        if (e.target.tagName === 'IMG' && (e.target.closest('.ba-card') || e.target.closest('#card-lightbox-body'))) {
            e.preventDefault();
        }
    });

    // Custom Toast Notification with Gold Accent (matching Dr. Henrique Leal VIP branding)
    function showCopyrightToast() {
        let toast = document.getElementById('copyright-toast');
        if (!toast) {
            toast = document.createElement('div');
            toast.id = 'copyright-toast';
            toast.style.cssText = `
                position: fixed;
                bottom: 30px;
                left: 50%;
                transform: translateX(-50%) translateY(100px);
                background-color: #0b1528; /* deep midnight blue */
                color: #FFFFFF;
                padding: 14px 28px;
                border-radius: 8px;
                font-family: 'Inter', sans-serif;
                font-size: 0.85rem;
                font-weight: 500;
                box-shadow: 0 10px 30px rgba(0, 0, 0, 0.5);
                z-index: 20000;
                transition: transform 0.4s cubic-bezier(0.16, 1, 0.3, 1), opacity 0.4s;
                opacity: 0;
                pointer-events: none;
                text-align: center;
                border-left: 4px solid #2A7DE1; /* Gold accent */
                border-right: 1px solid rgba(42, 125, 225, 0.15);
                border-top: 1px solid rgba(42, 125, 225, 0.15);
                border-bottom: 1px solid rgba(42, 125, 225, 0.15);
                max-width: 90%;
                line-height: 1.4;
            `;
            toast.innerHTML = 'Aviso: Uso não autorizado das imagens de pacientes é proibido por lei (Direitos Autorais)';
            document.body.appendChild(toast);
        }
        
        toast.style.opacity = '1';
        toast.style.transform = 'translateX(-50%) translateY(0)';
        
        clearTimeout(toast.timeoutId);
        toast.timeoutId = setTimeout(() => {
            toast.style.opacity = '0';
            toast.style.transform = 'translateX(-50%) translateY(100px)';
        }, 3000);
    }

    // --- Lenis Smooth Inertia Scrolling ---
    if (typeof Lenis !== 'undefined') {
        const lenis = new Lenis({
            duration: 1.25,
            easing: (t) => Math.min(1, 1.001 - Math.pow(2, -10 * t)),
            orientation: 'vertical',
            gestureOrientation: 'vertical',
            smoothWheel: true,
            wheelMultiplier: 0.95,
            touchMultiplier: 1.5,
            infinite: false,
        });

        function raf(time) {
            lenis.raf(time);
            requestAnimationFrame(raf);
        }
        requestAnimationFrame(raf);

        // Smooth anchor scrolling
        document.querySelectorAll('a[href^="#"]').forEach(anchor => {
            anchor.addEventListener('click', function (e) {
                const targetId = this.getAttribute('href');
                if (targetId && targetId !== '#' && targetId.length > 1) {
                    const targetEl = document.querySelector(targetId);
                    if (targetEl) {
                        e.preventDefault();
                        lenis.scrollTo(targetEl, { offset: -70, duration: 1.2 });
                    }
                }
            });
        });
    }

    // --- 3D Interactive Photo & Card Tilt Engine ---
    const tiltElements = document.querySelectorAll(
        '.about-authority-portrait, .hero-doctor-img, .faq-image, .google-rating-summary'
    );

    tiltElements.forEach(el => {
        el.classList.add('tilt-3d');

        // Add specular glare overlay if not present
        if (!el.querySelector('.tilt-glare')) {
            const glare = document.createElement('div');
            glare.className = 'tilt-glare';
            el.appendChild(glare);
        }

        let bounds;
        function updateBounds() {
            bounds = el.getBoundingClientRect();
        }

        function onMouseMove(e) {
            if (!bounds) updateBounds();
            const mouseX = e.clientX - bounds.left;
            const mouseY = e.clientY - bounds.top;

            const xPct = mouseX / bounds.width;
            const yPct = mouseY / bounds.height;

            const xOffset = (xPct - 0.5) * 2; // -1 to 1
            const yOffset = (yPct - 0.5) * 2; // -1 to 1

            const rotateX = -yOffset * 8; // max 8 deg
            const rotateY = xOffset * 8; // max 8 deg

            el.style.transform = `perspective(1000px) rotateX(${rotateX}deg) rotateY(${rotateY}deg) scale3d(1.02, 1.02, 1.02)`;
            el.style.setProperty('--mouse-x', `${xPct * 100}%`);
            el.style.setProperty('--mouse-y', `${yPct * 100}%`);
        }

        function onMouseLeave() {
            el.style.transition = 'transform 0.5s cubic-bezier(0.16, 1, 0.3, 1)';
            el.style.transform = 'perspective(1000px) rotateX(0deg) rotateY(0deg) scale3d(1, 1, 1)';
        }

        function onMouseEnter() {
            updateBounds();
            el.style.transition = 'transform 0.1s ease-out';
        }

        el.addEventListener('mouseenter', onMouseEnter);
        el.addEventListener('mousemove', onMouseMove);
        el.addEventListener('mouseleave', onMouseLeave);
    });

    // ===================================================
    // INTERACTIVE BEFORE & AFTER SLIDER (Desktop & Mobile)
    // ===================================================
    const baContainer = document.getElementById('baCompareContainer');
    const baAfterWrap = document.getElementById('baAfterWrap');
    const baHandle = document.getElementById('baHandle');
    const baImgAntes = document.getElementById('baImgAntes');
    const baImgDepois = document.getElementById('baImgDepois');
    const baTabs = document.querySelectorAll('#baTabs .ba-tab-btn');

    if (baContainer && baAfterWrap && baHandle && baImgAntes && baImgDepois) {
        let isPointerActive = false;

        function updateOverlayImageSize() {
            const containerWidth = baContainer.offsetWidth;
            const containerHeight = baContainer.offsetHeight;
            if (containerWidth > 0) {
                baImgDepois.style.width = containerWidth + 'px';
                baImgDepois.style.minWidth = containerWidth + 'px';
                baImgDepois.style.maxWidth = containerWidth + 'px';
                if (containerHeight > 0) {
                    baImgDepois.style.height = containerHeight + 'px';
                }
            }
        }

        window.addEventListener('resize', updateOverlayImageSize);
        window.addEventListener('orientationchange', updateOverlayImageSize);
        // Also run on load and after short timeout for webfont/layout stabilization
        updateOverlayImageSize();
        setTimeout(updateOverlayImageSize, 100);

        // Prevent native browser image drag
        baContainer.querySelectorAll('img').forEach(img => {
            img.setAttribute('draggable', 'false');
            img.ondragstart = () => false;
        });

        function setSliderPosition(clientX) {
            const rect = baContainer.getBoundingClientRect();
            let x = clientX - rect.left;
            let percentage = (x / rect.width) * 100;
            if (percentage < 0) percentage = 0;
            if (percentage > 100) percentage = 100;

            baAfterWrap.style.width = percentage + '%';
            baHandle.style.left = percentage + '%';
        }

        // PointerEvents (Mouse, Touch, Stylus unified)
        baContainer.addEventListener('pointerdown', (e) => {
            isPointerActive = true;
            try {
                baContainer.setPointerCapture(e.pointerId);
            } catch (err) {}
            setSliderPosition(e.clientX);
            e.preventDefault();
        });

        baContainer.addEventListener('pointermove', (e) => {
            if (!isPointerActive) return;
            setSliderPosition(e.clientX);
            e.preventDefault();
        });

        function stopPointer(e) {
            if (isPointerActive) {
                isPointerActive = false;
                try {
                    if (e && e.pointerId) baContainer.releasePointerCapture(e.pointerId);
                } catch (err) {}
            }
        }

        baContainer.addEventListener('pointerup', stopPointer);
        baContainer.addEventListener('pointercancel', stopPointer);
        baContainer.addEventListener('lostpointercapture', stopPointer);

        // Click anywhere to jump slider
        baContainer.addEventListener('click', (e) => {
            setSliderPosition(e.clientX);
        });

        // Tab Switching between clinical cases
        baTabs.forEach(tab => {
            tab.addEventListener('click', () => {
                baTabs.forEach(t => t.classList.remove('active'));
                tab.classList.add('active');

                const antesSrc = tab.getAttribute('data-antes');
                const depoisSrc = tab.getAttribute('data-depois');

                baImgAntes.style.opacity = '0.4';
                baImgDepois.style.opacity = '0.4';

                setTimeout(() => {
                    baImgAntes.src = antesSrc;
                    baImgDepois.src = depoisSrc;
                    updateOverlayImageSize();
                    baImgAntes.style.opacity = '1';
                    baImgDepois.style.opacity = '1';

                    baAfterWrap.style.transition = 'width 0.4s cubic-bezier(0.16, 1, 0.3, 1)';
                    baHandle.style.transition = 'left 0.4s cubic-bezier(0.16, 1, 0.3, 1)';
                    baAfterWrap.style.width = '50%';
                    baHandle.style.left = '50%';
                    setTimeout(() => {
                        baAfterWrap.style.transition = '';
                        baHandle.style.transition = '';
                    }, 400);
                }, 150);
            });
        });

        // Initial image load ensure sizing
        baImgAntes.addEventListener('load', updateOverlayImageSize);
        baImgDepois.addEventListener('load', updateOverlayImageSize);
    }

    // ===================================================
    // COUNT-UP ANIMATION FOR METRICS (+1.200 / 5.0)
    // ===================================================
    const counters = document.querySelectorAll('[data-count-target]');
    if (counters.length > 0) {
        const counterObserver = new IntersectionObserver((entries, observer) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    const el = entry.target;
                    const target = parseInt(el.getAttribute('data-count-target'), 10);
                    const prefix = el.getAttribute('data-prefix') || '';
                    const suffix = el.getAttribute('data-suffix') || '';
                    const duration = 1800;
                    const startTime = performance.now();

                    function updateCount(currentTime) {
                        const elapsed = currentTime - startTime;
                        const progress = Math.min(elapsed / duration, 1);
                        // Ease out cubic
                        const easeOut = 1 - Math.pow(1 - progress, 3);
                        const currentVal = Math.floor(easeOut * target);

                        if (target >= 1000) {
                            el.textContent = `${prefix}${currentVal.toLocaleString('pt-BR')}${suffix}`;
                        } else {
                            el.textContent = `${prefix}${currentVal}${suffix}`;
                        }

                        if (progress < 1) {
                            requestAnimationFrame(updateCount);
                        } else {
                            if (target >= 1000) {
                                el.textContent = `${prefix}${target.toLocaleString('pt-BR')}${suffix}`;
                            } else {
                                el.textContent = `${prefix}${target}${suffix}`;
                            }
                        }
                    }

                    requestAnimationFrame(updateCount);
                    observer.unobserve(el);
                }
            });
        }, { threshold: 0.2 });

        counters.forEach(c => counterObserver.observe(c));
    }

    // ===================================================
    // MOBILE FLOATING STICKY CTA BAR TRIGGER
    // ===================================================
    const mobileStickyBar = document.getElementById('mobileStickyBar');
    const heroSection = document.getElementById('hero');

    if (mobileStickyBar && heroSection) {
        function checkMobileSticky() {
            const scrollPos = window.pageYOffset || document.documentElement.scrollTop || window.scrollY || 0;
            const heroHeight = heroSection.offsetHeight || 500;
            if (scrollPos > heroHeight * 0.5) {
                mobileStickyBar.classList.add('visible');
            } else {
                mobileStickyBar.classList.remove('visible');
            }
        }

        window.addEventListener('scroll', checkMobileSticky, { passive: true });
        window.addEventListener('touchmove', checkMobileSticky, { passive: true });
        if (typeof lenis !== 'undefined') {
            lenis.on('scroll', checkMobileSticky);
        }
        checkMobileSticky();
    }

});

