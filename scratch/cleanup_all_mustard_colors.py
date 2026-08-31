# -*- coding: utf-8 -*-
import glob, re, os, shutil

# 1. Remove any leftover template directories in scratch
template_dir = "scratch/blog_template"
if os.path.exists(template_dir):
    shutil.rmtree(template_dir)
    print("Removed scratch/blog_template directory.")

# 2. Clean style.css
with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

css = css.replace("#2A7DE1", "#2A7DE1")
css = css.replace("#2A7DE1", "#2A7DE1")
css = css.replace("#FFFFFF", "#FFFFFF")
css = css.replace("#FFFFFF", "#FFFFFF")
css = css.replace("#2A7DE1", "#2A7DE1")
css = css.replace("#1E6BC9", "#1E6BC9")

with open("assets/css/style.css", "w", encoding="utf-8") as f:
    f.write(css)
print("Cleaned style.css of all mustard/yellow shades -> replaced with #2A7DE1 / #FFFFFF.")

# 3. Clean all HTML files
html_files = glob.glob("*.html")
cleaned_count = 0

for fn in html_files:
    with open(fn, "r", encoding="utf-8") as f:
        content = f.read()
    
    orig = content
    # Replace all mustard hex codes
    content = re.sub(r'#2A7DE1', '#2A7DE1', content, flags=re.IGNORECASE)
    content = re.sub(r'#1E6BC9', '#1E6BC9', content, flags=re.IGNORECASE)
    content = re.sub(r'#2A7DE1', '#2A7DE1', content, flags=re.IGNORECASE)
    content = re.sub(r'#2A7DE1', '#2A7DE1', content, flags=re.IGNORECASE)
    content = re.sub(r'#FFFFFF', '#FFFFFF', content, flags=re.IGNORECASE)
    content = re.sub(r'--color-accent: #2A7DE1;]+;', '--color-accent: #2A7DE1;', content)
    content = content.replace("var(--color-accent)", "var(--color-accent)")
    
    # Remove any inline yellow button styles
    content = re.sub(r'background:\s*#2A7DE1[^;]*;', 'background: #2A7DE1;', content, flags=re.IGNORECASE)
    content = re.sub(r'background-color:\s*#2A7DE1[^;]*;', 'background-color: #2A7DE1;', content, flags=re.IGNORECASE)
    content = re.sub(r'color:\s*#1B3A5C;\s*font-weight:\s*700;\s*border:\s*none;\s*background:\s*#2A7DE1', 'color: #FFFFFF; font-weight: 700; border: none; background: #2A7DE1', content)
    
    if content != orig:
        cleaned_count += 1
        with open(fn, "w", encoding="utf-8") as f:
            f.write(content)

print(f"Cleaned {cleaned_count} HTML files of any mustard/yellow colors!")

# 4. Also update python generators
for gen in glob.glob("scratch/*.py"):
    with open(gen, "r", encoding="utf-8") as f:
        c = f.read()
    c = re.sub(r'#2A7DE1', '#2A7DE1', c, flags=re.IGNORECASE)
    c = re.sub(r'#1E6BC9', '#1E6BC9', c, flags=re.IGNORECASE)
    c = re.sub(r'#2A7DE1', '#2A7DE1', c, flags=re.IGNORECASE)
    c = re.sub(r'#2A7DE1', '#2A7DE1', c, flags=re.IGNORECASE)
    c = re.sub(r'#FFFFFF', '#FFFFFF', c, flags=re.IGNORECASE)
    c = re.sub(r'--color-accent: #2A7DE1;]+;', '--color-accent: #2A7DE1;', c)
    c = c.replace("var(--color-accent)", "var(--color-accent)")
    with open(gen, "w", encoding="utf-8") as f:
        f.write(c)

print("Updated python generator scripts.")
