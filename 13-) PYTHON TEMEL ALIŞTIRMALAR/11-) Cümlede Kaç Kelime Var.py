# Kullanıcıdan cümle al
cumle = input("Bir cümle giriniz: ")

# Cümleyi boşluklara göre ayır ve kelime sayısını hesapla
kelime_sayisi = len(cumle.split())

# Sonucu ekrana yazdır
print(f"Girdiğiniz cümlede {kelime_sayisi} kelime var.")
