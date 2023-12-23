import numpy as np
import matplotlib.pyplot as plt
import skimage
origin = skimage.io.imread("Xray.png", as_gray=True)

plt.figure(figsize=(10, 8))
plt.subplot(2, 4, 1)
plt.title("Original image")
plt.imshow(origin, cmap="gray")

plt.subplot(2, 4, 2)
a = skimage.filters.laplace(origin)
plt.title("(a)")
plt.imshow(a, cmap="gray")

plt.subplot(2, 4, 3)
b = origin - a
plt.title("(b)")
plt.imshow(b, cmap="gray")

plt.subplot(2, 4, 4)
# xray_sobel_x = skimage.filters.sobel_v(b)
# xray_sobel_y = skimage.filters.sobel_h(b)
# c =b + xray_sobel_x + xray_sobel_y
c = skimage.filters.sobel(b)
plt.title("(c)")
plt.imshow(c, cmap="gray")

plt.subplot(2, 4, 5)
from scipy.signal import convolve2d

averaging = np.ones((5, 5)) / 25
d = convolve2d(c, averaging, mode="same")
plt.title("(d)")
plt.imshow(d, cmap="gray")

plt.subplot(2, 4, 6)
e = np.multiply(b, d)
plt.title("(e)")
plt.imshow(e, cmap="gray")

plt.subplot(2, 4, 7)
e_min = np.min(e)
e_max = np.max(e)
e_normalized = 255 * (e - e_min) / (e_max - e_min)
f = origin + e_normalized
plt.title("(f)")
plt.imshow(f, cmap="gray")

plt.subplot(2, 4, 8)
# f= skimage.exposure.rescale_intensity(f, out_range=(0, 255))
g = skimage.exposure.adjust_gamma(f, gamma=0.5)
plt.title("(g)")
plt.imshow(g, cmap="gray")

plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[])
plt.tight_layout()
plt.show()
