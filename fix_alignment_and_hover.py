import os
import glob
import re

html_files = [
    'about.html',
    'blog.html',
    'catering.html',
    'contact.html',
    'gallery.html',
    'wine-pairings.html'
]

for filename in html_files:
    if not os.path.exists(filename):
        continue
    
    with open(filename, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find the hero text container and add text-center
    # Usually it's something like <div class="relative z-10 px-6 ...">
    # Let's just blindly add text-center to the main container inside the hero section
    # Wait, it's safer to find the h1 tag inside the hero and its parent div.
    # Alternatively, I can just do a regex replace for the known hero text containers.
    # We will search for 'relative z-10' or 'relative z-10 max-w-4xl' etc inside the hero
    
    # We will replace `class="relative z-10 max-w-4xl` with `class="relative z-10 max-w-4xl text-center mx-auto` if it's missing text-center.
    # Also some might have `text-left`. We should replace `text-left` with `text-center`.

    # Simple approach: Replace `text-left` with `text-center` inside the first 200 lines.
    # Or just replace `text-left` with `text-center` for the Hero container.
    
    # In Catering, it was left aligned. Let's replace `text-left` with `text-center`.
    content = re.sub(r'(<!-- Hero.*?)(text-left)(.*?</section>)', r'\1text-center mx-auto\3', content, flags=re.DOTALL | re.IGNORECASE)
    
    # Also add text-center if neither text-left nor text-center exists in the z-10 container
    def add_center(match):
        classes = match.group(2)
        if 'text-center' not in classes and 'text-left' not in classes:
            return f'{match.group(1)}{classes} text-center mx-auto{match.group(3)}'
        return match.group(0)

    content = re.sub(r'(<!-- Hero.*?<div class="relative z-10[^>]*?class=")([^"]*)(".*?</section>)', add_center, content, flags=re.DOTALL | re.IGNORECASE)

    # Let's just replace `text-left` with `text-center` globally for any hero text container
    # Since I'm not sure of the exact markup, I'll do a robust replacement:
    
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

# Fix hover contrast in index.html
if os.path.exists('index.html'):
    with open('index.html', 'r', encoding='utf-8') as f:
        idx_content = f.read()
    
    # Task 20: hero CTA
    idx_content = idx_content.replace('hover:text-gray-900', 'hover:!text-gray-900')
    
    # Task 21: pricing CTA
    idx_content = idx_content.replace('hover:text-primary mt-auto', 'hover:!text-primary mt-auto')

    with open('index.html', 'w', encoding='utf-8') as f:
        f.write(idx_content)

# Fix hover contrast in pricing.html as well
if os.path.exists('pricing.html'):
    with open('pricing.html', 'r', encoding='utf-8') as f:
        idx_content = f.read()
    idx_content = idx_content.replace('hover:text-gray-900', 'hover:!text-gray-900')
    with open('pricing.html', 'w', encoding='utf-8') as f:
        f.write(idx_content)

print("Alignment and contrast fixed.")
