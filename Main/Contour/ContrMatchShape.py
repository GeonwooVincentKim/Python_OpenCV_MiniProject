import cv2
import numpy as np


target = cv2.imread("../../img/4star.jpg")
shapes = cv2.imread("../../img/shapestomatch.jpg")

targetGray = cv2.cvtColor(target, cv2.COLOR_BGR2GRAY)
shapesGray = cv2.cvtColor(shapes, cv2.COLOR_BGR2GRAY)

ret, targetTh = cv2.threshold(targetGray, 127, 255, cv2.THRESH_BINARY_INV)
ret, shapesTh = cv2.threshold(shapesGray, 127, 255, cv2.THRESH_BINARY_INV)

_, cntrs_target, _ = cv2.findContours(
    targetTh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)

_, cntrs_shapes, _ = cv2.findContours(
    shapesTh,
    cv2.RETR_EXTERNAL,
    cv2.CHAIN_APPROX_SIMPLE
)
