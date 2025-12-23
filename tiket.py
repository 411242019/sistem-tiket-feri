# tiket.py
"""
Modul tiket
Mengelola pemesanan dan pembatalan tiket feri
"""

from utils import input_tidak_kosong, validasi_tanggal

daftar_tiket = []

def pesan_tiket():
    """
    Memesan tiket feri
    """
    print("\n=== Pemesanan Tiket ===")
    nama = input_tidak_kosong("Nama Penumpang: ")
    tujuan = input_tidak_kosong("Tujuan: ")

    while True:
        tanggal = input("Tanggal (DD-MM-YYYY): ")
        if validasi_tanggal(tanggal):
            break
        print("Format tanggal salah!")

    tiket = {
        "nama": nama,
        "tujuan": tujuan,
        "tanggal": tanggal
    }
    daftar_tiket.append(tiket)
    print("✅ Tiket berhasil dipesan!")

def batalkan_tiket():
    """
    Membatalkan tiket berdasarkan nama penumpang
    """
    print("\n=== Pembatalan Tiket ===")
    nama = input("Masukkan nama penumpang: ")

    for tiket in daftar_tiket:
        if tiket["nama"].lower() == nama.lower():
            daftar_tiket.remove(tiket)
            print("❌ Tiket berhasil dibatalkan!")
            return

    print("⚠️ Tiket tidak ditemukan.")

def tampilkan_tiket():
    """
    Menampilkan semua tiket yang telah dipesan
    """
    print("\n=== Daftar Tiket ===")
    if not daftar_tiket:
        print("Belum ada tiket.")
        return

    for i, tiket in enumerate(daftar_tiket, start=1):
        print(f"{i}. {tiket['nama']} | {tiket['tujuan']} | {tiket['tanggal']}")
