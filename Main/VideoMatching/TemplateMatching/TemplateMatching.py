import cv2
import numpy as np


img = cv2.imread("../../../img/figures.jpg")
template = cv2.imread("../../../img/taekwonv1.jpg")
th, tw = template.shape[:2]
cv2.imshow("template", template)

methods = [
    'cv2.TM_CCOEFF_NORMED',
    'cv2.TM_CCORR_NORMED',
    'cv2.TM_SQDIFF_NORMED'
]

for i, method_name in enumerate(methods):
    img_draw = img.copy()
    method = eval(method_name)
    res = cv2.matchTemplate(img, template, method)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(res)
    print(
        method_name,
        min_val,
        max_val,
        min_loc,
        max_loc
    )

    if method in [cv2.TM_SQDIFF, cv2.TM_SQDIFF_NORMED]:
        top_left = min_loc
        match_val = min_val
    else:
        top_left = max_loc
        match_val = max_val
