# Kullanıcıdan Fibonacci serisi için eleman sayısını al
n = int(input("Kaç elemanlı Fibonacci serisi istiyorsunuz? "))

# İlk iki Fibonacci sayısı
fibonacci = [0, 1]

# Fibonacci serisini oluştur
for i in range(2, n):
    fibonacci.append(fibonacci[i-1] + fibonacci[i-2])

# Seriyi ekrana yazdır
print("Fibonacci Serisi:", fibonacci)
