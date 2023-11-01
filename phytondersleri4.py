print("*************  KULLANICI GİRİŞİ  *************")

sys_kullanıcı_adı = "emir"
sys_parola = "12345"

kullanıcı_adı = input("kullanıcı adı: ")
parola = input("parola: ")

if kullanıcı_adı == sys_kullanıcı_adı and parola == sys_parola:
    print("Sisteme başarıyla girdiniz...")
elif kullanıcı_adı == sys_kullanıcı_adı and parola != sys_parola:
    print("Parola hatalı...")
elif kullanıcı_adı != sys_kullanıcı_adı and parola == sys_parola:
    print("Kullanıcı adı hatalı...")
else:
    print("Kullanıcı adı ve parola hatalı...")
