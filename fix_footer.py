import glob
import re

html_files = glob.glob('d:/Specialty Cheese  Charcuterie Board Caterer project1/*.html')
count = 0
for f in html_files:
    with open(f, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Let's find the footer grid by regex to be safe
    pattern_grid = r'(<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-12 mb-12">)'
    
    if re.search(pattern_grid, content):
        content = re.sub(pattern_grid, '<div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-12 gap-8 lg:gap-12 mb-12">', content)
        
        # Replace the divs under it
        # We need to make sure we only replace the ones right after the comments
        content = re.sub(r'<!-- Company Info -->\s*<div>', '<!-- Company Info -->\n                <div class="lg:col-span-4">', content)
        content = re.sub(r'<!-- Quick Links -->\s*<div>', '<!-- Quick Links -->\n                <div class="lg:col-span-2">', content)
        content = re.sub(r'<!-- Services -->\s*<div>', '<!-- Services -->\n                <div class="lg:col-span-3">', content)
        content = re.sub(r'<!-- Newsletter -->\s*<div>', '<!-- Newsletter -->\n                <div class="lg:col-span-3">', content)

        with open(f, 'w', encoding='utf-8') as file:
            file.write(content)
        count += 1
        print(f'Updated {f}')

print(f'Total files updated: {count}')
