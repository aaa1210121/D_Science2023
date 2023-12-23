from skimage import transform
import matplotlib.pylab as plt
import numpy as np
import skimage


invoice = skimage.io.imread("invoice.jpg")

src = np.array([[0, 0], [0, 563], [422, 563], [422, 0]])
dst = np.array([[120, 200], [75, 520], [290, 520], [280, 190]])

tform3 = transform.ProjectiveTransform()
tform3.estimate(src, dst)
warped = transform.warp(invoice, tform3, output_shape=(563, 422))

gray_invoice = skimage.color.rgb2gray(warped)

local_threshold = skimage.filters.threshold_local(
    gray_invoice, block_size=95, method="gaussian"
)
otsu_thresh = skimage.filters.threshold_otsu(gray_invoice)
otsu_scanned = gray_invoice > otsu_thresh

yen_thresh = skimage.filters.threshold_yen(gray_invoice)
yen_scanned = gray_invoice > otsu_thresh

plt.subplot(1, 4, 1)
plt.imshow(invoice, cmap="gray")
plt.title("Origin image" ,fontsize =30)
plt.plot(dst[:, 0], dst[:, 1], ".r")

plt.subplot(1, 4, 2)
plt.imshow(warped, cmap=plt.cm.gray)
plt.title("Intermediate image" ,fontsize =30)

plt.subplot(1, 4, 3)
plt.imshow(otsu_scanned, cmap="gray" ,vmin=0 ,vmax=1)
plt.title("Scanned invoice_otsu",fontsize =30)

plt.subplot(1, 4, 4)
plt.imshow(yen_scanned, cmap="gray",vmin=0 ,vmax=1)
plt.title("Scanned invoice_yen",fontsize =30)

plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[])
plt.tight_layout()
plt.show()
