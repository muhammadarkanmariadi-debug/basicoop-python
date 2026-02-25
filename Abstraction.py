import abc
from abc import ABC, abstractmethod

class Kendaraan(ABC): 
 @abstractmethod
 def bergerak(self):
    pass
class Mobil(Kendaraan):
 def bergerak(self):
    print("Berjalan dengan roda")
class Kapal(Kendaraan):
 def bergerak(self):
    print("Berlayar di air")

m = Mobil()
m.bergerak() 