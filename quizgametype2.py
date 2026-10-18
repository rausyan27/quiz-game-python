soal_list =[
    {
        "pertanyaan": "Apa ibu kota Indonesia?",
        "jawaban_benar": "1",
        "pilihan":["Jakarta","Bandung","Surabaya","Medan"]
    },
    {
        "pertanyaan": "Berapa 2 + 2?",
        "jawaban_benar": "3",
        "pilihan":["2","3","4","5"]
    },
    {
        "pertanyaan": "Siapa presiden Indonesia saat ini?",
        "jawaban_benar": "2",
        "pilihan":["jokowi dodo","prabowo","ganjar","anies"]
    },
    {
        "pertanyaan": "Bahasa pemrograman apa yang kita pelajari?",
        "jawaban_benar": "1",
        "pilihan": ["Python", "Java", "C++", "JavaScript"]
    },
    {   
        "pertanyaan": "Berapa 10 x 10?",
        "jawaban_benar": "3",
        "pilihan": ["10", "110", "100", "1000"]
    }
]

skor = 0
total_soal = len(soal_list)

print("=====QUIZ GAME=====")
print(f"Total soal: {total_soal}\n")

for nomor,soal in enumerate(soal_list, 1):
    print(f"SOAL {nomor}: {soal['pertanyaan']}")

    for idx, pilihan in enumerate(soal["pilihan"], 1):
        print(f"  {idx}. {pilihan}")

    jawaban = input("Pilih nomor (1-4): ")

    if jawaban == soal["jawaban_benar"]:
            print("BENAR!\n")
            skor += 1
    else:
            jawaban_idx = int(soal["jawaban_benar"]) -1
            print(f"SALAH! jawaban benar: {soal['pilihan'][jawaban_idx]}\n")

print("=====HASIL AKHIR=====")
print(F"Skor: {skor}/{total_soal}")

if skor == total_soal:
    print("SEMPURNA!")
elif skor >= total_soal // 2:
    print("LUMAYAN!")
else:
    print("COBA LAGI!")

