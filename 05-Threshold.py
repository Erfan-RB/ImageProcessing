#Threshold
import numpy as np 
import cv2 as cv

img = cv.imread('')
imgray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
ret, threshold = cv.threshold(img, 15, 255, cv.THRESH_BINARY)
#OTSU THRESHOLDING
ret2, thresh2 = cv.threshold(imgray, 0, 255,cv.THRESH_BINARY+cv.THRESH_OTSU )

thresh3 = cv.adaptiveThreshold(imgray, 255, cv.ADSPTIVE_THRESH_GAUSSIAN_C, cv.THRESH_BINARY, 115,1)
cv.imshow('Orginal',img)
cv.imshow('Threshold',threshold)
cv.IMSHOW('OTSU', thresh2)
cv.imshow('adaptive',thresh3)
cv.waitKey(0)
cv.destoryAllWindows()
