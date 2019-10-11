import numpy as np
import cv2

img = cv2.imread('img/spongebob.jpg', 0)
t1 = cv2.imread('img/spongebob.jpg', 0)

rows, cols = t1.shape
alpha = 7/16
beta = 3/16
gamma = 5/16
delta = 1/16

for i in range(rows-1):
	for j in range(cols-1):
		initial = t1[i][j]
		if t1[i][j] >= 128:
			t1[i][j] = 255
		else:
			t1[i][j] = 0
			
		error = np.subtract(initial,t1[i][j])
		
		t1[i][j+1]=t1[i][j+1]+ alpha*error
		t1[i+1][j-1]= t1[i+1][j-1]+beta*error
		t1[i+1][j]=t1[i+1][j]+gamma*error
		t1[i+1][j+1]=t1[i+1][j+1]+delta*error
		
cv2.imshow('image',img)
cv2.imshow('Flyod Dithering',t1)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('img/FloydDithering.png',t1)