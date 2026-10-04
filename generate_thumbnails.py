import os
import subprocess
import glob

BASE_DIR = '/Users/sym/code/elden_ring_liveaction'

FOLDERS = [
    'cyberpunk',
    'zelda',
    'v2_realhuman',
    'v2_20_gallery',
    'originals'
]

total_orig_bytes = 0
total_thumb_bytes = 0
processed_count = 0

print("Generating high-performance web thumbnails using macOS sips...")

for folder in FOLDERS:
    folder_path = os.path.join(BASE_DIR, folder)
    if not os.path.exists(folder_path):
        continue
    
    thumb_dir = os.path.join(folder_path, 'thumbs')
    os.makedirs(thumb_dir, exist_ok=True)
    
    png_files = sorted(glob.glob(os.path.join(folder_path, '*.png')))
    for src_png in png_files:
        filename = os.path.basename(src_png)
        base_name, _ = os.path.splitext(filename)
        dest_jpg = os.path.join(thumb_dir, f"{base_name}.jpg")
        
        orig_sz = os.path.getsize(src_png)
        total_orig_bytes += orig_sz
        
        # Run sips to resize to max dimension 720px and export as optimized JPEG
        cmd = [
            'sips',
            '-s', 'format', 'jpeg',
            '-s', 'formatOptions', '82',
            '-Z', '720',
            src_png,
            '--out', dest_jpg
        ]
        res = subprocess.run(cmd, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if res.returncode == 0 and os.path.exists(dest_jpg):
            thumb_sz = os.path.getsize(dest_jpg)
            total_thumb_bytes += thumb_sz
            processed_count += 1
            saving_pct = (1 - thumb_sz / orig_sz) * 100
            print(f"  [{folder}] {filename} ({orig_sz/1024:.0f}KB) -> thumbs/{base_name}.jpg ({thumb_sz/1024:.0f}KB, -{saving_pct:.1f}%)")
        else:
            print(f"  ERROR processing {src_png}")

print(f"\n==========================================")
print(f"Thumbnails generated: {processed_count} images")
print(f"Original total: {total_orig_bytes / 1024 / 1024:.1f} MB")
print(f"Thumbnail total: {total_thumb_bytes / 1024 / 1024:.1f} MB")
total_saved = (1 - total_thumb_bytes / total_orig_bytes) * 100
print(f"Bandwidth reduction: {total_saved:.1f}%!")
print(f"==========================================")
