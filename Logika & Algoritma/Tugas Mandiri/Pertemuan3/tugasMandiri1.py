# inisialisasi value awal
bilangan1 = 60
bilangan2 = 20
bilangan3 = 100
bilangan4 = 40

# variable pembanding
bilangan_terbesar = bilangan1

# membandingkan variable bilangan2 dengan variable bilangan_terbesar mana yang lebih besar valuenya
if bilangan2 > bilangan_terbesar:
    # jika true, value variable bilangan_terbesar berubah menjadi value variable bilangan2
    bilangan_terbesar = bilangan2
    # jika false, makan akan ke "if condition" yang selanjutnya
    
# membandingkan variable bilangan3 dengan variable bilangan_terbesar mana yang lebih besar valuenya
if bilangan3 > bilangan_terbesar:
    # jika true, value variable bilangan_terbesar berubah menjadi value variable bilangan3
    bilangan_terbesar = bilangan3
    # jika false, makan akan ke "if condition" yang selanjutnya
    
# membandingkan variable bilangan4 dengan variable bilangan_terbesar mana yang lebih besar valuenya
if bilangan4 > bilangan_terbesar:
    # jika true, value variable bilangan_terbesar berubah menjadi value variable bilangan4
    bilangan_terbesar = bilangan4
    # jika false, maka value variable bilangan_terbesar akan tetap/tidak berubah

# print bilangan terbesar
print("Bilangan terbesar adalah:", bilangan_terbesar)