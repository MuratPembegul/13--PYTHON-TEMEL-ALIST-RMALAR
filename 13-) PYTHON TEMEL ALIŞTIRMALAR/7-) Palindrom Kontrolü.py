# Bir kelimenin palindrom olup olmadığını kontrol eden fonksiyon
def palindrom_mu(kelime):
    kelime = kelime.lower()  # Büyük/küçük harf farkını ortadan kaldır
    ters_kelime = kelime[::-1]  # Kelimeyi ters çevir
    return kelime == ters_kelime  # Karşılaştırma yap

# Kullanıcıdan giriş al
kelime = input("Bir kelime girin: ")

# Sonucu ekrana yazdır
if palindrom_mu(kelime):
    print(f"'{kelime}' bir palindromdur!")
else:
    print(f"'{kelime}' bir palindrom değildir.")
