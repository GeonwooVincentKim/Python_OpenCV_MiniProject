import cv2
from matplotlib import pyplot as plt

img = cv2.imread('../../../../img/People.jpg')

plt.imshow(img[:, :, ::-1])
plt.xticks([])
plt.yticks([])
plt.show()
