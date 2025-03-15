import random

# Rastgele bir sayı belirle (1 ile 100 arasında)
sayi = random.randint(1, 100)

print("1 ile 100 arasında bir sayıyı tahmin et!")

while True:
    tahmin = int(input("Tahmininizi girin: "))
    
    if tahmin < sayi:
        print("Daha büyük bir sayı girin!")
    elif tahmin > sayi:
        print("Daha küçük bir sayı girin!")
    else:
        print("Tebrikler, doğru tahmin ettiniz!")
        break  # Doğru tahminde döngü sonlanır
