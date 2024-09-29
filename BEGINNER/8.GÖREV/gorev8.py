# GÖREV 8: YAPILACAKLAR LİSTESİ PROJESİ

liste = []

while True:
    try:
        print("\n***** YAPILACAKLAR LİSTESİ *****")
        print("\n1. Yapılacak bir görev ekle")
        print("2. Yapılacaklar listesini görüntüle")
        print("3. Yapılacaklar listesinden görev sil")
        print("4. Çıkış yap")
        
        secim = int(input("\nSeçiminiz: "))
        if secim == 1:
            gorev = input("\nYapılacaklar listenize eklenecek görevi yazın: ")
            liste.append(gorev)
            print(f"{gorev} başarıyla eklendi")
            print(liste)
        elif secim == 2:
            print("\nYapılacaklar listeniz: ", liste)
        elif secim == 3:
            sil = input("Silmek istediğiniz görevi yazın: ")
            if sil in liste:
                liste.remove(sil)
                print(f"{sil} başarıyla silindi.")
            else:
                print(f"{sil} adlı görev bulunamadı.") 
        elif secim == 4:
            print("Çıkış yapılıyor...")
            break
        else:
            print("Böyle bir seçenek mevcut değil. Tekrar deneyin.")
    except ValueError:
        print("Geçersiz giriş. Tekrar deneyin.")


