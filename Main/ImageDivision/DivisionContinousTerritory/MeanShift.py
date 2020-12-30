import cv2
import numpy as np


img = cv2.imread("../../../img/taekwonv1.jpg")


def onChange(x):
    sp = cv2.getTrackbarPos('sp', 'img')
    sr = cv2.getTrackbarPos('sr', 'img')
    lv = cv2.getTrackbarPos('lv', 'img')
