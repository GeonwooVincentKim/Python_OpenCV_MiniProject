import cv2
import numpy as np


img = cv2.imread("../../../img/moon_gray.jpg")

k = cv2.getStructuringElement(cv2.MORPH_RECT, (9, 9))

top_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, k)
black_hat = cv2.morphologyEx(img, cv2.MORPH_TOPHAT, k)

merged = np.hstack((img, top_hat, black_hat))
cv2.imshow("Top-Hat Black-Hat", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
