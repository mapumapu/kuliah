# Identifikasi Masalah
# Bagaimana menghitung total harga yang harus dibayar oleh pembeli berdasarkan berat mangga yang dibeli dan harga per kilogramnya.

# Algoritma
# Masukkan harga perkilogram ke variable hrg
# Masukkan berat pembelian ke variable brt
# Hitung total harga mangga dengan mengalikan variable hrg dengan variable brt
# Simpan hasilnya ke variable byr
# Print variable byr sebagai total pembayaran yang harus dibayar oleh pembeli

# Implementasi dengan Python
# Input harga mangga dan berat yang dibeli
hrg = int(input('Harga Mangga(per kilo) : '))
brt = float(input('Berat Pembelian : '))

# Perhitungan biaya yang harus dibayar pembeli
byr = hrg * brt

# Print total harga yang harus dibayar pembeli
print('Total Harga : ' + str(byr))
