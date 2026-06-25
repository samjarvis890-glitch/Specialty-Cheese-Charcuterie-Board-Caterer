import glob
import re

html_files = glob.glob('*.html')

pattern = r'<!-- Dropdown Wrapper[^>]*>.*?<!-- Inner Dropdown[^>]*>.*?<div class="w-80 overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-xl dark:border-gray-700 dark:bg-gray-800">'

replacement = '''<!-- Dropdown Wrapper -->
                        <div class="absolute left-0 top-full z-50 hidden group-hover:block">
                            <!-- Inner Dropdown -->
                            <div class="mt-2 w-80 overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-xl dark:border-gray-700 dark:bg-gray-800">'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # We also need to match the version I replaced previously
    # It might look like this:
    # <!-- Dropdown Wrapper (No translation, no gap) -->
    # <div class="absolute left-0 top-full z-50 pt-2 opacity-0 invisible transition-all duration-300 group-hover:opacity-100 group-hover:visible">
    #     <!-- Inner Dropdown -->
    #     <div class="w-80 overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-xl dark:border-gray-700 dark:bg-gray-800">

    # Let's just use a more generic regex that grabs from "<!-- Dropdown Wrapper" up to the inner div.
    regex = r'<!-- Dropdown Wrapper.*?<!-- Inner Dropdown.*?<div class="w-80 overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-xl dark:border-gray-700 dark:bg-gray-800[^>]*>'
    
    new_content = re.sub(regex, replacement, content, flags=re.DOTALL)
    
    with open(file, 'w', encoding='utf-8') as f:
        f.write(new_content)

print('Updated dropdowns to foolproof hidden/block')
