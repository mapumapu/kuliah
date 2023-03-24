# Identifikasi Masalah
# 1. Berapa biaya yang akan dikeluarkan untuk membeli telur
# 2. Berapa sisa uang setelah membeli telur dan naik angkot

# Dengan function input()
# brt = int(input('Berat Telur(dalam Kilogram) : '))
# hrg = int(input('Harga Telur(per Kilogram) : '))
# ongkos = int(input('Biaya Transportasi(Pulang Pergi) : '))
# uang = int(input('Uang yang dibawa : '))

# Input manual
# Berat telur perkilo
brt = 5

# Harga telur perkilo
hrg = 26000

# ongkos transportasi pulang pergi
ongkos = 3500

# uang yang dibawa ibu
uang = 200000

# Perhitungan total harga telur
total = brt * hrg

# Perhitungan sisa uang ibu
sisa = uang - total - ongkos

# Print sisa uang ibu
print('Sisa uang ibu sebesar : ' + str(sisa)) 
