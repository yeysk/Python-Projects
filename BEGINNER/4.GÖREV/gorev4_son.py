
# GÖREV 4 : SAYI TAHMİN OYUNU

import random

sayi1 = random.randint(1, 101)
sayi2 = random.randint(1, 501)
sayi3 = random.randint(1, 1001)

bilgisayarTuttu = ""

def tahmin():
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
                main()
        except ValueError:
            print("Lütfen sadece rakam giriniz!")
def main():
    global bilgisayarTuttu
    while True:
        print("\n********ZORLUK SEVİYELERİ*********")
        print("\n1. Seviye")
        print("2. Seviye")
        print("3. Seviye")
        print("4. Çıkış")
        try:
            seviyeNo = int(input("\nSeviye no giriniz: "))
            
            if (seviyeNo == 1):
               
                print("Bilgisayarın tuttuğu sayı: ", sayi1)
                bilgisayarTuttu = sayi1
                tahmin()
                break
            elif (seviyeNo == 2):
                print("Bilgisayarın tuttuğu sayı: ", sayi2)
                bilgisayarTuttu = sayi2
                tahmin()
                break
            elif (seviyeNo == 3):
                print("Bilgisayarın tuttuğu sayı: ", sayi3)
                bilgisayarTuttu = sayi3
                tahmin()
                break
            elif (seviyeNo == 4):
                print("Çıkış yapılıyor...")
                break
            else:
                print("Geçersiz seviye no!Tekrar deneyiniz.")
        except ValueError:
            print("Lütfen sadece rakam giriniz!")
            
main()
            
      
        
