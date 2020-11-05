import cv2 as cv
import numpy as np
from matplotlib import pyplot as plt

img = cv.imread('Text.jpg',0)
img = cv.medianBlur(img,5)

ret,th1 = cv.threshold(img,127,255,cv.THRESH_BINARY)

th2 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_MEAN_C,\
            cv.THRESH_BINARY,11,5)
th3 = cv.adaptiveThreshold(img,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,3)

cv.imshow('Text', th2)
cv.imwrite('Text_Result.png',th2)
cv.imshow('Text2', th3)
cv.imwrite('Text_Result2.png',th3)

cv.waitKey(0)
cv.destroyAllWindows()