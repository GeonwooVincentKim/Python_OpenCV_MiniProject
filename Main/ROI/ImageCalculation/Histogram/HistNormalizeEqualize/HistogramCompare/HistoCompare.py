import cv2, numpy as np
import matplotlib.pylab as plt


img1 = cv2.imread('../../../../../../img/taekwon_v.jpg')
img2 = cv2.imread('../../../../../../img/taekwonv1.jpg')
img3 = cv2.imread('../../../../../../img/taekwonv2.jpg')
img4 = cv2.imread('../../../../../../img/taekwonv3.jpg')

cv2.imshow('query', img1)
imgs = [img1, img2, img3, img4]
hists = []

for i, img in enumerate(imgs):
    plt.subplot(1, len(imgs), i + 1)
    plt.title('img%d' % (i + 1))
    plt.axis('off')
    plt.imshow(img[:, :, ::-1])

    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
    hist = cv2.calcHist([hsv], [0, 1], None, [180, 256], [0, 180, 0, 256])
    cv2.normalize(hist, hist, 0, 1, cv2.NORM_MINMAX)
    hists.append(hist)

