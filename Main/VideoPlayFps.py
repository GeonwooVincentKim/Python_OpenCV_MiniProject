import cv2
video_file = "../img/video.avi"

cap = cv2.VideoCapture(video_file)
if cap.isOpened:
    fps = cap.get(cv2.CAP_PROP_FPS)
    delay = int(1000 / fps)
    print("FPS: %f, Delay: %dms" % (fps, delay))

    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow(video_file, img)
            cv2.waitKey(delay)

        else:
            break
else:
    print("Can't open video.")
cap.release()
cv2.destroyAllWindows()
