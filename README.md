# 13--PYTHON-TEMEL-ALISTIRMALAR

# 🐍 Python Temel Alıştırmalar README

## 📌 Giriş (Introduction)
Bu repo, **Python öğrenmek isteyenler için temel alıştırmalar** içermektedir. Her alıştırma, Python’un farklı yönlerini öğrenmeye yardımcı olacak şekilde tasarlanmıştır. 🚀

Python’a yeni başlayanlar veya temel bilgilerini pekiştirmek isteyenler için **uygulamalı örnekler ve çözümleriyle** birlikte sunulmaktadır. 💡

---

## 🚀 Kurulum (Installation)
Python'u yüklemek için aşağıdaki adımları takip edebilirsiniz:

1. [Python'un resmi web sitesinden](https://www.python.org/downloads/) indirin ve kurun.
2. Kurulumu doğrulamak için terminal veya komut istemcisine aşağıdaki komutu yazın:

```bash
python --version
```

3. Alıştırmaları çalıştırmak için bir Python dosyası oluşturun ve aşağıdaki gibi çalıştırın:

```bash
python dosya_adi.py
```

---

## 📚 Alıştırma Konuları
Aşağıdaki başlıklar altında **100'den fazla alıştırma** yer almaktadır:

### 📌 1. Temel Python Alıştırmaları
- Değişken Tanımlama ve Kullanımı
- Matematiksel İşlemler
- Kullanıcıdan Veri Alma ve Yazdırma
- Koşullu İfadeler (if-else)
- Döngüler (for, while)

### 📊 2. Veri Yapıları
- Listeler
- Demetler (Tuples)
- Sözlükler
- Kümeler

### 🏗️ 3. Fonksiyonlar
- Parametre Alan Fonksiyonlar
- Geri Döndüren Fonksiyonlar
- Lambda Fonksiyonları

### 🧠 4. Nesne Yönelimli Programlama (OOP)
- Sınıflar ve Nesneler
- Miras (Inheritance)
- Kapsülleme (Encapsulation)

### 📈 5. Dosya İşlemleri
- Dosya Okuma ve Yazma
- CSV ve JSON İşlemleri

### 🔍 6. Hata Yönetimi ve Debugging
- Try-Except Blokları
- Debugging Teknikleri

---

## 🔥 Örnek Alıştırmalar

### 1️⃣ Basit "Merhaba Dünya!" Programı
```python
print("Merhaba, Dünya!")
```

### 2️⃣ Kullanıcıdan Girdi Alma
```python
isim = input("Adınızı girin: ")
print(f"Merhaba, {isim}!")
```

### 3️⃣ Sayıların Toplamını Hesaplama
```python
a = int(input("Birinci sayıyı girin: "))
b = int(input("İkinci sayıyı girin: "))
print("Toplam:", a + b)
```

### 4️⃣ Faktöriyel Hesaplama
```python
def faktoriyel(n):
    if n == 0:
        return 1
    return n * faktoriyel(n - 1)

sayi = int(input("Bir sayı girin: "))
print(f"{sayi}! =", faktoriyel(sayi))
```

---

## 📜 Kaynaklar (Resources)
- [Python Resmi Belgeleri](https://docs.python.org/3/)
- [W3Schools Python Alıştırmaları](https://www.w3schools.com/python/exercise.asp)
- [LeetCode Python Alıştırmaları](https://leetcode.com/)

---

## 📌 Katkı Yapma (Contributing)
Yeni alıştırmalar eklemek veya mevcutları geliştirmek isterseniz fork'layıp PR gönderebilirsiniz! 🚀

---

## 📜 Lisans (License)
Bu proje MIT lisansı altındadır, dilediğiniz gibi kullanabilirsiniz! 😊

