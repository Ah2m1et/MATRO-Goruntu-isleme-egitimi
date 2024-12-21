import cv2  # Görüntü işleme için OpenCV

# 1. Yüz Algılama Modeli
# OpenCV'nin pre-trained yüz algılama modeli (Haarcascade) yükleniyor.
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# 2. Kamera Açma
cap = cv2.VideoCapture(0)

while True:
    # Kameradan görüntü alıyoruz.
    ret, frame = cap.read()

    # Gri tonlama
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Yüzleri tespit ediyoruz.
    faces = face_cascade.detectMultiScale(gray, 1.1, 4)

    # Her yüz için dikdörtgen çiziyoruz.
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Kameradan gelen görüntüyü gösteriyoruz.
    cv2.imshow("Face Detection", frame)

    # 'q' tuşuna basıldığında çıkıyoruz.
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
