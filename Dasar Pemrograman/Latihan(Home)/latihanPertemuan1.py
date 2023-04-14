print("   GEROBAK FRIED CHICKEN LUCIANA  ")
print("=============================")
print("Kode Jenis Potong Harga")
print("=============================")
print("D     Dada         2500")
print("P     Paha         2000")
print("S     Sayap        1500")

banyak_jenis = int(input("Banyak Jenis : "))
total_bayar = 0

print(" GEROBAK FRIED CHICKEN LUCIANA  ")
print("===========================================")
print("No   Jenis     Harga        Banyak    Jumlah")
print("     Potong    Satuan       Beli      Harga ")
print("===========================================")

for i in range(banyak_jenis):
    print("Jenis Ke - ", i+1)
    kode_potong = input("Kode Potong [D/P/S] : ")
    banyak_potong = int(input("Banyak Potong : "))

    if kode_potong == "D" or kode_potong == "d":
        jenis_potong = "Dada"
        harga = 2500
    elif kode_potong == "P" or kode_potong == "p":
        jenis_potong = "Paha"
        harga = 2000
    elif kode_potong == "S" or kode_potong == "s":
        jenis_potong = "Sayap"
        harga = 1500
    else:
        jenis_potong = "Kode Salah"
        harga = 0
        banyak_potong = 0

    jumlah = banyak_potong * harga
    total_bayar += jumlah

    print("%i    %s       %i        %i         %i" % (i+1, jenis_potong, harga, banyak_potong, jumlah))

pajak = total_bayar * 0.1 
print("Pajak 10 % Rp. ", pajak)
print("Total Bayar Rp. ", total_bayar + pajak)
jumlah_bayar = int(input("Jumlah Bayar Rp. "))

kembalian = jumlah_bayar - (total_bayar + pajak)
if kembalian >= 0:
    print("Kembalian Rp. ", kembalian)
else:
    print("Maaf uang anda kurang sebesar Rp. ", abs(kembalian))
