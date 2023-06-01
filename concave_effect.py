import cv2
import numpy as np
import math

img = cv2.imread("C:/Users/MSI/Desktop/cizim/ps/botanik2.png", cv2.IMREAD_GRAYSCALE)
rows, cols = img.shape[:2]

img_output = np.zeros(img.shape, dtype = img.dtype) 

for i in range(rows):
    for j in range(cols):
        offset_x = int(128.0 * math.sin(2 * 3.14 * i /(2*cols)))
        offset_y = 0

        if j+offset_x < cols:
            img_output[i,j] = img[i, (j+offset_x)%cols]
        else:
            img_output[i,j] = 0

cv2.imshow("Input", img)
cv2.imshow("Concave", img_output)

cv2.waitKey()