/**
 * WhatsApp Audio Testimonials Player & Tabs Controller
 * Dr. Henrique Leal - Medicina & Harmonização Facial
 */
document.addEventListener('DOMContentLoaded', function () {
    // ----------------------------------------------------
    // 1. TABS CONTROLLER (Audios vs Videos)
    // ----------------------------------------------------
    const tabButtons = document.querySelectorAll('.depo-tab-btn');
    const tabPanels = document.querySelectorAll('.depo-panel');

    tabButtons.forEach(btn => {
        btn.addEventListener('click', function () {
            const targetTab = this.getAttribute('data-tab');

            tabButtons.forEach(b => b.classList.remove('active'));
            this.classList.add('active');

            tabPanels.forEach(panel => {
                if (panel.id === 'panel-' + targetTab) {
                    panel.classList.remove('hidden');
                } else {
                    panel.classList.add('hidden');
                }
            });

            // If switching away from audios, pause all active audios
            if (targetTab !== 'audios') {
                pauseAllAudios();
            }
            // If switching away from videos, pause all playing videos
            if (targetTab !== 'videos') {
                document.querySelectorAll('#depoimentos video').forEach(v => v.pause());
            }
        });
    });

    // ----------------------------------------------------
    // 2. WHATSAPP VOICE NOTE AUDIO PLAYERS
    // ----------------------------------------------------
    const audioCards = document.querySelectorAll('.whatsapp-audio-card');
    let currentlyPlayingAudio = null;

    function formatTime(seconds) {
        if (isNaN(seconds) || seconds < 0) return '0:00';
        const mins = Math.floor(seconds / 60);
        const secs = Math.floor(seconds % 60);
        return mins + ':' + (secs < 10 ? '0' : '') + secs;
    }

    function pauseAllAudios() {
        audioCards.forEach(card => {
            const audio = card.querySelector('audio');
            const playBtn = card.querySelector('.wa-play-btn');
            if (audio && !audio.paused) {
                audio.pause();
            }
            if (playBtn) {
                const playIcon = playBtn.querySelector('.play-icon');
                const pauseIcon = playBtn.querySelector('.pause-icon');
                if (playIcon) playIcon.style.display = 'block';
                if (pauseIcon) pauseIcon.style.display = 'none';
            }
        });
        currentlyPlayingAudio = null;
    }

    audioCards.forEach(card => {
        const audio = card.querySelector('audio');
        const playBtn = card.querySelector('.wa-play-btn');
        const waveformWrap = card.querySelector('.wa-waveform-wrap');
        const waveformProg = card.querySelector('.wa-waveform-prog');
        const currentTimeEl = card.querySelector('.wa-current-time');
        const speedBtn = card.querySelector('.wa-speed-btn');

        if (!audio || !playBtn) return;

        const playIcon = playBtn.querySelector('.play-icon');
        const pauseIcon = playBtn.querySelector('.pause-icon');

        // Play/Pause toggle
        playBtn.addEventListener('click', function () {
            if (audio.paused) {
                // Pause any other playing audio
                if (currentlyPlayingAudio && currentlyPlayingAudio !== audio) {
                    pauseAllAudios();
                }

                // Pause any playing videos too so audio doesn't clash
                document.querySelectorAll('video').forEach(v => {
                    if (!v.paused) v.pause();
                });

                audio.play().then(() => {
                    currentlyPlayingAudio = audio;
                    if (playIcon) playIcon.style.display = 'none';
                    if (pauseIcon) pauseIcon.style.display = 'block';
                }).catch(err => {
                    console.warn('Playback prevented:', err);
                });
            } else {
                audio.pause();
                currentlyPlayingAudio = null;
                if (playIcon) playIcon.style.display = 'block';
                if (pauseIcon) pauseIcon.style.display = 'none';
            }
        });

        // Time and waveform progress update
        audio.addEventListener('timeupdate', function () {
            if (audio.duration) {
                const pct = (audio.currentTime / audio.duration) * 100;
                if (waveformProg) {
                    waveformProg.style.width = pct + '%';
                }
                if (currentTimeEl) {
                    currentTimeEl.textContent = formatTime(audio.currentTime);
                }
            }
        });

        // On audio end
        audio.addEventListener('ended', function () {
            if (waveformProg) waveformProg.style.width = '0%';
            if (currentTimeEl) currentTimeEl.textContent = '0:00';
            if (playIcon) playIcon.style.display = 'block';
            if (pauseIcon) pauseIcon.style.display = 'none';
            currentlyPlayingAudio = null;
        });

        // Click to seek on waveform
        if (waveformWrap) {
            waveformWrap.addEventListener('click', function (e) {
                const rect = waveformWrap.getBoundingClientRect();
                const clickX = e.clientX - rect.left;
                const ratio = Math.max(0, Math.min(1, clickX / rect.width));

                if (audio.duration) {
                    audio.currentTime = ratio * audio.duration;
                    if (waveformProg) {
                        waveformProg.style.width = (ratio * 100) + '%';
                    }
                    if (currentTimeEl) {
                        currentTimeEl.textContent = formatTime(audio.currentTime);
                    }
                }
            });
        }

        // Speed Toggle (1x -> 1.5x -> 2x)
        if (speedBtn) {
            const speeds = [1, 1.5, 2];
            let currentSpeedIndex = 0;

            speedBtn.addEventListener('click', function () {
                currentSpeedIndex = (currentSpeedIndex + 1) % speeds.length;
                const newSpeed = speeds[currentSpeedIndex];
                audio.playbackRate = newSpeed;
                speedBtn.textContent = newSpeed + 'x';
            });
        }
    });
});

