nilai = int(input("masukkan nilai (0-100): "))
kehadiran = int(input("masukkan kehadiran (0-100): "))

if nilai >= 80:
    if kehadiran >= 90:
        print("A plus")
    else:
        print ("A")

else:
    if nilai >= 70:
        if kehadiran >= 90:
            print("B plus")
        else:
            print("B")

    else:
        print("C")


    


    
    
