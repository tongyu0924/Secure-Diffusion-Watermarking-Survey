import cv2
import numpy as np
import pywt

# Embed watermark using DWT + DCT
def embed_dwt_dct(image_path, watermark_text, output_path):
    img = cv2.imread(image_path)
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    y = img_yuv[:, :, 0]

    coeffs = pywt.dwt2(y, 'haar')
    LL, (LH, HL, HH) = coeffs
    dct = cv2.dct(np.float32(LL))

    bits = ''.join(format(ord(c), '08b') for c in watermark_text)
    for i, b in enumerate(bits):
        row, col = i // 8, i % 8
        dct[row, col] += 1 if b == '1' else -1

    LL_mod = cv2.idct(dct)
    y_mod = pywt.idwt2((LL_mod, (LH, HL, HH)), 'haar')
    img_yuv[:, :, 0] = np.clip(y_mod, 0, 255)

    output_img = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)
    cv2.imwrite(output_path, output_img)

# Extract watermark from DWT + DCT image
def extract_dwt_dct(image_path, length):
    img = cv2.imread(image_path)
    img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)
    y = img_yuv[:, :, 0]

    LL, _ = pywt.dwt2(y, 'haar')
    dct = cv2.dct(np.float32(LL))

    bits = ''
    for i in range(length * 8):
        row, col = i // 8, i % 8
        bits += '1' if dct[row, col] > 0 else '0'

    chars = [chr(int(bits[i:i+8], 2)) for i in range(0, len(bits), 8)]
    return ''.join(chars)
