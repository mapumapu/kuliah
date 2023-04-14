# input total harga pembelian
totalHarga = int(input('Masukkan Total harga pembelian : '))

# 
if totalHarga > 200000 :
  potonganHarga = 0.2 * totalHarga
  print('Anda mendapatkan potongan harga sebesar 20%')

else :
  potonganHarga = 0
  print('Anda tidak mendapatkan potongan harga')

totalBayar = totalHarga - potonganHarga

print('Total Pembayaran : ', totalBayar)



