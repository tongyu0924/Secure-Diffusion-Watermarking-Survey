from diffusers import StableDiffusionPipeline
import torch

# Load the Stable Diffusion model
pipe = StableDiffusionPipeline.from_pretrained("CompVis/stable-diffusion-v1-4")
pipe = pipe.to("cuda")

# Define the prompt with a watermark phrase (customizable)
watermark_prompt = "A futuristic cityscape with hidden mark X in the background"

# Generate the image
image = pipe(prompt=watermark_prompt, num_inference_steps=50).images[0]

# Save the output image
image.save("watermarked_output.png")

print("Image generated and saved as watermarked_output.png")
