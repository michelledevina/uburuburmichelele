try:
    angka = int(input("Masukkan angka: "))
    print("Angka positif" if angka > 0 else "Angka negatif" if angka < 0 else "Nol")
except ValueError:
    print("Angka tidak valid! Coba lagi")
