import cv2
import numpy as np
import math

img = cv2.imread("C:/Users/MSI/Desktop/cizim/ps/botanik2.png", cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape[:2]

img_output = np.zeros(img.shape, dtype=img.dtype)

for i in range(rows):
    for j in range(cols):
        offset_x = 0
        offset_y = int(16.0 * math.sin(2 * 3.14 * j / 150))
        if i+offset_y < rows:
            img_output[i,j] = img[(i+offset_y)%rows,j]
        else:
            img_output[i,j]=0

cv2.imshow("Input", img)
cv2.imshow("Horizontal Wave", img_output)
cv2.waitKey()