# Lab, Bölüm 2: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest test_bolum2.py test_hatali_surumler.py -v

import pytest
# Eğer kendi dosyanda hazır bir import satırı varsa onu kullan, yoksa buradaki yorumu kaldırabilirsin:
from bolum2 import sifre_gucu, otopark_ucreti, yuzde_degisim


# 1. Şifre gücü
# - 0-7 karakter: "zayıf"
# - 8-11 karakter: "orta"
# - 12 ve daha fazla karakter: "güçlü"
# - Şifre boşsa ValueError fırlatır.

def test_sifre_gucu_zayif():
    assert sifre_gucu("123") == "zayıf"
    assert sifre_gucu("1234567") == "zayıf"  # Sınır değer (7 karakter)

def test_sifre_gucu_orta():
    assert sifre_gucu("12345678") == "orta"  # Alt sınır (8 karakter)
    assert sifre_gucu("12345678901") == "orta"  # Üst sınır (11 karakter)

def test_sifre_gucu_guclu():
    assert sifre_gucu("123456789012") == "güçlü"  # Alt sınır (12 karakter)
    assert sifre_gucu("cok_guclu_bir_sifre_123") == "güçlü"

def test_sifre_gucu_bos_hata():
    with pytest.raises(ValueError):
        sifre_gucu("")


# 2. Otopark ücreti
# - 0-15 dakika: 0 TL
# - 16-60 dakika: 20 TL
# - 61-180 dakika: 40 TL
# - 180 dakikadan fazla: 60 TL
# - Dakika negatifse ValueError fırlatır.    

def test_otopark_ucreti_ucretsiz():
    assert otopark_ucreti(0) == 0
    assert otopark_ucreti(10) == 0
    assert otopark_ucreti(15) == 0  # Sınır değer

def test_otopark_ucreti_kisa_sure():
    assert otopark_ucreti(16) == 20  # Alt sınır
    assert otopark_ucreti(45) == 20
    assert otopark_ucreti(60) == 20  # Üst sınır

def test_otopark_ucreti_orta_sure():
    assert otopark_ucreti(61) == 40  # Alt sınır
    assert otopark_ucreti(120) == 40
    assert otopark_ucreti(180) == 40  # Üst sınır

def test_otopark_ucreti_uzun_sure():
    assert otopark_ucreti(181) == 60  # Alt sınır
    assert otopark_ucreti(300) == 60

def test_otopark_ucreti_negatif_hata():
    with pytest.raises(ValueError):
        otopark_ucreti(-1)
    with pytest.raises(ValueError):
        otopark_ucreti(-50)


# 3. Yüzde değişim
# - Eski değerden yeni değere yüzde kaç değişim olduğunu döndürür: (yeni - eski) / eski × 100
#   Örnek: 200'den 250'ye %25 artış -> 25.0, 200'den 150'ye %25 azalış -> -25.0
# - Eski değer 0 ise ValueError fırlatır.

def test_yuzde_degisim_artis():
    assert yuzde_degisim(200, 250) == 25.0
    assert yuzde_degisim(100, 150) == 50.0

def test_yuzde_degisim_azalis():
    assert yuzde_degisim(200, 150) == -25.0
    assert yuzde_degisim(100, 50) == -50.0

def test_yuzde_degisim_sabit():
    assert yuzde_degisim(100, 100) == 0.0

def test_yuzde_degisim_eski_sifir_hata():
    with pytest.raises(ValueError):
        yuzde_degisim(0, 100)