import cv2
import numpy as np

img = cv2.imread("C:/Users/MSI/Desktop/cizim/ps/botanik2.png")
rows, cols = img.shape[:2]

kernel_identity = np.array([[0,0,0], [0,1,0], [0,0,0]])
kernel_3x3 = np.ones((3,3), np.float32)/9.0
kernel_5x5 = np.ones((5,5), np.float32)/25.0

cv2.imshow("Original Image", img)

output = cv2.filter2D(img, -1, kernel_identity)
cv2.imshow("Identity Filter", output)

output = cv2.filter2D(img, -1, kernel_3x3)
cv2.imshow("3x3 Filter", output)

output = cv2.filter2D(img, -1, kernel_5x5)
cv2.imshow("5x5 Filter", output)

cv2.waitKey()
