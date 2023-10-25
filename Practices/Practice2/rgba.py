from PIL import Image
import os

def convert_rgba_to_rgb(image_path, output_path):
    try:
        rgba_image = Image.open(image_path)
        rgb_image = rgba_image.convert("RGB")
        rgb_image.save(output_path, "JPEG")
        print(f"Imagen {image_path} convertida a RGB y guardada en {output_path}")
    except Exception as e:
        print(f"Error al convertir {image_path} a RGB: {e}")

# Ruta a tu directorio de imágenes RGBA
rgba_images_path = "D:\Trabajos\IA 2 - 2023-2\ejemParcial\\train\white-glass"

# Ruta donde deseas guardar las imágenes RGB
output_path = "D:\Trabajos\IA 2 - 2023-2\ejemParcial\\trash_dataset\white-glass"

if not os.path.exists(output_path):
    os.makedirs(output_path)

for filename in os.listdir(rgba_images_path):
    if filename.lower().endswith((".png", ".jpeg", ".jpg")):
        rgba_image_path = os.path.join(rgba_images_path, filename)
        rgb_image_filename = os.path.splitext(filename)[0] + "_rgb.jpg"
        rgb_image_path = os.path.join(output_path, rgb_image_filename)
        convert_rgba_to_rgb(rgba_image_path, rgb_image_path)
