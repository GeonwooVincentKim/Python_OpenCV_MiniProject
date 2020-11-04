import cv2
import numpy as np


cap = cv2.VideoCapture(0)
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)
rows, cols = 240, 320
map_y, map_x = np.incides((rows, cols), dtype=np.float32)

map_mirror_h_x, map_mirror_h_y = map_x.copy(), map_y.copy()
map_mirror_v_x, map_mirror_v_y = map_x.copy(), map_y.copy()

map_mirror_h_x[:, cols // 2:] = cols - map_mirror_h_x[:, cols // 2:] - 1
map_mirror_h_y[rows // 2:, :] = rows - map_mirror_v_y[rows // 2:, :] - 1

map_wave_x, map_wave_y = map_x.copy(), map_y.copy()
map_wave_x = map_wave_x + 15 * np.sin(map_y / 20)
map_wave_y = map_wave_y + 15 * np.sin(map_x / 20)

