import cv2

cap=cv2.VideoCapture("C:/Users/MSI/Desktop/animasyon/videolar/karkuresi.mp4")

while True:
    success, img=cap.read()
    cv2.imshow("video", img)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

    