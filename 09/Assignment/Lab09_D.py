import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage.morphology import erosion, thin

finger = skimage.io.imread("Fingerprint.tif", as_gray=True)

plt.figure(figsize=(12, 8))
plt.subplot(2, 2, 1)
plt.title("Original image")
plt.imshow(finger, cmap="gray")

plt.subplot(2, 2, 2)
thresh = skimage.filters.threshold_otsu(finger)
binary = finger > thresh
seed = finger > 70
reconstructed_image = skimage.morphology.reconstruction(seed, binary, method="erosion")
reconstructed_image = skimage.util.invert(reconstructed_image)
plt.title("Reconstruct image")
plt.imshow(reconstructed_image, cmap="gray")

plt.subplot(2, 2, 3)
a = skimage.morphology.skeletonize(reconstructed_image)
plt.title("Skeletonize image")
plt.imshow(a, cmap="gray")

plt.subplot(2, 2, 4)
plt.title("Features founded")

plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[])
plt.tight_layout()
plt.show()