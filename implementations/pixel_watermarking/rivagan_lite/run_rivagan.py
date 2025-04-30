from rivagan_utils import embed_riva, extract_riva

input_image = "sample_input.png"
output_image = "watermarked_riva.png"
watermark_bits = ''.join(format(ord(c), '08b') for c in "NTUST")

# Embed
embed_riva(input_image, watermark_bits, output_image)

# Extract
recovered = extract_riva(output_image, len("NTUST") * 8)
print("Extracted bits:", recovered)
