from PIL import Image
import qrcode
import os

def embed_qr_in_image(base_image_path, qr_text, output_path):
    # Load base image
    image = Image.open(base_image_path).convert("RGB")

    # Generate QR code image
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(qr_text)
    qr.make(fit=True)
    qr_img = qr.make_image(fill_color="black", back_color="white").convert("RGB")

    # Resize QR code to be small (e.g., 1/4 width)
    qr_size = image.width // 4
    qr_img = qr_img.resize((qr_size, qr_size))

    # Paste QR code on bottom-right corner
    position = (image.width - qr_size - 10, image.height - qr_size - 10)
    image.paste(qr_img, position)

    # Save image
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    image.save(output_path)
    print(f"QR embedded image saved at {output_path}")
