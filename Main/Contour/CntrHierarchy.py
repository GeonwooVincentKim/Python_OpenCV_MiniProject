import cv2
import numpy as np


img = cv2.imread("../../img/shapes_donut.png")
img2 = img.copy()

img_gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)

ret, imth_res = cv2.threshold(
    img_gray,
    127, 255,
    cv2.THRESH_BINARY_INV
)

im2, contour, hierarchy = cv2.findContours(
    imth_res,
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_SIMPLE
)

print(len(contour), hierarchy)

im2, contour2, hierarchy = cv2.findContours(
    imth_res,
    cv2.RETR_TREE,
    cv2.CHAIN_APPROX_SIMPLE
)

print(len(contour2), hierarchy)

cv2.drawContours(img, contour, -1, (0, 255, 0), 3)

for idx, count in enumerate(contour2):
    color = [int(i) for i in np.random.randint(0, 255, 3)]
    cv2.drawContours(img2, contour2, idx, color, 3)
    cv2.putText(
        img2,
        str(idx),
        tuple(count[0][0]),
        cv2.FONT_HERSHEY_PLAIN,
        1, (0, 0, 255)
    )

cv2.imshow('RETR_EXTERNAL', img)
cv2.imshow('RETR_TREE', img2)
cv2.waitKey(0)
cv2.destroyAllWindows()
