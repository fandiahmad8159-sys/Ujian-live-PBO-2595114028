class TransaksiKasir:
    def __init__(self, seng_tuku, barange, regone, jumlahe):
        self.seng_tuku = seng_tuku 
        self.barange = barange
        self.regone = regone
        self.jumlahe = jumlahe

    def hitung_subtotal(self):
        return self.regone * self.jumlahe

    def tentukan_diskon(self):
        subtotal = self.hitung_subtotal()
        if subtotal >= 500000:
            return 15
        elif subtotal >= 250000:
            return 10
        elif subtotal >= 100000:
            return 5
        return 0 
    
    def cetak_struk(self):
        subtotal = self.hitung_subtotal()
        persen = self.tentukan_diskon()
        potongan = int(subtotal * (persen / 100))
        total = subtotal - potongan 

        print("\n=== STRUK PEMBAYARAN ===")
        print(f"seng_tuku  : {self.seng_tuku}")
        print(f"barange    :{self.barange} ")
        print(f"subtotal   :Rp{subtotal:,}".replace(',', '.'))
        print(f"diskon     : {persen}%")
        print(f"potongan   :Rp {potongan:,}".replace(',', '.'))
        print(f"total bayar:Rp{total:,}".replace(',', '.'))
        print("=======================")

def main():
    print("=== KASIR MINIMARKET ===") 
    seng_tuku = input(" jenenge_seng_tuku : ")  
    barange  = input("jenenge_barange  : ") 
    

    while True:
        try: 
            regone = int(input("regone_barange : "))
            if regone > 0:
                break
            print("hargane harus bernilai positif")
        except ValueError:
            print("input harus berupa angka !") 

    while True:
        try: 
            jumlahe = int(input("jumlah_barange : "))  
            if jumlahe > 0:
                break 
            print("jumlah harus bernilai positif!")
        except ValueError:
                print("input harus berupa angaka!")       

    transaksi = TransaksiKasir(seng_tuku, barange, regone, jumlahe) 
    transaksi.cetak_struk()    

if __name__ == "__main__":
    main()
    



    




    
    
    