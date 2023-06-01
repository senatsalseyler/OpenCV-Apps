import cv2
import numpy as np

img = cv2.imread("C:/Users/MSI/Desktop/cizim/ps/botanik2.png", cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape[:2]

sobel_horizontal = cv2.Sobel(img, cv2.CV_64F, 1, 0, ksize = 5)
sobel_vertical = cv2.Sobel(img, cv2.CV_64F, 0, 1, ksize = 5)

cv2.imshow("Original", img)
cv2.imshow("Horizontal",sobel_horizontal)
cv2.imshow("Vertical", sobel_vertical)

cv2.waitKey()
