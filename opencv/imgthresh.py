import cv2

img = cv2.imread('lowlight.jpg',cv2.IMREAD_GRAYSCALE)

ret,threshold=cv2.threshold(img,80,255,cv2.THRESH_BINARY)
gauss = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,115,5)
#gauss1 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,cv2.THRESH_BINARY,15,0)
retv,otsu = cv2.threshold(img, 125,255,cv2.THRESH_BINARY+cv2.THRESH_OTSU)


cv2.imshow('gauss',gauss)
cv2.imshow('otsu',otsu)
cv2.waitKey(0)
cv2.destroyAllWindows()
