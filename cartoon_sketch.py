import cv2
from cv2 import cvtColor
import numpy as np

#median blur ---- bu fonksiyon bulanıklaştırma işleminden ziyade
#yumuşatma işlemi yapıyor

def cartoonize_image(img, ds_factor = 4, sketch_mode = False):
    img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    img_gray = cv2.medianBlur(img_gray, 7)

    edges = cv2.Laplacian(img_gray, cv2.CV_8U, ksize = 5)
#    edges = cv2.Canny(img_gray, 50, 240)
    ret, mask = cv2.threshold(edges, 100, 255, cv2.THRESH_BINARY_INV)

    if sketch_mode:
        return cv2.cvtColor(mask, cv2.COLOR_GRAY2BGR)
    
#resmin daha hızlı işlem görebilmesi için boyutu küçültülüyor

    img_small = cv2.resize(img, None, fx = 1.0/ds_factor, fy = 1.0/ds_factor, interpolation = cv2.INTER_AREA)
    num_repetitions = 10
    sigma_color = 5 
    sigma_space = 7
    size = 5

    for i in range(num_repetitions):
        img_small = cv2.bilateralFilter(img_small, size, sigma_color, sigma_space)
    
    img_output = cv2.resize(img_small, None, fx = ds_factor, fy = ds_factor, interpolation = cv2.INTER_AREA)

    dst = np.zeros(img_gray.shape)

    dst = cv2.bitwise_and(img_output, img_output, mask=mask)
    return dst

if __name__ == "__main__":
    cap = cv2.VideoCapture(0)

    if not cap.isOpened():
        raise IOError("Cannot open webcam")

    cur_char = -1
    prev_char = -1

    while True:
        ret, frame = cap.read()
        frame = cv2.resize(frame, None, fx = 1.25, fy= 1.25, interpolation = cv2.INTER_AREA)

        c = cv2.waitKey(1)
        if c == 27:
            break

        if c > -1 and c != prev_char:
            cur_char = c
        prev_char = c

        if cur_char == ord('s'):
            cv2.imshow("Cartoonize", cartoonize_image(frame, sketch_mode = True))
        elif cur_char == ord('c'):
            cv2.imshow("Cartoonize", cartoonize_image(frame, sketch_mode = False))
        else:
            cv2.imshow("Cartoonize", frame)

    cap.release()
    cv2.destroyAllWindows()