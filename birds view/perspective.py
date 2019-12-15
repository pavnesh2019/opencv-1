import cv2 as cv
import numpy as np

img1 = cv.imread("opencv/birds view/try.jpeg", cv.IMREAD_COLOR)
cv.imshow('dd',img1)
image = np.zeros((700, 700, 3), np.uint8)
src = np.array([[0,200],[480,200],[480,360],[0,360]],np.float32)
dst = np.array([[0,0],[480,0],[300,360],[180,360]],np.float32)

M = cv.getPerspectiveTransform(src, dst)
warp = cv.warpPerspective(img1.copy(), M, (480, 360))
cv.imshow('transform', warp)
cv.waitKey(0)
cv.destroyAllWindows()