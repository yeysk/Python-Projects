
   # GÖREV 3: HESAP MAKİNESİ

import math

def toplama_islemi():
    while True:
        try:
            x = float(input("\nİlk sayıyı giriniz: "))
            break
        except ValueError:
            print("Sadece sayı giriniz.")
   
    while True:
        try:
            y = float(input("\nİkinci sayıyı giriniz: "))
            break
        except ValueError:
            print("Sadece sayı giriniz.")
    return "Sonuç:", x + y
    
   
def cıkarma_islemi():
    while True:
        try:
            x = float(input("\nİlk sayıyı giriniz: "))
            break
        except ValueError:
            print("Sadece sayı giriniz.")
   
    while True:
        try:
            y = float(input("\nİkinci sayıyı giriniz: "))
            break
        except ValueError:
            print("Sadece sayı giriniz.")
    return "Sonuç:", x - y

def carpma_islemi():
    while True:
        try:
            x = float(input("\nİlk sayıyı giriniz: "))
            break
        except ValueError:
            print("Sadece sayı giriniz.")
   
    while True:
        try:
            y = float(input("\nİkinci sayıyı giriniz: "))
            break
        except ValueError:
            print("Sadece sayı giriniz.")
        
    return "Sonuç:", x * y

def bolme_islemi():
    
    while True:
        try:
            x = float(input("\nİlk sayıyı giriniz: "))
            y = float(input("\nİkinci sayıyı giriniz: "))
            print(f"Sonuç: {x} / {y} = {round(x/y,4)}")
            break
        except ValueError:
            print("Sadece sayı giriniz.")
        except ZeroDivisionError:
            print("0 dışında bir sayı giriniz.")
       
    return ""

def faktöriyel_hesapla():
    while True:
        try:
            sayi = int(input("\nLütfen faktöriyelini bulmak istediğiniz sayıyı giriniz:"))
            faktoriyel = 1
             
            if sayi >= 0:
                for i in range(1, sayi + 1):
                    faktoriyel *= i
                print(f"Girdiğiniz sayının faktöriyeli: {sayi}! = {faktoriyel}")
                break
            else:
                print("Negatif sayıların faktöriyeli olmaz!")
        except ValueError:
            print("Geçersiz giriş.Tekrar deneyiniz.")
    return ""
def us_alma():
    while True:
        try:
            x = float(input("\nİlk sayıyı giriniz: "))
            break
        except ValueError:
            print("Sadece sayı giriniz.")
   
    while True:
       try:
            y = float(input("\nİkinci sayıyı giriniz: "))
            return "Sonuç:", x**y
        except Exception as e:
            print(e)
def mod_alma():
    while True:
        try:
            x = float(input("\nİlk sayıyı giriniz: "))
            y = float(input("\nİkinci sayıyı giriniz: "))
            mod = x % y
            print("Sonuç", mod)
            break
        except ValueError:
            print("Sadece sayı giriniz.")
        except ZeroDivisionError:
            print("0 dışında bir sayı giriniz.")
    return ""   
    
def kok_hesapla():
    while True:
        
        while True:
            try:
                a = int(input("\na katsayısı için bir değer giriniz: "))
                if a == 0:
                    print("0 olamaz.Tekrar deneyin.")
                    continue
                break
            except ValueError:
                print("Sadece sayı girişi yapınız.")
            
        while True:   
            try:
                b = int(input("b katsayısi için bir değer giriniz: "))
                break
            except ValueError:
                print("Geçersiz karakter! Lütfen geçerli bir tamsayı girin.")
          
        while True:
            try:
                c = int(input("c katsayısı için bir değer giriniz: "))
                break
            except ValueError:
                print("Geçersiz karakter! Lütfen geçerli bir tamsayı girin.")
        
        delta = b**2 - 4*a*c
        print(f"\nDiskriminant: {delta}")
            
        if delta < 0:
                print("Denklemin reel kökü yoktur!")
                break
        elif delta == 0:
                x = -b / (2*a)
                print(f"Kök: {x}")
                break
        else:
                x1 = (-b  - math.sqrt(delta)) / (2*a)
                x2 = (-b  + math.sqrt(delta)) / (2*a)
                print(f"Kökler: {x1, x2}")
                break
    return ""
        
def menu():
    while True:
        try:
            print("\n****** İşlem Menüsü ******")
            print("\nLütfen yapmak istediğiniz işlemin numarasını giriniz. ")
            print("\n1. Toplama")
            print("2. Çıkarma")
            print("3. Çarpma")
            print("4. Bölme")
            print("5. Faktöriyel")
            print("6. Üs Alma")
            print("7. Mod Alma")
            print("8. İkinci Dereceden Denklem Çözme")
            print("9. Çıkış")
            
            islem_no = int(input("\nLütfen bir işlem numarası seçiniz: "))
                
            if islem_no == 1:
                print(toplama_islemi())
                
            elif islem_no == 2:
                print(cıkarma_islemi())
                
            elif islem_no == 3:
                print(carpma_islemi())
                
            elif islem_no == 4:
                print(bolme_islemi())
                
            elif islem_no == 5:
                print(faktöriyel_hesapla())
                
            elif islem_no == 6:  
                print(us_alma())
                
            elif islem_no == 7:
                print(mod_alma())
                
            elif islem_no == 8:
                print(kok_hesapla())
            elif islem_no == 9:
                print("Çıkış yapılıyor...")
                break 
            else:
                print("Böyle bir işlem mevcut değildir.Lütfen tekrar deneyiniz.")
        except ValueError:
            print("Geçersiz giriş.Tekrar deneyin.")
        
menu()
        

    





