const http = require('http');
const fs = require('fs');
const path = require('path');

// Test suite for Agent Readiness & Ora Audit Criteria
async function runTests() {
    console.log('🧪 Iniciando Verificação de Prontidão para Agentes (Is Agentic Readiness Test)...\n');

    let allPassed = true;

    // Helper to make HTTP request
    function fetchUrl(urlPath, headers = {}) {
        return new Promise((resolve, reject) => {
            const req = http.request({
                hostname: '127.0.0.1',
                port: 8055,
                path: urlPath,
                method: 'GET',
                headers: headers
            }, (res) => {
                let data = '';
                res.on('data', chunk => data += chunk);
                res.on('end', () => {
                    resolve({
                        statusCode: res.statusCode,
                        headers: res.headers,
                        body: data
                    });
                });
            });
            req.on('error', reject);
            req.end();
        });
    }

    try {
        // --- TEST 1: Agent-Friendly 404s ---
        console.log('--- Teste 1: 404s Amigáveis para Agentes ---');
        const res404Html = await fetchUrl('/caminho-que-nao-existe-xyz');
        if (res404Html.statusCode === 404) {
            console.log('  ✅ [PASS] Caminho inexistente retorna status HTTP 404');
        } else {
            console.error(`  ❌ [FAIL] Esperado 404, recebido: ${res404Html.statusCode}`);
            allPassed = false;
        }

        const res404Md = await fetchUrl('/caminho-que-nao-existe-xyz', { 'Accept': 'text/markdown' });
        if (res404Md.statusCode === 404 && res404Md.headers['content-type']?.includes('text/markdown') && res404Md.body.includes('sitemap.xml')) {
            console.log('  ✅ [PASS] 404 com Accept: text/markdown retorna Markdown estruturado com links de recuperação');
        } else {
            console.error('  ❌ [FAIL] 404 Markdown inválido:', res404Md.headers['content-type'], res404Md.statusCode);
            allPassed = false;
        }

        // --- TEST 2: Markdown Content Negotiation (acceptmarkdown.com) ---
        console.log('\n--- Teste 2: Negociação de Conteúdo Markdown (acceptmarkdown.com) ---');
        const resHomeMd = await fetchUrl('/', { 'Accept': 'text/markdown' });
        if (resHomeMd.statusCode === 200 && resHomeMd.headers['content-type']?.includes('text/markdown')) {
            console.log('  ✅ [PASS] Requisitar / com Accept: text/markdown retorna text/markdown; charset=utf-8');
        } else {
            console.error('  ❌ [FAIL] Falha em Accept: text/markdown na home:', resHomeMd.headers['content-type']);
            allPassed = false;
        }

        if (resHomeMd.headers['vary'] && resHomeMd.headers['vary'].includes('Accept')) {
            console.log(`  ✅ [PASS] Cabeçalho Vary presente com Accept: "${resHomeMd.headers['vary']}"`);
        } else {
            console.error(`  ❌ [FAIL] Cabeçalho Vary faltando Accept: "${resHomeMd.headers['vary']}"`);
            allPassed = false;
        }

        const resHomeHtml = await fetchUrl('/');
        if (resHomeHtml.headers['vary'] && resHomeHtml.headers['vary'].includes('Accept')) {
            console.log(`  ✅ [PASS] Resposta HTML padrão inclui Vary: "${resHomeHtml.headers['vary']}" para segurança de cache`);
        } else {
            console.error(`  ❌ [FAIL] Resposta HTML sem Vary Accept: "${resHomeHtml.headers['vary']}"`);
            allPassed = false;
        }

        // --- TEST 3: Trust Anchor Pages (> 500 chars) ---
        console.log('\n--- Teste 3: Páginas de Confiança (Trust Anchors) ---');
        const trustPages = [
            { path: '/sobre', name: 'Sobre (/sobre)' },
            { path: '/about', name: 'About (/about)' },
            { path: '/contato', name: 'Contato (/contato)' },
            { path: '/contact', name: 'Contact (/contact)' },
            { path: '/privacidade', name: 'Privacidade (/privacidade)' },
            { path: '/privacy', name: 'Privacy (/privacy)' },
            { path: '/termos', name: 'Termos (/termos)' },
            { path: '/terms', name: 'Terms (/terms)' }
        ];

        for (const page of trustPages) {
            const res = await fetchUrl(page.path);
            const charCount = res.body.length;
            if (res.statusCode === 200 && charCount >= 500) {
                console.log(`  ✅ [PASS] ${page.name}: Status 200 OK (${charCount} caracteres)`);
            } else {
                console.error(`  ❌ [FAIL] ${page.name}: Status ${res.statusCode} (${charCount} caracteres)`);
                allPassed = false;
            }
        }

        // --- TEST 4: Agent Instructions & When-to-Use ---
        console.log('\n--- Teste 4: Instruções para Agentes (llms.txt / agent-instructions.md) ---');
        const llmsTxt = fs.readFileSync(path.join(__dirname, '../llms.txt'), 'utf-8');
        const agentInst = fs.readFileSync(path.join(__dirname, '../agent-instructions.md'), 'utf-8');

        if (llmsTxt.includes('Quando Recomendar') && llmsTxt.includes('When to Use This') && llmsTxt.includes('When NOT to Use')) {
            console.log('  ✅ [PASS] llms.txt contém seções bilíngues de Quando Recomendar / When to Use e When NOT to Use');
        } else {
            console.error('  ❌ [FAIL] llms.txt faltando seções de orientação');
            allPassed = false;
        }

        if (agentInst.includes('Agent Instructions') && agentInst.includes('When to Use This')) {
            console.log('  ✅ [PASS] agent-instructions.md existe e contém diretrizes formais para IAs');
        } else {
            console.error('  ❌ [FAIL] agent-instructions.md incompleto');
            allPassed = false;
        }

        // --- TEST 5: JSON-LD Structured Data & Metadata Completeness ---
        console.log('\n--- Teste 5: Metadados & Dados Estruturados JSON-LD ---');
        const indexHtml = fs.readFileSync(path.join(__dirname, '../index.html'), 'utf-8');

        if (indexHtml.includes('<link rel="canonical" href="https://drhenriqueleal.com.br/">')) {
            console.log('  ✅ [PASS] Canonical URL presente na página inicial');
        } else {
            console.error('  ❌ [FAIL] Canonical URL faltando na página inicial');
            allPassed = false;
        }

        if (indexHtml.includes('<html lang="pt-BR">')) {
            console.log('  ✅ [PASS] Tag html lang="pt-BR" presente');
        } else {
            console.error('  ❌ [FAIL] Tag html lang faltando');
            allPassed = false;
        }

        if (indexHtml.includes('og:image') && indexHtml.includes('og:type') && indexHtml.includes('twitter:card')) {
            console.log('  ✅ [PASS] Tags Open Graph (og:image, og:type) e Twitter Card completas');
        } else {
            console.error('  ❌ [FAIL] Tags sociais incompletas');
            allPassed = false;
        }

        // Extract JSON-LD
        const jsonLdMatch = indexHtml.match(/<script type="application\/ld\+json">([\s\S]*?)<\/script>/);
        if (jsonLdMatch) {
            const parsedJsonLd = JSON.parse(jsonLdMatch[1]);
            const graph = parsedJsonLd['@graph'];
            const person = graph.find(item => item['@type'] === 'Person');
            const medical = graph.find(item => Array.isArray(item['@type']) ? item['@type'].includes('MedicalBusiness') : item['@type'] === 'MedicalBusiness');

            if (person && person.name && person.description && person.jobTitle && person.url) {
                console.log(`  ✅ [PASS] JSON-LD Person completo: "${person.name}" - ${person.description.substring(0, 60)}...`);
            } else {
                console.error('  ❌ [FAIL] JSON-LD Person incompleto:', person);
                allPassed = false;
            }

            if (medical && medical.name && medical.address && medical.telephone && medical.geo) {
                console.log(`  ✅ [PASS] JSON-LD MedicalBusiness/Clinic completo: "${medical.name}" no Água Verde, Curitiba`);
            } else {
                console.error('  ❌ [FAIL] JSON-LD MedicalBusiness incompleto:', medical);
                allPassed = false;
            }
        } else {
            console.error('  ❌ [FAIL] JSON-LD não encontrado no index.html');
            allPassed = false;
        }

        console.log('\n=============================================');
        if (allPassed) {
            console.log('🎉 TODOS OS TESTES PASSARAM COM SUCESSO! 100% PRONTO PARA AGENTES.');
        } else {
            console.log('⚠️ ALGUNS TESTES APRESENTARAM FALHAS.');
        }
        console.log('=============================================\n');

    } catch (err) {
        console.error('Erro durante a execução dos testes:', err);
    }
}

runTests();
