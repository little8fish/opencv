import cv2
import numpy as np

template = cv2.imread('/Users/dengjiacheng/Downloads/1284.jpeg', 0)
image = cv2.imread('/Users/dengjiacheng/Downloads/1284 (1).jpeg')
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# 获取可能像素点位置的可能性
match = cv2.matchTemplate(gray_image, template, cv2.TM_CCOEFF_NORMED)
locations = np.where(match >= 0.9)
w, h = template.shape
temp1 = locations[::-1]
for p in zip(*locations[::-1]):
    x1, y1 = p[0], p[1]
    x2, y2 = x1+w, y1+h
    cv2.rectangle(image, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('result', image)
cv2.waitKey()

