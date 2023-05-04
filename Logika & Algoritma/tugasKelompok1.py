tinggi = int(input('Masukkan Tinggi Segitiga Sama Kaki(Max 100) : '))

if tinggi >= 1 and tinggi <= 100 :
  for i in range(1, tinggi + 1) :
    print(' ' * (tinggi - i), end = '')
    
    print('* ' * i)

else :
  print('Tinggi melebihi batas!')