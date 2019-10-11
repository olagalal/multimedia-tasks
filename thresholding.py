import numpy as np
import cv2

img = cv2.imread('img/flower2.jpg', 0)

retval1, t1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)
t2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,17,2)

cv2.imshow('image',img)
cv2.imshow('Thresholding 128',t1)
cv2.imshow('Adaptive Thresholding',t2)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('Thresholding128.png',t1)
cv2.imwrite('AdaptiveThresholding.png',t2)

