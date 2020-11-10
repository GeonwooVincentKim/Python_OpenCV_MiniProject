import cv2
import numpy as np


img = cv2.imread('../../../img/gaussian_noise.jpg')

blur1 = cv2.GaussianBlur(img, (5, 5), 0)
blur2 = cv2.bilateralFilter(img, 5, 75, 75)

merged = np.hstack((img, blur2, blur2))

cv2.imshow('bilateral', merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
