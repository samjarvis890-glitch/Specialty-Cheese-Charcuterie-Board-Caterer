import os
import re
import glob

html_files = glob.glob('*.html')

replacements = [
    (r'<a href="#" class="flex items-center gap-2 text-2xl font-serif font-bold text-primary mb-4">', r'<a href="index.html" class="flex items-center gap-2 text-2xl font-serif font-bold text-primary mb-4">'),
    (r'<a href="#" class="text-gray-600 dark:text-white hover:text-primary text-sm transition-colors">Wedding Catering</a>', r'<a href="catering.html" class="text-gray-600 dark:text-white hover:text-primary text-sm transition-colors">Wedding Catering</a>'),
    (r'<a href="#" class="text-gray-600 dark:text-white hover:text-primary text-sm transition-colors">Corporate Events</a>', r'<a href="catering.html" class="text-gray-600 dark:text-white hover:text-primary text-sm transition-colors">Corporate Events</a>'),
    (r'<a href="#" class="text-gray-600 dark:text-white hover:text-primary text-sm transition-colors">Birthday Parties</a>', r'<a href="catering.html" class="text-gray-600 dark:text-white hover:text-primary text-sm transition-colors">Birthday Parties</a>'),
    (r'<a href="#" class="text-gray-600 dark:text-white hover:text-primary text-sm transition-colors">Luxury Grazing Tables</a>', r'<a href="catering.html" class="text-gray-600 dark:text-white hover:text-primary text-sm transition-colors">Luxury Grazing Tables</a>'),
    (r'<a href="#" class="text-gray-600 dark:text-white hover:text-primary text-sm transition-colors">Wine Pairings</a>', r'<a href="wine-pairings.html" class="text-gray-600 dark:text-white hover:text-primary text-sm transition-colors">Wine Pairings</a>'),
    (r'<a href="#" class="text-gray-600 dark:text-white hover:text-primary text-sm transition-colors">Private Chef Service</a>', r'<a href="catering.html" class="text-gray-600 dark:text-white hover:text-primary text-sm transition-colors">Private Chef Service</a>'),
    (r'<a href="#" class="btn-primary"><i class="fa-brands fa-instagram mr-2"></i> View Full Gallery</a>', r'<a href="gallery.html" class="btn-primary"><i class="fa-brands fa-image mr-2"></i> View Full Gallery</a>'),
    (r'<a href="#" class="btn-primary text-lg"><i class="fa-solid fa-calendar-plus mr-2"></i> Reserve Your Event Date</a>', r'<a href="board-builder.html" class="btn-primary text-lg"><i class="fa-solid fa-calendar-plus mr-2"></i> Reserve Your Event Date</a>'),
    (r'<a href="#" class="btn-outline border-white text-white hover:bg-white hover:text-gray-900 text-lg">Request a Custom Quote</a>', r'<a href="contact.html" class="btn-outline border-white text-white hover:bg-white hover:text-gray-900 text-lg">Request a Custom Quote</a>'),
    (r'<a href="#" class="mt-4 md:mt-0 btn-primary hidden md:inline-block"><i class="fa-brands fa-instagram mr-2"></i> Follow Us</a>', r'<a href="https://instagram.com" target="_blank" class="mt-4 md:mt-0 btn-primary hidden md:inline-block"><i class="fa-brands fa-instagram mr-2"></i> Follow Us</a>'),
    (r'<a href="#" class="btn-primary inline-block"><i class="fa-brands fa-instagram mr-2"></i> Follow Us</a>', r'<a href="https://instagram.com" target="_blank" class="btn-primary inline-block"><i class="fa-brands fa-instagram mr-2"></i> Follow Us</a>'),
    (r'<a href="#" class="mt-8 btn-primary inline-block"><i class="fa-brands fa-instagram mr-2"></i> Follow @LArtisan</a>', r'<a href="https://instagram.com" target="_blank" class="mt-8 btn-primary inline-block"><i class="fa-brands fa-instagram mr-2"></i> Follow @LArtisan</a>'),
    (r'<a href="#" class="w-10 h-10 rounded-full bg-gray-800 flex items-center justify-center hover:bg-primary transition-colors text-white"><i class="fa-brands fa-instagram"></i></a>', r'<a href="https://instagram.com" target="_blank" class="w-10 h-10 rounded-full bg-gray-800 flex items-center justify-center hover:bg-primary transition-colors text-white"><i class="fa-brands fa-instagram"></i></a>'),
    (r'<a href="#" class="w-10 h-10 rounded-full bg-gray-800 flex items-center justify-center hover:bg-primary transition-colors text-white"><i class="fa-brands fa-facebook-f"></i></a>', r'<a href="https://facebook.com" target="_blank" class="w-10 h-10 rounded-full bg-gray-800 flex items-center justify-center hover:bg-primary transition-colors text-white"><i class="fa-brands fa-facebook-f"></i></a>'),
    (r'<a href="#" class="w-10 h-10 rounded-full bg-gray-800 flex items-center justify-center hover:bg-primary transition-colors text-white"><i class="fa-brands fa-pinterest-p"></i></a>', r'<a href="https://pinterest.com" target="_blank" class="w-10 h-10 rounded-full bg-gray-800 flex items-center justify-center hover:bg-primary transition-colors text-white"><i class="fa-brands fa-pinterest-p"></i></a>'),
    (r'<a href="#" class="text-gray-600 dark:text-gray-300 hover:text-primary transition-colors"><i class="fa-brands fa-instagram text-xl"></i></a>', r'<a href="https://instagram.com" target="_blank" class="text-gray-600 dark:text-gray-300 hover:text-primary transition-colors"><i class="fa-brands fa-instagram text-xl"></i></a>'),
    (r'<a href="#" class="text-gray-600 dark:text-gray-300 hover:text-primary transition-colors"><i class="fa-brands fa-facebook text-xl"></i></a>', r'<a href="https://facebook.com" target="_blank" class="text-gray-600 dark:text-gray-300 hover:text-primary transition-colors"><i class="fa-brands fa-facebook text-xl"></i></a>'),
    (r'<a href="#" class="text-gray-600 dark:text-gray-300 hover:text-primary transition-colors"><i class="fa-brands fa-x-twitter text-xl"></i></a>', r'<a href="https://twitter.com" target="_blank" class="text-gray-600 dark:text-gray-300 hover:text-primary transition-colors"><i class="fa-brands fa-x-twitter text-xl"></i></a>'),
]

for file_path in html_files:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
    
    original_content = content
    for old, new in replacements:
        content = content.replace(old, new)
        
    if content != original_content:
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        print(f"Updated {file_path}")
