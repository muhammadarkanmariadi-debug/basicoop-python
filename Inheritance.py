class Hewan:
    def makan(self):
        print("Hewan ini sedang makan.")

class Burung(Hewan):
    def terbang(self):
        print("Burung sedang terbang.")


beo = Burung()
beo.makan()
beo.terbang()
