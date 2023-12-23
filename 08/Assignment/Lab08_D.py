import numpy as np
import matplotlib.pyplot as plt
import skimage
from skimage.morphology import diamond

y_fan = skimage.io.imread("YellowFan.png")
img = np.zeros((y_fan.shape[0], y_fan.shape[1]))

y_fanhsv = skimage.color.rgb2hsv(y_fan)
img[np.logical_and(y_fanhsv[:, :, 0] > 0.15, y_fanhsv[:, :, 0] < 0.19)] = 255
fan_erosion = skimage.morphology.binary_erosion(img, diamond(5))
fan_dilation = skimage.morphology.binary_dilation(fan_erosion, diamond(5))

f, (ax0, ax1) = plt.subplots(1, 2)
ax0.imshow(y_fan)
ax1.imshow(fan_dilation, cmap="gray")

plt.tight_layout()
plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[])
labeled_mask = skimage.measure.label(fan_dilation)
fan_properties = skimage.measure.regionprops(labeled_mask)
fan_area_size = fan_properties[0].area
print(f"Area size of the yellow fan: {fan_area_size} pixels")
plt.show()
