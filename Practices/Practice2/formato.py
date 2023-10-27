from PIL import Image
import os

def convert_images_to_jpg(dataset_path, output_path):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    
    for filename in os.listdir(dataset_path):
        if filename.lower().endswith((".png", ".jpeg", ".bmp", ".gif", ".tiff", ".webp")):
            image_path = os.path.join(dataset_path, filename)
            try:
                img = Image.open(image_path)
                img = img.convert("RGB")  # Convertir a formato RGB antes de guardar como JPG
                new_filename = os.path.splitext(filename)[0] + ".jpg"
                new_path = os.path.join(output_path, new_filename)
                img.save(new_path, "JPEG")
            except Exception as e:
                print(f"Error processing {image_path}: {e}")
                continue

# Ruta a tu directorio de imágenes
dataset_path = "path"
output_path = "path"
convert_images_to_jpg(dataset_path, output_path)
