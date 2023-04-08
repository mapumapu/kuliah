print('{:^62}'.format('TOKO MAINAN'))
print('{:^62}'.format('====================='))

namaPembeli = input('Masukkan Nama Pmebeli : ')
kodeMainan = input('Masukkan Kode Mainan : ')
harga = int(input('Masukkan Harga : '))
jumlahBeli = int(input('Masukkan Jumlah Beli : '))
total = harga * jumlahBeli

print('=========================================')
print('{:<12} = {}'.format('Nama Pembeli', namaPembeli))
print('{:<12} = {}'.format('Kode Mainan', kodeMainan))
print('{:<12} = {}'.format('Harga', harga))
print('{:<12} = {}'.format('Jumlah Beli', jumlahBeli))
print('{:<12} = {}'.format('Total', total))