# Lab, Bölüm 2: Testleri bu dosyaya SİZ yazacaksınız.
#
# Aşağıda örnek olarak bir test var. Yanına her fonksiyon için kendi testlerinizi ekleyin.
# Çalıştırmak için bu klasörde:  python -m pytest test_bolum2.py test_hatali_surumler.py -v
import pytest

from bolum2 import sifre_gucu, otopark_ucreti, yuzde_degisim

# 1. Şifre gücü
# - 0-7 karakter: "zayıf"
# - 8-11 karakter: "orta"
# - 12 ve daha fazla karakter: "güçlü"
# - Şifre boşsa ValueError fırlatır.
def test_kisa_sifre_zayif():
    assert sifre_gucu("abc") == "zayıf"
    assert sifre_gucu("1234567") == "zayıf"
    assert sifre_gucu("12345678") == "orta"
    assert sifre_gucu("123456789012") == "güçlü"
    assert sifre_gucu("12345678901234567890") == "güçlü"
    assert sifre_gucu("abcdefgh") == "orta"
    assert sifre_gucu("abcdefghijk") == "orta"
    assert sifre_gucu("abcdefghijkl") == "güçlü"
    with pytest.raises(ValueError):
        sifre_gucu("")


    
# 2. Otopark ücreti
# - 0-15 dakika: 0 TL
# - 16-60 dakika: 20 TL
# - 61-180 dakika: 40 TL
# - 180 dakikadan fazla: 60 TL
# - Dakika negatifse ValueError fırlatır.    
def test_otopark_ucreti():
    assert otopark_ucreti(60) == 20
    assert otopark_ucreti(120) == 40
    assert otopark_ucreti(181) == 60
    assert otopark_ucreti(15) == 0
    assert otopark_ucreti(180) == 40
    with pytest.raises(ValueError):
        otopark_ucreti(-1)

# 3. Yüzde değişim
# - Eski değerden yeni değere yüzde kaç değişim olduğunu döndürür: (yeni - eski) / eski × 100
#   Örnek: 200'den 250'ye %25 artış -> 25.0, 200'den 150'ye %25 azalış -> -25.0
# - Eski değer 0 ise ValueError fırlatır.
def test_yuzde_degisim():
    assert yuzde_degisim(100, 150) == 50.0
    assert yuzde_degisim(100, 50) == -50.0
    assert yuzde_degisim(200, 250) == 25.0
    assert yuzde_degisim(200, 150) == -25.0
    assert yuzde_degisim(100, 100) == 0.0
    assert yuzde_degisim(50, 75) == 50.0
    with pytest.raises(ValueError):
        yuzde_degisim(0, 25)