import cv2  # Görüntü işleme kütüphanesi
import numpy as np  # Matematiksel işlemler için NumPy kütüphanesi

# 1. Resmi Okuma
# "ornek_resim.jpg" adlı resmi okuyoruz.
image = cv2.imread("ornek_resim.jpg")

# 2. Rastgele Gürültü Oluşturma
# Resim boyutlarına uygun rastgele bir gürültü matrisi oluşturuyoruz.
noise = np.random.normal(0, 25, image.shape).astype(np.uint8)

# 3. Gürültüyü Resme Ekleme
# Gürültüyü orijinal resimle birleştiriyoruz.
noisy_image = cv2.add(image, noise)

# 4. Gürültülü Görüntüyü Gösterme
# Gürültü eklenmiş resmi bir pencerede gösteriyoruz.
cv2.imshow("Gurultulu Resim", noisy_image)

# 5. Bekleme ve Kapatma
# Bir tuşa basılana kadar bekliyoruz ve ardından tüm pencereleri kapatıyoruz.
cv2.waitKey(0)
cv2.destroyAllWindows()
