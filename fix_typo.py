import re

with open('board-builder.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('class="truncate"  class="', 'class="truncate ')

with open('board-builder.html', 'w', encoding='utf-8') as f:
    f.write(content)
