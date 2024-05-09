import numpy as np

ALPHA = 0.2 # Contrast control (1.5 increases contrast)
BETA = 0 # Brightness control (0 has no effect)

OG_DIRECTORY = "datasets/original/"
PP_DIRECTORY = "datasets/preprocessed/"


def adjust_contrast(image):
    """
    Adjusts the contrast and brightness of an image from an
    image path and variables: alpha, and beta.
    """
    # Convert the image from uint8 to float to avoid overflow/underflow
    image = image.astype(np.float64)

    # Adjust contrast and brightness using `f(x) = alpha * x + beta` formula
    image = image * ALPHA + BETA
    # Clamp values to stay within the 0-255 range and convert back to uint8
    image = np.clip(image, 0, 255).astype(np.uint8)

    return image

