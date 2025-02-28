try:    

    sisi_1 = int (input("Masukkan sisi 1: "))
    sisi_2 = int (input("Masukkan sisi 2: "))
    sisi_3 = int (input("Masukkan sisi 3: "))

    if sisi_1 == sisi_2 == sisi_3:
        print ("3 sisi sama")
    elif sisi_1 != sisi_2 and sisi_1 != sisi_3 and sisi_2 != sisi_3:
        print ("Tidak ada yang sama")
    else: 
        print ("2 sisi sama")

except ValueError:
    print("Input tidak valid!")       



