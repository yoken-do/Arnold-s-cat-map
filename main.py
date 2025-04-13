import numpy as np
import matplotlib.pyplot as plt

def chaos_transform(image: np.array, iterations: int) -> np.array:
    image_ = np.copy(image)
    if iterations <= 0:
        return image_
    for _ in range(0, iterations):
        result = np.zeros_like(image_)
        for y in range(image.shape[0]):
            for x in range(image.shape[1]):
                nx, ny = (x + y) % image.shape[1], (x + 2*y) % image.shape[0]
                result[ny, nx] = image_[y, x]
        image_ = result
    return image_

def unchaos_transform(image: np.array, iterations: int) -> np.array:
    image_ = np.copy(image)
    if iterations <= 0:
        return image_
    for _ in range(0, iterations):
        result = np.zeros_like(image_)
        for y in range(image.shape[0]):
            for x in range(image.shape[1]):
                ny = (y - x) % image.shape[0]
                nx = (x - ny) % image.shape[1]
                result[ny, nx] = image_[y, x]
        image_ = result
    return image_

image = plt.imread("image.jpg")

i = 1
transformed = chaos_transform(image, 1)
plt.imsave(f"transformed_image_{i}.png", transformed)

while not(np.array_equal(image, transformed)):
    transformed = chaos_transform(transformed, 1)
    i+=1
    plt.imsave(f"transformed_image_{i}.png", transformed)
print(i)