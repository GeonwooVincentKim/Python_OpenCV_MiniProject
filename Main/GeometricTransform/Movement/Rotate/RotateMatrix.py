import cv2
import numpy as np


img = cv2.imread('../../../../img/fish.jpg')
rows, cols = img.shape[:2]

# Calculate Radian-Angle (Convert 60-systems to circular-method).
d45 = 45.0 * np.pi / 180
d90 = 90.0 * np.pi / 180

# Generate Transform Matrix for Rotation.
m45 = np.float32([[np.cos(d45), -1 * np.sin(d45), rows // 2],
                  [np.sin(d45), np.cos(d45), -1 * cols // 4]])
m90 = np.float32([[np.cos(d90), -1 * np.sin(d90), rows],
                  [np.sin(d90), np.cos(d90), 0]])

# Apply Rotation Transform-Matrix.
r45 = cv2.warpAffine(img, m45, (cols, rows))
r90 = cv2.warpAffine(img, m90, (rows, cols))

# Display each images results.
cv2.imshow('origin', img)
cv2.imshow('45', r45)
cv2.imshow('90', r90)
cv2.waitKey(0)
cv2.destroyAllWindows()
