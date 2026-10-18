skor = 0

print("====QUIZ GAME====\n")


print ("Soal 1:Apa Ibu Kota Indonesia?")
print("1.Jakarta")
print("2.Bandung")
print("3.Bekasi")

jawaban = input("pilih jawaban (1/2/3): ")

if jawaban == "1":
    print("BENAR!\n")
    skor += 1

else:
    print("SALAH! jawaban benar : jakarta\n")



print (" Soal 2:Berapa 2 + 2?")
print ("1. 2")
print ("2. 3")
print ("3. 4")

jawaban = input("pilih jawaban (1/2/3): ")

if jawaban == "3":
    print("BENAR!\n")
    skor += 1

else:
    print("SALAH! Jawaban Benar: 4\n")
  

print (f"=== HASIL AKHIR ===")
print (f"Skor Kamu: {skor}/2")

if skor == 2:
    print("SEMPURNA!")
elif skor == 1:
    print("LUMAYAN!")
else:
    print("COBA LAGI YA!")

