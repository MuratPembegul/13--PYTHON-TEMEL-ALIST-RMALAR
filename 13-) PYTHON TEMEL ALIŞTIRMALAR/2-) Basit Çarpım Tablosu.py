# 📌 Kullanıcıdan bir sayı al
sayi = int(input("Çarpım tablosu için bir sayı girin: "))

# 📌 1’den 10’a kadar çarpım tablosunu yazdır
print(f"{sayi} sayısının çarpım tablosu:")
for i in range(1, 11):  # 1’den 10’a kadar döngü
    print(f"{sayi} x {i} = {sayi * i}")  # Çarpım işlemini yazdır
