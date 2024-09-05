#TextDetection
import numpy as np
import cv2 as cv
from matplotlib import pyplot as plt
import easyocr
car_img = cv.imread(".jpg")
car_plate_img = cv.imread(".jpg", 0)
plt.imshow(cv.cvtColor(car_plate_img, cv.COLOR_BGR2RGB))
reader = easyocr.Reader(['fa'])
plate_info = reader.readtext(car_plate_img)
print(plate_info)
plate_text = plate_info[0][-2]
plate_text
