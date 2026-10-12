import pytest
from alistirma import kargo_ucreti, bilet_fiyati, ortalama

# --- Kargo Ücreti Testleri ---
def test_kargo_buyuk_sipariste_ucretsiz():
    assert kargo_ucreti(800) == 0

def test_kargo_tam_sinir():
    #  >= 500 yerine > 500 yazılmış olabilir tam 500 ü deniyoruz
    assert kargo_ucreti(500) == 0

def test_kargo_sifir_tutar():
    # 0 TL lik siparişte < 0 ile <= 0 sıkıntısını önlemek için
    assert kargo_ucreti(0) == 50

def test_kargo_negatif_deger_hata_firlatmali():
    with pytest.raises(ValueError):
        kargo_ucreti(-10)


# --- Müze Bileti Testleri ---
def test_bilet_alti_yas_siniri():
    # 6 yaş ücretsiz sınırı
    assert bilet_fiyati(6) == 0

def test_bilet_onsekiz_yas_siniri():
    # Bilet alt yaşı 18 olmalı
    assert bilet_fiyati(18) == 100

def test_bilet_atmisbes_yas_siniri():
    # 65 yaş indirimi sınırı
    assert bilet_fiyati(65) == 60

def test_bilet_negatif_hata_firlatmali():
    with pytest.raises(ValueError):
        bilet_fiyati(-5)


# --- Not Ortalaması Testleri ---
def test_ortalama_kusuratli_sonuc():
    # tam sayı hatasını yakalıyor mu
    assert ortalama([70, 85]) == 77.5

def test_ortalama_bos_liste_hata_firlatmali():
    # boş listede 0 veriyormu yoksa istediğimiz hatayı veriyor mu
    with pytest.raises(ValueError):
        ortalama([])