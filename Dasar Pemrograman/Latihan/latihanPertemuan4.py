print('{:^100}'.format('Input Data Pendaftaran'))
print('{:^100}'.format('======================================'))

formatHeaderPrint = '=============================== \nBiaya Kuliah \n==============================='
nis = input('Nomor Induk Siswa : ')
nama = input('Nama Lengkap : ')
jurusan = input('Jurusan (SI/SIA): ').lower()
namaProdi = ''
harga = ''

if jurusan == 'si' :
  print(formatHeaderPrint)
  namaProdi = 'Sistem Informasi'
  harga = '2,400,000'
  
elif jurusan == 'sia' :
  print(formatHeaderPrint)
  namaProdi = 'Sistem Informasi Akutansi'
  harga = '2,000,000'
  
else : 
  print('input jurusan salah! inputkan SI atau SIA')

if jurusan == 'si' or jurusan == 'sia' :
  print('Nama Prodi : '+namaProdi+'\nBiaya : '+harga)

