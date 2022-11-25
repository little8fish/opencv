import cv2

img = cv2.imread('9699603efae9a04c072733b9576467cc.jpeg')

print(img.shape)
img_crop = img[1000:1500, 3000:]

cv2.imshow('crop', img_crop)

cv2.waitKey()