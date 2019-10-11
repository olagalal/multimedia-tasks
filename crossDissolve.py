from time import sleep
import numpy as np
import cv2

img1 = cv2.imread('img/flower1.jpg')
img2 = cv2.imread('img/flower2.jpg')

for i in range(0,100):
    fadein = i/100.0
    dst = cv2.addWeighted( img1, 1-fadein, img2, fadein, 0)
    cv2.imshow('img', dst)
    cv2.waitKey(1)
    sleep(0.005)

	   
cv2.waitKey(0)
cv2.destroyAllWindows()
