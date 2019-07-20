import cv2
import numpy as np

frame = cv2.imread('color-theory.jpg',cv2.IMREAD_COLOR)


hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

lower_blue = np.array([110,50,50])
upper_blue = np.array([130,255,255])


mask = cv2.inRange(hsv,lower_blue,upper_blue)
result = cv2.bitwise_and(frame,frame,mask = mask)

kernel = np.ones((15,15),np.float32)/255
smooth = cv2.filter2D(result,-1,kernel)

blur = cv2.GaussianBlur(result,(5,5),0)

median = cv2.medianBlur(result,15)

bilateral = cv2.bilateralFilter(result,15,75,75)

cv2.imshow('smooth',smooth)
# cv2.imshow('result',result)
cv2.imshow('blur',blur)
cv2.imshow('median',median)
cv2.imshow('bilateral',bilateral)

cv2.waitKey(0)

cv2.destroyAllWindows()
