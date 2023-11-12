# Kullanıcıdan bir sayı girişi alın
sayi = int(input("Bir sayı girin: "))

# Sayının basamak sayısını hesaplayın
basamak_sayisi = len(str(sayi))

# Her basamağın kuvvetini hesaplamak için bir değişken oluşturun
toplam = 0
gecici_sayi = sayi

while gecici_sayi > 0:
    basamak = gecici_sayi % 10
    toplam += basamak ** basamak_sayisi
    gecici_sayi //= 10

# Armstrong sayısını kontrol edin
if toplam == sayi:
    print(sayi, "bir Amstrong sayısıdır.")
else:
    print(sayi, "bir Armstrong sayısı değildir.")
