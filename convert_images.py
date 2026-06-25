import os
import glob
from PIL import Image

src_dir = r"C:\Users\Sam John\.gemini\antigravity\brain\2fc7cd57-70fb-40cd-8028-485d4b2142b6"
dest_dir = r"d:\Specialty Cheese  Charcuterie Board Caterer project1\assets\images\home"

mapping = {
    "hero_editorial_grazing_table": "hero-editorial-grazing-table.webp",
    "featured_catering_collection": "featured-catering-collection.webp",
    "interactive_board_builder_preview": "interactive-board-builder-preview.webp",
    "wine_pairing_experience": "wine-pairing-experience.webp",
    "upcoming_catering_events": "upcoming-catering-events.webp",
    "luxury_catering_packages": "luxury-catering-packages.webp",
    "happy_catering_guests": "happy-catering-guests.webp",
    "gallery_preview_signature_board": "gallery-preview-signature-board.webp",
    "reserve_event_cta": "reserve-event-cta.webp",
}

if not os.path.exists(dest_dir):
    os.makedirs(dest_dir)

for prefix, out_name in mapping.items():
    pattern = os.path.join(src_dir, f"{prefix}_*.png")
    matches = glob.glob(pattern)
    if matches:
        latest = max(matches, key=os.path.getctime)
        print(f"Converting {latest} to {out_name}...")
        img = Image.open(latest)
        dest_path = os.path.join(dest_dir, out_name)
        img.save(dest_path, "webp", quality=90)
        print(f"Saved {dest_path}")
    else:
        print(f"No match found for {prefix}")

print("Done!")
