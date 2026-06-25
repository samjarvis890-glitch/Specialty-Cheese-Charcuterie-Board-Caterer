import re

with open('board-builder.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add gap-4 to the label
content = re.sub(
    r'(<label class="flex items-center justify-between p-4 )(border-2)',
    r'\1gap-4 \2',
    content
)

# 2. Add flex-1 min-w-0 to the inner wrapper
content = re.sub(
    r'(<div class="flex items-center gap-4)">',
    r'\1 flex-1 min-w-0">',
    content
)

# 3. Add shrink-0 to the icon div
content = re.sub(
    r'(<div class="w-12 h-12 rounded-full[^>]*flex items-center justify-center shadow-sm)">',
    r'\1 shrink-0">',
    content
)

# 4. Add min-w-0 to the text div (the one right before <h4>)
content = re.sub(
    r'(<div>\s*<h4)',
    r'<div class="min-w-0">\n                                            <h4 class="truncate" ',
    content
)

# Wait, the previous replace was bad because it removed the class="font-bold ... " part of h4.
# Let's do it safer:
# Replace <div>\n<h4 with <div class="min-w-0">\n<h4
content = re.sub(
    r'(<div>)(\s*<h4)',
    r'<div class="min-w-0">\2',
    content
)

# 5. Add shrink-0 to the radio buttons
content = re.sub(
    r'(<input type="radio" name="board_style"[^>]*class="[^"]*)(">)',
    r'\1 shrink-0\2',
    content
)

# Let's fix the add-ons checkboxes too just in case
content = re.sub(
    r'(<input type="checkbox" class="mt-1 w-5 h-5 text-primary rounded border-gray-300 focus:ring-primary accent-primary)(">)',
    r'\1 shrink-0\2',
    content
)

with open('board-builder.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Done')
