import cv2
import numpy as np

img = cv2.imread("opencv/birds view/s_coins.png")

cv2.circle(img, (500, 0), 5, (0, 0, 255), -1)
cv2.circle(img, (700, 0), 5, (0, 0, 255), -1)
cv2.circle(img, (0, 720), 5, (0, 0, 255), -1)
cv2.circle(img, (1280, 720), 5, (0, 0, 255), -1)

pts1 = np.float32([[470, 206], [1479, 198], [32, 1122], [1980, 1125]])
pts2 = np.float32([[0, 0], [500, 0], [0, 600], [500, 600]])
matrix = cv2.getPerspectiveTransform(pts1, pts2)

result = cv2.warpPerspective(img, matrix, (500, 600))

cv2.imshow("Img", img)
cv2.imshow("Perspective transformation", result)
cv2.imwrite("perspective_transformed.jpg", result)

cv2.waitKey(0)
cv2.destroyAllWindows()