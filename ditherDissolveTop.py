from time import sleep
from math import ceil
import numpy as np
import cv2

img1 = cv2.imread('img/flower1.jpg')
img2 = cv2.imread('img/flower2.jpg')

dst = img2
rows, cols, chan = img1.shape

alpha = 0.003 #> 600*0.003 = 2  > 2  cols
#alpha = 0.005 #> 600*0.005 = 3  > 3  cols
#alpha = 0.01  #> 600*0.01  = 6  > 6  cols
#alpha = 0.03  #> 600*0.03  = 20 > 20 cols
#alpha = 0.05  #> 600*0.05  = 30 > 30 cols

steps = int(ceil(cols*alpha))
#print(cols)
#print(steps)

start =  rows - 4

for i in reversed(range(0,start,steps)):
	for j in range(cols):
		for k in range (0, steps):
			dst[i+k][j] = img1[i+k][j]
	cv2.imshow('img', dst)
	cv2.waitKey(1)
	sleep(0.05)

cv2.waitKey(0)
cv2.destroyAllWindows()