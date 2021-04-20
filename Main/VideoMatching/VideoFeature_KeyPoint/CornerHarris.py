import cv2
import numpy as np


img = cv2.imread("../../../img/house.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
