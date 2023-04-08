gajiPokok = int(input('Gaji Pokok : '))
tunjangan = gajiPokok * 0.2
totalJamKerja = int(input('Total Jam Kerja(Per Jam) : '))
uangLembur = 0

if totalJamKerja > 200 :
    uangLembur = (totalJamKerja - 200) * 20000
    
totalGaji = gajiPokok + tunjangan + uangLembur
pajak = 0.1 * totalGaji
gajiBersih = totalGaji - pajak

print(gajiBersih)