import cv2
import numpy as np


img = cv2.imread("../../../img/sudoku.png")
img2 = img.copy()
imgray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(imgray, 50, 200)

lines = cv2.HoughLinesP(
    edges,
    1,
    np.pi / 180,
    10, None,
    20,
    2
)

for line in lines:
    x1, y1, x2, y2 = line[0]
    cv2.line(
        img,
        (x1, y1),
        (x2, y2),
        (0, 255, 0),
        1
    )

cv2.imshow("Probability Hough Line", img)
cv2.waitKey()
cv2.destroyAllWindows()
