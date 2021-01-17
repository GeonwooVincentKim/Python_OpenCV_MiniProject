import cv2


img = cv2.imread("../../../img/pistol.jpg")
gray = cv2.cvtColor(
    img,
    cv2.COLOR_BGR2GRAY
)

gray = cv2.resize(
    gray,
    (16, 16)
)
avg = gray.mean()

bin = 1 * (gray > avg)
print(bin)

d_hash = []
for row in bin.tolist():
    s = ''.join([str(i) for i in row])
    d_hash.append(
        "%02x" %
        (int(s, 2))
    )

d_hash = ''.join(d_hash)
print(d_hash)

cv2.imshow("pistol", img)
cv2.waitKey(0)
