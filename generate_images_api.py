import os
import urllib.request
from PIL import Image
import io
import time
import urllib.parse

base_dir = 'd:/Specialty Cheese  Charcuterie Board Caterer project1/assets/images/gallery'

# Dictionary of path to prompt
images_to_generate = {
    'signature/luxury-grazing.webp': 'A massive luxury grazing table for a premium event, overflowing with artisan cheeses, cured meats, fresh fruits, and vibrant edible flowers. Cinematic lighting, photorealistic, top-down view.',
    'signature/artisan-cheese.webp': 'A beautiful, curated artisan cheese board with high-end local and imported cheeses, honeycomb, and crackers. High quality, food photography.',
    'signature/brunch-collection.webp': 'A stunning brunch grazing board with fresh pastries, waffles, fresh fruits, and morning favorites beautifully arranged. Bright natural lighting.',
    'signature/dessert-board.webp': 'A decadent dessert charcuterie board filled with chocolates, macarons, sweet treats, and berries. Moody cinematic lighting, high-end catering.',
    
    'transformations/wedding-empty.webp': 'An empty, sterile wedding venue reception hall before any decorations are added. Blank canvas, natural light.',
    'transformations/wedding-setup.webp': 'The same wedding venue transformed with a breathtaking 15-foot grazing table focal point, floral integration, elegant lighting. Luxury wedding reception.',
    'transformations/corporate-empty.webp': 'A sterile, empty corporate office lobby or hall before an event.',
    'transformations/corporate-setup.webp': 'A vibrant corporate networking event space centered around dual symmetrical grazing tables, professional, sophisticated.',
    
    'process/ingredient-selection.webp': 'Close up of hands carefully selecting fresh artisan ingredients, fresh produce and premium cheeses. High quality food prep photography.',
    'process/board-layout.webp': 'Top down view of the initial layout of a charcuterie board being built, empty spaces, placing large cheese wheels.',
    'process/styling-garnishing.webp': 'Close up of a chef styling and garnishing a charcuterie board with fresh herbs and edible flowers. Culinary art.',
    'process/final-presentation.webp': 'A flawlessly presented, completed charcuterie board ready for an event. Professional food photography.',
    
    'pairings/brie-chardonnay.webp': 'A wedge of creamy Brie cheese elegantly plated next to a glass of white Chardonnay wine. High-end culinary photography.',
    'pairings/gouda-pinot.webp': 'A wedge of aged Gouda cheese with caramel notes paired with a glass of red Pinot Noir wine. Dark moody background.',
    'pairings/blue-port.webp': 'Intense blue cheese crumbles paired with a small glass of vintage Port wine. Sophisticated food styling.',
    'pairings/cheddar-cabernet.webp': 'Sharp aged cheddar cheese paired with a glass of bold red Cabernet Sauvignon wine. Rustic elegant setting.',
    
    'stories/sarah-michael.webp': 'A beautiful grazing table at a wedding reception with guests mingling in the background. Floral integration, elegant.',
    'stories/corporate-gala.webp': 'A sophisticated corporate gala event with attendees networking around a large, impressive charcuterie centerpiece.',
    'stories/holiday-family.webp': 'A warm, inviting private holiday family gathering in a beautiful kitchen with a large grazing board on the island centerpiece.',
    
    'seasonal/spring-garden.webp': 'A vibrant spring garden party grazing board featuring fresh seasonal berries, bright edible flowers, and fresh cheeses. Sunny natural light.',
    'seasonal/summer-picnic.webp': 'A summer vineyard picnic charcuterie board laid out on a blanket with wine glasses. Warm summer glow.',
    'seasonal/autumn-harvest.webp': 'An autumn harvest grazing board with seasonal fruits, figs, dark cheeses, and rustic fall colors. Cozy lighting.',
    'seasonal/winter-holiday.webp': 'A festive winter holiday charcuterie board with cranberries, rosemary sprigs, and rich cheeses. Warm indoor lighting.',
    
    'behind-scenes/ingredient-prep.webp': 'A candid, polaroid-style photo of early morning food prep in a catering kitchen. Chopping vegetables, preparing cheeses.',
    'behind-scenes/delivery-setup.webp': 'A candid photo of a catering team setting up a massive 15-foot grazing table at a venue. Behind the scenes action.',
    'behind-scenes/team-moments.webp': 'A candid, joyful photo of a professional catering team working together in a kitchen. Warm, authentic moment.',
    
    'social/social-1.webp': 'An instagram-style square photo of a perfect charcuterie cup. High engagement food post.',
    'social/social-2.webp': 'An instagram-style square photo of a beautiful cheese wheel being sliced. Aesthetic food post.',
    'social/social-3.webp': 'An instagram-style square photo of a colorful grazing table detail shot. vibrant colors.',
    'social/social-4.webp': 'An instagram-style square photo of a glass of wine next to artisan crackers and cheese. Aesthetic.',
    'social/social-5.webp': 'An instagram-style square photo of an elaborate dessert grazing board with chocolate strawberries.',
    'social/social-6.webp': 'An instagram-style square photo of a rustic outdoor picnic charcuterie setup.',
}

print('Generating images via pollinations.ai...')
for path, prompt in images_to_generate.items():
    full_path = os.path.join(base_dir, path)
    
    # Force regeneration
        
    encoded_prompt = urllib.parse.quote(prompt)
    url = f'https://image.pollinations.ai/prompt/{encoded_prompt}?width=800&height=600&nologo=true'
    
    try:
        req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64)'})
        with urllib.request.urlopen(req) as response:
            image_data = response.read()
            img = Image.open(io.BytesIO(image_data))
            img = img.convert('RGB')
            img.save(full_path, 'WEBP', quality=85)
            print(f'Generated and saved {path}')
    except Exception as e:
        print(f'Failed to generate {path}: {e}')
    
    time.sleep(1) # Be nice to the API

print('Done generating all images.')
