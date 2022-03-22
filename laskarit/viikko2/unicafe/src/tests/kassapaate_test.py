
import unittest
from kassapaate import Kassapaate

class TestKassapaate(unittest.TestCase):
    def setUp(self):
        self.kassapaate = Kassapaate()
        self.edullinen = 240
        self.maukas = 400

    # Test initial state
    def test_rahamaara_alussa(self):
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000)

    def test_myydyt_edulliset_alussa(self):
        self.assertEqual(self.kassapaate.edulliset, 0)

    def test_myydyt_maukkaat_alussa(self):
        self.assertEqual(self.kassapaate.maukkaat, 0)

    # Test cash transactions
    def test_edullinen_kateismaksu_kasvattaa_rahamaaraa(self):
        self.kassapaate.syo_edullisesti_kateisella(maksu=300)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+self.edullinen)

    def test_edullinen_kateismaksu_vaihtorahan_maara(self):
        maksu = 300
        vaihtoraha = self.kassapaate.syo_edullisesti_kateisella(maksu=maksu)
        self.assertEqual(vaihtoraha, maksu-self.edullinen)

    def test_maukas_kateismaksu_kasvattaa_rahamaaraa(self):
        self.kassapaate.syo_maukkaasti_kateisella(maksu=600)
        self.assertEqual(self.kassapaate.kassassa_rahaa, 100000+self.maukas)

    def test_maukas_kateismaksu_vaihtorahan_maara(self):
        maksu = 600
        vaihtoraha = self.kassapaate.syo_maukkaasti_kateisella(maksu=maksu)
        self.assertEqual(vaihtoraha, maksu-self.maukas)

