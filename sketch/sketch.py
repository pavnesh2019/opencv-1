import numpy as np 
import cv2 as cv
import imageio
import scipy.ndimage
from matplotlib import pyplot as ply

img="sketch//sketch.jpeg"
def grayscale(rgb):
    return np.dot(rgb[...,:3],[0.299,0.587,0.114])

def dodge(front,back):
    result=front*255/(255-back)
    result[result>255]=255
    result[back==255]=255
    return result.astype('uint8')


     


s=imageio.imread(img)
g=grayscale(s)
i=255-g

b=scipy.ndimage.filters.gaussian_filter(i,sigma=10)
r=dodge(b,g)
cv.imwrite('sketch//sketchf.jpg',r)
img1=cv.imread("sketch//sketchf.jpg")
cv.imshow("Sketch",img1)
cv.waitKey(0)
key=cv.waitKey(1) & 0xFF
if key==ord("q"):
    cv.destroyAllWindows()
