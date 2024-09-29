# İkinci dereceden denklem hesabı yapan program

import math

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
        elif delta == 0:
                x = -b / (2*a)
                print(f"Kök: {x}")
        else:
                x1 = (-b  - math.sqrt(delta)) / (2*a)
                x2 = (-b  + math.sqrt(delta)) / (2*a)
                print(f"Kökler: {x1, x2}")
    
        cont = True
        while cont:
            tekrar = input("\nYeni bir işlem yapmak ister misiniz?(E/H): ").lower()
            if tekrar == 'e':
                cont = False
            elif tekrar == 'h':
                print("Program sonlandırılıyor...")
                return ""
            else:
                print("Geçersiz giriş! Lütfen sadece E veya H girin.")
            
kok_hesapla()



