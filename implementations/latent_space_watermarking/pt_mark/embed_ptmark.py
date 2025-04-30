from diffusers import StableDiffusionPipeline
import torch
from PIL import Image
import numpy as np
from null_prompt_optimizer import apply_semantic_alignment

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
pipe = StableDiffusionPipeline.from_pretrained(
    "CompVis/stable-diffusion-v1-4", torch_dtype=torch.float16 if device.type == "cuda" else torch.float32
).to(device)
pipe.enable_attention_slicing()

def tensor_to_pil(tensor):
    tensor = tensor.detach().cpu().float()
    tensor = (tensor + 1) / 2.0
    tensor = tensor.clamp(0, 1)
    array = tensor.permute(1, 2, 0).numpy() * 255
    return Image.fromarray(array.astype(np.uint8))

def embed_watermark(prompt, secret_key, strength=0.01):
    torch.manual_seed(secret_key)
    latents = torch.randn(
        (1, pipe.unet.config.in_channels, pipe.unet.config.sample_size, pipe.unet.config.sample_size),
        device=device,
        dtype=torch.float16 if device.type == "cuda" else torch.float32,
    )

    text_inputs = pipe.tokenizer(prompt, padding="max_length", max_length=pipe.tokenizer.model_max_length,
                                  truncation=True, return_tensors="pt")
    text_embeddings = pipe.text_encoder(text_inputs.input_ids.to(device))[0]

    scheduler = pipe.scheduler
    scheduler.set_timesteps(50, device=device)

    for t in scheduler.timesteps:
        noise_pred = pipe.unet(latents, t, encoder_hidden_states=text_embeddings).sample
        latents = scheduler.step(noise_pred, t, latents).prev_sample

    # Semantic-aware watermark adjustment (dummy for now)
    latents = apply_semantic_alignment(latents, prompt)

    images = pipe.vae.decode(latents / pipe.vae.config.scaling_factor).sample
    return tensor_to_pil(images[0])
