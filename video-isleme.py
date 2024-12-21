import cv2  # OpenCV kütüphanesini içe aktarıyoruz

# 1. Kamera Kaynağını Açma
# Kamerayı başlatıyoruz. Eğer cihazınızda bir kamera varsa otomatik olarak açılacaktır.
capture = cv2.VideoCapture(0)  # 0, varsayılan web kamerayı temsil eder.

if not capture.isOpened():  # Kamera açılamazsa hata mesajı gösterir.
    print("Kamera açılamadı. Lütfen cihazınızı kontrol edin.")
    exit()

# 2. Canlı Video İşleme
while True:
    # Her kareyi okuyoruz. 'ret' başarılı olup olmadığını, 'frame' ise görüntüyü içerir.
    ret, frame = capture.read()

    if not ret:  # Eğer görüntü alınamazsa döngüyü sonlandırıyoruz.
        print("Görüntü alınamadı. Kamerayı kontrol edin.")
        break

    # Gri Tonlamaya Çevirme
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)  # Her kareyi gri tonlamaya çeviriyoruz.

    # 3. Görüntüyü Gösterme
    # Orijinal ve gri tonlamalı görüntüleri iki ayrı pencerede gösteriyoruz.
    cv2.imshow('Canlı Kamera - Orijinal', frame)  # Orijinal görüntü
    cv2.imshow('Canlı Kamera - Gri Tonlama', gray_frame)  # Gri tonlamalı görüntü

    # 'q' tuşuna basıldığında çıkış yapar.
    if cv2.waitKey(1) & 0xFF == ord('q'):  # Her 1 ms'de bir klavye girdisi kontrol edilir.
        print("Çıkış yapılıyor...")
        break

# 4. Kaynakları Serbest Bırakma
capture.release()  # Kamerayı serbest bırakıyoruz.
cv2.destroyAllWindows()  # Tüm pencereleri kapatıyoruz.
