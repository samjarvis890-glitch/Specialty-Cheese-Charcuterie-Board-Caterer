import os
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Update header container padding
    # Find the header element and its inner container div
    pattern = r'(<header[^>]*>\s*)<div class="container mx-auto px-6 md:px-12 lg:px-24">'
    replacement = r'\1<div class="container mx-auto px-4 md:px-6 lg:px-8 xl:px-12 2xl:px-24">'
    content = re.sub(pattern, replacement, content)
    
    # Add whitespace-nowrap and reduce space on the nav
    content = content.replace(
        'class="hidden xl:flex space-x-8 rtl:space-x-reverse h-full"',
        'class="hidden xl:flex space-x-4 xl:space-x-6 2xl:space-x-8 rtl:space-x-reverse h-full whitespace-nowrap"'
    )
    
    # Also reduce space-x-4 on desktop icons to give more room if necessary
    content = content.replace(
        'class="hidden xl:flex items-center space-x-4 rtl:space-x-reverse"',
        'class="hidden xl:flex items-center space-x-2 xl:space-x-4 rtl:space-x-reverse"'
    )
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated header alignment in {len(html_files)} files.")
