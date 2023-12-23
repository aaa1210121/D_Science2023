import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage import img_as_float, io
from skimage.morphology import square, disk, square, rectangle, diamond
from skimage.filters.rank import median, minimum, maximum, mean

Saturn = skimage.io.imread("Saturn.jpg")
print(Saturn.shape)
plt.subplot(3, 4, 1)
plt.imshow(Saturn)
plt.title("Saturn", fontsize=30)

plt.subplot(3, 4, 2)
ball = skimage.morphology.ball(radius=5)
mean_img = skimage.filters.rank.mean(Saturn, ball)
plt.imshow(mean_img)
plt.title("Mean filter", fontsize=30)


plt.subplot(3, 4, 3)
gaussian_img = skimage.filters.gaussian(Saturn, sigma=1, channel_axis=-1)
plt.imshow(gaussian_img)
plt.title("Gaussian filter", fontsize=30)

plt.subplot(3, 4, 4)
tv_img = skimage.restoration.denoise_tv_chambolle(Saturn, weight=0.2, channel_axis=-1)
plt.imshow(tv_img)
plt.title(" Total variation filter", fontsize=30)

plt.subplot(3, 4, 5)
bilateral_img = skimage.restoration.denoise_bilateral(
    Saturn, sigma_color=0.1, sigma_spatial=15, channel_axis=-1
)
plt.imshow(bilateral_img)
plt.title(" Bilateral filter", fontsize=30)

plt.subplot(3, 4, 6)
Wavelet_img = skimage.restoration.denoise_wavelet(
    Saturn, channel_axis=-1, convert2ycbcr=True, rescale_sigma=True
)
plt.imshow(Wavelet_img)
plt.title(" Wavelet denoising filter", fontsize=30)


Saturn = img_as_float(io.imread("Saturn.jpg", as_gray=True))
neighborhood = square(width=3)
Saturn_smoothed = img_as_float(minimum(Saturn, neighborhood))
detail = Saturn - Saturn_smoothed
coins_sharpend = Saturn + detail * 2


plt.subplot(3, 4, 7)
plt.imshow(Saturn_smoothed, cmap="gray", vmin=0, vmax=1)
plt.title("Smoothed image", fontsize=30)
plt.subplot(3, 4, 8)
plt.imshow(detail, cmap="gray", vmin=-0.5, vmax=1)
plt.title("Detail", fontsize=30)
plt.subplot(3, 4, 9)
plt.imshow(coins_sharpend, cmap="gray", vmin=0, vmax=1)
plt.title("Sharpened", fontsize=30)


Saturn_laplacian = skimage.filters.laplace(Saturn)
plt.subplot(3, 4, 10)
plt.title("Laplacian", fontsize=30)
plt.imshow(Saturn_laplacian, cmap="gray", vmin=-0.1, vmax=0.1)

Saturn_enhanced = Saturn + Saturn_laplacian * 2
plt.subplot(3, 4, 11)
plt.title("Enhanced image", fontsize=30)
plt.imshow(Saturn_enhanced, cmap="gray", vmax=1.0, vmin=0)

plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[])
plt.tight_layout()
plt.show()
