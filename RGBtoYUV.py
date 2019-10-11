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

#to apply colormap
lut_u, lut_v = colormap_u(), colormap_v()

ux = 127.5 * (1.0 - u)
ux = np.asarray(np.dstack((ux, ux, ux)), dtype=np.uint8)
vx = 127.5 * (1.0 - v)
vx = np.asarray(np.dstack((vx, vx, vx)), dtype=np.uint8)

u_mapped = cv2.LUT(ux, lut_u)
v_mapped = cv2.LUT(vx, lut_v)

cv2.imshow('image',img)
cv2.imshow('Y',y)
cv2.imshow('U',u_mapped)
cv2.imshow('V',v_mapped)

cv2.waitKey(0)
cv2.destroyAllWindows()

# YUV to RGB
newImage = []
for i in range(0, len(y)):
    row = []
    for j in range(0, len(y[i])):
        pixel = []
        R = (y[i][j] + (v[i][j] * ((1 - WR) / V_MAX)))
        G = ((y[i][j] / WG) - ((u[i][j]* WB * (1 - WB)) / (U_MAX * WG)) - ((v[i][j] * WR * (1 - WR)) / (V_MAX * WG)))
        B = (y[i][j] + (u[i][j] * ((1 - WB) / U_MAX)))
        pixel += [R]
        pixel += [G]
        pixel += [B]
        row += [pixel]
    newImage += [row]


displayNewImage = np.asarray(newImage)
#print(img[0],displayNewImage[0])

cv2.imshow('after',displayNewImage)
cv2.waitKey(0)
cv2.destroyAllWindows()
