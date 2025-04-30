from dwt_dct_utils import embed_dwt_dct, extract_dwt_dct

# Input and output paths
input_image = "sample_input.png"
output_image = "watermarked_dwt_dct.png"

# Embed watermark text
embed_dwt_dct(input_image, "NTUST2025", output_image)

# Extract watermark from watermarked image
result = extract_dwt_dct(output_image, length=9)  # 9 = len("NTUST2025")
print("Extracted Watermark:", result)
