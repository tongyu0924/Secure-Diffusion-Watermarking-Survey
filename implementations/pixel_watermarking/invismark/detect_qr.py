from PIL import Image
from pyzbar.pyzbar import decode

def decode_qr_from_image(image_path):
    image = Image.open(image_path)
    decoded = decode(image)

    if not decoded:
        print("No QR code detected.")
        return None
    for obj in decoded:
        print(f"QR Code content: {obj.data.decode('utf-8')}")
    return decoded[0].data.decode('utf-8') if decoded else None
