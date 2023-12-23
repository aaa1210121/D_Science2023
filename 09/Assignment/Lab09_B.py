import numpy as np
import matplotlib.pyplot as plt
import skimage

SingleRice = skimage.io.imread("SingleRice.jpg")
gray_SingleRice = skimage.color.rgb2gray(SingleRice)
thresh = skimage.filters.threshold_isodata(gray_SingleRice)
binary = gray_SingleRice > thresh
rice_erosion = skimage.morphology.binary_erosion(binary, skimage.morphology.diamond(3))
rice_dilation = skimage.morphology.binary_dilation(
    rice_erosion, skimage.morphology.diamond(17)
)
rice_erosion = skimage.morphology.binary_erosion(
    rice_dilation, skimage.morphology.diamond(23)
)
contours = skimage.measure.find_contours(rice_erosion, 0.9)


plt.subplot(1, 2, 1)
plt.imshow(SingleRice)

plt.subplot(1, 2, 2)
plt.imshow(SingleRice)
for contour in contours:
    plt.plot(contour[:, 1], contour[:, 0], color="red", linewidth=2)

plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[])
plt.tight_layout()
plt.show()