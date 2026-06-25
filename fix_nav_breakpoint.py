import os
import glob

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Replace the desktop nav
    content = content.replace('class="hidden lg:flex space-x-8 rtl:space-x-reverse h-full"', 'class="hidden xl:flex space-x-8 rtl:space-x-reverse h-full"')
    
    # Replace the desktop icons
    content = content.replace('class="hidden lg:flex items-center space-x-4 rtl:space-x-reverse"', 'class="hidden xl:flex items-center space-x-4 rtl:space-x-reverse"')
    
    # Replace the mobile menu button
    content = content.replace('<div class="lg:hidden flex items-center">', '<div class="xl:hidden flex items-center">')
    
    # Replace the mobile menu overlay
    content = content.replace('transition-transform duration-300 lg:hidden overflow-y-auto"', 'transition-transform duration-300 xl:hidden overflow-y-auto"')
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print(f"Updated {len(html_files)} files.")
