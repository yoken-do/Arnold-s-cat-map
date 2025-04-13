import numpy as np
import matplotlib.pyplot as plt

image = plt.imread("void.jpg")

def step_1(image: np.array) -> np.array:
    image_ = np.copy(image)
    result = np.zeros_like(image_)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            nx, ny = (x + y) % image.shape[1], y % image.shape[0]
            result[ny, nx] = image_[y, x]
    image_ = result
    return image_

def step_2(image: np.array) -> np.array:
    image_ = np.copy(image)
    result = np.zeros_like(image_)
    for y in range(image.shape[0]):
        for x in range(image.shape[1]):
            nx, ny = x % image.shape[1], (x + y) % image.shape[0]
            result[ny, nx] = image_[y, x]
    image_ = result
    return image_

image_ = step_1(image)
plt.imsave(f"step_transformed_image_1.png", image_)
image_ = step_2(image_)
plt.imsave(f"step_transformed_image_2.png", image_)