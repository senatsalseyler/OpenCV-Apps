import cv2
import numpy as np

img = cv2.imread("C:/Users/MSI/Desktop/cizim/ps/botanik2.png", cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape[:2]

lap_img = cv2.Laplacian(img, cv2.CV_64F)

cv2.imshow("Original Image", img)
cv2.imshow("Laplacian", lap_img)

cv2.waitKey()