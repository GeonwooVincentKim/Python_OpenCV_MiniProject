import cv2
import numpy as np


img = cv2.imread("../../../../img/coins_connected.jpg")
rows, cols = img.shape[: 2]
cv2.imshow("original", img)

mean = cv2.pyrMeanShiftFiltering(img, 20, 20)
cv2.imshow("mean", mean)
gray = cv2.cvtColor(mean, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)

_, thresh = cv2.threshold(
    gray,
    0, 255,
    cv2.THRESH_BINARY | cv2.THRESH_OTSU
)
cv2.imshow("thresh", thresh)
dst = cv2.distanceTransform(
    thresh,
    cv2.DIST_L2,
    3
)
dst = (
        dst /
        (dst.max() - dst.min())
        * 255
).astype(np.uint8)
cv2.imshow("dst", dst)

localMx = cv2.dilate(
    dst,
    np.ones(
        (50, 50),
        np.uint8
    )
)
lm = np.zeros((rows, cols), np.uint8)
lm[(localMx == dst) & (dst != 0)] = 255
cv2.imshow("localMx", lm)
