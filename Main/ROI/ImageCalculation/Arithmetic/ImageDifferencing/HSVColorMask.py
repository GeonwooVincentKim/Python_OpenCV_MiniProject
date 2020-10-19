import cv2
import numpy as np
import matplotlib.pylab as plt


img = cv2.imread('../../../../../img/cube.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)


blue1 = np.array([90, 50, 50])
blue2 = np.array([120, 255, 255])

green1 = np.array([45, 50, 50])
green2 = np.array([75, 255, 255])

red1 = np.array([0, 50, 50])
red2 = np.array([15, 255, 255])
red3 = np.array([165, 50, 50])
red4 = np.array([180, 255, 255])

yellow1 = np.array([20, 50, 50])
yellow2 = np.array([35, 255, 255])

mask_blue = cv2.inRange(hsv, blue1, blue2)
mask_green = cv2.inRange(hsv, green1, green2)
mask_red = cv2.inRange(hsv, red1, red2)
mask_red2 = cv2.inRange(hsv, red3, red4)
mask_yellow = cv2.inRange(hsv, yellow1, yellow2)

res_blue = cv2.bitwise_and(img, img, mask=mask_blue)
res_green = cv2.bitwise_and(img, img, mask=mask_green)
res_red1 = cv2.bitwise_and(img, img, mask=mask_red)
res_red2 = cv2.bitwise_and(img, img, mask=mask_red2)
res_red = cv2.bitwise_and(img, img, mask=mask_red2)
res_yellow = cv2.bitwise_and(img, img, mask=mask_yellow)

imgs = {'original': img, 'blue': res_blue, 'green': res_green,
        'red': res_red, 'yellow': res_yellow}

for i, (k, v) in enumerate(imgs.items()):
    plt.subplot(2, 3, i+1)
    plt.title(k)
    plt.imshow(v[:, :, ::-1])
    plt.xticks([])
    plt.yticks([])

plt.show()
