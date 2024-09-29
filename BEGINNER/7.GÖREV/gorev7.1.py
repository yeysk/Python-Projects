kitaplar = { 
    'kitap1': {
        'isim': 'suç ve ceza',
        'yazar': 'dostoyevski',
        'stok': 5,
     },
    'kitap2': {
        'isim': 'insan ne ile yaşar',
        'yazar': 'tolstoy',
        'stok': 7
     },
    'kitap3': {
         'isim': 'fareler ve insanlar',
         'yazar': 'john steinbeck',
         'stok': 3,
     },
     'kitap4': {
         'isim': 'devlet',
         'yazar': 'platon',
         'stok': 10       
     },
     'kitap5': {    
         'isim': 'anna karanina',
         'yazar': 'tolstoy',
         'stok': 8
     }     
}            
            
while True:
     
    print("\n******* KÜTÜPHANE YÖNETİM SİSTEMİ *******")
    print("\n1. Mevcut kitapları göster")
    print("2. Kitap ekle")
    print("3. Kitap sil")
    print("4. Çıkış")
     
    try:
        secim = int(input("\nBir işlem seçin: "))
         
        if secim == 1:
            print("\nMevcut kitaplar: ")
            for kitap_key, kitap in kitaplar.items():
                print(f"Kitap Adı: {kitap['isim']}, Yazar: {kitap['yazar']}, Stok: {kitap['stok']}")
     
        elif secim == 2:
            isim = input("\nİsim: ")
            yazar = input("Yazar: ")
            stok = int(input("Stok: "))
            
            kitap_id = 'kitap' + str(len(kitaplar) + 1)
            kitaplar[kitap_id] = {'isim': isim, 'yazar': yazar, 'stok': stok}
            print("\nKitap başarıyla eklendi!")
            print(kitaplar)
             
        elif secim == 3:
            silinen_kitap = input("\nSilmek istediğiniz kitabın ismi: ").lower()
            kitap_bulundu = False
            for kitap_key, kitap in list(kitaplar.items()):
                if kitap['isim'].lower() == silinen_kitap:
                    del kitaplar[kitap_key]
                    kitap_bulundu = True
                    print(f"\n'{kitap['isim']}' başarıyla silindi.")
                    break

            if not kitap_bulundu:
                print(f"\n'{silinen_kitap}' adlı kitap listede mevcut değil.")
             
        elif secim == 4:
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")
     
    except ValueError:
        print("Lütfen sadece rakam giriniz.")


