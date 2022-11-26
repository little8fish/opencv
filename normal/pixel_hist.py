import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np
from tools import cv_show as cs

# img = cv.imread('/Users/dengjiacheng/PycharmProjects/opencv1/normal/image/cat.jpeg')

# hist = cv.calcHist([img], [0], None, [256], [0, 256])
# plt.figure(figsize=(10, 6), dpi=100)
# plt.plot(hist)
# plt.grid()
# plt.show()


# img = cv.imread('/Users/dengjiacheng/PycharmProjects/opencv1/normal/image/cat.jpeg')
# mask = np.zeros(img.shape[:2], dtype=np.uint8)
# mask[400:650, 200:500] = 1
# masked_img = cv.bitwise_and(img, img, mask=mask)
# mask_hist = cv.calcHist([img], [0], mask, [256], [0, 256])
# cs(img, mask, masked_img)
# plt.figure(figsize=(10, 6), dpi=100)
# plt.plot(mask_hist)
# plt.grid()
# plt.show()


# img = cv.imread('/Users/dengjiacheng/PycharmProjects/opencv1/normal/image/cat.jpeg', 0)
# dst = cv.equalizeHist(img)
# cs(img, dst)


img = cv.imread('/Users/dengjiacheng/PycharmProjects/opencv1/normal/image/cat.jpeg', 0)
clahe = cv.createCLAHE(2)
cl1 = clahe.apply(img)
cs(img, cl1)