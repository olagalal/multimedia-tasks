import numpy as np
import cv2

alpha = cv2.imread('img/alpha.jpg')
foreground = cv2.imread('img/foreground.jpg')
background = cv2.imread('img/background.jpg')

alpha = alpha.astype(float)/255

resultAlpha = (alpha*foreground) + ((1-alpha)*background)
# to keep instensity between 0 and 1 for alpha mask
cv2.imshow('result',resultAlpha/255)
cv2.imshow('aplha',alpha)
cv2.imshow('Foreground',foreground)
cv2.imshow('Background',background)
cv2.waitKey(0)
cv2.destroyAllWindows()

#to write an image
cv2.imwrite('img/result.png',resultAlpha)

