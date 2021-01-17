import cv2


img = cv2.imread("../../../img/pistol.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

gray = cv2.resize(gray, (16, 16))
avg = gray.mean()

bin = 1 * (gray > avg)
print(bin)
