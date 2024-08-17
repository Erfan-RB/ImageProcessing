#Display(cv/matplotlib)
#Liberay
import numpy as np 
import cv2 as cv
from matplotlib import pyplot as plt
#Read
img = cv.imread('R&M.jpg', cv.IMREAD_GRAYSCALE)
imgcolor = cv.imread('R&M.jpg', cv.IMREAD_COLOR)

#Color
#cv.IMREAD_GRAYSCALE   0
#cv.IMREAD_COLOR    1
#cv.IMREAD_UNCHANGED   -1

##CV
#Display
cv.imshow('IMAGE', img)
cv.imshow('IMAGE', imgcolor)

cv.waitKey(0)
cv.destroyAllWindows()

#Color
#RGB(34, 45, 56)
#BGR
#RGBA, BGRA

#Save
cv.imwrite('R&M2.jpg', img)


##Matplotlib
plt.imshow(img, cmap='gray', interpolation='bicubic' )
plt.show()

