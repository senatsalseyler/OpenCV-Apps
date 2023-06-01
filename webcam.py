import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    raise IOError("Cannot open webcam")

while True:
    ret, frame = cap.read()
    frame = cv2.resize(frame, None, fx = 0.75, fy = 0.75, interpolation = cv2.INTER_AREA)
    cv2.imshow("Input", frame)

    c = cv2.waitKey(1)    #esc tusunun ASCII degeri 27
    if c == 27:
        break

cap.release()
cv2.destroyAllWindows()
