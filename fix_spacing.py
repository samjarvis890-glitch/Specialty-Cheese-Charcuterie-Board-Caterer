import glob
import re

html_files = glob.glob('*.html')

replacement_desktop = '''<!-- Inner Dropdown -->
                            <div class="mt-2 w-48 overflow-hidden rounded-2xl border border-gray-200 bg-white shadow-xl dark:border-gray-700 dark:bg-gray-800">
                                <a href="index.html" class="group/item block border-b border-gray-100 px-4 py-2 transition-colors hover:bg-gray-50 dark:border-gray-700 dark:hover:bg-gray-700">
                                    <div class="font-semibold text-gray-900 dark:text-white group-hover/item:text-primary transition-colors">Home 1</div>
                                </a>
                                <a href="board-builder.html" class="group/item block px-4 py-2 transition-colors hover:bg-gray-50 dark:hover:bg-gray-700">
                                    <div class="font-semibold text-gray-900 dark:text-white group-hover/item:text-primary transition-colors">Home 2</div>
                                </a>
                            </div>'''

replacement_mobile = '''<div id="mobile-home-menu" class="hidden pl-4 py-2 space-y-2">
                    <a href="index.html" class="block text-gray-600 dark:text-white hover:text-primary transition-colors">Home 1</a>
                    <a href="board-builder.html" class="block text-gray-600 dark:text-white hover:text-primary transition-colors">Home 2</a>
                </div>'''

for file in html_files:
    with open(file, 'r', encoding='utf-8') as f:
        content = f.read()

    # Desktop Dropdown regex
    regex_desktop = r'<!-- Inner Dropdown -->\s*<div class="mt-2 w-80[^>]*>.*?</a>\s*</div>'
    new_content = re.sub(regex_desktop, replacement_desktop, content, flags=re.DOTALL)
    
    # Mobile Dropdown regex
    regex_mobile = r'<div id="mobile-home-menu" class="hidden pl-4 py-2 space-y-2">.*?</div>'
    new_content = re.sub(regex_mobile, replacement_mobile, new_content, flags=re.DOTALL)

    if content != new_content:
        with open(file, 'w', encoding='utf-8') as f:
            f.write(new_content)
        print(f"Updated {file}")
