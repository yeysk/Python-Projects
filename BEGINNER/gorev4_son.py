
# GÖREV 4 : SAYI TAHMİN OYUNU

# çökmüyor, ama işlem sonunda kapanıyor.

import random

sayi1 = random.randint(1, 101)
sayi2 = random.randint(1, 501)
sayi3 = random.randint(1, 1001)

print("********ZORLUK SEVİYELERİ*********")
print("\n1. Seviye")
print("2. Seviye")
print("3. Seviye")

while True:
    try:
        seviyeNo = int(input("\nSeviye no giriniz: "))
    
        if (seviyeNo == 1):
             print("Bilgisayarın tuttuğu sayı: ", sayi1)
             bilgisayarTuttu = sayi1
             break
        elif (seviyeNo == 2):
             print("Bilgisayarın tuttuğu sayı: ", sayi2)
             bilgisayarTuttu = sayi2
             break
        elif (seviyeNo == 3):
             print("Bilgisayarın tuttuğu sayı: ", sayi3)
             bilgisayarTuttu = sayi3
             break
        else:
             print("Geçersiz seviye no!")
    except ValueError:
            print("Lütfen sadece rakam giriniz!")

tahmin_asamasi = True
    
while tahmin_asamasi:
    try:
        tahmin = int(input("Lütfen tahmininizi giriniz: "))
        
        if tahmin > bilgisayarTuttu:
            print("Daha küçük!")
        elif tahmin < bilgisayarTuttu:
            print("Daha büyük!")
        else:
            print("Tebrikler, oyunu kazandınız!")
            tahmin_asamasi = False
    except ValueError:
        print("Lütfen sadece rakam giriniz!")
            
      
        