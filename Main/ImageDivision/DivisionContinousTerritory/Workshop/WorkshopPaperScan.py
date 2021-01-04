import cv2
import numpy as np


win_name = "scan"
img = cv2.imread("../../../../img/paper.jpg")
cv2.imshow("original", img)
cv2.waitKey(0)
draw = img.copy()

gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)
edged = cv2.Canny(gray, 75, 200)
cv2.imshow(win_name, edged)
cv2.waitKey(0)

(_, cnts, _) = cv2.findContours(
    edged.copy(),
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
cv2.drawContours(
    draw,
    cnts,
    -1,
    (0, 255, 0)
)
cv2.imshow(win_name, draw)
cv2.waitKey(0)

cnts = sorted(
    cnts,
    key=cv2.contourArea,
    reverse=True
)[:5]
for c in cnts:
    peri = cv2.arcLength(c, True)
    vertices = cv2.approxPolyDP(
        c,
        0.02 * peri,
        True
    )
    if len(vertices) == 4:
        break

pts = vertices.reshape(4, 2)
for x, y in pts:
    cv2.circle(
        draw,
        (x, y),
        10,
        (0, 255, 0),
        -1
    )

cv2.imshow(win_name, draw)
cv2.waitKey(0)
merged = np.hstack((img, draw))
