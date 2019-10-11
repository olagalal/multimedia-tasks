import numpy as np
import cv2

img = cv2.imread('img/spongebob.jpg', 0)
#for 2*2 pattern dithering
t2 = cv2.imread('img/spongebob.jpg', 0)
#for 3*3 pattern dithering
t1 = cv2.imread('img/spongebob.jpg', 0)

rows, cols = t1.shape
rows2, cols2 = t2.shape


for i in range(0,rows2-1,2):
	for j in range(0,cols2-1,2):
		for x in range (0,2,2):
			for y in range (0,2,2):
				avg = (np.add(t2[i][j],t2[i+1][j])+np.add(t2[i][j+1],t2[i+1][j+1]))/400
				#print(t1[i][j],t1[i+1][j],t1[i][j+1],t1[i+1][j+1])
				#print(x, y, avg)
				
				if avg >= 0.8:
					t2[i][j]=255
					t2[i+1][j]=255
					t2[i][j+1]=255
					t2[i+1][j+1]=255
				elif avg>= 0.6:
					t2[i][j]=255
					t2[i+1][j]=255
					t2[i][j+1]=255
					t2[i+1][j+1]=0
				elif avg>= 0.4:
					t2[i][j]=0
					t2[i+1][j]=255
					t2[i][j+1]=255
					t2[i+1][j+1]=0
				elif avg>= 0.2:
					t2[i][j]=0
					t2[i+1][j]=255
					t2[i][j+1]=0
					t2[i+1][j+1]=0
				else:
					t2[i][j]=0
					t2[i+1][j]=0
					t2[i][j+1]=0
					t2[i+1][j+1]=0		
	
		
for i in range(0,rows-2,3):
	for j in range(0,cols-2,3):
		for x in range (0,3,3):
			for y in range (0,3,3):
				r1 = t1[i][j]+t1[i+1][j]+t1[i+2][j]
				r2 = t1[i][j+1]+t1[i+1][j+1]+t1[i+2][j+1]
				r3 = t1[i][j+2]+t1[i+1][j+2]+t1[i+2][j+2]
				avg=(r1+r2+r3)/900
				#print(t1[i][j],t1[i+1][j],t1[i][j+1],t1[i+1][j+1])
				#print(x, y, avg)
				
				if avg >= 0.9:
					#r1
					t1[i][j]=255
					t1[i+1][j]=255
					t1[i+2][j]=255
					#r2
					t1[i][j+1]=255
					t1[i+1][j+1]=255
					t1[i+2][j+1]=255
					#r3
					t1[i][j+2]=255
					t1[i+1][j+2]=255
					t1[i+2][j+2]=255
				elif avg >= 0.8:
					#r1
					t1[i][j]=255
					t1[i+1][j]=255
					t1[i+2][j]=255
					#r2
					t1[i][j+1]=255
					t1[i+1][j+1]=0
					t1[i+2][j+1]=255
					#r3
					t1[i][j+2]=255
					t1[i+1][j+2]=255
					t1[i+2][j+2]=255
				elif avg >= 0.7:
					#r1
					t1[i][j]=255
					t1[i+1][j]=255
					t1[i+2][j]=255
					#r2
					t1[i][j+1]=0
					t1[i+1][j+1]=0
					t1[i+2][j+1]=255
					#r3
					t1[i][j+2]=255
					t1[i+1][j+2]=255
					t1[i+2][j+2]=255
				elif avg >= 0.6:
					#r1
					t1[i][j]=255
					t1[i+1][j]=0
					t1[i+2][j]=255
					#r2
					t1[i][j+1]=0
					t1[i+1][j+1]=0
					t1[i+2][j+1]=255
					#r3
					t1[i][j+2]=255
					t1[i+1][j+2]=255
					t1[i+2][j+2]=255
				elif avg >= 0.5:
					#r1
					t1[i][j]=255
					t1[i+1][j]=0
					t1[i+2][j]=255
					#r2
					t1[i][j+1]=0
					t1[i+1][j+1]=0
					t1[i+2][j+1]=255
					#r3
					t1[i][j+2]=255
					t1[i+1][j+2]=255
					t1[i+2][j+2]=0
				elif avg >= 0.4:
					#r1
					t1[i][j]=255
					t1[i+1][j]=0
					t1[i+2][j]=255
					#r2
					t1[i][j+1]=0
					t1[i+1][j+1]=0
					t1[i+2][j+1]=0
					#r3
					t1[i][j+2]=255
					t1[i+1][j+2]=255
					t1[i+2][j+2]=0	
				elif avg >= 0.3:
					#r1
					t1[i][j]=255
					t1[i+1][j]=0
					t1[i+2][j]=255
					#r2
					t1[i][j+1]=0
					t1[i+1][j+1]=0
					t1[i+2][j+1]=0
					#r3
					t1[i][j+2]=0
					t1[i+1][j+2]=255
					t1[i+2][j+2]=0	
				elif avg >= 0.2:
					#r1
					t1[i][j]=0
					t1[i+1][j]=0
					t1[i+2][j]=255
					#r2
					t1[i][j+1]=0
					t1[i+1][j+1]=0
					t1[i+2][j+1]=0
					#r3
					t1[i][j+2]=0
					t1[i+1][j+2]=255
					t1[i+2][j+2]=0
				elif avg >= 0.1:
					#r1
					t1[i][j]=0
					t1[i+1][j]=0
					t1[i+2][j]=0
					#r2
					t1[i][j+1]=0
					t1[i+1][j+1]=0
					t1[i+2][j+1]=0
					#r3
					t1[i][j+2]=0
					t1[i+1][j+2]=255
					t1[i+2][j+2]=0
				else:
					#r1
					t1[i][j]=0
					t1[i+1][j]=0
					t1[i+2][j]=0
					#r2
					t1[i][j+1]=0
					t1[i+1][j+1]=0
					t1[i+2][j+1]=0
					#r3
					t1[i][j+2]=0
					t1[i+1][j+2]=0
					t1[i+2][j+2]=0	
					
cv2.imshow('image',img)
cv2.imshow('Pattern 2*2 Dithering',t2)
cv2.imshow('Pattern 3*3 Dithering',t1)
cv2.waitKey(0)
cv2.destroyAllWindows()

cv2.imwrite('img/PatternDithering2.png',t2)
cv2.imwrite('img/PatternDithering3.png',t1)
