import os
import glob
import shutil

# Create directory
os.makedirs('assets/images/home2', exist_ok=True)

# Find generated images in the brain folder
brain_dir = r'C:\Users\Sam John\.gemini\antigravity\brain\03b64f2d-d3b7-49bb-b24f-47ef5873de16'

images = {
    'hero_builder': 'hero-builder.png',
    'event_type': 'event-type.png',
    'guest_planner': 'guest-planner.png',
    'board_config': 'board-config.png',
    'live_price': 'live-price.png',
    'reservation_calendar': 'reservation-calendar.png'
}

for prefix, dest_name in images.items():
    found = glob.glob(os.path.join(brain_dir, f'{prefix}_*.png'))
    if found:
        # copy the newest one
        found.sort(key=os.path.getmtime)
        shutil.copy(found[-1], os.path.join('assets', 'images', 'home2', dest_name))
        print(f'Copied {dest_name}')

print('Images setup complete.')
