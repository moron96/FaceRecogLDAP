
import time
import cv2


cv2.namedWindow("preview")
vc = cv2.VideoCapture(1)

while vc.isOpened():
    _, frame = vc.read()
    img = frame

    cv2.imshow("preview", img)

cv2.destroyWindow("preview")