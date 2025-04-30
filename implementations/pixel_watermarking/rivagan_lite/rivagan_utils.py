from PIL import Image
import numpy as np

# Embed watermark bits into the least significant bit
def embed_riva(image_path, watermark_bits, output_path):
    img = Image.open(image_path).convert("RGB")
    img_arr = np.array(img).flatten()

    for i, b in enumerate(watermark_bits):
        img_arr[i] = (img_arr[i] & ~1) | int(b)

    watermarked = img_arr.reshape(img.size[1], img.size[0], 3)
    Image.fromarray(watermarked.astype(np.uint8)).save(output_path)

# Extract watermark bits from LSB
def extract_riva(image_path, length):
    img = Image.open(image_path).convert("RGB")
    flat = np.array(img).flatten()
    return ''.join(str(flat[i] & 1) for i in range(length))
