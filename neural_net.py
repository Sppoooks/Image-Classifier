import numpy as np
import cv2

def sigmoid(x):
    return 1/(1+np.exp(-x))

def sigmoid_der(x):
    return sigmoid(x)*(1-sigmoid(x))

# Input
img = cv2.imread("images/vertical.png", cv2.IMREAD_GRAYSCALE)
img = img/255
img_flattened = img.flatten()

# Weights
weights = np.array([0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5, 0.5])

# Weighted sum
weighted_sum = sum(img_flattened*weights)

# Activation function
result = sigmoid(weighted_sum)

# Output
if result < 0.5:
    print("Vertical")
elif result >= 0.5:
    print("Horizontal")

# Error
error = result - 0

# Error correction
adjustment = error*sigmoid_der(result)
weights -= np.dot(img_flattened, adjustment)
print(weights)