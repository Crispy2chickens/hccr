import cv2
import numpy as np
import os

def contrast_stretching(image):
    # Convert image to grayscale if it's not already
    if len(image.shape) == 3:
        gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    else:
        gray_image = image.copy()

    # Apply contrast stretching
    min_val = np.min(gray_image)
    max_val = np.max(gray_image)
    stretched = 255 * ((gray_image - min_val) / (max_val - min_val))

    return stretched.astype(np.uint8)

def save_images(directory, output_directory):
    for root, dirs, files in os.walk(directory):
        # Recreate the directory structure in the output directory
        relative_path = os.path.relpath(root, directory)
        output_path = os.path.join(output_directory, relative_path)
        os.makedirs(output_path, exist_ok=True)

        for file in files:
            if file.endswith('.png'):
                filepath = os.path.join(root, file)
                image = cv2.imread(filepath)

                enhanced_image = contrast_stretching(image)

                relative_image_path = os.path.join(relative_path, file)
                output_image_path = os.path.join(output_directory, relative_image_path)
                cv2.imwrite(output_image_path, enhanced_image)

main_directory = 'processed-mine'

for subdirectory in os.listdir(main_directory):
    subdirectory_path = os.path.join(main_directory, subdirectory)
    if os.path.isdir(subdirectory_path):
        save_images(subdirectory_path, subdirectory)