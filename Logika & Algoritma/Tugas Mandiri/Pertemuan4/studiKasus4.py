gajiPokok = 5000000

# input produk terjual dan harga jual produk
produkTerjual = int(input('Total produk terjual : '))
hargaJualProduk = int(input('Harga Jual Produk : '))

# perhitungan omset dan bonus
omsetPejualan = produkTerjual * hargaJualProduk
bonus = int(0.1 * omsetPejualan)

# perhitungan bonus jika produk terjual lebih dari 100
if produkTerjual > 100 :
  bonus = int(0.2 * omsetPejualan)

# perhitungan gaji akhir yang diterima
gajiAkhir = gajiPokok + bonus


print('Gaji Pokok         : Rp.', gajiPokok)
print('Produk Terjual     :', produkTerjual, 'pcs')
print('Harga Jual Produk  : Rp.', hargaJualProduk, 'per pcs')
print('Omset Penjualan    : Rp.', omsetPejualan)
print('Bonus              : Rp.', bonus)
print('==============================')
print('Total Gaji yang diterima : Rp.', gajiAkhir)  
