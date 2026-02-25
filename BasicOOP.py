


class Kucing:

    def __init__(self, nama, warna):
        self.nama = nama 
        self.warna = warna 
 
    def suara(self):
        return f"{self.nama} berkata: Meow!"
    
    



kucing1 = Kucing("Luna", "Putih")
kucing2 = Kucing("Garfield", "Oranye")

print(kucing1.nama) 
print(kucing2.suara()) 














