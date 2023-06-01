import cv2

img = cv2.imread("C:/Users/MSI/Desktop/cizim/ps/botanik.png")

imgGray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
imgBlur = cv2.GaussianBlur(imgGray, (17,17),0)

cv2.imshow("botanik",img)
cv2.imshow("botanik blur", imgGray)
cv2.imshow("botanik grayscale", imgBlur)
cv2.waitKey(0)