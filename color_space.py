import cv2

img = cv2.imread("C:/Users/MSI/Desktop/cizim/ps/botanik2.png")

hsv_img=cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

cv2.imshow("hsv color", hsv_img)

cv2.imshow("h channel", hsv_img[:,:,0])
cv2.imshow("s channel", hsv_img[:,:,1])
cv2.imshow("v channel", hsv_img[:,:,2])


cv2.waitKey(0)