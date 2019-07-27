import cv2 
import numpy as np

img = cv2.imread('shape.png')
grayimg = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
gray = np.float32(grayimg)

corner = cv2.goodFeaturesToTrack(gray,30,0.01,10)
corner = np.int0(corner)
for i in corner:
	x,y = i.ravel()
	cv2.circle(img,(x,y),3,255,-1)	

cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()

