import cv2

video = cv2.VideoCapture("mlbb.mp4")
while True:
    ret,frame = video.read()
    if not ret:
        break 

    cv2.imshow("video",frame)
    if cv2.waitKey(30) & 0xFF == ord('q'):
        break

video.release
cv2.destroyAllWindows


