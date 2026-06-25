import os
import glob
import re

html_files = glob.glob('*.html')

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Change tailwind primary color to blue
    content = content.replace("DEFAULT: '#D4AF37'", "DEFAULT: '#2563EB'")
    content = content.replace("dark: '#b5952f'", "dark: '#1D4ED8'")
    
    # 2. Change css variable in case they use it
    content = content.replace("var(--color-primary)", "#2563EB")
    
    # 3. Change favicon color
    content = content.replace("fill='%23D4AF37'", "fill='%232563EB'")

    # 4. Fix dropdown nav. The issue is likely pointer-events-none and hover gaps.
    # We will replace the dropdown wrapper with a simpler version.
    
    old_dropdown = '''<!-- Dropdown Wrapper (No translation, no gap) -->
                        <div class="absolute left-0 top-full z-50 pt-4 opacity-0 pointer-events-none transition-opacity duration-300 group-hover:opacity-100 group-hover:pointer-events-auto">
                            <!-- Inner Dropdown (Has translation) -->
                            <div class="w-80 overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-xl dark:border-gray-700 dark:bg-gray-800 transform translate-y-2 transition-transform duration-300 ease-out group-hover:translate-y-0">'''
                            
    new_dropdown = '''<!-- Dropdown Wrapper (No translation, no gap) -->
                        <div class="absolute left-0 top-full z-50 pt-2 opacity-0 invisible transition-all duration-300 group-hover:opacity-100 group-hover:visible">
                            <!-- Inner Dropdown -->
                            <div class="w-80 overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-xl dark:border-gray-700 dark:bg-gray-800">'''

    content = content.replace(old_dropdown, new_dropdown)
    
    # Just in case there's another variation, let's use regex
    # find the dropdown wrapper
    pattern1 = r'<!-- Dropdown Wrapper[^>]*>\s*<div class="absolute left-0 top-full z-50 pt-4 opacity-0 pointer-events-none transition-opacity duration-300 group-hover:opacity-100 group-hover:pointer-events-auto">\s*<!-- Inner Dropdown[^>]*>\s*<div class="w-80 overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-xl dark:border-gray-700 dark:bg-gray-800 transform translate-y-2 transition-transform duration-300 ease-out group-hover:translate-y-0">'
    
    replacement1 = '''<!-- Dropdown Wrapper -->
                        <div class="absolute left-0 top-full z-50 pt-2 opacity-0 invisible transition-all duration-300 group-hover:opacity-100 group-hover:visible">
                            <!-- Inner Dropdown -->
                            <div class="w-80 overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-xl dark:border-gray-700 dark:bg-gray-800">'''
                            
    content = re.sub(pattern1, replacement1, content)
    
    # What if the user also wants the mobile dropdown fixed?
    # mobile dropdown works with javascript usually.

    with open(file, 'w', encoding='utf-8') as f:
        f.write(content)

print('Done updating HTML files.')
