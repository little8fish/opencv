import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from tools import cv_show as cs


# img = cv.imread('/Users/dengjiacheng/PycharmProjects/opencv1/normal/image/wulin.jpeg')
# # cs(img)
# template = cv.imread('/Users/dengjiacheng/PycharmProjects/opencv1/normal/image/wulin2.jpeg')

# res = cv.matchTemplate(img, template, cv.TM_CCORR)
# min_val, max_val, min_loc, max_loc = cv.minMaxLoc(res)
# cv.rectangle(img, max_loc, (max_loc[0]+template.shape[1], max_loc[1]+template.shape[0]), (0, 0, 255), 2)
# cs(img)

# source = cv.imread('/Users/dengjiacheng/PycharmProjects/opencv1/normal/image/rili.jpg')
# img = cv.imread('/Users/dengjiacheng/PycharmProjects/opencv1/normal/image/rili.jpg', 0)
# canny = cv.Canny(img, 50, 150)
# # print(canny)
# # cs(canny)
# lines = cv.HoughLines(canny, 0.8, np.pi/180, 150)
# for line in lines:
#     rho, theta = line[0]
#     a = np.cos(theta)
#     b = np.sin(theta)
#     x0 = a*rho
#     y0 = b*rho
#     x1 = int(x0 + 1000 * (-b))
#     y1 = int(y0 + 1000 * (a))
#     x2 = int(x0 - 1000 * (-b))
#     y2 = int(y0 - 1000 * (a))
#     cv.line(source, (x1, y1), (x2, y2), (0, 255, 0), 1)
# cs(source)


img = cv.imread('/Users/dengjiacheng/PycharmProjects/opencv1/normal/image/star.jpeg')
# cs(img)
gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
median = cv.medianBlur(gray, 9)
# cs(median, img)
circles = cv.HoughCircles(median, cv.HOUGH_GRADIENT, 1, 200, param1=100, param2=30, minRadius=0,maxRadius=100)
for i in circles[0, :]:
    cv.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
    # 绘制圆心
    cv.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)
cs(img)