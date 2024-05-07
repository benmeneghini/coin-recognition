import cv2
import numpy as np

ALPHA = 1.5 # Contrast control (1.5 increases contrast)
BETA = 0 # Brightness control (0 has no effect)

def adjust_contrast(image_path, alpha=ALPHA, beta=BETA):
    """
    Adjusts the contrast and brightness of an image.
    """
    # Read the image
    image = cv2.imread(image_path)

    # Convert the image from uint8 to float to avoid overflow/underflow
    image = image.astype(np.float64)

    # Adjust contrast and brightness
    image = image * alpha + beta

    # Clip values to stay within the 0-255 range and convert back to uint8
    image = np.clip(image, 0, 255).astype(np.uint8)

    return image
