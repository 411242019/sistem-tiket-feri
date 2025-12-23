# utils.py
"""
Modul utils
Berisi fungsi pendukung seperti validasi input
"""

def input_tidak_kosong(pesan):
    """
    Memastikan input tidak kosong
    """
    while True:
        data = input(pesan).strip()
        if data:
            return data
        print("Input tidak boleh kosong!")

def validasi_tanggal(tanggal):
    """
    Validasi format tanggal sederhana (DD-MM-YYYY)
    """
    if len(tanggal) == 10 and tanggal[2] == "-" and tanggal[5] == "-":
        return True
    return False
