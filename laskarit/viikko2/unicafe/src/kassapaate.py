class Kassapaate:
    def __init__(self):
        self.kassassa_rahaa = 100000
        # Save information of products into a dict
        self.tuotteet = {
            "edullinen": {"hinta": 240, "ostettu": 0},
            "maukas": {"hinta": 400, "ostettu": 0},
        }

    def _kateismaksu(self, tuote: str, maksu: int):
        hinta = self.tuotteet[tuote]["hinta"]
        if maksu < hinta:
            return maksu
        self.kassassa_rahaa += hinta
        self.tuotteet[tuote]["ostettu"] += 1
        return maksu - hinta
            
    def _korttimaksu(self, tuote: str, kortti):
        hinta = self.tuotteet[tuote]["hinta"]
        if kortti.saldo < hinta:
            return False
        kortti.ota_rahaa(hinta)
        self.tuotteet[tuote]["ostettu"] += 1
        return True

    def syo_edullisesti_kateisella(self, maksu):
        return self._kateismaksu(tuote="edullinen", maksu=maksu)

    def syo_maukkaasti_kateisella(self, maksu):
        return self._kateismaksu(tuote="maukas", maksu=maksu)

    def syo_edullisesti_kortilla(self, kortti):
        return self._korttimaksu(tuote="edullinen", kortti=kortti)

    def syo_maukkaasti_kortilla(self, kortti):
        return self._korttimaksu(tuote="maukas", kortti=kortti)

    def lataa_rahaa_kortille(self, kortti, summa):
        if summa <= 0:
            return
        kortti.lataa_rahaa(summa)
        self.kassassa_rahaa += summa
