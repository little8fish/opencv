import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

def cv_show(*imgs):
    for i, img in enumerate(imgs):
        print(img.shape)
        cv.imshow(str(i), img)
    cv.waitKey()

# 膨胀与腐蚀
# img1 = cv.imread('/Users/dengjiacheng/Downloads/1-51.png')
#
# kernel = np.ones((5, 5), dtype=np.uint8)
#
# erosion = cv.erode(img1, kernel)
# dilate = cv.dilate(img1, kernel)
#
# cv_show(erosion, img1, dilate)
#
# cv.waitKey()


# 开闭运算
# img = cv.imread('/Users/dengjiacheng/Downloads/images.png')
# # img1 = cv.imread('/Users/dengjiacheng/Downloads/1-51.png', 0)
# # cv_show(img)
# kernel = np.ones((10, 10), np.uint8)
#
# cv_open = cv.morphologyEx(img, cv.MORPH_OPEN, kernel)
# cv_close = cv.morphologyEx(img, cv.MORPH_CLOSE, kernel)
#
# cv_show(cv_open, img, cv_close)


# 礼帽和黑帽
img = cv.imread('/Users/dengjiacheng/Downloads/images.png')

kernel = np.ones((10, 10), np.uint8)

cv_tophat = cv.morphologyEx(img, cv.MORPH_TOPHAT, kernel)
cv_blackhat = cv.morphologyEx(img, cv.MORPH_BLACKHAT, kernel)

cv_show(cv_tophat, img, cv_blackhat)

