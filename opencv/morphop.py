import cv2
import numpy as np

frame = cv2.imread('color-theory.jpg',cv2.IMREAD_COLOR)


hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])


mask = cv2.inRange(hsv,lower_blue,upper_blue)
result = cv2.bitwise_and(frame,frame,mask = mask)

kernel = np.ones((15,15),np.uint8)

erode = cv2.erode(result,kernel,iterations = 1)
dilate = cv2.dilate(result,kernel,iterations = 1)

openin = cv2.morphologyEx(result, cv2.MORPH_OPEN,kernel)
closin = cv2.morphologyEx(result, cv2.MORPH_CLOSE,kernel)


# cv2.imshow('erode',erode)
# cv2.imshow('dilate',dilate)
cv2.imshow('openin',openin)
cv2.imshow('closin',closin)

cv2.imshow('result',result)

cv2.waitKey(0)

cv2.destroyAllWindows()
