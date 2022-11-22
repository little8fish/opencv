import cv2
import numpy as np
# /Users/dengjiacheng/Downloads/logo.png
img = cv2.imread('9699603efae9a04c072733b9576467cc.jpeg')

cv2.imshow('b', img[:,:,0])
cv2.imshow('g', img[:,:,1])
cv2.imshow('r', img[:,:,2])

print(img[:, :, 0] == img[:, :, 1])

cv2.imshow('b*3', np.stack((img[:,:,0],)*3, axis=-1))
# print(np.concatenate(img[:,:,0]).shape)


gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cv2.imshow('gray', gray)
cv2.imshow('src', img)

cv2.waitKey()