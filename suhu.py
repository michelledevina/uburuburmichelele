try:
    suhu = int(input("Masukkan suhu tubuh: "))

    if suhu >= 38: 
        print ("Anda demam")
    else:
        print ("Anda tidak demam")
except: 
    print ("Input tidak valid!")
    