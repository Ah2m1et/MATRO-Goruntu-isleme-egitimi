import cv2  # Görüntü işleme için OpenCV

# 1. Resmi Okuma
# Gri tonlamalı bir resim olarak yüklüyoruz.
image = cv2.imread("ornek_resim.jpg", 0)

# 2. Gradyan Hesaplama
# Laplacian yöntemiyle kenar tespiti yapıyoruz.
laplacian = cv2.Laplacian(image, cv2.CV_64F)

# 3. Görüntüyü Gösterme
# Gradyan sonucu resmi gösteriyoruz.
cv2.imshow("Gradyan", laplacian)

# 4. Bekleme ve Kapatma
cv2.waitKey(0)
cv2.destroyAllWindows()
