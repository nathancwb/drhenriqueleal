// ===================================================
// DR. HENRIQUE LEAL ROSA — LP Conversão Interactions
// Carousel, Accordion, Dynamic WhatsApp CTAs
// ===================================================

document.addEventListener('DOMContentLoaded', () => {

    // --- 1. Results Carousel Touch & Drag ---
    const track = document.getElementById('lpCarouselTrack');
    const prevBtn = document.getElementById('lpPrevBtn');
    const nextBtn = document.getElementById('lpNextBtn');

    if (track && prevBtn && nextBtn) {
        let currentPos = 0;
        const cardWidth = 404; // 380px + 24px gap

        const getMaxScroll = () => {
            return track.scrollWidth - track.parentElement.clientWidth;
        };

        const updatePosition = () => {
            const maxScroll = getMaxScroll();
            if (currentPos > 0) currentPos = 0;
            if (currentPos < -maxScroll) currentPos = -maxScroll;
            track.style.transform = `translateX(${currentPos}px)`;
        };

        nextBtn.addEventListener('click', () => {
            currentPos -= cardWidth;
            updatePosition();
        });

        prevBtn.addEventListener('click', () => {
            currentPos += cardWidth;
            updatePosition();
        });

        // Touch & Drag Support
        let isDown = false;
        let startX;
        let scrollLeftPos;

        track.addEventListener('mousedown', (e) => {
            isDown = true;
            startX = e.pageX - track.offsetLeft;
            scrollLeftPos = currentPos;
        });

        track.addEventListener('mouseleave', () => isDown = false);
        track.addEventListener('mouseup', () => isDown = false);

        track.addEventListener('mousemove', (e) => {
            if (!isDown) return;
            e.preventDefault();
            const x = e.pageX - track.offsetLeft;
            const walk = (x - startX) * 1.2;
            currentPos = scrollLeftPos + walk;
            updatePosition();
        });

        // Mobile Touch Events
        track.addEventListener('touchstart', (e) => {
            isDown = true;
            startX = e.touches[0].pageX - track.offsetLeft;
            scrollLeftPos = currentPos;
        }, { passive: true });

        track.addEventListener('touchend', () => isDown = false);

        track.addEventListener('touchmove', (e) => {
            if (!isDown) return;
            const x = e.touches[0].pageX - track.offsetLeft;
            const walk = (x - startX) * 1.2;
            currentPos = scrollLeftPos + walk;
            updatePosition();
        }, { passive: true });
    }

    // --- 2. FAQ Accordion ---
    const faqItems = document.querySelectorAll('.lp-faq-item');

    faqItems.forEach(item => {
        const btn = item.querySelector('.lp-faq-question');
        const answer = item.querySelector('.lp-faq-answer');

        if (btn && answer) {
            btn.addEventListener('click', () => {
                const isOpen = item.classList.contains('active');

                faqItems.forEach(other => {
                    if (other !== item) {
                        other.classList.remove('active');
                        const otherAns = other.querySelector('.lp-faq-answer');
                        if (otherAns) otherAns.style.maxHeight = null;
                    }
                });

                if (isOpen) {
                    item.classList.remove('active');
                    answer.style.maxHeight = null;
                } else {
                    item.classList.add('active');
                    answer.style.maxHeight = answer.scrollHeight + 'px';
                }
            });
        }
    });

});
