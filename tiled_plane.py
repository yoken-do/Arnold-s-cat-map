import matplotlib.pyplot as plt
from skimage.transform import resize
import numpy as np

image = plt.imread('image.jpg')
resized_image = resize(image, (100, 100), anti_aliasing=True)
resized_image = (resized_image * 255).astype('uint8')

new_image = np.zeros((200, 200, 3)).astype('uint8')

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

for i in range(2):
    for j in range(2):
        x_start, x_end = i * 100, (i + 1) * 100
        y_start, y_end = j * 100, (j + 1) * 100
        new_image[x_start:x_end, y_start:y_end] = step_1(resized_image)

plt.imsave("tiled_plane_transform.jpg", new_image)
