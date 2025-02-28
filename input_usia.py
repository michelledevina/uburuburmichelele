try:
    usia = int(input("Masukkan usia: "))
    print(f"Usia Anda: {usia}")
except ValueError:
    print("Tidak valid! Silakan masukkan angka")
