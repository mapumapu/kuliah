# input gaji pokok dan total jam kerja
gajiPokok = int(input('Gaji Pokok : '))
totalJamKerja = int(input('Total Jam Kerja(Per Jam) : '))

# perhitungan tunjangan dan uang lembur jika kurang dari 200 jam
tunjangan = int(gajiPokok * 0.2)

# default value variable uangLembur
uangLembur = 0

# perhitungan uang lembur jika total jam kerja lebih dari 200 jam
if totalJamKerja > 200 :
    uangLembur = (totalJamKerja - 200) * 20000

# perhitungan total gaji sebelum pajak
totalGaji = gajiPokok + tunjangan + uangLembur

# perhitungan pajak
pajak = int(0.1 * totalGaji)

# perhitungan total gaji setelah dikurangi pajak
gajiBersih = totalGaji - pajak


print('==============================')
print('# PENGHASILAN #')
print('Gaji Pokok : Rp.',gajiPokok)
print('Tunjangan : Rp.',tunjangan)
print('Uang Lembur : Rp.',uangLembur)
print('Total Penghasilan : Rp.',totalGaji)
print('==============================')
print('# PENGURANGAN #')
print('Besaran Pajak (10%) : Rp.',pajak)
print('Total Pengurangan : Rp.',pajak)
print('==============================')
print('# PENGHASILAN YANG DITERIMA #')
print('Gaji Bersih : Rp.',gajiBersih)
print('==============================')