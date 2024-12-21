import cv2  # Görüntü işleme için OpenCV

# 1. Resmi Okuma
# Gri tonlamalı bir resim olarak yüklüyoruz.
image = cv2.imread("ornek_resim.jpg", 0)

# 2. Histogram Eşitleme
# Resmin kontrastını artırıyoruz.
equalized = cv2.equalizeHist(image)

# 3. Görüntüleri Gösterme
# Orijinal ve kontrast arttırılmış görüntüleri karşılaştırıyoruz.
cv2.imshow("Orijinal", image)
cv2.imshow("Kontrast Arttirilmis", equalized)

# 4. Bekleme ve Kapatma
cv2.waitKey(0)
cv2.destroyAllWindows()
