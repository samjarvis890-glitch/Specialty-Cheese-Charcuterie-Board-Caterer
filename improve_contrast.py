import re
import os

filepath = 'index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Function to make text-gray shades lighter in dark mode
def improve_contrast(match):
    prefix = match.group(1)
    shade = int(match.group(2))
    # Make it brighter by subtracting 100 (e.g. 400 -> 300)
    new_shade = max(100, shade - 100)
    return f"{prefix}{new_shade}"

# Replace dark:text-gray-XXX
content = re.sub(r'(dark:text-gray-)(\d00)', improve_contrast, content)

# Also improve text-gray-300 that are used directly on dark backgrounds
content = content.replace('"text-gray-300 ', '"text-gray-200 ')
content = content.replace(' text-gray-300 ', ' text-gray-200 ')
content = content.replace(' text-gray-300"', ' text-gray-200"')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Contrast improved successfully.")
