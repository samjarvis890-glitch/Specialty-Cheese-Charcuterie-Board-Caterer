import re

filepath = 'index.html'
with open(filepath, 'r', encoding='utf-8') as f:
    content = f.read()

# Make all text extremely visible in dark mode
# 100, 200, 300 -> white
# 400 -> 200
# 500, 600, 700, 800 -> 300
def max_contrast(match):
    prefix = match.group(1)
    shade = int(match.group(2))
    
    if shade <= 300:
        return "dark:text-white"
    elif shade == 400:
        return "dark:text-gray-200"
    else:
        return "dark:text-gray-300"

content = re.sub(r'(dark:text-gray-)(\d00)', max_contrast, content)

# Also fix the text-gray-400 social icons that don't have dark mode set
content = content.replace('text-gray-400 hover:text-primary', 'text-gray-600 dark:text-gray-300 hover:text-primary')

with open(filepath, 'w', encoding='utf-8') as f:
    f.write(content)

print("Max contrast applied.")
