harga_satuan = float(input("Masukkan harga satuan: "))
jumlah = int(input("Masukkan jumlah barang: "))
persen_diskon = float(input("Masukkan persen diskon: "))

subtotal = harga_satuan * jumlah
nominal_diskon = subtotal * persen_diskon / 100
total_bayar = subtotal - nominal_diskon

print("Subtotal =", subtotal)
print("Nominal diskon =", nominal_diskon)
print("Total bayar =", total_bayar)
