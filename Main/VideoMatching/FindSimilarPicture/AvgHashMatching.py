import cv2
import numpy as np
import glob


img = cv2.imread("../../../img/pistol.jpg")
cv2.imshow("query", img)

search_dir = "../../../img/101_ObjectCategories"
