print("=====CHATBOT=====")
print("ketik 'bye' untuk keluar\n")

while True:
    pesan = input("kamu: ").lower()

    if pesan == "halo" or pesan == "hi":
        print("Bot:Halo! Ada yang bisa dibantu?")
    elif pesan == "siapa kamu":
        print("Bot:Aku chatbot sederhana buatan Ocan!")
    elif pesan == "apa hobi kamu":
        print("Bot:mengabdi padamu")
    elif pesan == "bye":
        print("Bot: Dadah! Sampai jumpa!")
        break  # keluar dari loop
    else:
        print("Bot: Maaf, aku belum paham itu.")

     

