print('      PROGRAM HITUNG GAJI KARYAWAN')
print('')
nama = input('        Nama Karyawan : ')
golongan = input      ('          Golongan Jabatan(1/2/3)  : ')
pendidikan = input    ('          Pendidikan(SMA/D1/D3/S1) : ').lower()
jamKerja = float(input('          Jumlah Jam Kerja         : '))
gaji = 300000


# Tunjangan Jabatan
if golongan == '1' :
  tunjanganJabatan = 0.05 * gaji

elif golongan == '2' :
  tunjanganJabatan = 0.1 * gaji

elif golongan == '3' :
  tunjanganJabatan = 0.15 * gaji
  

# Tunjangan Pendidikan
if pendidikan == 'sma' :
  tunjanganPendidikan = 0.025 * gaji

elif pendidikan == 'd1' : 
  tunjanganPendidikan = 0.05 * gaji
  
elif pendidikan == 'd3' : 
  tunjanganPendidikan = 0.2 * gaji
  
elif pendidikan == 's1' : 
  tunjanganPendidikan = 0.3 * gaji
  

# Lembur
if jamKerja > 8 :
  honorLembur = 3500 * (jamKerja - 8)

else :
  honorLembur = 0
  

totalGaji = gaji + tunjanganJabatan + tunjanganPendidikan + honorLembur

print('')
print('        Karyawan yang bernama ', nama )
print('        Honor yang diterima')
print('          Tunjangan Jabatan      Rp.', tunjanganJabatan)
print('          Tunjangan  Pendidikan  Rp.', tunjanganPendidikan)
print('          Honor Lembur           Rp.', honorLembur)
print('                                   ______________ +')
print('           Total Gaji              Rp.', totalGaji)
print('(Gaji pokok + tunjangan + lembur)')
