
import os
from PIL import Image

def resize_images_in_folder(folder_path, output_folder_path):
    # Crea la carpeta de salida si no existe
    if not os.path.exists(output_folder_path):
        os.makedirs(output_folder_path)

    # Recorre todos los archivos en la carpeta
    for filename in os.listdir(folder_path):
        if filename.endswith(".jpg") or filename.endswith(".png"):
            # Obtiene la ruta completa del archivo de entrada
            input_image_path = os.path.join(folder_path, filename)

            # Obtiene el nuevo nombre del archivo de salida
            output_image_path = os.path.join(output_folder_path, filename)

            # Abre la imagen utilizando Pillow
            image = Image.open(input_image_path)

            # Redimensiona la imagen al tamaño deseado (800x600)
            resized_image = image.resize((800, 600))

            # Guarda la imagen redimensionada
            resized_image.save(output_image_path)

    print("¡Redimensionado completado!")

# Ruta de la carpeta que contiene las imágenes originales
folder_path = "E:\Imagenes para IA CARTONES"

# Ruta de la carpeta de salida para las imágenes redimensionadas
output_folder_path = "E:\Redimensionadas"

# Llama a la función para redimensionar todas las imágenes en la carpeta
resize_images_in_folder(folder_path, output_folder_path)