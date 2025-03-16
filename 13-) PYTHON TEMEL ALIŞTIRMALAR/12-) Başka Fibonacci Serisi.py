# Kullanıcıdan limit al
limit = int(input("Fibonacci serisinin sınırını giriniz: "))

# Fibonacci serisini başlat
a, b = 0, 1

# İlk iki terimi yazdır
print(a, b, end=" ")

# Döngü ile devamını getir
while b < limit:
    a, b = b, a + b
    if b < limit:
        print(b, end=" ")
