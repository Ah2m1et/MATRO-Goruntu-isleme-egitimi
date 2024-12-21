# Matro Görüntü İşleme Eğitimi - OpenCV

Bu proje, **Matro Topluluğu** tarafından düzenlenen "Görüntü İşleme ve OpenCV" eğitimi kapsamında hazırlanan kod örneklerini içerir. Görüntü işleme temellerinden başlayarak ileri düzey konulara kadar birçok uygulamalı örnek sunmaktadır.

---

## İçindekiler

- [Proje Hakkında](#proje-hakkında)
- [Gereksinimler](#gereksinimler)
- [Kurulum](#kurulum)
- [Kod İçerikleri](#kod-içerikleri)
  - [Resim İşleme](#resim-i̇şleme)
  - [Video İşleme](#video-i̇şleme)
  - [Şekil ve Metin İşleme](#şekil-ve-metin-i̇şleme)
  - [Diğer Temel OpenCV Fonksiyonları](#diğer-temel-opencv-fonksiyonları)
- [OpenCV Temel Fonksiyonları](#opencv-temel-fonksiyonları)
- [Katkıda Bulunma](#katkıda-bulunma)
- [Lisans](#lisans)

---

## Proje Hakkında

Bu eğitim dosyaları, görüntü işleme alanında kullanılan temel teknikleri öğrenmek ve OpenCV kütüphanesini uygulamalı olarak kullanmak isteyenlere yöneliktir. Eğitim sürecinde:

1. Görüntü ve video işleme temelleri,
2. Şekil ve metin çizimi,
3. Filtreleme ve kenar bulma gibi temel konular işlenmiştir.

---

## Gereksinimler

Projeyi çalıştırmak için aşağıdaki araçlar gereklidir:

- **Python 3.7+**
- **OpenCV** kütüphanesi
- **NumPy** kütüphanesi

### Python Kütüphanelerini Yükleme

Gerekli kütüphaneleri yüklemek için aşağıdaki komutu çalıştırabilirsiniz:

```bash
pip install opencv-python opencv-python-headless numpy
```

---

## Kurulum

1. Bu projeyi bilgisayarınıza klonlayın:
   ```bash
   git clone https://github.com/Matro-Topluluk/goruntu-isleme-egitimi.git
   cd goruntu-isleme-egitimi
   ```

2. Gerekli Python kütüphanelerini yükleyin:
   ```bash
   pip install -r requirements.txt
   ```

3. Örnek kodları çalıştırarak eğitime başlayabilirsiniz. Örneğin:
   ```bash
   python resim_isleme.py
   ```

---

## Kod İçerikleri

### Resim İşleme

- **Resmi okuma ve kaydetme**: `cv2.imread`, `cv2.imwrite`
- **Piksel manipülasyonu**: `cv2.add`, `cv2.multiply`
- **Görüntü yansıması**: `cv2.flip`
- **Görüntü boyutlandırma ve kırpma**: `cv2.resize`, dilimleme

### Video İşleme

- **Videoyu okuma ve oynatma**: `cv2.VideoCapture`
- **Webcam'den görüntü alma**: Canlı video akışı örnekleri

### Şekil ve Metin İşleme

- **Çizgi, daire, dikdörtgen çizme**: `cv2.line`, `cv2.circle`, `cv2.rectangle`
- **Görüntüye metin ekleme**: `cv2.putText`

### Diğer Temel OpenCV Fonksiyonları

- **Görüntü gösterme**: `cv2.imshow`
- **Görüntü dönüştürme**: Örneğin, gri tonlamaya çevirmek için `cv2.cvtColor`
- **Klavye ile etkileşim**: `cv2.waitKey`

---

## OpenCV Temel Fonksiyonları

Aşağıda OpenCV ile çalışırken sıkça kullanılan temel fonksiyonlar açıklanmıştır:

1. **Görüntü Okuma ve Yazma**
   - `cv2.imread(filename, flag)`: Resmi okur. `flag` değeri 0 (gri tonlama), 1 (renkli) olabilir.
   - `cv2.imwrite(filename, image)`: Görüntüyü kaydeder.

2. **Görüntü Gösterme**
   - `cv2.imshow(window_name, image)`: Görüntüyü bir pencerede gösterir.
   - `cv2.waitKey(delay)`: Klavyeden giriş bekler. `delay` 0 ise sonsuz bekler.

3. **Görüntü Manipülasyonu**
   - `cv2.resize(image, dsize)`: Görüntüyü verilen boyutlara yeniden boyutlandırır.
   - `cv2.flip(image, flip_code)`: Görüntüyü ayna simetri ile döndürür. Örneğin, `flip_code=1` yatay aynalamadır.
   - `cv2.add(image1, image2)`: İki görüntüyü toplar.

4. **Video İşleme**
   - `cv2.VideoCapture(source)`: Video dosyasını veya kamera kaynağını açar.
   - `capture.read()`: Video karesi okur.

5. **Şekiller ve Çizimler**
   - `cv2.line(image, pt1, pt2, color, thickness)`: Çizgi çizer.
   - `cv2.circle(image, center, radius, color, thickness)`: Daire çizer.
   - `cv2.rectangle(image, pt1, pt2, color, thickness)`: Dikdörtgen çizer.
   - `cv2.putText(image, text, org, font, fontScale, color, thickness)`: Metin ekler.

6. **Renk Dönüşümleri**
   - `cv2.cvtColor(image, code)`: Görüntüyü renk uzayları arasında dönüştürür (örneğin, BGR'den Gri).

---

## Katkıda Bulunma

Projeye katkıda bulunmak isterseniz, lütfen bir [pull request](https://github.com/Matro-Topluluk/goruntu-isleme-egitimi/pulls) oluşturun. Her türlü öneri ve iyileştirme memnuniyetle karşılanır.

---

## Lisans

Bu proje **MIT Lisansı** altında lisanslanmıştır. Daha fazla bilgi için `LICENSE` dosyasını inceleyebilirsiniz.

---

Matro Topluluğu'na katılarak daha fazla bilgi ve eğitimlere erişebilirsiniz. İyi çalışmalar! 🎉
