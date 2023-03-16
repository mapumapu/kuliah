print('{:^100}'.format('TOKO MAINAN'))
print('{:^100}'.format('======================'))

namaPembeli = str(input('Nama Pembeli : '))
kodeMainan = str(input('Kode Mainan : '))
harga = int(input('Harga : '))
jumlahBeli = int(input('Jumlah Beli : '))
total = harga * jumlahBeli

print('===========================================')
print('{:<12} = {}'.format('Nama Pembeli',namaPembeli))
print('{:<12} = {}'.format('Kode Mainan',kodeMainan))
print('{:<12} = {}'.format('Harga',harga))
print('{:<12} = {}'.format('Jumlah Beli',jumlahBeli))
print('{:<12} = {}'.format('Total',total))
