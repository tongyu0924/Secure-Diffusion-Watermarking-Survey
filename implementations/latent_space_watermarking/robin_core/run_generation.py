import torch
from diffusers import StableDiffusionPipeline
from models.embedder import Embedder
from utils.watermark_utils import decode_with_vae, get_latents
from PIL import Image
import numpy as np
import os


def tensor_to_pil(tensor):
    tensor = tensor.detach().cpu().float()
    tensor = (tensor + 1.0) / 2.0
    tensor = tensor.clamp(0, 1)
    array = tensor.permute(1, 2, 0).numpy() * 255
    array = array.astype(np.uint8)
    return Image.fromarray(array)


def generate_watermarked_image(prompt, embedder, vae, tokenizer, text_encoder, device, secret_key=1234):
    with torch.no_grad():
        # Generate text embedding
        text_inputs = tokenizer(
            prompt,
            padding="max_length",
            max_length=tokenizer.model_max_length,
            truncation=True,
            return_tensors="pt",
        )
        text_embeddings = text_encoder(text_inputs.input_ids.to(device))[0]

        # Generate initial latent
        latent_shape = (1, vae.config.latent_channels, vae.sample_size, vae.sample_size)
        latents = torch.randn(latent_shape).to(device)

        # Embed watermark into latent
        w_key = torch.randn(1, 128).to(device)
        latents_with_watermark = embedder(latents, w_key)

        # Decode to image
        images = vae.decode(latents_with_watermark / vae.config.scaling_factor).sample
        return tensor_to_pil(images[0])


if __name__ == "__main__":
    prompt = "A futuristic robot playing chess"
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")

    # Load SD components
    pipe = StableDiffusionPipeline.from_pretrained(
        "CompVis/stable-diffusion-v1-4",
        torch_dtype=torch.float16 if device.type == "cuda" else torch.float32
    ).to(device)
    vae = pipe.vae.eval()
    tokenizer = pipe.tokenizer
    text_encoder = pipe.text_encoder

    # Load trained embedder
    embedder = Embedder(latent_dim=4, key_dim=128).to(device)
    embedder.load_state_dict(torch.load("checkpoints/embedder.pth", map_location=device))
    embedder.eval()

    # Generate watermarked image
    image = generate_watermarked_image(prompt, embedder, vae, tokenizer, text_encoder, device)
    os.makedirs("outputs", exist_ok=True)
    image.save("outputs/generated_watermarked.png")
    print("Saved: outputs/generated_watermarked.png")
