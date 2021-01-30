import cv2
import numpy as np
import glob


img = cv2.imread("../../../img/pistol.jpg")
cv2.imshow("query", img)

search_dir = "../../../img/101_ObjectCategories"


def img2hash(img):
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    gray = cv2.resize(gray, (16, 16))
    avg = gray.mean()
    bi = 1 * (gray > avg)
    return bi


def hamming_distance(a, b):
    a = a.reshape(1, -1)
    b = b.reshape(1, -1)
    distance = (a != b).sum()
    return distance


query_hash = img2hash(img)
