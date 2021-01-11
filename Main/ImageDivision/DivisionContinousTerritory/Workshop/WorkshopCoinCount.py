import cv2
import numpy as np


img = cv2.imread("../../../../img/coins_connected.jpg")
rows, cols = img.shape[: 2]
cv2.imshow("original", img)

mean = cv2.pyrMeanShiftFiltering(img, 20, 20)
cv2.imshow("mean", mean)
gray = cv2.cvtColor(mean, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (3, 3), 0)

_, thresh = cv2.threshold(
    gray,
    0, 255,
    cv2.THRESH_BINARY | cv2.THRESH_OTSU
)
cv2.imshow("thresh", thresh)
dst = cv2.distanceTransform(
    thresh,
    cv2.DIST_L2,
    3
)
dst = (
        dst /
        (dst.max() - dst.min())
        * 255
).astype(np.uint8)
cv2.imshow("dst", dst)

localMx = cv2.dilate(
    dst,
    np.ones(
        (50, 50),
        np.uint8
    )
)
lm = np.zeros((rows, cols), np.uint8)
lm[(localMx == dst) & (dst != 0)] = 255
cv2.imshow("localMx", lm)

seeds = np.where(lm == 255)
seed = np.stack(
    (seeds[1], seeds[0]),
    axis=-1
)
fill_mask = np.zeros((
    rows + 2,
    cols + 2
), np.uint8)

for x, y, in seed:
    ret = cv2.floodFill(
        mean,
        fill_mask,
        (x, y),
        (255, 255, 255),
        (10, 10, 10),
        (10, 10, 10)
    )
    cv2.imshow("floodFill", mean)

gray = cv2.cvtColor(mean, cv2.COLOR_BGR2GRAY)
gray = cv2.GaussianBlur(gray, (5, 5), 0)

ret , thresh = cv2.threshold(
    gray,
    0, 255,
    cv2.THRESH_BINARY | cv2.THRESH_OTSU
)
dst = cv2.distanceTransform(
    thresh,
    cv2.DIST_L2,
    5
)
dst = (
    (
        dst / (
            dst.max() - dst.min()
        )
    )
    * 255
).astype(np.uint8)
cv2.imshow("dst2", dst)

ret, sure_fg = cv2.threshold(
    dst,
    0.5 * dst.max(),
    255,
    0
)
cv2.imshow("sure_fg", sure_fg)

# Error occurs
_, bg_th = cv2.threshold(
    dst,
    0.3 * dst.max(),
    255,
    cv2.THRESH_BINARY_INV
)
bg_dst = cv2.distanceTransform(
    bg_th,
    cv2.DIST_L2,
    5
)
bg_dst = (
    (
        bg_dst / (
            bg_dst.max() - bg_dst.min()
        )
    ) * 255
).astype(np.uint8)

# Error Occurs..
sure_bg = cv2.threshold(
    bg_dst,
    0.3 * bg_dst.max(),
    255,
    cv2.THRESH_BINARY
)
cv2.imshow("sure_bg", sure_bg)

inv_sure_bg = cv2.threshold(
    sure_bg,
    127, 255,
    cv2.THRESH_BINARY_INV
)
unknown = cv2.subtract(
    inv_sure_bg, sure_fg
)
cv2.imshow("unknown", unknown)

_, markers = cv2.connectedComponents(sure_fg)

markers += markers
markers[unknown == 255] = 0
print("WaterShed Sun", np.unique(markers))

colors = []
marker_show = np.zeros_like(img)

for mid in np.unique(markers):
    color = [int(j) for j in np.random.randint(0, 255, 3)]
    colors.append((mid, color))
    marker_show[markers == mid] = color
    coords = np.where(markers == mid)
    x, y = coords[1][0], coords[0][0]
    cv2.putText(
        marker_show,
        str(mid),
        (x + 20, y + 20),
        cv2.FONT_HERSHEY_PLAIN,
        2,
        (255, 255, 255)
    )
cv2.imshow("before", marker_show)
