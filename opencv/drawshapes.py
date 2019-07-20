import cv2
import matplotlib.pyplot as plt

img = cv2.imread('color-theory.jpg',cv2.IMREAD_COLOR)
cv2.line(img, (12,12),(120,120),(0,0,0),5)

cv2.rectangle(img , (120,120), (240,240) , (0,255,255) , 12)
cv2.circle(img , (340,340) , 100 , (255,0,255), -1)

cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()
