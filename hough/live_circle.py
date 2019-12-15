import cv2
import numpy as np
import sys

cap = cv2.VideoCapture('opencv/optical_flow/slow_circles.mp4')

while(True):

    ret, frame = cap.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray,5)
    cimg = frame.copy()
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 10, np.array([]), 200, 100, 10, 50000)
    #circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 150, np.array([]),param1=100, param2=5, minRadius=10, maxRadius=80)
    if circles == 1:
        print('Circle true')
    else:
        print('No circle')
    cv2.imshow('video',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()