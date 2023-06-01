import cv2

img = cv2.imread("C:/Users/MSI/Desktop/cizim/ps/botanik2.png")

img_scaled = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation= cv2.INTER_LINEAR)
cv2.imshow("Scaling - Linear Interpolation", img_scaled)

img_scaled2 = cv2.resize(img, None, fx=1.2, fy=1.2, interpolation=cv2.INTER_CUBIC)
cv2.imshow("Scaling - Cubic Interpolation", img_scaled2)

img_scaled3= cv2.resize(img, (140,200), interpolation= cv2.INTER_AREA)
cv2.imshow("Scaling - Skewed Size", img_scaled3)

cv2.waitKey()