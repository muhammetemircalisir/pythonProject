# Kullanıcıdan bir sayı girişi alın
sayi = int(input("lütfen bir sayı giriniz: "))
# Bölenlerin toplamını hesaplamak için bir değişken oluşturun
toplam=0
# 1'den sayıya kadar olan sayıları bölenleri olarak kontrol edin
for i in range(1,sayi):
    if sayi % i == 0:
        toplam += i

# Toplam, girilen sayıya eşitse mükemmel bir sayıdır
if toplam == sayi:
    print(sayi,"bir mükemmel sayidir")
else :
    print(sayi,"mükemmel sayi değildir")
