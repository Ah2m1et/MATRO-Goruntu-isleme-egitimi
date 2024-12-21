import cv2

cap = cv2.VideoCapture(0)

if not cap.isOpened:
    print("kameran bozuk fakir")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("kameradan veri gelmedi")
        break
    cv2.imshow("webcam",frame)
    if cv2.waitKey(1) & 0xff == ord('q'):
        break
 

cap.release
cv2.destroyAllWindows