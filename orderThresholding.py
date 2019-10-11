import numpy as np
import cv2

img = cv2.imread('img/spongebob.jpg', 0)
t1 = cv2.imread('img/spongebob.jpg', 0)

rows, cols = t1.shape

A = [[0, 128, 32, 160],
	[192, 64, 224, 96],
	[48, 176, 16, 144],
	[240, 112, 208, 80]]


for x in range(rows):
	for y in range(cols):
		i = np.mod(rows,2)
		j = np.mod(cols,2)
		if t1[x][y] > A[i][j]:
			t1[x][y] = 255
		else:
			t1[x][y] = 0
		
	
	
'''
A = [[0,128],
	[192, 64]]

#height = math.ceil(rows/len(A[0]))
#width = math.ceil(cols/len(A))
#print(height, width)
#print(rows, cols)

if(rows %2!=0):
	rows= rows-1
	
if(cols %2!=0):
	cols= cols-1

for i in range(0,rows,2):
	for j in range(0,cols,2):
		for k in range(0,2,2):
			for m in range (0,2,2):
				if(t1[i][j]> A[k][m]):
					t1[i][j]=255
				else:
					t1[i][j]=0
				
				if(t1[i][j+1]> A[k][m+1]):
					t1[i][j+1]=255
				else:
					t1[i][j+1]=0
				
				if(t1[i+1][j]> A[k+1][m]):
					t1[i+1][j]=255
				else:
					t1[i+1][j]=0
					
				if(t1[i+1][j+1]> A[k+1][m+1]):
					t1[i+1][j+1]=255
				else:
					t1[i+1][j+1]=0

'''
	
cv2.imshow('image',img)
cv2.imshow('Order Thresholding',t1)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('img/OrderThresholding.png',t1)
