import cv2

img_file = "../img/People.jpg"
save_file = '../img/People_gary.jpg'
img = cv2.imread(img_file, cv2.IMREAD_GRAYSCALE)

if img is not None:
    cv2.imshow(img_file, img)
    cv2.imwrite(save_file, img)
    cv2.waitKey()
    cv2.destroyAllWindows()
else:
    print("No Image File.")
