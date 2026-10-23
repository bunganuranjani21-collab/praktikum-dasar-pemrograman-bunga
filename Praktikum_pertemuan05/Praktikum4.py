def buat_biodata(nama, umur, jurusan):
    # Menampilkan biodata mahasiswa
    print("=== BIODATA MAHASISWA ===")
    print(f"Nama    : {nama}")
    print(f"Umur    : {umur} tahun")
    print(f"Jurusan : {jurusan}")

# UJI DENGAN DUA CARA PEMANGGILAN

# Cara 1: Positional Argument (Urutan argumen harus sesuai dengan parameter fungsi)
print("--- Menggunakan Positional Argument ---")
buat_biodata("Bunga", 18, "Sistem Informasi")

# Cara 2: Keyword Argument (Urutan bebas karena nama parameter disebutkan)
print("\n--- Menggunakan Keyword Argument (Urutan Berbeda) ---")
buat_biodata(jurusan="Sistem Informasi", nama="Bunga", umur=18)
