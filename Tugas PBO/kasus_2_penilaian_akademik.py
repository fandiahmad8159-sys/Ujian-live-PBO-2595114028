class PenilaianMahasiswa:
    def __init__(self, nim, nama, tugas, uts, uas):
        self.nim = nim
        self.nama = nama
        self.tugas = tugas
        self.uts = uts
        self.uas = uas

    def hitung_akhir(self):
        return (self.tugas * 0.3) + (self.uts * 0.4) + (self.uas * 0.4)

    def tentukan_grade(self):
        nilai = self.hitung_akhir()
        if nilai >= 90 :
            return "A"
        elif nilai >= 80 :
            return "B" 
        elif nilai >= 68 :
            return "C" 
        elif nilai >= 52 :
            return "E" 

    def tentukan_status(self):  
        if self.hitung_akhir() >= 68 :
            return "LULUS"
        return "TIDAK LULUS"    

    def cetak_hasil(self):
        akhir = self.hitung_akhir()
        grade = self.tentukan_grade()
        status = self.tentukan_status()

        print("=== HASIL AKADEMIK ===")
        print(f"NIM          :{self.nim}")
        print(f"nama         :{self.nama}")
        print(f"nilai akhir  :{grade}")
        print(f"grade        :{status}")
        print("=====================") 

def input_nilai(tesk):
        while True: 
            try:
                nilai = float(input(tesk))  
                if 0 <= nilai <= 100:
                    return nilai 
                print("nilai hanya boleh 0 sampai 100!") 
            except ValueError:
                print("input harus berupa angka!")

def main():
        print("=== SISTEM PENILAIAN ===") 
        nim =input("nim       : ")  
        nama =input("nama     : ")
        tugas = input_nilai("nilai tugas : ")
        uts = input_nilai("nilai uts : ") 
        uas = input_nilai("nilai uas : ") 

        mahasiswa = PenilaianMahasiswa(nim, nama, tugas, uts, uas) 
        mahasiswa.cetak_hasil()

if __name__=="__main__" :
        main()        



