from PIL import Image, ImageDraw
import os

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

                canvas_size = (64, 64)
                canvas = Image.new("RGB", canvas_size, color="white")

                image_width, image_height = image.size
                position = ((canvas_size[0] - image_width) // 2, (canvas_size[1] - image_height) // 2)

                canvas.paste(image, position)

                # Get the relative path for the output image
                relative_image_path = os.path.join(relative_path, file)
                output_image_path = os.path.join(output_directory, relative_image_path)
                canvas.save(output_image_path)

main_directory = 'processed-mine2'

for subdirectory in os.listdir(main_directory):
    subdirectory_path = os.path.join(main_directory, subdirectory)
    if os.path.isdir(subdirectory_path):
        save_images(subdirectory_path, subdirectory)