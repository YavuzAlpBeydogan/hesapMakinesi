print("Yapmak istediğiniz işlemi seçiniz:")
secim = input("""
1.Toplama
2.Çarpma
3.Bölme
4.Çıkartma
""")

# Toplama İşlemi İçin
if secim == "1":
    print("Toplama işlemi seçildi.")
    kacSecim = int(input("Kaç tane sayı toplamak istiyorsunuz?"))
    toplam = 0

    while kacSecim > 0:
        sayi = float(input("Sayı giriniz: "))
        toplam += sayi
        kacSecim -= 1

    print("Toplam:", toplam)

# Çarpma İşlemi İçin
elif secim == "2":
    print("Çarpma işlemi seçildi.")
    kacSecim = int(input("Kaç tane sayı çarpmak istiyorsunuz?"))
    carpim = 1

    while kacSecim > 0:
        sayi = float(input("Sayı giriniz: "))
        carpim *= sayi
        kacSecim -= 1

    print("Çarpım:", carpim)

# Bölme İşlemi İçin
elif secim == "3":
    print("Bölme işlemi seçildi.")
    bolunen = float(input("Bölünen sayıyı seçiniz:"))
    bolen = float(input("Bölen sayıyı seçiniz:"))
    
    if bolen != 0:
        bolum = bolunen // bolen  # Tam bölme
        kalan = bolunen % bolen  # Kalan

        print("Bölüm: ", bolum)
        print("Kalan: ", kalan)
    else:
        print("Hata: Bölen sıfır olamaz.")

# Çıkartma İşlemi İçin
elif secim == "4":
    print("Çıkartma işlemi seçildi.")
    
    kacSecim = int(input("Kaç tane sayıyı çıkartmak istiyorsunuz?"))
    
    # İlk sayıyı direk olarak atıyoruz
    cikart = float(input("Sayı giriniz:  "))  

    while kacSecim > 1:  # İlk sayıyı daha önce aldık, geriye kalanları çıkartacağız
        sayi = float(input("Sayı giriniz: "))
        cikart -= sayi
        kacSecim -= 1
        
    print("Çıkartma sonucu: ", cikart)


