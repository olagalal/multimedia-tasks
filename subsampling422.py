import numpy as np
from numpy import array
import cv2
from PIL import Image
import math

img = cv2.imread('img/flower1.jpg', 1)
r, g, b = cv2.split(img)

WR = 0.299
WG = 0.587
WB = 0.114

U_MAX = 0.436
V_MAX = 0.615

imageY = []
imageU = []
imageV = []

def colormap_u():
    return np.array([[[i,255-i,0] for i in range(256)]],dtype=np.uint8)

def colormap_v():
    return np.array([[[0,255-i,i] for i in range(256)]],dtype=np.uint8)

#RGB to YUV
for i in range(0, len(img)):
    rowsY = []
    rowsU = []
    rowsV = []
    for j in range(0, len(img[i])):
        tempY = (WR * r[i][j] + WG * g[i][j] + WB * b[i][j])/255
        tempU = (U_MAX * ((b[i][j] - tempY) / (1 - WB)))/255
        tempV = (V_MAX * ((r[i][j] - tempY) / (1 - WR)))/255
        rowsY += [tempY]
        rowsU += [tempU]
        rowsV += [tempV]

    imageY += [rowsY]
    imageU += [rowsU]
    imageV += [rowsV]

y = array(imageY)
u = array(imageU)
v = array(imageV)

# Apply 4:2:2 Sampling
sampledU = []
sampledV = []
for i in range(0, len(imageU)):
    sampledURow = []
    sampledVRow = []
    for j in range(0, len(imageU[i])):
        if (j % 2) == 0:
            sampledURow += [imageU[i][j]]
            sampledVRow += [imageV[i][j]]
    sampledU += [sampledURow]
    sampledV += [sampledVRow]
	

# return U and V to it's original length
newImageU = []
newImageV = []
for i in range(0, len(sampledU)):
    newImageURow = []
    newImageVRow = []
    for j in range(0, len(sampledU[i])):
        newImageURow += [imageU[i][j * 2], (sampledU[i][j] + sampledU[i][j - 1]) / 2]
        newImageVRow += [imageV[i][j * 2], (sampledV[i][j] + sampledV[i][j - 1]) / 2]
    newImageU += [newImageURow]
    newImageV += [newImageVRow]

u = array(newImageU)
v = array(newImageV)

cv2.imshow('U',u)
cv2.imshow('V',v)
cv2.waitKey(0)
cv2.destroyAllWindows()

# YUV to RGB
newImage = []
for i in range(0, len(imageY)):
    row = []
    for j in range(0, len(imageY[i])):
        pixel = []
        R = (y[i][j] + (v[i][j] * ((1 - WR) / V_MAX)))
        G = ((y[i][j] / WG) - ((u[i][j] * WB * (1 - WB)) / (U_MAX * WG)) - ((v[i][j] * WR * (1 - WR)) / (V_MAX * WG)))
        B = (y[i][j] + (u[i][j] * ((1 - WB) / U_MAX)))
        pixel += [R]
        pixel += [G]
        pixel += [B]
        row += [pixel]
    newImage += [row]
	
displayNewImage = np.asarray(newImage)
#print (displayNewImage)
cv2.imshow('after',displayNewImage)

cv2.waitKey(0)
cv2.destroyAllWindows()