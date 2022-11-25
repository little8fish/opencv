import cv2

gray = cv2.imread('/Users/dengjiacheng/Downloads/threshold.jpg')
ret, binary = cv2.threshold(gray, 80, 0, cv2.THRESH_BINARY_INV)
binary_adaptive = cv2.adaptiveThreshold(
    gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 115, 1)


cv2.imshow('gray', gray)
cv2.imshow('binary', binary)
cv2.imshow('binary_adaptive', binary_adaptive)

cv2.waitKey()