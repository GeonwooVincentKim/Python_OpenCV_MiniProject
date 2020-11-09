import cv2
import numpy as np


img = cv2.imread("../../../img/salt_pepper_noise.jpg")

blur = cv2.medianBlur(img, 5)

merged = np.hstack((img, blur))
cv2.imshow("media", merged)
cv2.waitKey(0)
cv2.destroyAllWindows()
