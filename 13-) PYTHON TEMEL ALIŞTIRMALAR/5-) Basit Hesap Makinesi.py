# Basit bir hesap makinesi programı
def hesap_makinesi():
    print("Hesap Makinesi\nİşlemler: +, -, *, /")
    
    # Kullanıcıdan sayı ve işlem türünü al
    sayi1 = float(input("Birinci sayıyı girin: "))
    islem = input("İşlem seçin (+, -, *, /): ")
    sayi2 = float(input("İkinci sayıyı girin: "))

    # İşlem türüne göre sonucu hesapla
    if islem == "+":
        print(f"Sonuç: {sayi1 + sayi2}")
    elif islem == "-":
        print(f"Sonuç: {sayi1 - sayi2}")
    elif islem == "*":
        print(f"Sonuç: {sayi1 * sayi2}")
    elif islem == "/":
        if sayi2 != 0:
            print(f"Sonuç: {sayi1 / sayi2}")
        else:
            print("Hata: Sıfıra bölme yapılamaz!")
    else:
        print("Geçersiz işlem!")

# Fonksiyonu çağır
hesap_makinesi()
