import os
from PIL import Image
from pathlib import Path
def save_images(directory, output_directory):
    for root, dirs, files in os.walk(directory):
        # Recreate the directory structure in the output directory
        relative_path = os.path.relpath(root, directory)
        output_path = os.path.join(output_directory, relative_path)
        os.makedirs(output_path, exist_ok=True)

        for file in files:
            if file.endswith('.png'):
                filepath = os.path.join(root, file)
                image = Image.open(filepath)
                image.thumbnail((64, 64))
                # Get the relative path for the output image
                relative_image_path = os.path.join(relative_path, file)
                output_image_path = os.path.join(output_directory, relative_image_path)
                image.save(output_image_path)

main_directory = 'mine'

for subdirectory in os.listdir(main_directory):
    subdirectory_path = os.path.join(main_directory, subdirectory)
    if os.path.isdir(subdirectory_path):
        save_images(subdirectory_path, subdirectory)