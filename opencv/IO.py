import cv2
import matplotlib.pyplot as plt
import numpy

img = cv2.imread('color-theory.jpg',cv2.IMREAD_GRAYSCALE)

# cv2.imshow('img',img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

plt.imshow(img,cmap = 'gray' , interpolation = 'bicubic')
plt.show()