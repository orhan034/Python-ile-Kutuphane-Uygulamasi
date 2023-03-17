from kütüphane import *
print("""*********************
Kütüphane programına hoşgeldiniz.
İşlemler,
1. Kitapları Göster
2. Kitap Sorgula
3. Kitap Ekle
4. Kitap Sil
5. Baskı Yükselt

Çıkmak için 'q' tıklayınız
***************************""")

kütüphane = Kütüphane()

while True:
    islem = input("Yapacağiniz İşlem numarasını giriniz:")
    if islem =="q":
        print("Program sonlandırılıyor......")
        print("Yine bekleriz.....")
        break
    elif islem =="1":
        kütüphane.kitaplari_goster()

    elif islem =="2":
        isim = input("Hangi kitabı istiyorsunuz:")
        print("Kitap sorgulanıyor...")
        time.sleep(2)

        kütüphane.kitap_sorgula(isim)

    elif islem =="3":
        isim = input("Kitabın İsmi:")
        yazar = input("Kitabın Yazarı:")
        yayinevi = input("Yayin Evi:")
        türü = input("Kitabın Türü:")
        baski = int(input("Kitabın baskısı:"))
        
        yeni_kitap = Kitap(isim,yazar,yayinevi,türü,baski)
        print("Kitap ekleniyor.....")
        time.sleep(2)
        kütüphane.kitap_ekle(yeni_kitap)
        print("Kitap eklendi...")
    elif islem =="4":
        isim = input("Hangi kitabı silmek istiyorsunuz:")
        cevap = input("Emin misiniz ? (E/H):")
        if cevap =="E":
            print("Kitap siliniyor...")
            time.sleep(2)
            kütüphane.kitap_sil(isim)
            print("Kitap silindi...")
        
    elif islem =="5":
        isim = input("Hangi kitabın baskısını yükseltmek istiyorsunuz:")
        print("Baskı yükseltiliyor...")
        time.sleep(2)
        kütüphane.baski_yükselt(isim)
        print("Baskı yükseltildi....")
    else:
        print("Geçersiz işlem.....")
