class AkunBank:
     def __init__(self, saldo):
        self.__saldo = saldo 
     def cek_saldo(self):
        return self.__saldo
     def setor(self, jumlah):
        if jumlah > 0:
            self.__saldo += jumlah


rekening = AkunBank(1000)
rekening.setor(500)
print(rekening.cek_saldo())