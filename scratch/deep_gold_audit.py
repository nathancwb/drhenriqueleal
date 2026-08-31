import re, glob

gold_patterns = [
    r'#c5a47e', r'#c9a227', r'#d4af37', r'#ffdf73', r'#d4a017', r'#b8966c', 
    r'#e5c07b', r'#ffd700', r'rgba?\(\s*212\s*,\s*175\s*,\s*55',
    r'rgba?\(\s*201\s*,\s*162\s*,\s*39', r'rgba?\(\s*197\s*,\s*164\s*,\s*126'
]

files = glob.glob("**/*.html", recursive=True) + glob.glob("**/*.css", recursive=True) + glob.glob("**/*.js", recursive=True)

findings = []
for fn in files:
    if "node_modules" in fn or ".git" in fn or "scratch/check_cases" in fn:
        continue
    try:
        with open(fn, "r", encoding="utf-8") as f:
            lines = f.readlines()
        for idx, line in enumerate(lines, 1):
            for pat in gold_patterns:
                if re.search(pat, line, re.IGNORECASE):
                    findings.append((fn, idx, line.strip()))
    except Exception as e:
        pass

print(f"Total occurrences found: {len(findings)}")
for f in findings:
    print(f"{f[0]}:{f[1]} -> {f[2]}")
