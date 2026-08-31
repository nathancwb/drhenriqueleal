import glob, re

for fn in glob.glob("*.html"):
    with open(fn, "r", encoding="utf-8") as f:
        content = f.read()
    
    # Replace author-img-circle border
    content = re.sub(r'(\.author-img-circle\s*\{[^}]*?border:\s*)[^;]+;', r'\1 2.5px solid #2A7DE1 !important;', content)
    
    with open(fn, "w", encoding="utf-8") as f:
        f.write(content)

# Update generate_blog_drhenrique_brand.py
with open("scratch/generate_blog_drhenrique_brand.py", "r", encoding="utf-8") as f:
    gen = f.read()
gen = gen.replace("border: 2px solid var(--color-accent);", "border: 2.5px solid #2A7DE1 !important;")
with open("scratch/generate_blog_drhenrique_brand.py", "w", encoding="utf-8") as f:
    f.write(gen)

print("Updated author-img-circle to Royal Blue (#2A7DE1) in all files!")
