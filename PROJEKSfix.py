import csv
import os
import time

nama_file = "TabelPeminjaman.csv"

def clearscreen():
    os.system('cls' if os.name == 'nt' else 'clear')

def menu_utama() :
    clearscreen()
    print("="*38)
    print("   Aplikasi Daftar Peminjaman Buku")
    print("="*38)
    print('''    | 1| Buat daftar baru [.csv]
    | 2| Tambah data
    | 3| Lihat data
    | 4| Hapus data
    | 5| Keluar ''')
    print("="*38)
    pilihan_menu = input(" Pilih tindakan : ")
    if(pilihan_menu == "1"):
        buat_data()
    elif(pilihan_menu == "2"):
        tambahkan()
    elif(pilihan_menu == "3"):
        tampil_data()
    elif(pilihan_menu == "4"):
        hapus()
    elif(pilihan_menu == "5"):
        exit()
    else:
        menu_utama()
    kembali()

def kembali():
    input("\n Press enter key to continue...")
    menu_utama()

def buat_data():
    clearscreen()
    with open(nama_file, 'w', newline='') as csv_file: 
        print(" File Berhasil Dibuat Dengan Nama 'TabelPeminjaman.csv' ")
    kembali()

def tambahkan():
    clearscreen()
    with open(nama_file, 'a', newline='') as csv_file:
        nama = input('Nama Peminjam : ') 
        judul = input('Judul Buku    : ') 
        nomorBuku = input('Nomor Buku    : ')
        tanggal = time.strftime('%d/%m/%Y',time.localtime())
        tanggalKembali = input("Tanggal Kembali\n(dd/mm/yyyy)  : ")
        data = [nama,judul,nomorBuku,tanggal,tanggalKembali]
        tulis = csv.writer(csv_file, delimiter=';')
        tulis.writerow(data)
    print("\n Data berhasil ditambahkan!")
    kembali()

def tampil_data():
    clearscreen()
    data = []
    with open(nama_file) as csv_file:
        read_data = csv.reader(csv_file, delimiter=";")
        for row in read_data:
            data.append(row)

    print ("="*122)
    print("No. \t Nama Peminjam\t\tJudul Buku\t\tNomor Buku\tTanggal Peminjaman\tTanggal Pengembalian")
    print ("="*122)
    number = 0
    for dt in data:
        number += 1
        print("{}.\t {}\t\t{}\t\t{}\t\t{}\t\t{}".format(number,dt[0],dt[1],dt[2],dt[3],dt[4]))
        print ("-"*122)                           
    kembali()

def hapus():
    clearscreen()
    data = []
    with open(nama_file) as csv_file:
        read_data = csv.reader(csv_file, delimiter=";")
        for row in read_data:
            data.append(row)
    print ("="*122)
    print("No. \t Nama Peminjam\t\tJudul Buku\t\tNomor Buku\tTanggal Peminjaman\tTanggal Pengembalian")
    print ("="*122)
    number = 0
    for dt in data:
        number += 1
        print("{}.\t {}\t\t{}\t\t{}\t\t{}\t\t{}".format(number,dt[0],dt[1],dt[2],dt[3],dt[4]))
        print ("-"*122)
    no = int(input('Data pada nomor berapa yang akan dihapus?  '))
    no -= 1
    konfirmasi = input('Apakah anda yakin ingin menghapus data tersebut? [y/t] ')
    if konfirmasi =='y':
        del data[no]
        with open(nama_file, 'w', newline='') as csv_file:
            tulis = csv.writer(csv_file, delimiter=';')
            for dt in data:
                data = [dt[0],dt[1],dt[2],dt[3],dt[4]]
                tulis.writerow(data)
            print("\n Data berhasil dihapus!")
        kembali()

if __name__== "__main__":
    while True:
        menu_utama()
