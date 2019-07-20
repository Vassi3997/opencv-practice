import cv2
import numpy as np

frame = cv2.imread('color-theory.jpg',cv2.IMREAD_COLOR)


hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])


mask = cv2.inRange(hsv,lower_blue,upper_blue)
result = cv2.bitwise_and(frame,frame,mask = mask)

cv2.imshow('frame',frame)
cv2.imshow('result',result)

cv2.waitKey(0)

cv2.destroyAllWindows()
