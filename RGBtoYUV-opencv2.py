import numpy as np
import cv2

img = cv2.imread('img/flower1.jpg')
	
def colormap_u():
    return np.array([[[i,255-i,0] for i in range(256)]],dtype=np.uint8)

def colormap_v():
    return np.array([[[0,255-i,i] for i in range(256)]],dtype=np.uint8)

img_yuv = cv2.cvtColor(img, cv2.COLOR_RGB2YUV)
y, u, v = cv2.split(img_yuv)
lut_u, lut_v = colormap_u(), colormap_v()

# Convert back to RGB to apply the Lookup table
y = cv2.cvtColor(y, cv2.COLOR_GRAY2RGB)
u = cv2.cvtColor(u, cv2.COLOR_GRAY2RGB)
v = cv2.cvtColor(v, cv2.COLOR_GRAY2RGB)

u_mapped = cv2.LUT(u, lut_u)
v_mapped = cv2.LUT(v, lut_v)

cv2.imshow('image',img)
cv2.imshow('Y',y)
cv2.imshow('U',u_mapped)
cv2.imshow('V',v_mapped)
cv2.waitKey(0)
cv2.destroyAllWindows()

RGB=cv2.cvtColor(img_yuv,cv2.COLOR_YUV2RGB)
cv2.imshow('RGB',RGB)
cv2.waitKey(0)
cv2.destroyAllWindows()
