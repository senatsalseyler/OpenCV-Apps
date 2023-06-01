import cv2
import numpy as np

img = cv2.imread("C:/Users/MSI/Desktop/cizim/ps/botanik2.png")

img_yuv = cv2.cvtColor(img, cv2.COLOR_BGR2YUV)

img_yuv[:,:,0] = cv2.equalizeHist(img_yuv[:,:,0])
img_output = cv2.cvtColor(img_yuv, cv2.COLOR_YUV2BGR)

img_scaled1 = cv2.resize(img, None, fx=0.5, fy=0.5, interpolation= cv2.INTER_LINEAR)
img_scaled2 = cv2.resize(img_output, None, fx=0.5, fy=0.5, interpolation= cv2.INTER_LINEAR)

cv2.imshow("Input", img_scaled1)
cv2.imshow("Histogram Equalized", img_scaled2)
cv2.waitKey()
