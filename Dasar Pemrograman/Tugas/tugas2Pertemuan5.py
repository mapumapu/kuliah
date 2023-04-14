print('GEROBAK FRIED CHICKEN')
print('----------------------------')
print('Kode   Jenis Potong   Harga')
print('----------------------------')
print(' D        Dada      Rp. 2500')
print(' P        Paha      Rp. 2000')
print(' S        Sayap     Rp. 1500')
print('----------------------------')
print('')

banyakJenis = int(input('Banyak Jenis : '))
print('')

kodePotong = []
banyakPotong = []
jenisPotong = []
harga = []
jumlahHarga = []

for i in range(banyakJenis) :
  print('Jenis Ke-', i + 1)
  kodePotong.append(input('Kode Potong[D/P/S] : ').lower())
  banyakPotong.append(int(input('Banyak Potong : '))) 
  print('')

  if kodePotong[i] == 'd' :
    jenisPotong.append('Dada')
    harga.append(2500)
    
  elif kodePotong[i] == 'p' :
    jenisPotong.append('Paha')
    harga.append(2000)
  
  elif kodePotong[i] == 's' :
    jenisPotong.append('Sayap')
    harga.append(1500)

  jumlahHarga.append(harga[i] * banyakPotong[i])
  

print('GEROBAK FRIED CHICKEN')
print('-----------------------------------------------------------------')
print('No.   Jenis Potong    Harga Satuan    Banyak Beli    Jumlah Harga')
print('-----------------------------------------------------------------')

for j in range(banyakJenis) :
  print(f'{j + 1}         {jenisPotong[j]}            {harga[j]}              {banyakPotong[j]}           Rp.{jumlahHarga[j]}')

jumlahBayar = 0
for k in jumlahHarga :
  jumlahBayar = jumlahBayar + k
  
pajak = 0.1 * jumlahBayar
totalBayar = jumlahBayar + pajak

print('-----------------------------------------------------------------')
print('Jumlah Bayar   Rp.',jumlahBayar)
print('Pajak 10%      Rp.',pajak)
print('Total Bayar    Rp.',totalBayar)