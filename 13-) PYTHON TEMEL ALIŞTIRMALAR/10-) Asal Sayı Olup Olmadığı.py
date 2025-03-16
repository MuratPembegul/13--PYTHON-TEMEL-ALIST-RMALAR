# Kullanıcıdan sayı al
sayi = int(input("Bir sayı giriniz: "))

# Asallık kontrolü için değişken
asal_mi = True  

# 2'den başlayarak sayının kareköküne kadar kontrol et
for i in range(2, int(sayi ** 0.5) + 1):
    if sayi % i == 0:
        asal_mi = False
        break  

# Sonucu yazdır
if asal_mi and sayi > 1:
    print(f"{sayi} bir asal sayıdır.")
else:
    print(f"{sayi} asal değildir.")
