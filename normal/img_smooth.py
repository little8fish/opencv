import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from tools import cv_show as cvs


img = cv.imread('/Users/dengjiacheng/PycharmProjects/opencv1/normal/image/dogsp.jpeg')
# cvs(img)
# blur = cv.blur(img, (10, 10)) # 均值滤波
# blur = cv.GaussianBlur(img, (5, 5), 1) # 高斯滤波
blur = cv.medianBlur(img, 5) # 中值滤波
cvs(img, blur)