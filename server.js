const http = require('http');
const fs = require('fs');
const path = require('path');
const url = require('url');

const PORT = process.env.PORT || 8055;
const PUBLIC_DIR = __dirname;

const MIME_TYPES = {
    '.html': 'text/html; charset=utf-8',
    '.md': 'text/markdown; charset=utf-8',
    '.css': 'text/css; charset=utf-8',
    '.js': 'application/javascript; charset=utf-8',
    '.json': 'application/json; charset=utf-8',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.jpeg': 'image/jpeg',
    '.webp': 'image/webp',
    '.svg': 'image/svg+xml',
    '.ico': 'image/x-icon',
    '.mp4': 'video/mp4',
    '.webm': 'video/webm',
    '.xml': 'application/xml',
    '.txt': 'text/plain; charset=utf-8',
    '.woff2': 'font/woff2',
    '.woff': 'font/woff',
    '.ttf': 'font/ttf'
};

const server = http.createServer((req, res) => {
    // Parse URL with standard WHATWG URL API
    const reqUrl = new URL(req.url, `http://${req.headers.host || 'localhost'}`);
    let pathname = decodeURIComponent(reqUrl.pathname);

    const acceptHeader = (req.headers.accept || '').toLowerCase();
    const wantsMarkdown = acceptHeader.includes('text/markdown') || acceptHeader.includes('text/x-markdown');

    // Clean Path resolution
    let cleanPath = pathname.replace(/\/$/, '');
    if (cleanPath === '' || cleanPath === '/index') {
        cleanPath = '/index';
    }

    let resolvedFile = null;

    // 1. Content Negotiation: Check if client specifically wants Markdown
    if (wantsMarkdown) {
        // Direct .md file exists?
        const mdCandidate = path.join(PUBLIC_DIR, cleanPath + '.md');
        if (fs.existsSync(mdCandidate) && fs.statSync(mdCandidate).isFile()) {
            resolvedFile = mdCandidate;
        } else if (cleanPath === '/index' && fs.existsSync(path.join(PUBLIC_DIR, 'llms.txt'))) {
            resolvedFile = path.join(PUBLIC_DIR, 'llms.txt');
        }
    }

    // 2. Standard HTML / Static File Resolution
    if (!resolvedFile) {
        let filePath = path.join(PUBLIC_DIR, pathname === '/' ? '/index.html' : pathname);

        if (!path.extname(filePath)) {
            if (fs.existsSync(filePath + '.html')) {
                filePath += '.html';
            } else if (fs.existsSync(path.join(filePath, 'index.html'))) {
                filePath = path.join(filePath, 'index.html');
            }
        }

        if (fs.existsSync(filePath) && fs.statSync(filePath).isFile()) {
            resolvedFile = filePath;
        }
    }

    // 3. Handle 404 (Non-existent path)
    if (!resolvedFile) {
        const error404Md = path.join(PUBLIC_DIR, '404.md');
        const error404Html = path.join(PUBLIC_DIR, '404.html');

        if (wantsMarkdown && fs.existsSync(error404Md)) {
            const content = fs.readFileSync(error404Md);
            res.writeHead(404, {
                'Content-Type': 'text/markdown; charset=utf-8',
                'Content-Length': Buffer.byteLength(content),
                'Vary': 'Accept, Accept-Encoding',
                'Cache-Control': 'no-cache'
            });
            res.end(content);
            return;
        }

        if (fs.existsSync(error404Html)) {
            const content = fs.readFileSync(error404Html);
            res.writeHead(404, {
                'Content-Type': 'text/html; charset=utf-8',
                'Content-Length': Buffer.byteLength(content),
                'Vary': 'Accept, Accept-Encoding',
                'Cache-Control': 'no-cache'
            });
            res.end(content);
            return;
        }

        res.writeHead(404, {
            'Content-Type': 'text/plain; charset=utf-8',
            'Vary': 'Accept, Accept-Encoding'
        });
        res.end('# 404 — Página Não Encontrada\nConsulte o sitemap em: https://drhenriqueleal.com.br/sitemap.xml ou llms.txt');
        return;
    }

    // 4. Serve Found File
    fs.stat(resolvedFile, (err, stats) => {
        if (err || !stats.isFile()) {
            res.writeHead(404, { 'Content-Type': 'text/html; charset=utf-8', 'Vary': 'Accept, Accept-Encoding' });
            res.end('<h1>404 — Página não encontrada</h1>');
            return;
        }

        const ext = path.extname(resolvedFile).toLowerCase();
        const contentType = MIME_TYPES[ext] || 'application/octet-stream';

        // Support HTTP Range requests for MP4 video streaming
        const range = req.headers.range;
        if (range && (ext === '.mp4' || ext === '.webm')) {
            const parts = range.replace(/bytes=/, "").split("-");
            const start = parseInt(parts[0], 10);
            const end = parts[1] ? parseInt(parts[1], 10) : stats.size - 1;
            const chunksize = (end - start) + 1;
            const fileStream = fs.createReadStream(resolvedFile, { start, end });

            res.writeHead(206, {
                'Content-Range': `bytes ${start}-${end}/${stats.size}`,
                'Accept-Ranges': 'bytes',
                'Content-Length': chunksize,
                'Content-Type': contentType,
                'Cache-Control': 'public, max-age=3600',
                'Vary': 'Accept, Accept-Encoding'
            });
            fileStream.pipe(res);
            return;
        }

        // Normal file response with Vary: Accept, Accept-Encoding for CDN/cache safety
        res.writeHead(200, {
            'Content-Type': contentType,
            'Content-Length': stats.size,
            'Accept-Ranges': 'bytes',
            'Vary': 'Accept, Accept-Encoding',
            'Cache-Control': (ext === '.html' || ext === '.md' || ext === '.txt') ? 'no-cache' : 'public, max-age=86400'
        });

        fs.createReadStream(resolvedFile).pipe(res);
    });
});

server.listen(PORT, '0.0.0.0', () => {
    console.log(`🚀 Ultra-fast Node server with Content Negotiation on http://localhost:${PORT}/`);
});
