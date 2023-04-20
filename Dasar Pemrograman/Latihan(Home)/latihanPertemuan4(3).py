nama = input('Nama : ')
nis = input('NIS : ')
kodeProdi = input('Kode Prodi[SI/SIA] : ').lower()

if kodeProdi == 'si' :
  namaProdi = 'Sistem Informasi'
  harga = '2,400,000'

elif kodeProdi == 'sia' :
  namaProdi = 'Sistem Informasi Akutansi'
  harga = '2,000,000'
  
else :
  print('Input Kode Jurusan Salah')
  exit()


if kodeProdi == 'si' or kodeProdi == 'sia' :
  print('==================================')
  print('Nama               : ', nama)
  print('NIS                : ', nis)
  print('Kode Prodi         : ',(kodeProdi).upper())
  print('Nama Prodi Pilihan : ',namaProdi)
  print('Biaya              : ', harga)
  print('==================================')