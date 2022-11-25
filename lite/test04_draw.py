import cv2
import numpy as np

img = np.zeros((300, 800, 3), dtype=np.uint8)
cv2.line(img, (0,0), (800, 300), (255, 0, 0), 2)
cv2.rectangle(img, (100, 100), (200, 200), (0, 255, 0), 2)
cv2.circle(img, (200, 200), 100, (0, 0, 255), 4)
cv2.putText(img, "hello world", (700, 250), 0, 1, (255, 255, 255), 4)

cv2.imshow('draw', img)
cv2.waitKey()