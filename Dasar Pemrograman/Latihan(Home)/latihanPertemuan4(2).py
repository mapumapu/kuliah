namaPembeli = input('Nama Pembeli : ')
nomorHandphone = input('No. Handphone : ')
jurusan = input('Jurusan [SBY/BL/LMP] : ').lower()

if jurusan == 'sby' :
  kotaTujuan = 'Surabaya'
  harga = 300000

elif jurusan == 'bl' :
  kotaTujuan = 'Bali'
  harga = 350000
  
elif jurusan == 'lmp' :
  kotaTujuan = 'Lampung'
  harga = 500000

else :
  print('Jurusan tidak tersedia')
  
jumlahBeli = int(input('Jumlah Beli : '))
potongan = 0

if jumlahBeli >= 3 :
  potongan = (jumlahBeli * harga) * 0.1
  
total = (jumlahBeli * harga) - potongan

print('======================')
print(namaPembeli)
print(nomorHandphone)
print((jurusan).upper())
print(kotaTujuan)
print(harga)
print(jumlahBeli)

print('======================')
print(potongan)
print(total)

uangBayar = int(input('Masukkan Uang Bayar : '))
uangKembali = uangBayar - total
print(uangKembali)


  