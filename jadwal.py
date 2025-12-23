# jadwal.py
"""
Modul jadwal
Menyediakan fungsi untuk menampilkan jadwal keberangkatan feri
"""

jadwal_feri = [
    {"tujuan": "Batam", "jam": "08:00"},
    {"tujuan": "Tanjung Pinang", "jam": "10:00"},
    {"tujuan": "Karimun", "jam": "13:00"},
    {"tujuan": "Batam", "jam": "16:00"}
]

def tampilkan_jadwal():
    """
    Menampilkan daftar jadwal keberangkatan feri
    """
    print("\n=== Jadwal Keberangkatan Feri ===")
    for i, jadwal in enumerate(jadwal_feri, start=1):
        print(f"{i}. Tujuan: {jadwal['tujuan']} | Jam: {jadwal['jam']}")
