import cv2
import numpy as np


cap = cv2.VideoCapture(0)

while cap.isOpened():
    ret, frame = cap.read()
    frame = cv2.resize(frame, None,
                       fx=0.5, fy=0.5,
                       interpolation=cv2.INTER_AREA)

    if cv2.waitKey(1) == 27:
        break

    img_gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    img_gray = cv2.GaussianBlur(img_gray, (9, 9), 0)
    edges = cv2.Laplacian(img_gray, -1, None, 5)
    ret, sketch = cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY_INV)

    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    sketch = cv2.erode(sketch, kernel)
    sketch = cv2.medianBlur(sketch, 5)
    img_sketch = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)

    img_paint = cv2.blur(frame, (10, 10))
    img_paint = cv2.bitwise_and(img_paint, img_paint, mask=sketch)

cap.release()
cv2.destroyAllWindows()
