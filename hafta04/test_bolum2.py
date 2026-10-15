# Lab, Bölüm 2: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest test_bolum2.py test_hatali_surumler.py -v

import pytest

from bolum2 import sifre_gucu, otopark_ucreti, yuzde_degisim


# Şifre gücü testleri

def test_kisa_sifre_zayif():
    assert sifre_gucu("abc") == "zayıf"


def test_orta_uzunlukta_sifre():
    assert sifre_gucu("abc12345") == "orta"


def test_guclu_sifre():
    assert sifre_gucu("Abc123!xyz") == "güçlü"


# Otopark ücreti testleri

def test_otopark_ucreti_sifir_saat():
    assert otopark_ucreti(0) == 0


def test_otopark_ucreti_bir_saat():
    assert otopark_ucreti(1) > 0


def test_otopark_ucreti_fazla_saat():
    assert otopark_ucreti(5) > otopark_ucreti(2)


# Yüzde değişim testleri

def test_yuzde_degisim_artis():
    assert yuzde_degisim(100, 150) == 50


def test_yuzde_degisim_azalis():
    assert yuzde_degisim(100, 80) == -20


def test_yuzde_degisim_degisiklik_yok():
    assert yuzde_degisim(100, 100) == 0