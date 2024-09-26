
# İkinci dereceden denklem hesabı yapan program

import math

def kok_hesapla():
    while True:
        
        while True:
            try:
                a = int(input("a katsayısı için bir değer giriniz: "))
                if a == 0:
                    print("0 olamaz.Tekrar deneyin.")
                    continue
                break
            except ValueError:
                print("Sadece sayı girişi yapınız.")
                #a = int(input("a katsayısı için bir değer giriniz: "))
                #break
            #break    
            
            
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
            
        if delta < 0:
                print("Denklemin reel kökü yoktur!")
        elif delta == 0:
                x = -b / (2*a)
                print("Kök: ", x)
        else:
                x1 = (-b  - math.sqrt(delta)) / (2*a)
                x2 = (-b  + math.sqrt(delta)) / (2*a)
                print("Kökler: ", x1, x2)
    
        while True:
            tekrar = input("Yeni bir işlem yapmak ister misiniz?(E/H): ").lower()
            if tekrar == 'e':
                break
            elif tekrar == 'h':
                print("Program sonlandırılıyor...")
                break
            else:
                print("Geçersiz giriş! Lütfen sadece E veya H girin.")
            
print(kok_hesapla())



