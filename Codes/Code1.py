# From the attached images perform the most suitable 
# Threshold Operation to segmentate a new image showing up 
# the desire result.

#Libraries
import cv2
import numpy as np 

#Select the image
image1 = cv2.imread('Hueso.jpg')
image2 = cv2.imread('Palo.jpg')

#Image converted to grayscale
img1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
img2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

#Implementation of thresholds
ret, th1 = cv2.threshold(img1, 121, 255, cv2.THRESH_BINARY)
ret, th2 = cv2.threshold(img2, 20, 255, cv2.THRESH_BINARY) 

cv2.imshow('Hueso_Binary', th1)
cv2.imwrite('Hueso_Result.png',th1)

cv2.imshow('Palo_Binary', th2)
cv2.imwrite('Palo_Result.png',th2)

cv2.waitKey(0)
cv2.destroyAllWindows()