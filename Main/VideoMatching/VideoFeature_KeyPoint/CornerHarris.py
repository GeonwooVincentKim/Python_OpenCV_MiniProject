import cv2
import numpy as np


img = cv2.imread("../../../img/house.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

corner = cv2.cornerHarris(gray, 2, 3, 0.04)
coord = np.where(corner > 0.1 * corner.max())
coord = np.stack((coord[1], coord[0]), axis=1)

for x, y in coord:
    cv2.circle(
        img,
        (x, y),
        5,
        (0, 0, 255),
        1,
        cv2.LINE_AA
    )
