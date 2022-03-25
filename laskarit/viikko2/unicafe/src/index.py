from maksukortti import Maksukortti
from kassapaate import Kassapaate


def main():
    unicafe_exactum = Kassapaate()
    kortti = Maksukortti(10000)

    unicafe_exactum.syo_edullisesti_kateisella(maksu=250)
    unicafe_exactum.syo_edullisesti_kortilla(kortti)

    print(unicafe_exactum.tuotteet["edullinen"]["ostettu"])
    print(kortti)


if __name__ == "__main__":
    main()
