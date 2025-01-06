class Mahasiswa:
    def __init__(self, nama, nim):
        self.nama = nama
        self.nim = nim
        self.spp_terbayar = False
        self.mata_kuliah = []
        self.nilai_akhir = {}

    def bayar_spp(self):
        print(f"{self.nama} sedang membayar SPP...")
        self.spp_terbayar = True
        print("SPP berhasil dibayar!")

    def daftar_mata_kuliah(self, daftar_mk):
        if not self.spp_terbayar:
            print("SPP belum dibayar! Silakan bayar SPP terlebih dahulu.")
            return
        print(f"{self.nama} sedang mendaftar mata kuliah...")
        self.mata_kuliah.extend(daftar_mk)
        print("Mata kuliah berhasil didaftarkan:", ", ".join(self.mata_kuliah))

    def ikuti_perkuliahan(self):
        if not self.mata_kuliah:
            print("Belum ada mata kuliah yang didaftarkan!")
            return
        print(f"{self.nama} sedang mengikuti perkuliahan...")
        for mk in self.mata_kuliah:
            print(f"- Mengikuti perkuliahan {mk}")

    def kerjakan_tugas_dan_ujian(self):
        if not self.mata_kuliah:
            print("Tidak ada mata kuliah untuk dikerjakan tugas dan ujian!")
            return
        print(f"{self.nama} sedang mengerjakan tugas dan ujian...")
        for mk in self.mata_kuliah:
            self.nilai_akhir[mk] = round(50 + 50 * random.random(), 2)  # Simulasi nilai

    def lihat_nilai_akhir(self):
        if not self.nilai_akhir:
            print("Nilai akhir belum tersedia!")
            return
        print(f"Nilai akhir {self.nama}:")
        for mk, nilai in self.nilai_akhir.items():
            print(f"- {mk}: {nilai}")

import random

def main():
    # Buat objek mahasiswa
    mahasiswa = Mahasiswa("Anisa", "12345678")

    # Tahapan proses kuliah
    mahasiswa.bayar_spp()
    mahasiswa.daftar_mata_kuliah(["Algoritma dan Pemrograman", "Struktur Data", "Basis Data"])
    mahasiswa.ikuti_perkuliahan()
    mahasiswa.kerjakan_tugas_dan_ujian()
    mahasiswa.lihat_nilai_akhir()

if __name__ == "__main__":
    main()
