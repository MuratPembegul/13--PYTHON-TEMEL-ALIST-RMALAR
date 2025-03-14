# 📌 Kullanıcıdan bir sayı al
sayi = int(input("Faktöriyel hesaplamak için bir sayı girin: "))

# 📌 Faktöriyel hesaplama
faktoriyel = 1
for i in range(1, sayi + 1):  # 1’den kullanıcının sayısına kadar döngü
    faktoriyel *= i  # Çarpma işlemi

# 📌 Sonucu yazdır
print(f"{sayi}! = {faktoriyel}")
