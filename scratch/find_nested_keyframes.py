with open("assets/css/style.css", "r", encoding="utf-8") as f:
    css = f.read()

import re

# Find any @keyframes inside @media
# We can fix by moving all @keyframes out or lifting pulseStatus
lines = css.split('\n')
in_media = False
media_depth = 0

for idx, line in enumerate(lines):
    if '@media' in line:
        in_media = True
    if in_media and '@keyframes' in line:
        print(f"Nested @keyframes at line {idx+1}: {line}")

