import cv2
import numpy as np
import sys

cap = cv2.VideoCapture('opencv/optical_flow/slow_circles.mp4')

while(True):

    ret, frame = cap.read()


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray = cv2.medianBlur(gray,5)
    cimg = frame.copy()
    #circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 10, np.array([]), 200, 100, 10, 50000)
    circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 150,param1=100, param2=5, minRadius=10, maxRadius=80)
    if circles is not None:
     circles = np.uint16(np.around(circles))
     for i in circles[0, :]:
        
        cv2.circle(gray, (i[0], i[1]), i[2], (0, 255, 0), 2)
        circles = cv2.HoughCircles(gray, cv2.HOUGH_GRADIENT, 1, 150, param1=100, param2=5, minRadius=5000, maxRadius=8000)
        cv2.circle(gray, (i[0], i[1]), 2, (0, 0, 255), 3)


    cv2.imshow('circles',gray)
    cv2.waitKey(0)
   
     #cv2.imshow('video',gray)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break


cap.release()
cv2.destroyAllWindows()