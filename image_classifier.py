import cv2
import numpy as np

# Load images
img1 = cv2.imread("images/vertical.png", cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("images/horizontal.png", cv2.IMREAD_GRAYSCALE)

def classify_image(image):

    # Image preperation
    img = image/255

    # Flatten image
    img_flattened = img.flatten()

    # Filter
    filter = [1, -1, 1, 1, -1, 1, 1, -1, 1]

    array_sum = sum(img_flattened*filter)

    # Return result
    if array_sum == 1:
        return "Image is horizontal"
        
    else:
        return "Image is vertical"

if __name__ == "__main__":
    result = classify_image(img2)
    print(result)
