class Anjing:
     def suara(self):
        return "Guk Guk!"
class Kucing:
    def suara(self):
        return "Meow!"

def tes_suara(hewan):
 print(hewan.suara())
hewan1 = Anjing()
hewan2 = Kucing()
tes_suara(hewan1) 
tes_suara(hewan2)