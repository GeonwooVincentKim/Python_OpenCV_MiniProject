import cv2
import numpy as np


file_name = "../../../../img/fish.jpg"
img = cv2.imread(file_name)
rows, cols = img.shape[:2]
