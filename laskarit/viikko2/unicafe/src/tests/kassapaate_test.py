import unittest
from kassapaate import Kassapaate
from maksukortti import Maksukortti

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.maksukortti_10e = Maksukortti(1000)
        self.maksukortti_2e = Maksukortti(200)
        self.edullinen = 240
        self.maukas = 400

    # Test initial state
    def test_rahamaara_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myydyt_edulliset_alussa(self):
        #self.assertEqual(self.kassapaate.edulliset, 0) # test for non-refactored code
        self.assertEqual(self.kassapaate.tuotteet["maukas"]["ostettu"], 0)

    def test_myydyt_maukkaat_alussa(self):
        #self.assertEqual(self.kassapaate.maukkaat, 0) # test for non-refactored code
        self.assertEqual(self.kassapaate.tuotteet["maukas"]["ostettu"], 0)

    # Test cash transactions
    def test_edullinen_kateismaksu_kasvattaa_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(maksu=300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+self.edullinen)

    def test_maukas_kateismaksu_kasvattaa_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(maksu=600)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+self.maukas)

    def test_edullinen_kateismaksu_vaihtorahan_maara(self):
        maksu = 300
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(maksu=maksu)
        self.assertEqual(vaihtoraha, maksu-self.edullinen)

    def test_maukas_kateismaksu_vaihtorahan_maara(self):
        maksu = 600
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(maksu=maksu)
        self.assertEqual(vaihtoraha, maksu-self.maukas)

    def test_edullinen_kateismaksu_lounaiden_maara_kasvaa(self):
        for _ in range(3):
            self.kassapaate.syo_edullisesti_kateisella(maksu=self.edullinen)
        #self.assertEqual(self.kassapaate.edulliset, 3) # test for non-refactored code
        self.assertEqual(self.kassapaate.tuotteet["edullinen"]["ostettu"], 3)

    def test_maukas_kateismaksu_lounaiden_maara_kasvaa(self):
        for _ in range(10):
            self.kassapaate.syo_maukkaasti_kateisella(maksu=self.maukas)
        #self.assertEqual(self.kassapaate.maukkaat, 10) # test for non-refactored code
        self.assertEqual(self.kassapaate.tuotteet["maukas"]["ostettu"], 10)

    def test_liian_pieni_edullinen_kateismaksu_ei_kasvata_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(maksu=200)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_liian_pieni_maukas_kateismaksu_ei_kasvata_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(maksu=300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_liian_pieni_edullinen_kateismaksu_vaihtorahan_maara(self):
        maksu = 200
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(maksu=maksu)
        self.assertEqual(vaihtoraha, maksu)

    def test_liian_pieni_maukas_kateismaksu_vaihtorahan_maara(self):
        maksu = 300
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(maksu=maksu)
        self.assertEqual(vaihtoraha, maksu)

    def test_liian_pieni_edullinen_kateismaksu_ei_lisaa_myytyja(self):
        self.kassapaate.syo_edullisesti_kateisella(maksu=200)
        #self.assertEqual(self.kassapaate.edulliset, 0) # test for non-refactored code
        self.assertEqual(self.kassapaate.tuotteet["edullinen"]["ostettu"], 0)

    def test_liian_pieni_maukas_kateismaksu_ei_lisaa_myytyja(self):
        self.kassapaate.syo_maukkaasti_kateisella(maksu=300)
        #self.assertEqual(self.kassapaate.maukkaat, 0) # test for non-refactored code
        self.assertEqual(self.kassapaate.tuotteet["maukas"]["ostettu"], 0)

    # Test card transactions
    def test_edullinen_korttimaksu_vahentaa_saldoa(self):
        alku = self.maksukortti_10e.saldo
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_10e)
        self.assertEqual(self.maksukortti_10e.saldo, alku-self.edullinen)

    def test_maukas_korttimaksu_vahentaa_saldoa(self):
        alku = self.maksukortti_10e.saldo
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_10e)
        self.assertEqual(self.maksukortti_10e.saldo, alku-self.maukas)

    def test_edullinen_korttimaksu_palautusarvo(self):
        self.assertEqual(
            self.kassapaate.syo_edullisesti_kortilla(kortti=self.maksukortti_10e),
            True,
        )

    def test_maukas_korttimaksu_palautusarvo(self):
        self.assertEqual(
            self.kassapaate.syo_maukkaasti_kortilla(kortti=self.maksukortti_10e),
            True,
        )

    def test_edullinen_korttimaksu_lisaa_myytyja(self):
        self.kassapaate.syo_edullisesti_kortilla(kortti=self.maksukortti_10e)
        #self.assertEqual(self.kassapaate.edulliset, 1) # test for non-refactored code
        self.assertEqual(self.kassapaate.tuotteet["edullinen"]["ostettu"], 1)

    def test_maukas_korttimaksu_lisaa_myytyja(self):
        self.kassapaate.syo_maukkaasti_kortilla(kortti=self.maksukortti_10e)
        #self.assertEqual(self.kassapaate.maukkaat, 1) # test for non-refactored code
        self.assertEqual(self.kassapaate.tuotteet["maukas"]["ostettu"], 1)

    def test_liian_pieni_edullinen_korttimaksu_ei_vahenna_saldoa(self):
        self.kassapaate.syo_edullisesti_kortilla(self.maksukortti_2e)
        self.assertEqual(self.maksukortti_2e.saldo, 200)

    def test_liian_pieni_maukas_korttimaksu_ei_vahenna_saldoa(self):
        self.kassapaate.syo_maukkaasti_kortilla(self.maksukortti_2e)
        self.assertEqual(self.maksukortti_2e.saldo, 200)

    def test_liian_pieni_edullinen_korttimaksu_palautusarvo(self):
        self.assertEqual(
            self.kassapaate.syo_edullisesti_kortilla(kortti=self.maksukortti_2e),
            False,
        )

    def test_liian_pieni_maukas_korttimaksu_palautusarvo(self):
        self.assertEqual(
            self.kassapaate.syo_maukkaasti_kortilla(kortti=self.maksukortti_2e),
            False,
        )

    def test_liian_pieni_edullinen_korttimaksu_ei_lisaa_myytyja(self):
        self.kassapaate.syo_edullisesti_kortilla(kortti=self.maksukortti_2e)
        #self.assertEqual(self.kassapaate.edulliset, 0) # test for non-refactored code
        self.assertEqual(self.kassapaate.tuotteet["edullinen"]["ostettu"], 0)

    def test_liian_pieni_maukas_korttimaksu_ei_lisaa_myytyja(self):
        self.kassapaate.syo_maukkaasti_kortilla(kortti=self.maksukortti_2e)
        #self.assertEqual(self.kassapaate.maukkaat, 0) # test for non-refactored code
        self.assertEqual(self.kassapaate.tuotteet["maukas"]["ostettu"], 0)

    def test_korttimaksu_ei_lisaa_kassan_rahaa(self):
        alku = self.kassapaate.kassassa_rahaa
        self.kassapaate.syo_edullisesti_kortilla(kortti=self.maksukortti_10e)
        self.kassapaate.syo_maukkaasti_kortilla(kortti=self.maksukortti_10e)
        self.kassapaate.syo_edullisesti_kortilla(kortti=self.maksukortti_2e)
        self.kassapaate.syo_maukkaasti_kortilla(kortti=self.maksukortti_2e)
        self.assertEqual(self.kassapaate.kassassa_rahaa, alku)

    def test_rahan_lataus_kortille_kasvattaa_kortin_saldoa(self):
        alku = self.maksukortti_2e.saldo
        lisays = 800
        self.kassapaate.lataa_rahaa_kortille(
            kortti=self.maksukortti_2e,
            summa=lisays
        )
        self.assertEqual(self.maksukortti_2e.saldo, alku+lisays)

    def test_rahan_lataus_kortille_lisaa_kassaan_rahaa(self):
        alku = self.kassapaate.kassassa_rahaa
        lisays = 800
        self.kassapaate.lataa_rahaa_kortille(
            kortti=self.maksukortti_10e,
            summa=lisays
        )
        self.assertEqual(self.kassapaate.kassassa_rahaa, alku+lisays)

    def test_negatiivinen_lataus_kortille_ei_muuta_saldoa(self):
        alku = self.maksukortti_2e.saldo
        lisays = -100
        self.kassapaate.lataa_rahaa_kortille(
            kortti=self.maksukortti_2e,
            summa=lisays
        )
        self.assertEqual(self.maksukortti_2e.saldo, alku)

    def test_negatiivinen_lataus_kortille_ei_muuta_kassan_rahamaaraa(self):
        alku = self.kassapaate.kassassa_rahaa
        lisays = -500
        self.kassapaate.lataa_rahaa_kortille(
            kortti=self.maksukortti_10e,
            summa=lisays
        )
        self.assertEqual(self.kassapaate.kassassa_rahaa, alku)
