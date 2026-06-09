const { chromium } = require('/usr/local/lib/node_modules/playwright');
const fs = require('fs');
const https = require('https');
const path = require('path');

(async () => {
    console.log('Iniciando o navegador...');
    const browser = await chromium.launch({
        executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        headless: true
    });
    
    const context = await browser.newContext({
        viewport: { width: 1280, height: 800 },
        userAgent: 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'
    });
    
    const page = await context.newPage();
    const url = 'https://www.instagram.com/reels/DYhnfBHRdyb/';
    console.log(`Navegando para: ${url}`);
    
    try {
        await page.goto(url, { waitUntil: 'networkidle', timeout: 30000 });
        console.log('Página carregada. Procurando elemento de vídeo...');
        
        // Espera pelo seletor de vídeo
        await page.waitForSelector('video', { timeout: 15000 });
        
        // Extrai todas as URLs de vídeo na página
        const videoSources = await page.evaluate(() => {
            const videos = Array.from(document.querySelectorAll('video'));
            return videos.map(v => ({
                src: v.getAttribute('src'),
                type: v.getAttribute('type'),
                id: v.getAttribute('id')
            }));
        });
        
        console.log('Vídeos encontrados na página:', JSON.stringify(videoSources, null, 2));
        
        if (videoSources.length > 0) {
            console.log('Vídeo encontrado! Iniciando a reprodução e a captura de frames...');
            
            // Iniciar a reprodução do vídeo
            await page.evaluate(() => {
                const videos = document.querySelectorAll('video');
                videos.forEach(v => {
                    v.muted = true;
                    v.play().catch(e => console.log('Erro ao iniciar vídeo:', e.message));
                });
            });
            
            // Capturar 10 frames em intervalos de 800ms
            const outputDir = '/Users/nathanalmeida/.gemini/antigravity/brain/dee3a385-7da7-4b5b-ba43-53bfd98e0ceb';
            console.log('Capturando frames sequenciais...');
            
            for (let i = 1; i <= 10; i++) {
                await page.waitForTimeout(800);
                const framePath = path.join(outputDir, `reel_frame_${i}.png`);
                
                // Tirar print de toda a área visível do viewport (que conterá o vídeo centralizado)
                await page.screenshot({ path: framePath });
                console.log(`Frame ${i} salvo em: ${framePath}`);
            }
            
            console.log('Captura de frames concluída com sucesso!');
        } else {
            console.log('Nenhum vídeo encontrado na página.');
        }
    } catch (error) {
        console.error('Erro durante a execução:', error);
        const screenshotPath = path.join('/Users/nathanalmeida/.gemini/antigravity/brain/dee3a385-7da7-4b5b-ba43-53bfd98e0ceb', 'error_screenshot.png');
        await page.screenshot({ path: screenshotPath });
        console.log(`Screenshot de erro salva em: ${screenshotPath}`);
    } finally {
        await browser.close();
    }
})();
