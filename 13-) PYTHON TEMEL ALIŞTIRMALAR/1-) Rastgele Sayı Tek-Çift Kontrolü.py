# 📌 Kullanıcıdan bir sayı girmesini isteriz
sayi = int(input("Bir sayı girin: "))

# 📌 Sayının tek mi çift mi olduğunu kontrol ederiz
if sayi % 2 == 0:
    print(f"{sayi} çift bir sayıdır.")  # Eğer 2’ye tam bölünüyorsa çifttir
else:
    print(f"{sayi} tek bir sayıdır.")  # 2’ye tam bölünmüyorsa tektir
