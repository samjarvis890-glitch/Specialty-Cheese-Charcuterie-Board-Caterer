import os

file_path = r"d:\Specialty Cheese  Charcuterie Board Caterer project1\index.html"

with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

replacements = {
    'class="container mx-auto px-4"': 'class="container mx-auto px-6 md:px-12 lg:px-24"',
    'class="container mx-auto px-4 sm:px-6 lg:px-8"': 'class="container mx-auto px-6 md:px-12 lg:px-24"',
    'class="relative z-10 text-center px-4 max-w-4xl mx-auto"': 'class="relative z-10 text-center px-6 md:px-12 lg:px-24 max-w-4xl mx-auto"',
    'class="container mx-auto px-4 relative z-20"': 'class="container mx-auto px-6 md:px-12 lg:px-24 relative z-20"',
    'class="container mx-auto px-4 max-w-5xl"': 'class="container mx-auto px-6 md:px-12 lg:px-24 max-w-5xl"',
    'class="container mx-auto px-4 text-center"': 'class="container mx-auto px-6 md:px-12 lg:px-24 text-center"',
    'class="relative z-20 text-center px-4 max-w-3xl mx-auto"': 'class="relative z-20 text-center px-6 md:px-12 lg:px-24 max-w-3xl mx-auto"',
}

for old, new in replacements.items():
    content = content.replace(old, new)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)

print("Padding applied successfully.")
