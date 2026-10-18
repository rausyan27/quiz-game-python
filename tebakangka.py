angka_rahasia = 8
tebakan = 0
while tebakan != angka_rahasia:
   tebakan = int(input("tebaklah angka 1-10: "))
   if tebakan < angka_rahasia:
      print("terlalu kecil!")
   elif tebakan > angka_rahasia:
      print("terlalu besar!")
   else:
      print("anda benar!")

print("Game selesai!")

