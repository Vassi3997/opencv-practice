import cv2

img1 = cv2.imread('cover.jpg')
img2 = cv2.imread('logo.jpg')

r,c,chan = img2.shape
print(r,c)
roi = img1[0:r,0:c]


grayimg2 = cv2.cvtColor(img2,cv2.COLOR_BGR2GRAY)

ret,mask = cv2.threshold(grayimg2,220 ,255 ,cv2.THRESH_BINARY_INV)

mask_inv = cv2.bitwise_not(mask)

imgbg = cv2.bitwise_and(roi,roi,mask = mask_inv)
imgfg = cv2.bitwise_and(img2,img2,mask = mask)


dst = cv2.add(imgbg,imgfg)
img1[0:r,0:c]=dst


#cv2.imshow('mask', mask)
#cv2.imshow('mask_inv',mask_inv)

cv2.imshow('imgbg',imgbg)
cv2.imshow('imgfg',imgfg)

cv2.imshow('logo',img1)

cv2.waitKey(0)
cv2.destroyAllWindows()
