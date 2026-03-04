import abc
from abc import ABC, abstractmethod

daftar_barang = []
class Abstract(ABC):
    @abstractmethod
    def tampil_detail(stok, harga, nama):
        pass

    def hitung_total(pajak, harga ):
        pass


class InputBarang(Abstract):
    def __init__(self, nama, harga, stok):
       self.nama = nama
       self.is_valid = True
       if int(stok) < 0 or int(harga) < 0:
            print(f"Error: Input untuk '{nama}' ditolak karena harga/stok minus!")
            self.is_valid = False
            self.__stok = 0
            self.__harga = 0
       else:
            self.__stok = int(stok)
            self.__harga = int(harga)

    def tampil_detail(self):
        if not self.is_valid:
          return f'Nilai tidak boleh negatif'
        else:
          return f'Nama Barang : {self.nama}\nHarga Barang : {self.__harga}\nStok Barang : {self.__stok}'

    def get_stock(self):
        return self.__stok

    def set_stock(self, jumlah):
        if jumlah > 0:
            self.__harga == jumlah
        else:
            self.is_valid = False
            print('STOK TIDAK BOLEH NEGATIF!')
                
    def get_harga(self):
        return self.__harga

    def set_harga(self, harga):
        if harga > 0:
            self.__stok == harga
        else:
            self.is_valid = False
            print('STOK TIDAK BOLEH NEGATIF!')    
                
    def hitung_total(self, pajak, harga):
        self.pajak = pajak
        self.harga = harga






class Laptop(InputBarang):
    def __init__(self, nama, harga, stok, spek):
        super().__init__(nama, harga, stok)
        self.spek = spek
        if self.is_valid:
          barang = {
          'nama' : self.nama,
          'stok' : self.get_stock(),
          'harga' : self.get_harga(),
          'spek' : spek,
          'harga_after_pajak' : self.hitung_total()
        }
          daftar_barang.append(barang)
        

    def tampil_detail(self):
      if not self.is_valid:
          return f'Nilai tidak boleh negatif'
      else:
          return f'[LAPTOP]\n{super().tampil_detail()}\nSpek : {self.spek}'   
      

    def hitung_total(self, pajak = 0.10):
        hitung_pajak = self.get_harga() * pajak
        hitung_total = self.get_harga() - hitung_pajak
        
        if not self.is_valid:
            return
        else:
            return  int(hitung_total)
    
class Handphone(InputBarang):
    def __init__(self, nama, harga, stok, spek):
        super().__init__(nama, harga, stok)
        self.spek = spek
        barang = {
         'nama' : self.nama,
         'stok' : self.get_stock(),
         'harga' : self.get_harga(),
         'spek' : spek,
         'harga_after_pajak' : self.hitung_total()
        }
        daftar_barang.append(barang)

    def tampil_detail(self):
      if not self.is_valid:
          return f'Nilai tidak boleh negatif'
      else:
          return f'[HANDPHONE]\n{super().tampil_detail()}\nSpek : {self.spek}'   


    def hitung_total(self, pajak = 0.05):
        hitung_pajak = self.get_harga() * pajak
        hitung_total = self.get_harga() - hitung_pajak
        if not self.is_valid:
            return
        else:
            return int(hitung_total)


def transaksi(daftar_barang):
    print("\n" + "="*40)
    print(f"{'LAPORAN PEMBELIAN ITEM':^40}")
    print("="*40)
    
    total_seluruh_modal = 0
    
    if not daftar_barang:
        print("Tidak ada transaksi yang tercatat.")
        return
    for item in daftar_barang:
        qty =  int(input(f'masukkan banyak barang untuk {item['nama']}  : '))
        subtotal = item['harga_after_pajak'] * int(qty)
        total_seluruh_modal += subtotal
        
        print(f"Barang   : {item['nama']}")
        print(f"Detail   : {item['spek']}")
        print(f"Qty      : {qty}")
        print(f"Harga    : {item['harga']}")
        print(f"Harga setelah pajak    : {item['harga_after_pajak']}")
        print(f"Subtotal : {subtotal}")
        print("-" * 40)
        
    print(f"{'TOTAL TRANSAKSI':<25} : {total_seluruh_modal}")
    print("="*40)



    


macbook = Laptop('pro m5', 12000, 12, 'apple silicon') 
print(macbook.tampil_detail())  
print('\n')
iphone = Handphone('17 promag', 14000, 12, 'A18') 
print(iphone.tampil_detail())     


print(macbook.hitung_total())
print(iphone.hitung_total())

print(transaksi(daftar_barang))










