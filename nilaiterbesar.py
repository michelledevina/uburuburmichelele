try:
    A = int(input("Masukkan nilai A: "))
    B = int(input("Masukkan nilai B: "))
    C = int(input("Masukkan nilai C: "))

    if A > B and A > C: 
        print("A terbesar")
    elif B > A and B > C:
        print("B terbesar")
    elif C > A and C > B: 
        print("C terbesar")
except: 
    print("Angka tidak valid! Masukkan angka yang valid!")