import cv2
import numpy as np

img = cv2.imread("C:/Users/MSI/Desktop/cizim/ps/botanik2.png", cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape[:2]

canny = cv2.Canny(img, 50, 240)

cv2.imshow("Original Image", img)
cv2.imshow("Canny", canny)

cv2.waitKey()