import numpy as np
import cv2
from matplotlib import pyplot as plt


img = cv2.imread('sbb_photo.png', cv2.IMREAD_UNCHANGED)
img2 = img[:, :, ::-1]

plt.subplot(121)
plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.subplot(122)
plt.imshow(img2)#, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])
plt.show()

cv2.namedWindow('window name', cv2.WINDOW_NORMAL)
cv2.imshow('window name', img)
cv2.waitKey(0)
cv2.destroyAllWindows()




