gajiPokok = 5000000
produkTerjual = int(input('Terjual : '))

if produkTerjual >= 100 :
  bonus = 0.2 * gajiPokok

else :
  bonus = 0.1 * gajiPokok

gajiAkhir = gajiPokok + bonus

print(gajiAkhir)