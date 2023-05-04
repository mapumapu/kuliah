ayam = int(input('Input Angka 1 - 100 : '))

if ayam >= 1 and ayam <= 100:
  print('tek kotek kotek kotek, anak ayam turun berkotek')
   
  for i in range(ayam) :
    anakAyam = (ayam - i - 1)
    
    if anakAyam == 0 :
      anakAyam = 'induknya'
      
    print('anak ayam turunlah',(ayam - i),'mati satu tinggallah', anakAyam )

else :
  print('Input melebihi batas!')

    