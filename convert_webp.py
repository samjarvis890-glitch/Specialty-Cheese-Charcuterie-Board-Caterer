import os
import glob
from PIL import Image

image_dir = 'assets/images/home2'
png_files = glob.glob(os.path.join(image_dir, '*.png'))

for png_file in png_files:
    webp_file = png_file.rsplit('.', 1)[0] + '.webp'
    img = Image.open(png_file)
    img.save(webp_file, 'webp')
    os.remove(png_file)
    print(f'Converted {png_file} to {webp_file}')

with open('home2.html', 'r', encoding='utf-8') as f:
    content = f.read()

content = content.replace('.png', '.webp')

with open('home2.html', 'w', encoding='utf-8') as f:
    f.write(content)

print('Updated home2.html to use .webp')
