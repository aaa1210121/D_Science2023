import numpy as np
import matplotlib.pyplot as plt
import skimage

a = np.array(
    [
        [1, 1, 1, 1, 1, 1, 1, 1, 1, 1],
        [1, 1, 0, 0, 0, 0, 0, 1, 1, 1],
        [1, 0, 0, 1, 1, 1, 0, 0, 0, 1],
        [1, 0, 0, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 0, 1, 1, 0, 1, 1],
        [1, 0, 1, 1, 0, 0, 0, 0, 1, 1],
        [1, 0, 1, 1, 1, 1, 1, 0, 0, 1],
        [1, 0, 0, 0, 1, 1, 0, 0, 0, 1],
        [1, 1, 1, 0, 0, 0, 0, 0, 1, 1],
        [1, 1 ,1 ,1, 1, 1, 1, 1, 1, 1,]
        ]
)

erosion = skimage.morphology.binary_erosion(
    a, footprint=np.ones((2, 2)), out=np.zeros_like(a)
)

plt.figure(figsize=(8, 4))
plt.subplot(2, 2, 1)
plt.title("Origin", fontsize=16)
plt.imshow(a, cmap="gray")
plt.subplot(2, 2, 2)
plt.title("After Erosion", fontsize=16)
plt.imshow(erosion, cmap="gray")
plt.setp(plt.gcf().get_axes(), xticks=[], yticks=[])
plt.tight_layout()
plt.show()
 
