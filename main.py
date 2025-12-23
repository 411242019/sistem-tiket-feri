# main.py
"""
Program utama Sistem Manajemen Tiket Feri
"""

from jadwal import tampilkan_jadwal
from tiket import pesan_tiket, batalkan_tiket, tampilkan_tiket

def menu():
    print("""
=== Sistem Manajemen Tiket Feri ===
1. Tampilkan Jadwal Feri
2. Pesan Tiket
3. Batalkan Tiket
4. Lihat Daftar Tiket
5. Keluar
""")

def main():
    while True:
        menu()
        pilihan = input("Pilih menu (1-5): ")

        if pilihan == "1":
            tampilkan_jadwal()
        elif pilihan == "2":
            pesan_tiket()
        elif pilihan == "3":
            batalkan_tiket()
        elif pilihan == "4":
            tampilkan_tiket()
        elif pilihan == "5":
            print("Terima kasih telah menggunakan sistem.")
            break
        else:
            print("Pilihan tidak valid!")

if __name__ == "__main__":
    main()
