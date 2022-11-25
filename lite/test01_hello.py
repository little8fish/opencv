import cv2

print(cv2.getVersionString())

image = cv2.imread('9699603efae9a04c072733b9576467cc.jpeg')
# print(image)
# print(image.shape)
cv2.imshow('img', image)
cv2.waitKey()