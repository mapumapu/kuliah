tinggi = int(input("Masukkan tinggi segitiga siku-siku(Max 100) : "))

if tinggi >= 1 and tinggi <= 100 :

    for i in range(1, tinggi + 1):

        print('* ' * i, end='')
        
        print('')
        
else :
    print('Input melebihi batas!')
    
