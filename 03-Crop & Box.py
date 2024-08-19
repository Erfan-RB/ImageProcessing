#Crop & Box
import numpy as np
import cv2 as cv

img = cv.imread('R&M.jpg',cv.IMREAD_COLOR)
imgray=cv.convertColor(img,cv.COLOR_BGR2GRAY)
#Crop
img2 = imgray[100:300,250:500]
#White box   
imgray[100:300,250:500] = 255
#Black box
img[40:150,40:250]=[0,0,0]
cv.imshow('image', img)
cv.imshow('image',img)
cv.waitKey(0)
cv.destroyAllWindows()
