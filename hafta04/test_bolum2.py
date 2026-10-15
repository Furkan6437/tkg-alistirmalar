# Lab, Bölüm 2: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest test_bolum2.py test_hatali_surumler.py -v

import pytest

from bolum2 import sifre_gucu, otopark_ucreti, yuzde_degisim


# --- 1. Şifre Gücü Testleri ---
def test_kisa_sifre_zayif():
    assert sifre_gucu("abc") == "zayıf"
    assert sifre_gucu("1234567") == "zayıf"  # Sınır değer: 7

def test_orta_sifre():
    assert sifre_gucu("12345678") == "orta"  # Alt sınır: 8
    assert sifre_gucu("12345678901") == "orta"  # Üst sınır: 11

def test_guclu_sifre():
    assert sifre_gucu("123456789012") == "güçlü"  # Alt sınır: 12
    assert sifre_gucu("cok_guclu_bir_sifre") == "güçlü"

def test_sifre_bos_hata():
    with pytest.raises(ValueError):
        sifre_gucu("")


# --- 2. Otopark Ücreti Testleri ---
def test_otopark_ucretsiz():
    assert otopark_ucreti(0) == 0
    assert otopark_ucreti(15) == 0  # Üst sınır: 15

def test_otopark_20_tl():
    assert otopark_ucreti(16) == 20  # Alt sınır: 16
    assert otopark_ucreti(60) == 20  # Üst sınır: 60

def test_otopark_40_tl():
    assert otopark_ucreti(61) == 40  # Alt sınır: 61
    assert otopark_ucreti(180) == 40  # Üst sınır: 180

def test_otopark_60_tl():
    assert otopark_ucreti(181) == 60  # Alt sınır: 181
    assert otopark_ucreti(300) == 60

def test_otopark_negatif_hata():
    with pytest.raises(ValueError):
        otopark_ucreti(-1)


# --- 3. Yüzde Değişim Testleri ---
def test_yuzde_degisim_artis():
    assert yuzde_degisim(200, 250) == 25.0
    assert yuzde_degisim(100, 150) == 50.0

def test_yuzde_degisim_azalis():
    assert yuzde_degisim(200, 150) == -25.0
    assert yuzde_degisim(100, 50) == -50.0

def test_yuzde_degisim_sabit():
    assert yuzde_degisim(100, 100) == 0.0

def test_yuzde_degisim_sifir_hata():
    with pytest.raises(ValueError):
        yuzde_degisim(0, 100)