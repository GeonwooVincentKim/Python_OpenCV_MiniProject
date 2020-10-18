import cv2
import numpy as np

a = np.array([[1, 2]], dtype=np.uint8)
b = np.array([[10, 20]], dtype=np.uint8)
mask = np.array([[1, 0]], dtype=np.uint8)

cv1 = cv2.add(a, b, None, mask)
print(cv1)
cv2 = cv2.add(a, b, b, mask)
print(cv2)
