import cv2
import numpy as np
from matplotlib import pyplot as plt


file_name = '../../../../img/fish.jpg'
img = cv2.imread(file_name)
rows, cols = img.shape[:2]

pts1 = np.float32([[100, 50], [200, 50], [100, 200]])
pts2 = np.float32([[80, 70], [210, 60], [250, 120]])

