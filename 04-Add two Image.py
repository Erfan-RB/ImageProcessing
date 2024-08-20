#Add two Image
import numpy as np 
import cv2 as cv

img1 = cv.imread('')
img2 = cv.imread('')
#Add
added = img1 + img2
added = cv.add(img1,img2)
added = cv.addWeighted(img1, 0.8, img2, 0.2, 0)

img2gray = cv.cvtColor(img2,cv.COLOR_BGR2GRAY)
ret, mask = cv.threshold(img2gray, 100,255,cv.THRESH_BINARY)
mask_inv = cv.bitwise_not(mask)  
img1_m = cv.bitwise_and(img1,img1, mask=mask)
cv.imshow('Img1', img1)
cv.imshow('Img2', img2)
cv.imshow('Mask', mask)
cv.imshow('Img1', mask_inv)

cv.imshow('Add', added)
cv.waitKey(0)
cv.destroyAllWindows
