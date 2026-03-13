from PIL import Image

def optimize_favicon():
    img_path = "assets/img/logo-seal.jpg"
    out_path = "assets/img/logo-seal.jpg"
    
    # Open the image
    img = Image.open(img_path).convert("RGBA")
    width, height = img.size
    
    # The logo consists of a central tooth/face profile with text wrapped around it.
    # To make the favicon legible, we must crop out the text and leave just the central logo.
    
    # Crop to the central portion where the logo usually is (approx 25% to 75% of width/height)
    left = int(width * 0.28)
    top = int(height * 0.3)
    right = int(width * 0.72)
    bottom = int(height * 0.72)
    
    cropped = img.crop((left, top, right, bottom))
    
    # Get the bounding box of non-transparent pixels to trim further
    bbox = cropped.getbbox()
    if bbox:
        cropped = cropped.crop(bbox)
        
    # Resize to have a bit of padding (e.g., 10%)
    max_dim = max(cropped.size)
    padded_size = int(max_dim * 1.2)
    final_img = Image.new("RGBA", (padded_size, padded_size), (255, 255, 255, 0))
    
    # Center the cropped image
    offset = ((padded_size - cropped.size[0]) // 2, (padded_size - cropped.size[1]) // 2)
    final_img.paste(cropped, offset)
    
    # Save back over the original image
    final_img.save(out_path, format="PNG")
    print("Favicon optimized successfully.")

if __name__ == "__main__":
    try:
        optimize_favicon()
    except Exception as e:
        print("Error:", e)
