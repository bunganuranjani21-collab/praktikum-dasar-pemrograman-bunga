def konversi_menit_ke_detik(menit):
    """
    Fungsi untuk mengonversi waktu dari satuan menit ke satuan detik.

    Parameter:
    menit (int/float): Jumlah waktu dalam satuan menit yang akan dikonversi.

    Return:
    int/float: Hasil konversi waktu dalam satuan detik.
    """
    # Menghitung detik (1 menit = 60 detik)
    detik = menit * 60
    # Return hasil
    return detik

print(konversi_menit_ke_detik(3))
print(konversi_menit_ke_detik.__doc__)