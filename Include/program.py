from rich.table import Table
from rich.panel import Panel
from rich.traceback import install
from rich import print
install()

from keyboard import record

# from time import sleep
from os import system

from konek import tambah, hapus, pilih

# membuat sebuah fungsi untuk mengupdate tabel di database ke tabel program
def perbarui_tabel():
    # Membuat tabel untuk program
    tabel = Table()

    header, data = pilih() # mengambil kepala dan data dari tabel database

    # membuat header tabel sesuai dengan banyak header di tabel database
    for kepala_tabel in header:
        tabel.add_column(str(kepala_tabel))

    # membuat badan tabel sesuai dengan banyak data di tabel database
    for badan_tabel in data:
        tabel.add_row(str(badan_tabel[0]), str(badan_tabel[1]), str(badan_tabel[2]))
        tabel.add_section()
    
    return tabel

def grafik_tambah_record():
    while True:
        system('cls')
        print(perbarui_tabel())

        no = input("\nNo Barang: ")
        nama = input("Nama Barang: ")
        stok = input("Stok Barang: ")

        jwban1 = str(input("Yakin ? (y/n/batal)"))
        
        if jwban1 == 'y':n = tambah(no, nama, stok)
        elif jwban1 == 'batal':break
        else:continue

        if n == 1:
            print("\nRecord Berhasil Ditambahkan!")

        jwban = str(input("Tambah data lagi? (y/n)"))
        if jwban == 'y':
            continue
        else:
            break

def grafik_hapus_record():
    while True:
        system('cls')
        print(perbarui_tabel())

        no = int(input("\nNo Barang Yang Ingin Di Hapus: "))

        jwban1 = str(input("Yakin ? (y/n/batal)"))
        
        if jwban1 == 'y':n = hapus(no)
        elif jwban1 == 'batal':break
        else:continue

        if n == 1:
            print("\nRecord Berhasil Dihapus!")

        jwban = str(input("Hapus data lagi? (y/n)"))
        if jwban == 'y':
            continue
        else:
            break
    

# Fungsi menjalankan program
def main():
    i = 0
    while True:
        system('cls')

        print(perbarui_tabel())
        print(Panel.fit("[T] Tambah Record\n[H] Hapus Record\n[Q] Keluar"))

        x = record('enter')

        if x[-2].name == 't':
            input()
            grafik_tambah_record()
        elif x[-2].name == 'h':
            input()
            grafik_hapus_record()
        if x[-2].name == 'q':
            input()
            system('cls')
            break

if __name__ == "__main__":
    main()
    # print([x.name for x in record(until='enter')])