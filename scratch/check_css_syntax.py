with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Check curly braces balance
open_braces = 0
line_no = 1
errors = []

for i, char in enumerate(css):
    if char == '\n':
        line_no += 1
    elif char == '{':
        open_braces += 1
    elif char == '}':
        open_braces -= 1
        if open_braces < 0:
            errors.append(f"Extra closing brace at line {line_no}")
            open_braces = 0

print(f"Total lines: {line_no}, Open braces at EOF: {open_braces}")
if errors:
    print("Errors:", errors[:5])
