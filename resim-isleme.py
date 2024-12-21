import cv2  # OpenCV kütüphanesi, görüntü işleme için kullanılır

# 1. Resmi Okuma
# 'ornek.jpg' adlı resmi okuyoruz. Eğer bu dosya yoksa hata alırsınız.
img = cv2.imread('ornek.jpg')  # Resmi okuma, BGR formatında gelir.

# 2. Renk Dönüşümü
# Resmi gri tonlamaya çeviriyoruz (siyah-beyaz olarak gösterilecek).
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# 3. Yeniden Boyutlandırma
# Gri tonlamaya çevrilmiş resmi 200x200 piksel boyutuna küçültüyoruz.
resized = cv2.resize(gray, (200, 200))  # Yeni boyut: 200x200 piksel

# 4. Görüntüleri Gösterme
# Orijinal ve gri tonlamalı resmi ayrı pencerelerde gösteriyoruz.
cv2.imshow('Orijinal Resim', img)  # Orijinal görüntü penceresi
cv2.imshow('Gri Tonlama', gray)  # Gri tonlamalı görüntü penceresi

# 5. Bekleme ve Pencereleri Kapatma
# Bir tuşa basılmasını bekliyoruz, ardından tüm pencereleri kapatıyoruz.
cv2.waitKey(0)  # Sonsuz süreyle bekler
cv2.destroyAllWindows()  # Tüm pencereleri kapatır
