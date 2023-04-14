nama = input('Nama : ')
nis = input('NIS : ')
jurusan = input('Kode Jurusan(SI/SIA) : ').lower()

if jurusan == 'si' :
  namaProdi = 'Sistem Informasi'
  harga = '2.400.000'

elif jurusan == 'sia' :
  namaProdi = 'Sistem Informasi Akutansi'
  harga = '2.000.000'
  
else :
  print('Jurusan Tidak Tersedia')
  exit()
  
print('==================================')
print('Nama               : ',nama)
print('NIS                : ',nis)
print('Kode Prodi         : ',(jurusan).upper())
print('Nama Prodi Pilihan : ',namaProdi)
print('Biaya              : ',harga)
print('==================================')
