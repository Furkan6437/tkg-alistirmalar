import pytest

from alistirma import indirim_orani, sepet_toplami, en_pahali_urun


def test_sepet_toplami():
    sepet = [
        {"urun": "çay", "fiyat": 20, "adet": 2},
        {"urun": "simit", "fiyat": 15, "adet": 3},
        {"urun": "tost", "fiyat": 60, "adet": 1},
    ]
    assert sepet_toplami(sepet) == 145


# --- Öğrencinin eklediği testler ---

# 1. indirim_orani testleri
def test_indirim_orani_0_arasi():
    assert indirim_orani(50) == 0

def test_indirim_orani_100_arasi():
    assert indirim_orani(100) == 5
    assert indirim_orani(300) == 5

def test_indirim_orani_500_arasi():
    assert indirim_orani(500) == 10
    assert indirim_orani(800) == 10

def test_indirim_orani_1000_uzeri():
    assert indirim_orani(1000) == 15
    assert indirim_orani(1500) == 15

def test_indirim_orani_negatif():
    with pytest.raises(ValueError):
        indirim_orani(-5)


# 2. sepet_toplami testleri
def test_bos_sepet_toplami():
    sepet = []
    assert sepet_toplami(sepet) == 0

def test_sepet_adet_sifir_hata():
    sepet = [
        {"urun": "su", "fiyat": 10, "adet": 0}
    ]
    with pytest.raises(ValueError):
        sepet_toplami(sepet)


# 3. en_pahali_urun testleri
def test_en_pahali_urun_bulma():
    sepet = [
        {"urun": "su", "fiyat": 10, "adet": 2},
        {"urun": "et", "fiyat": 250, "adet": 1},
        {"urun": "kola", "fiyat": 35, "adet": 1}
    ]
    assert en_pahali_urun(sepet) == "et"

def test_en_pahali_urun_bos_sepet():
    sepet = []
    assert en_pahali_urun(sepet) is None

def test_en_pahali_urun_ayni_fiyat_ilk_gelen():
    sepet = [
        {"urun": "elma", "fiyat": 50, "adet": 1},
        {"urun": "armut", "fiyat": 50, "adet": 1}
    ]
    # Aynı fiyatta ilk olanı (elma) döndürmeli
    assert en_pahali_urun(sepet) == "elma"