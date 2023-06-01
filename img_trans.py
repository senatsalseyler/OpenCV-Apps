#shiffting an image means translation in computer vision terminology

import cv2
from cv2 import warpAffine
import numpy as np

img = cv2.imread("C:/Users/MSI/Desktop/cizim/ps/botanik2.png")
num_rows, num_cols = img.shape[:2]

translation_matrix = np.float32([[1, 0, 70], [0, 1, 110]])
img_translation = cv2.warpAffine(img, translation_matrix, (num_rows, num_cols))

cv2.imshow("Translation", img_translation)
cv2.waitKey()