const fs = require('fs');
const css = fs.readFileSync('assets/css/style.css', 'utf8');

// Check for unclosed @media or @keyframes or braces
let depth = 0;
let lines = css.split('\n');
for (let i = 0; i < lines.length; i++) {
    let l = lines[i];
    for (let c of l) {
        if (c === '{') depth++;
        if (c === '}') depth--;
    }
    if (depth < 0) {
        console.log(`Error at line ${i+1}: negative brace depth`);
        break;
    }
}
console.log(`Final brace depth: ${depth}, total lines: ${lines.length}`);
