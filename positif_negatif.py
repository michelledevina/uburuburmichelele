try:    
    angka = int(input("Masukkan angka: "))
    if angka > 0:
        print("Angka positif")
    elif angka < 0:
        print("Angka negatif")
    else: 
        print("Nol")
except:
    print("Angka tidak valid! Coba lagi")


