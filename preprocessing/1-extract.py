import os
import struct
import numpy as np
from PIL import Image

def read_gnt_file(file_path):
    images = []
    with open(file_path, 'rb') as f:
        while True:
            # Read sample size
            sample_size_bytes = f.read(4)
            if not sample_size_bytes:
                break
            sample_size = struct.unpack('<I', sample_size_bytes)[0]

            # Read tag code (GB)
            tag_code = struct.unpack('<H', f.read(2))[0]

            # Convert tag code to Chinese character using provided encoding information
            chinese_character = tag_code.to_bytes(2, byteorder='little').decode('gb18030')

            # Read width and height
            width = struct.unpack('<H', f.read(2))[0]
            height = struct.unpack('<H', f.read(2))[0]

            # Read bitmap
            bitmap_bytes = f.read(width * height)
            bitmap = np.frombuffer(bitmap_bytes, dtype=np.uint8)
            bitmap = np.reshape(bitmap, (height, width))

            images.append((chinese_character, bitmap))
    return images


def save_as_png(images, output_dir):
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    for i, (chinese_character, bitmap) in enumerate(images):
        image = Image.fromarray(bitmap, mode='L')
        image_path = os.path.join(output_dir, f'{chinese_character}.png')
        image.save(image_path)
        # print(f'Saved {image_path}')


# Example usage
for i in range(60):
    input_gnt_file = f'HWDB1.1tst_gnt/{i+1241}-c.gnt'
    output_directory = f'{i+1241}'
    images = read_gnt_file(input_gnt_file)
    save_as_png(images, output_directory)
