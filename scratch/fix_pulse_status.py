with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

# Replace nested pulseStatus
old_block = """    @keyframes pulseStatus {
        0%, 100% {
            opacity: 1;
            transform: scale(1);
        }
        50% {
            opacity: 0.4;
            transform: scale(1.3);
        }
    }"""

new_block = """@keyframes pulseStatus {
    0%, 100% {
        opacity: 1;
        transform: scale(1);
    }
    50% {
        opacity: 0.4;
        transform: scale(1.3);
    }
}"""

css = css.replace(old_block, "")
css = css.replace("@keyframes hintPulse {", new_block + "\n\n@keyframes hintPulse {")

with open("assets/css/style.css", "w", encoding="utf-8") as f:
    f.write(css)

print("Moved @keyframes pulseStatus out of @media query!")
