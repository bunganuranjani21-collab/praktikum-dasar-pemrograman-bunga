def sapa_mahasiswa(nama, sapaan='Selamat belajar'):
    # Menampilkan sapaan dan nama mahasiswa
    print(f"{sapaan}, {nama}!")

# UJI DENGAN DUA CARA PEMANGGILAN

# Cara 1: Memanggil fungsi dengan satu argumen (menggunakan sapaan default)
print("--- Cara 1 (Default) ---")
sapa_mahasiswa("Bunga")

# Cara 2: Memanggil fungsi dengan kedua argumen (mengubah sapaan default)
print("\n--- Cara 2 (Kustom) ---")
sapa_mahasiswa("Bunga", "Selamat pagi")