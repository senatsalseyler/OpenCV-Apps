import cv2
import numpy as np

img = cv2.imread("C:/Users/MSI/Desktop/cizim/ps/botanik2.png")
rows, cols = img.shape[:2]

kernel_x = cv2.getGaussianKernel(cols,150)
kernel_y = cv2.getGaussianKernel(rows,150)
kernel = kernel_y * kernel_x.T
mask = 255 * kernel / np.linalg.norm(kernel)
output = np.copy(img)

for i in range(3):
    output[:,:,i] = output[:,:,i] * mask

cv2.imshow("Original", img)
cv2.imshow("Vignette", output)
cv2.waitKey()