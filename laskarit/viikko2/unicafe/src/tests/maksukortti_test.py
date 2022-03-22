import unittest
from maksukortti import Maksukortti

class TestMaksukortti(unittest.TestCase):
    def setUp(self):
        self.maksukortti = Maksukortti(1000)

    def test_luotu_kortti_on_olemassa(self):
        self.assertNotEqual(self.maksukortti, None)

    def test_kortin_saldo_alussa_oikein(self):
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_rahan_lataaminen_kasvattaa_saldoa(self):
        self.maksukortti.lataa_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 15.0")

    def test_saldo_vahenee_oikein_kun_rahaa_tarpeeksi(self):
        self.maksukortti.ota_rahaa(500)
        self.assertEqual(str(self.maksukortti), "saldo: 5.0")

    def test_saldo_ei_vahene_kun_rahaa_ei_tarpeeksi(self):
        self.maksukortti.ota_rahaa(5000)
        self.assertEqual(str(self.maksukortti), "saldo: 10.0")

    def test_rahan_ottaminen_palauttaa_oikean_arvon_kun_nosto_onnistuu(self):
        self.assertEqual(self.maksukortti.ota_rahaa(500), True)

    def test_rahan_ottaminen_palauttaa_oikean_arvon_kun_nosto_ei_onnistu(self):
        self.assertEqual(self.maksukortti.ota_rahaa(5000), False)
