const { chromium } = require('/usr/local/lib/node_modules/playwright');
const path = require('path');

(async () => {
    console.log('Iniciando o navegador...');
    // Lançando o Google Chrome instalado no sistema ou o Chromium padrão
    const browser = await chromium.launch({
        executablePath: '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome',
        headless: true
    });
    
    const context = await browser.newContext({
        viewport: { width: 1280, height: 800 },
        deviceScaleFactor: 2 // Retorna prints em alta definição (retina)
    });
    
    const page = await context.newPage();
    
    // Capturar logs do console e erros da página
    page.on('console', msg => console.log('PAGE LOG:', msg.text()));
    page.on('pageerror', err => console.error('PAGE ERROR:', err.message));
    
    const filePath = 'file://' + path.resolve(__dirname, 'cursos-vip.html');
    console.log(`Navegando para: ${filePath}`);
    
    await page.goto(filePath);
    
    // Esperar um pouco para carregar a página
    await page.waitForTimeout(1000);
    
    // Função para remover a splash screen instantaneamente
    const dismissSplash = async () => {
        await page.evaluate(() => {
            // Desativar scroll suave temporariamente para prints precisos instantâneos
            document.documentElement.style.scrollBehavior = 'auto';
            if (document.body) {
                document.body.style.scrollBehavior = 'auto';
            }
            
            const splash = document.getElementById('splash-screen');
            if (splash) splash.remove();
            document.body.classList.remove('splash-active');
        });
    };
    
    const outputDir = '/Users/nathanalmeida/.gemini/antigravity/brain/dee3a385-7da7-4b5b-ba43-53bfd98e0ceb';
    
    // Print 1: Hero Fase 1 (sem scroll)
    await dismissSplash();
    await page.waitForTimeout(500);
    console.log('Capturando Hero - Fase 1...');
    await page.screenshot({ path: path.join(outputDir, 'screenshot_hero_fase1.png') });
    
    // Scroll para revelar o Hero Fase 2
    // A seção Hero tem scroll-sticky, vamos rolar para baixo cerca de 400px
    console.log('Scroll para Hero - Fase 2...');
    await page.evaluate(() => window.scrollTo(0, 500));
    await page.waitForTimeout(500);
    await page.screenshot({ path: path.join(outputDir, 'screenshot_hero_fase2.png') });
    
    // Scroll para Público Alvo
    // Rolar mais para baixo para ver a seção de público-alvo
    console.log('Scroll para Público Alvo...');
    await page.evaluate(() => {
        const el = document.getElementById('block-publico');
        if (el) el.scrollIntoView();
    });
    await page.waitForTimeout(500);
    await page.screenshot({ path: path.join(outputDir, 'screenshot_publico_dentistas.png') });
    
    // Rolar dentro da seção de público alvo para ver a segunda fase (biomédicos)
    console.log('Scroll para Público Alvo - Fase 2 (Biomédicos)...');
    await page.evaluate(() => window.scrollBy(0, 600));
    await page.waitForTimeout(500);
    await page.screenshot({ path: path.join(outputDir, 'screenshot_publico_biomedicos.png') });
    
    // Scroll para Mentorias
    console.log('Scroll para Mentorias - Fios de PDO...');
    await page.evaluate(() => {
        const el = document.getElementById('block-mentorias');
        if (el) el.scrollIntoView();
    });
    await page.waitForTimeout(500);
    await page.screenshot({ path: path.join(outputDir, 'screenshot_mentorias_1.png') });
    
    // Rolar para ver a segunda mentoria
    console.log('Scroll para Mentorias - Harmonização Íntima...');
    await page.evaluate(() => window.scrollBy(0, 800));
    await page.waitForTimeout(500);
    await page.screenshot({ path: path.join(outputDir, 'screenshot_mentorias_2.png') });
    
    // Scroll para Metodologia
    console.log('Scroll para Metodologia...');
    await page.evaluate(() => {
        const el = document.getElementById('block-metodologia');
        if (el) el.scrollIntoView();
    });
    await page.evaluate(() => window.scrollBy(0, 300));
    await page.waitForTimeout(500);
    await page.screenshot({ path: path.join(outputDir, 'screenshot_metodologia.png') });
    
    // Scroll para Candidatura
    console.log('Scroll para Candidatura...');
    await page.evaluate(() => {
        const el = document.getElementById('block-candidatura');
        if (el) el.scrollIntoView();
    });
    await page.waitForTimeout(500);
    await page.screenshot({ path: path.join(outputDir, 'screenshot_candidatura.png') });
    
    // Scroll para FAQ e Mapa
    console.log('Scroll para FAQ e Mapa...');
    await page.evaluate(() => {
        const el = document.getElementById('lp-static-info');
        if (el) el.scrollIntoView();
    });
    await page.waitForTimeout(500);
    await page.screenshot({ path: path.join(outputDir, 'screenshot_faq_mapa.png') });
    
    console.log('Captura de prints concluída com sucesso!');
    await browser.close();
})();
