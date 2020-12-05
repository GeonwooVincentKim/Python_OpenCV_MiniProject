import cv2
import numpy as np


img = cv2.imread("../../img/lightning.png")
img_gray = cv2.cvtColor(
    img, cv2.COLOR_BGR2GRAY
)

ret, th = cv2.threshold(
    img_gray,
    127, 255,
    cv2.THRESH_BINARY_INV
)

im, contours, hr = cv2.findContours(
    th, cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

contr = contours[0]

x, y, w, h = cv2.boundingRect(contr)
cv2.rectangle(
    img,
    (x, y),
    (x + w, y + h),
    (0, 0, 0),
    3
)

rect = cv2.minAreaRect(contr)
box = cv2.boxPoints(rect)
box = np.int0(box)
cv2.drawContours(
    img,
    [box],
    -1,
    (0, 255, 0),
    3
)

(x, y), radius = cv2.minEnclosingCircle(contr)
cv2.circle(
    img,
    (int(x), int(y)),
    int(radius),
    (255, 0, 0),
    2
)

ret, tri = cv2.minEnclosingTriangle(contr)
cv2.polylines(
    img,
    [np.int32(tri)],
    True,
    (255, 0, 255), 2
)

ellipse = cv2.fitEllipse(contr)
cv2.ellipse(
    img,
    ellipse,
    (0, 255, 255),
    3
)
