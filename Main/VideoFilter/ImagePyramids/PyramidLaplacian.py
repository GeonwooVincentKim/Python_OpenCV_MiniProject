import cv2
import numpy as np


img = cv2.imread("../../../img/taekwonv1.jpg")

smaller = cv2.pyrDown(img)
bigger = cv2.pyrUp(smaller)

laplacian = cv2.subtract(img, bigger)
restored = bigger + laplacian
merged = np.hstack((img, laplacian, bigger, restored))
