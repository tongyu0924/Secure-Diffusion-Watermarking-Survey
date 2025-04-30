from PIL import Image
import torch
from diffusers import StableDiffusionPipeline
import numpy as np
from watermark_utils import apply_latent_watermark

torch.manual_seed(42)

# GPU or CPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"Using device: {device}")

# Load model
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16 if device.type == "cuda" else torch.float32
).to(device)
pipe.enable_attention_slicing()

def tensor_to_pil(tensor):
    tensor = tensor.detach().cpu().float()
    tensor = (tensor + 1.0) / 2.0
    tensor = tensor.clamp(0, 1)
    array = tensor.permute(1, 2, 0).numpy() * 255
    array = array.astype(np.uint8)
    return Image.fromarray(array)

def generate_image_with_cluemark(prompt, secret_key, strength=0.01):
    with torch.no_grad():
        latents = torch.randn(
            (1, pipe.unet.config.in_channels, pipe.unet.config.sample_size, pipe.unet.config.sample_size),
            device=device,
            dtype=torch.float16 if device.type == "cuda" else torch.float32,
        )

        text_inputs = pipe.tokenizer(
            prompt,
            padding="max_length",
            max_length=pipe.tokenizer.model_max_length,
            truncation=True,
            return_tensors="pt",
        )
        text_embeddings = pipe.text_encoder(text_inputs.input_ids.to(device))[0]

        scheduler = pipe.scheduler
        scheduler.set_timesteps(50, device=device)
        for t in scheduler.timesteps:
            noise_pred = pipe.unet(latents, t, encoder_hidden_states=text_embeddings).sample
            latents = scheduler.step(noise_pred, t, latents).prev_sample

        latents = apply_latent_watermark(latents, secret_key, strength)
        images = pipe.vae.decode(latents / pipe.vae.config.scaling_factor).sample
        return tensor_to_pil(images[0])

if __name__ == "__main__":
    prompt = "A beautiful futuristic cityscape at sunset, ultra detailed"
    secret_key = 123456
    image = generate_image_with_cluemark(prompt, secret_key)
    image.save("cluemark_watermarked.png")
    print("CLUE-MARK style watermarked image saved successfully!")
