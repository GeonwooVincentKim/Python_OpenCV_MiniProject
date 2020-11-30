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
