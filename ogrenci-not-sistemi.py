import time

ogrenciler = []

GECME_NOTU = 50

def not_hesapla(vize, final):
    return (vize * 0.4) + (final * 0.6)

def harf_notu_belirle(ortalama):
    if ortalama >= 90:
        return "AA"
    elif ortalama >= 85:
        return "BA"
    elif ortalama >= 70:
        return "BB"
    elif ortalama >= GECME_NOTU:
        return "CC"
    else:
        return "FF"
    
def ogrenci_ekle():
    print("\n--- Yeni Öğrenci Ekleme ---")
    ad = input("Öğrencinin Adı: ").capitalize()
    soyad = input("Öğrencinin Soyadı: ").upper()

    while True:
        try:
            vize = float(input(f"{ad} için Vize Notu (0-100): "))
            final = float(input(f"{ad} için Final Notu (0-100): "))

            if not (0 <= vize <= 100 and 0 <= final <= 100):
                print("Hata: Notlar 0 ile 100 arasında olmalıdır!")
                continue

            break
        except ValueError:
            print("Hata: Lütfen sayısal bir değer giriniz!")

    ort = not_hesapla(vize, final)
    durum = "Geçti" if ort >= GECME_NOTU else "Kaldı"
    harf = harf_notu_belirle(ort)

    yeni_ogrenci = {
        "ad_soyad" : f"{ad} {soyad}",
        "vize" : vize,
        "final" : final,
        "ortalama" : round(ort, 2),
        "harf" : harf,
        "durum" : durum
    }

    ogrenciler.append(yeni_ogrenci)
    print("✅ Öğrenci başarıyla kaydedildi!")
    time.sleep(1)

def listeyi_goster():
    print("\n" + "="*40)
    print(f"{'AD SOYAD':<20} {'ORT':<10} {'DURUM'}")
    print("-" * 40)

    if len(ogrenciler) == 0:
        print("Listede henüz kayıtlı öğrenci yok.")
    else:
        for ogrenci in ogrenciler:
            print(f"{ogrenci['ad_soyad']:<20} {ogrenci['ortalama']:<10} {ogrenci['durum']}")
    print("="*40 + "\n")

def main():
    print("🎓 Öğrenci Not Sistemi v1.0 Başlatılıyor...")

    while True:
        print("\n[1] Öğrenci Ekle")
        print("[2] Listeyi Göster")
        print("[3] Çıkış")

        secim = input("Seçiminiz (1/2/3): ")

        if secim == '1':
            ogrenci_ekle()
        elif secim == '2':
            listeyi_goster()
        elif secim == '3':
            print("Sistemden çıkılıyor. İyi günler!")
            break
        else:
            print("Geçersiz seçim, lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()

