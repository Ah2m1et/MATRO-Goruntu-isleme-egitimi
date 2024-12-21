import cv2  # OpenCV kütüphanesi, görüntü işleme için kullanılır

# 1. Resmi Okuma
# 'mustang.jpg' adlı resmi okuyoruz. Eğer dosya yoksa hata alınır.
image = cv2.imread("mustang.jpg")

# 2. Gaussian Bulanıklaştırma
# Görüntüyü bulanıklaştırıyoruz. (15, 15), bulanıklaştırma için kullanılan kernel boyutudur.
blurred = cv2.GaussianBlur(image, (15, 15), 0)

# 3. Görüntüyü Gösterme
# Bulanıklaştırılmış görüntüyü bir pencerede gösteriyoruz.
cv2.imshow("Bulanik", blurred)

# 4. Pencereyi Kapama
# Bir tuşa basılmasını bekler, ardından pencereyi kapatır.
cv2.waitKey(0)
cv2.destroyAllWindows()
