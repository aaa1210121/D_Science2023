import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import io


# Do NOT modifify the function names


def fade_gradually(img):
    processed = img.copy()
    # TODO_B1
    height, width, channels = processed.shape
    for i in range(width):
        for j in range(height):
            gray = (
                1 / 3 * processed[j, i, 0]
                + 1 / 3 * processed[j, i, 1]
                + 1 / 3 * processed[j, i, 2]
            )
            processed[j, i, :] = (1 - i / width) * processed[j, i, :] + (
                i / width
            ) * gray
    return processed


def image_matting(img):
    processed = img.copy()
    # TODO_B2
    gray = skimage.color.rgb2gray(processed)
    foreground = gray > 0.005
    height, width, channels = processed.shape
    processed = np.zeros((height, width, 4), dtype=np.uint8)
    processed[foreground, :3] = img[foreground, :3]
    processed[foreground, 3] = 255

    return processed


def my_resize(img, height, width):
    # TODO_B3

    return


# You are incouraged to test your program in the main function


def main():
    monkey_island = io.imread("monkey_island.jpg")
    fade_monkey_island = fade_gradually(monkey_island)
    f, ax = plt.subplots(2, 2)
    ax[0, 0].imshow(monkey_island)
    ax[0, 0].axis("off")
    ax[0, 1].imshow(fade_monkey_island)
    ax[0, 1].axis("off")
    print(fade_monkey_island.shape)

    cat = io.imread("cat.png")
    mat_cat = image_matting(cat)
    ax[1, 0].imshow(cat)
    ax[1, 0].axis("off")
    ax[1, 1].imshow(mat_cat)
    ax[1, 1].axis("off")
    f.tight_layout()
    plt.show()
    pass

if __name__ == "__main__":
    main()

