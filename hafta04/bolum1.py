
# Lab, Bölüm 1: Python. Bu dosyadaki fonksiyonları SİZ yazacaksınız.
#
# Testler test_bolum1.py dosyasında hazır; o dosyayı değiştirmeyin.
# Çalıştırmak için bu klasörde:  python -m pytest test_bolum1.py -v
#
# 1-4: `pass` satırını silip fonksiyonu yazın.
# 5-6: Fonksiyon yazılmış ama içinde bir hata var. Testleri çalıştırın, hatayı bulun ve düzeltin.

# 1. Vize-final sonucu
def vize_final_sonuc(vize, final):
    ortalama = vize * 0.4 + final * 0.6

    if ortalama >= 50 and final >= 50:
        return "Geçti"
    else:
        return "Kaldı"


# 2. Asal sayı mı?
def asal_mi(n):
    if n < 2:
        return False

    for i in range(2, n):
        if n % i == 0:
            return False

    return True


# 3. Palindrom mu?
def palindrom_mu(metin):
    metin = metin.lower()
    metin = metin.replace(" ", "")

    if metin == metin[::-1]:
        return True
    else:
        return False


# 4. En uzun kelime
def en_uzun_kelime(cumle):
    kelimeler = cumle.split()

    if len(kelimeler) == 0:
        return ""

    en_uzun = kelimeler[0]

    for kelime in kelimeler:
        if len(kelime) > len(en_uzun):
            en_uzun = kelime

    return en_uzun


# 5. En düşük not
def en_dusuk_not(notlar):
    if len(notlar) == 0:
        return None

    en_dusuk = notlar[0]

    for n in notlar:
        if n < en_dusuk:
            en_dusuk = n

    return en_dusuk


# 6. 1'den n'ye kadar toplam
def toplam(n):
    sonuc = 0

    for i in range(1, n + 1):
        sonuc = sonuc + i

    return sonuc