from matplotlib import image as img
import matplotlib.pyplot as plt
from copy import deepcopy


def increase_contrast(image, a, s, t):
    res = deepcopy(image)
    width, height, depth = res.shape
    for i in range(width):
        for j in range(height):
            red, green, blue = res[i][j]
            new_red = min(255, max(0, a * (red - s) + t))
            new_green = min(255, max(0, a * (green - s) + t))
            new_blue = min(255, max(0, a * (blue - s) + t))
            res[i][j] = [new_red, new_green, new_blue]
    return res


def plot_image(original, transformed, a, s, t):
    fig = plt.figure(figsize=(10, 7))

    fig.add_subplot(1, 2, 1)
    plt.imshow(original)
    plt.title("Original Image")

    fig.add_subplot(1, 2, 2)
    plt.imshow(transformed)
    plt.title("Transformed Image a = "+str(a)+' s = '+str(s)+' t = '+str(t))

    plt.show()


if __name__ == '__main__':

    img_blurred = img.imread('img/img_blured.jpg')
    img_detailed = img.imread('img/img_detailed.jpg')
    img_high_contrast = img.imread('img/img_high_contrast.jpg')
    img_low_contrast = img.imread('img/img_low_contrast.jpg')

    images_n_params = [
        {'image': img_blurred, 'a': 0.8, 's': 20, 't': 3},
        {'image': img_detailed, 'a': 0.8, 's': 20, 't': 3},
        {'image': img_high_contrast, 'a': 0.8, 's': 20, 't': 3},
        {'image': img_low_contrast, 'a': 0.8, 's': 20, 't': 3}
    ]

    for entity in images_n_params:
        trans = increase_contrast(image=entity['image'], a=entity['a'], s=entity['s'], t=entity['t'])
        plot_image(original=entity['image'], transformed=trans, a=entity['a'], s=entity['s'], t=entity['t'])
