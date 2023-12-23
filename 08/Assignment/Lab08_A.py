import numpy as np
import matplotlib.pyplot as plt
import skimage
from scipy.signal import convolve2d

coin = skimage.io.imread("building.jpg", as_gray=True)

plt.subplot(2, 3, 1)
plt.imshow(coin, cmap="gray")
plt.title("coin", fontsize=30)

plt.subplot(2, 3, 2)
a = np.full((3, 3), -1)
a[1, :] = 2
filter_a = convolve2d(coin, a, mode="same")
plt.imshow(filter_a, cmap="gray", vmin=-0.1, vmax=0.1)
plt.title("(a)", fontsize=30)

plt.subplot(2, 3, 3)
b = np.full((3, 3), -1)
b[(2, 1, 0), (0, 1, 2)] = 2
filter_b = convolve2d(coin, b, mode="same")
plt.imshow(filter_b, cmap="gray", vmin=-0.1, vmax=0.1)
plt.title("(b)", fontsize=30)

plt.subplot(2, 3, 4)
c = np.full((3, 3), -1)
c[1, 1] = 8
filter_c = convolve2d(coin, c, mode="same")
plt.imshow(filter_c, cmap="gray", vmin=-0.1, vmax=0.1)
plt.title("(c)", fontsize=30)

plt.subplot(2, 3, 5)
d = np.full((3, 3), 0)
d[(0, 2), 0] = -1
d[1, 0] = -2
d[1, 2] = 2
d[(0, 2), 2] = 1
filter_d = convolve2d(coin, d, mode="same")
plt.imshow(filter_d, cmap="gray", vmin=-0.1, vmax=0.1)
plt.title("(d)", fontsize=30)

plt.subplot(2, 3, 6)
e = np.full((3, 3), 0)
e[1, (0, 2)] = 1
e[(0, 2), 1] = -1
filter_e = convolve2d(coin, e, mode="same")
plt.imshow(filter_e, cmap="gray", vmin=-0.1, vmax=0.1)
plt.title("(e)", fontsize=30)
plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[])
plt.tight_layout()
plt.show()
