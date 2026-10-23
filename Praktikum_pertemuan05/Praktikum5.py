biaya_admin = 2500 # variabel global

def hitung_total(harga):
    # Membuat variabel lokal total (harga ditambah biaya_admin)
    total = harga + biaya_admin
    # Kembalikan total
    return total

print(hitung_total(15000))