from PIL import Image
import torch
from transformers import CLIPProcessor, CLIPModel

# Load the CLIP model and processor
model = CLIPModel.from_pretrained("openai/clip-vit-base-patch32").to("cuda")
processor = CLIPProcessor.from_pretrained("openai/clip-vit-base-patch32")

# Load the generated image
image_path = "watermarked_output.png"
image = Image.open(image_path)

# Define the original prompt used to generate the image
original_prompt = "A futuristic cityscape with hidden mark X in the background"

# Preprocess the image and prompt
inputs = processor(text=[original_prompt], images=image, return_tensors="pt", padding=True).to("cuda")

# Forward through CLIP
outputs = model(**inputs)

# Get similarity score
similarity_score = outputs.logits_per_image.softmax(dim=1)[0][0].item()

# Display result
print(f" CLIP similarity score: {similarity_score:.4f}")

# Simple threshold check (adjustable)
if similarity_score > 0.3:
    print("The image likely matches the intended prompt.")
else:
    print("The image may not contain the intended watermark prompt.")
