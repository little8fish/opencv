import cv2 as cv
import matplotlib.pyplot as plt

img = cv.imread('/Users/dengjiacheng/PycharmProjects/opencv1/normal/source_img/5a2d5db2aa882d1fd93f376401b81b17.jpg')

cv.imshow('cv_show', img)
# plt.imshow(img[:,:,::-1])
# plt.axis('off')
# plt.show()

cv.waitKey()

cv.imwrite('save1.png', img)