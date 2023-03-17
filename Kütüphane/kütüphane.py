import sqlite3
import time
class Kitap():
    def __init__(self,isim,yazar,yayinevi,tür,baski):
        self.isim = isim
        self.yazar = yazar
        self.yayinevi = yayinevi
        self.tür = tür
        self.baski = baski
    
    def __str__(self):
        return "Kitap İsmi: {}\nYazar: {}\nYayinevi: {}\nTür :{}\nBasi :{}".format(self.isim,self.yazar,self.yayinevi,self.tür,self.baski)

class Kütüphane():
    def __init__(self):
        self.baglanti_olustur()
    
    def baglanti_olustur(self):
        self.baglanti = sqlite3.connect("kutupahne.db")  
        self.cursor = self.baglanti.cursor()
        sorgu = "Create Table If not exists kitaplar (isim TEXT, yazar TEXT, yayinevi TEXT, tür TEXT, baski INT)"
        self.cursor.execute(sorgu)
        self.baglanti.commit()

    def baglantiyi_kes(self):
        self.baglanti.close()

    def kitaplari_goster(self):
        sorgu = "Select * From kitaplar"
        self.cursor.execute(sorgu)
        kitaplar = self.cursor.fetchall()
        if len(kitaplar)==0:
            print("Kütüphanede kitap bulunmuyor...")
        else:
            for i in kitaplar:
                kitap = Kitap(i[0],i[1],i[2],i[3],i[4])
                print(kitap)
    
    def kitap_sorgula(self,isim):
        sorgu = "Select * From kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar = self.cursor.fetchall()
        if len(kitaplar)==0:
            print("Böyle bir kitap bulunmuyor...")
        else:
            kitap = Kitap(kitaplar[0][0],kitaplar[0][1],kitaplar[0][2],kitaplar[0][3],kitaplar[0][4])
            print(kitap)
    
    def kitap_ekle(self,kitap):
        sorgu = "Insert into kitaplar Values(?,?,?,?,?)"
        self.cursor.execute(sorgu,(kitap.isim,kitap.yazar,kitap.yayinevi,kitap.tür,kitap.baski))
        self.baglanti.commit()

    def kitap_sil(self,isim):
        sorgu = "Delete From kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        self.baglanti.commit()

    def baski_yükselt(self,isim):
        sorgu = "Select * From kitaplar where isim = ?"
        self.cursor.execute(sorgu,(isim,))
        kitaplar = self.cursor.fetchall()

        if len(kitaplar)==0:
            print("Böyle bir kitap bulunmuyor...")
        else:
            baski = kitaplar[0][4]
            baski+=1
            sorgu2 = "Update kitaplar set baski = ? where isim = ?"
            self.cursor.execute(sorgu2,(baski,isim))
            self.baglanti.commit()


