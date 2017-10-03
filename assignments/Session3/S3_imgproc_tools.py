import cv2
import numpy as np

img_gray = cv2.imread('./images/cat_small.jpg', 0)
img_bgr = cv2.imread('./images/cat_small.jpg', 1)

cv2.imshow("Gray levels image", img_gray)
cv2.imshow("BGR image", img_bgr)
cv2.waitKey(0)