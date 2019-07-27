import cv2
import numpy as np
import matplotlib.pyplot as pt

frame = cv2.imread('3d.jpg')

mask =np.zeros(frame.shape[:2],np.uint8)

bgM = np.zeros((1,65),np.float64)
fgM = np.zeros((1,65),np.float64)

rect = (40,40,170,140)
cv2.grabCut(frame,mask,rect,bgM,fgM,5,cv2.GC_INIT_WITH_RECT)
mask2 = np.where((mask == 2)| (mask ==0),0,1).astype('uint8')
img = frame*mask2[:,:,np.newaxis]


cv2.imshow('image',img)
cv2.waitKey(0)
cv2.destroyAllWindows()


