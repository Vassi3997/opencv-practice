import cv2
import numpy as np

img = cv2.imread('rep.png',0)
temp = cv2.imread('temp.png',0)

w,h = temp.shape[::-1]

result = cv2.matchTemplate(img,temp,cv2.TM_CCOEFF_NORMED)
threshold = 0.60
loc = np.where(result >= threshold)

for pt in zip(*loc[::-1]):
	cv2.rectangle(img,pt,(pt[0]+w,pt[0]+h),(255,255,255),1)

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
