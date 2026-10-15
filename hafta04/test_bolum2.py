# Lab, Bölüm 2: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest test_bolum2.py test_hatali_surumler.py -v

import pytest

from bolum2 import sifre_gucu, otopark_ucreti, yuzde_degisim


def test_kisa_sifre_zayif():
    assert sifre_gucu("abc") == "zayıf"
    assert sifre_gucu("12345") == "zayıf"

def test_orta_sifre():
    assert sifre_gucu("abcdefgh") == "orta"
    assert sifre_gucu("1234567890") == "orta"

def test_guclu_sifre():
    assert sifre_gucu("abcdefghijkl") == "güçlü"
    assert sifre_gucu("123456789012345") == "güçlü"

def test_sifre_sinir():
    assert sifre_gucu("1234567") == "zayıf"
    assert sifre_gucu("12345678") == "orta"
    assert sifre_gucu("123456789012") == "güçlü"

def test_bos_sifre_hata():
    with pytest.raises(ValueError):
        sifre_gucu("")


def test_otopark_ucreti():
    assert otopark_ucreti(0) == 0
    assert otopark_ucreti(10) == 0
    assert otopark_ucreti(15) == 0
    assert otopark_ucreti(16) == 20
    assert otopark_ucreti(60) == 20
    assert otopark_ucreti(61) == 40
    assert otopark_ucreti(180) == 40
    assert otopark_ucreti(181) == 60


def test_otopark_ucreti_negatif_hata():
    with pytest.raises(ValueError):
        otopark_ucreti(-5)


def test_yuzde_degisim():
    assert yuzde_degisim(200, 250) == 25.0
    assert yuzde_degisim(200, 150) == -25.0
    assert yuzde_degisim(100, 100) == 0.0

def test_yuzde_degisim_eski_sifir():
    with pytest.raises(ValueError):
        yuzde_degisim(0, 100)