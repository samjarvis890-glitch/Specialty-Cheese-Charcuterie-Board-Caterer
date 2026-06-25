import glob
import re

html_files = glob.glob('*.html')

# The current HTML for Home 1 and Home 2 is:
# <a href="index.html" class="block border-b border-gray-100 px-5 py-4 transition-colors hover:bg-gray-50 dark:border-gray-700 dark:hover:bg-gray-700">
#     <div class="font-semibold text-gray-900 dark:text-white">Home 1 – Editorial Experience</div>
# ...
# <a href="board-builder.html" class="block px-5 py-4 transition-colors hover:bg-gray-50 dark:hover:bg-gray-700">
#     <div class="font-semibold text-gray-900 dark:text-white">Home 2 – Build Your Board</div>

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # We will use regex to find the links and add group/item and group-hover/item:text-primary
    
    # Home 1 link replacement
    h1_pattern = r'<a href="index\.html" class="block border-b border-gray-100 px-5 py-4 transition-colors hover:bg-gray-50 dark:border-gray-700 dark:hover:bg-gray-700">\s*<div class="font-semibold text-gray-900 dark:text-white">Home 1 – Editorial Experience</div>'
    h1_replacement = '''<a href="index.html" class="group/item block border-b border-gray-100 px-5 py-4 transition-colors hover:bg-gray-50 dark:border-gray-700 dark:hover:bg-gray-700">
                                    <div class="font-semibold text-gray-900 dark:text-white group-hover/item:text-primary transition-colors">Home 1 – Editorial Experience</div>'''
    
    # Home 2 link replacement
    h2_pattern = r'<a href="board-builder\.html" class="block px-5 py-4 transition-colors hover:bg-gray-50 dark:hover:bg-gray-700">\s*<div class="font-semibold text-gray-900 dark:text-white">Home 2 – Build Your Board</div>'
    h2_replacement = '''<a href="board-builder.html" class="group/item block px-5 py-4 transition-colors hover:bg-gray-50 dark:hover:bg-gray-700">
                                    <div class="font-semibold text-gray-900 dark:text-white group-hover/item:text-primary transition-colors">Home 2 – Build Your Board</div>'''
                                    
    # Also fix mobile menu links just in case
    # <a href="index.html" class="block text-gray-600 dark:text-white">Home 1 – Editorial Experience</a>
    mob_h1_pattern = r'<a href="index\.html" class="block text-gray-600 dark:text-white">Home 1 – Editorial Experience</a>'
    mob_h1_replacement = r'<a href="index.html" class="block text-gray-600 dark:text-white hover:text-primary transition-colors">Home 1 – Editorial Experience</a>'
    
    mob_h2_pattern = r'<a href="board-builder\.html" class="block text-gray-600 dark:text-white">Home 2 – Build Your Board</a>'
    mob_h2_replacement = r'<a href="board-builder.html" class="block text-gray-600 dark:text-white hover:text-primary transition-colors">Home 2 – Build Your Board</a>'

    new_content = re.sub(h1_pattern, h1_replacement, content)
    new_content = re.sub(h2_pattern, h2_replacement, new_content)
    new_content = re.sub(mob_h1_pattern, mob_h1_replacement, new_content)
    new_content = re.sub(mob_h2_pattern, mob_h2_replacement, new_content)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)

print('Updated hover colors for Home 1 and Home 2')
