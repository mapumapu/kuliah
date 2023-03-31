# Identifikasi Masalah
# Bagaimana menghitung total harga yang harus dibayar oleh pembeli berdasarkan berat mangga yang dibeli dan harga per kilogramnya.

# Algoritma
# Masukkan harga mangga perkilogram ke variable hrg
# Masukkan berat mangga yang dibeli ke variable brt
# Hitung total harga mangga dengan mengalikan harga mangga perkilo(hrg) dengan berat mangga yang dibeli(brt)
# Simpan hasilnya ke variable byr
# Print variable byr sebagai total pembayaran yang harus dibayar oleh pembeli

# Pseudocode
# input hrg
# input brt
# byr = hrg * brt
# print byr

# Contoh Implementasi dengan Python
# Input harga mangga dan berat yang dibeli
hrg = float(input('Harga Mangga(per kilo) : '))
brt = float(input('Berat Pembelian : '))

# Perhitungan biaya yang harus dibayar pembeli
byr = hrg * brt

# Print total harga yang harus dibayar pembeli
print('Total Harga : ' + str(byr))
