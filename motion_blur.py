import cv2
import numpy as np

img = cv2.imread("C:/Users/MSI/Desktop/cizim/ps/botanik2.png")
cv2.imshow("Original", img)

size = 15

kernel_motion_blur = np.zeros((size,size))
kernel_motion_blur[int((size-1)/2), :] = np.ones(size)
kernel_motion_blur = kernel_motion_blur / size

output = cv2.filter2D(img, -1, kernel_motion_blur)
cv2.imshow("Motion Blur", output)
cv2.waitKey()