const { chromium } = require('/usr/local/lib/node_modules/playwright');
const path = require('path');
const fs = require('fs');

(async () => {
    console.log('Iniciando captura de screenshots...');
    const outputDir = '/Users/nathanmarcelosantosalmeida/.gemini/antigravity-ide/brain/02febe8f-412a-4ee7-be5f-cdd5ee78744c';
    
    if (!fs.existsSync(outputDir)) {
        fs.mkdirSync(outputDir, { recursive: true });
    }

    const browser = await chromium.launch({
        headless: true
    });
    
    const context = await browser.newContext({
        viewport: { width: 1440, height: 900 },
        deviceScaleFactor: 2
    });
    
    const page = await context.newPage();
    
    // Captura Home
    console.log('Navegando para Home...');
    await page.goto('http://localhost:8000/index.html');
    await page.waitForTimeout(1000);
    
    // Screenshot Hero
    await page.screenshot({ path: path.join(outputDir, 'screenshot_home_hero.png') });
    console.log('Hero capturado.');

    // Screenshot Full Page Home
    await page.screenshot({ path: path.join(outputDir, 'screenshot_home_full.png'), fullPage: true });
    console.log('Home completa capturada.');

    // Captura Procedimentos
    console.log('Navegando para Procedimentos...');
    await page.goto('http://localhost:8000/procedimentos.html');
    await page.waitForTimeout(1000);
    await page.screenshot({ path: path.join(outputDir, 'screenshot_procedimentos_full.png'), fullPage: true });
    console.log('Procedimentos completo capturado.');

    // Captura Resultados
    console.log('Navegando para Resultados...');
    await page.goto('http://localhost:8000/resultados.html');
    await page.waitForTimeout(1000);
    await page.screenshot({ path: path.join(outputDir, 'screenshot_resultados_full.png'), fullPage: true });
    console.log('Resultados completo capturado.');

    await browser.close();
    console.log('Capturas finalizadas com sucesso!');
})();
