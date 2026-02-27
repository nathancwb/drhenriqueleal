// ===================================================
// DR. HENRIQUE LEAL ROSA — Main JavaScript
// ===================================================

document.addEventListener('DOMContentLoaded', () => {

    // --- Splash Screen FLIP Animation ---
    const splashScreen = document.getElementById('splash-screen');
    const splashLogo = document.getElementById('splash-logo');
    const headerLogoImg = document.getElementById('header-logo-img');

    if (splashScreen && splashLogo && headerLogoImg) {
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
    }

    // --- Mobile Menu ---
    const menuToggle = document.querySelector('.menu-toggle');
    const navLinks = document.querySelector('.nav-links');

    if (menuToggle && navLinks) {
        menuToggle.addEventListener('click', () => {
            menuToggle.classList.toggle('active');
            navLinks.classList.toggle('active');
        });

        // Close on link click
        navLinks.querySelectorAll('a').forEach(link => {
            link.addEventListener('click', () => {
                menuToggle.classList.remove('active');
                navLinks.classList.remove('active');
            });
        });

        // Close on outside click
        document.addEventListener('click', (e) => {
            if (!menuToggle.contains(e.target) && !navLinks.contains(e.target)) {
                menuToggle.classList.remove('active');
                navLinks.classList.remove('active');
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

    // --- Scroll Animations (IntersectionObserver) ---
    const animatedElements = document.querySelectorAll('.fade-in, .fade-in-left, .fade-in-right');

    if (animatedElements.length > 0 && 'IntersectionObserver' in window) {
        const observer = new IntersectionObserver((entries) => {
            entries.forEach(entry => {
                if (entry.isIntersecting) {
                    entry.target.classList.add('visible');
                    observer.unobserve(entry.target);
                }
            });
        }, {
            threshold: 0.12,
            rootMargin: '0px 0px -40px 0px'
        });

        animatedElements.forEach(el => observer.observe(el));
    } else {
        // Fallback: show all
        animatedElements.forEach(el => el.classList.add('visible'));
    }

    // --- Smooth Scroll for Anchor Links ---
    document.querySelectorAll('a[href^="#"]').forEach(anchor => {
        anchor.addEventListener('click', (e) => {
            const targetId = anchor.getAttribute('href');
            if (targetId === '#') return;

            const targetEl = document.querySelector(targetId);
            if (targetEl) {
                e.preventDefault();
                const headerHeight = header ? header.offsetHeight : 0;
                const targetPos = targetEl.getBoundingClientRect().top + window.pageYOffset - headerHeight;

                window.scrollTo({
                    top: targetPos,
                    behavior: 'smooth'
                });
            }
        });
    });



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

    // --- Results Carousel Navigation ---
    const resultsCarousel = document.querySelector('.ba-carousel');
    const prevBtn = document.querySelector('.carousel-nav.prev');
    const nextBtn = document.querySelector('.carousel-nav.next');

    if (resultsCarousel && prevBtn && nextBtn) {
        const scrollAmount = 450; // Approx card width (420px) + gap (30px)
        let autoScrollInterval;

        // Manual Navigation
        prevBtn.addEventListener('click', () => {
            resultsCarousel.scrollBy({ left: -scrollAmount, behavior: 'smooth' });
            resetAutoScroll();
        });

        nextBtn.addEventListener('click', () => {
            // Check if near end
            if (resultsCarousel.scrollLeft + resultsCarousel.clientWidth >= resultsCarousel.scrollWidth - 10) {
                // Loop back to start
                resultsCarousel.scrollTo({ left: 0, behavior: 'smooth' });
            } else {
                resultsCarousel.scrollBy({ left: scrollAmount, behavior: 'smooth' });
            }
            resetAutoScroll();
        });

        // Auto Scroll Function
        const startAutoScroll = () => {
            autoScrollInterval = setInterval(() => {
                // Check if we reached the end
                if (resultsCarousel.scrollLeft + resultsCarousel.clientWidth >= resultsCarousel.scrollWidth - 10) {
                    // Loop back to start
                    resultsCarousel.scrollTo({ left: 0, behavior: 'smooth' });
                } else {
                    resultsCarousel.scrollBy({ left: scrollAmount, behavior: 'smooth' });
                }
            }, 2500); // 2.5 seconds interval
        };

        const resetAutoScroll = () => {
            clearInterval(autoScrollInterval);
            startAutoScroll();
        };

        // Pause on hover
        resultsCarousel.addEventListener('mouseenter', () => clearInterval(autoScrollInterval));
        resultsCarousel.addEventListener('mouseleave', startAutoScroll);

        // Start initially
        startAutoScroll();
    }

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

});
