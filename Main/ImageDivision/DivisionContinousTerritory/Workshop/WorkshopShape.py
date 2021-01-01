import cv2
import numpy as np


img = cv2.imread("../../../../img/5shapes.jpg")
img2 = img.copy()
im_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
ret, th = cv2.threshold(
    im_gray,
    127, 255,
    cv2.THRESH_BINARY_INV
)

_, contours, _ = cv2.findContours(
    th,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

for contour in contours:
    approx = cv2.approxPolyDP(
        contour,
        0.01 * cv2.arcLength(
            contour,
            True
        ),
        True
    )
    vertices = len(approx)
    print("Vertices: ", vertices)

    mmt = cv2.moments(contour)
    cx, cy = int(
        mmt['m10'] / mmt['m00']
    ), int(mmt['m01'] / mmt['m00'])

    name = 'Unknown'
