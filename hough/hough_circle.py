import cv2
import numpy as np




img = cv2.imread('opencv/hough/circles.jpg', cv2.IMREAD_COLOR)
# Convert to gray-scale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
img_blur = cv2.medianBlur(gray, 5)
circles = cv2.HoughCircles(img_blur, cv2.HOUGH_GRADIENT, 1, 150, param1=100, param2=5, minRadius=10, maxRadius=80)
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)


cv2.imshow('circles',img)
cv2.waitKey(0)



cv2.destroyAllWindows()
cap.release()
out.release()