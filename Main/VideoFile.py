import cv2

video_file = '../img/video.avi'

cap = cv2.VideoCapture(video_file)
if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(25)
        else:
            break

else:
    print("Can't open video.")
cap.release()
cv2.destroyAllWindows()
