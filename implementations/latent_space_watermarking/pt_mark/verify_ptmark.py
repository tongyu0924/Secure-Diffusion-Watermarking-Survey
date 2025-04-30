from skimage.metrics import structural_similarity as ssim
import numpy as np
from PIL import Image

def compute_ssim_score(img1: Image.Image, img2: Image.Image) -> float:
    img1 = np.array(img1.convert("L"))
    img2 = np.array(img2.convert("L"))
    return ssim(img1, img2)
