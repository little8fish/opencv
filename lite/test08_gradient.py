import cv2
import numpy as np

gray = cv2.imread('/Users/dengjiacheng/Downloads/logo.png', 0)

laplac = cv2.Laplacian(gray, cv2.CV_64F)
canny = cv2.Canny(gray, 100, 200)

cv2.imshow("laplac", laplac)
cv2.imshow("canny", canny)
cv2.waitKey()

