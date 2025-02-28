try:

    bulan = int(input("Masukkan bulan (1-12): "))

    jumlah_hari = {
        1: 31, 2: 29, 3: 31, 4: 30, 5: 31, 6: 30,
        7: 31, 8: 31, 9: 30, 10: 31, 11: 30, 12: 31
    }
    
    if 1 <= bulan <= 12:
        print(f"Jumlah hari: {jumlah_hari[bulan]}")
    else:
        print("Bulan tidak valid!")

except ValueError:
    print("Input tidak valid! Harap masukkan angka antara 1-12.")
