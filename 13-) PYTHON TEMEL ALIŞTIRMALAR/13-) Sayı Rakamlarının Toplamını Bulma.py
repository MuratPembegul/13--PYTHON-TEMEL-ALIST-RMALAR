# Kullanıcıdan bir sayı al
sayi = int(input("Bir sayı giriniz: "))

# Rakamları toplamak için değişken
toplam = 0

# Sayının rakamlarını toplamak için döngü
while sayi > 0:
    toplam += sayi % 10  # Son rakamı al ve toplama ekle
    sayi //= 10  # Son rakamı at

# Sonucu ekrana yazdır
print(f"Rakamların toplamı: {toplam}")
