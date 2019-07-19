import cv2

img = cv2.imread('color-theory.jpg', cv2.IMREAD_COLOR)

#px  = img[155,250] # gives the pixel value



#print(px)

#img[250:255,550:555] = [0,0,0] #changing pixel color (values)


img[0:100,0:100] = img[250:350,250:350] #copying part of image
cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows() 
