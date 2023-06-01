import cv2
import numpy as np

img = cv2.imread("C:/Users/MSI/Desktop/cizim/ps/botanik2.png", 0)

histeq = cv2.equalizeHist(img)

img_scaled1 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation= cv2.INTER_LINEAR)
img_scaled2 = cv2.resize(histeq, None, fx=0.5, fy=0.5, interpolation= cv2.INTER_LINEAR)

cv2.imshow("Input",img_scaled1)
cv2.imshow("Histogram Equalized", img_scaled2)
cv2.waitKey()
