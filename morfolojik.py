import cv2  # Görüntü işleme için OpenCV
import numpy as np  # Matematiksel işlemler için NumPy

# 1. Resmi Okuma
# Siyah-beyaz (ikili) bir resmi okuyoruz.
image = cv2.imread("binary_resim.jpg", 0)

# 2. Çekirdek Tanımlama
# 5x5 boyutunda bir kare çekirdek (kernel) oluşturuyoruz.
kernel = np.ones((5, 5), np.uint8)

# 3. Dilate (Genişletme) İşlemi
# Resimdeki beyaz alanları genişletiyoruz.
dilated = cv2.dilate(image, kernel, iterations=1)

# 4. Görüntüyü Gösterme
# Morfolojik işlem uygulanmış görüntüyü gösteriyoruz.
cv2.imshow("Morfolojik Operasyon", dilated)

# 5. Bekleme ve Kapatma
cv2.waitKey(0)
cv2.destroyAllWindows()
