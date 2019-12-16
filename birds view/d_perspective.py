import cv2
import numpy as np

cap = cv2.VideoCapture("opencv/birds view/pers_slow_coins.mp4")

while True:
    _, frame = cap.read()
    print(frame.shape)
    cv2.circle(frame, (600,0), 5, (0, 0, 255), -1)
    cv2.circle(frame, (700,0), 5, (0, 0, 255), -1)
    cv2.circle(frame, (200, 720), 5, (0, 0, 255), -1)
    cv2.circle(frame, (900, 720), 5, (0, 0, 255), -1)
    pts1 = np.float32([[600, 0], [700, 0], [200, 720], [900, 720]])
    pts2 = np.float32([[0, 0], [1280, 0], [0, 720], [1280, 720]])
    matrix = cv2.getPerspectiveTransform(pts1, pts2)
    result = cv2.warpPerspective(frame, matrix, (1280, 720))
    cv2.imshow("Frame", frame)
    cv2.imshow("Perspective transformation", result)
    key = cv2.waitKey(1)
    if key == 27:
        break
cap.release()
cv2.destroyAllWindows()