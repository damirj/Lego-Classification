import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg


img = mpimg.imread("dataset/2357 brick corner 1x2x2 000L.png")
print("Shape of the image: {}".format(img.shape))
print("Max value: {}".format(np.amax(img)))

plt.imshow(img)
plt.show()