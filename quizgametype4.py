import os

soal_list = [
    {
        "pertanyaan": "Apa ibu kota Indonesia?",
        "jawaban_benar": "1",
        "pilihan": ["Jakarta", "Bandung", "Surabaya", "Medan"]
    },
    {
        "pertanyaan": "Berapa 2 + 2?",
        "jawaban_benar": "3",
        "pilihan": ["2", "3", "4", "5"]
    },
    {
        "pertanyaan": "Siapa presiden Indonesia saat ini?",
        "jawaban_benar": "2",
        "pilihan": ["Joko Widodo", "Prabowo", "Ganjar", "Anies"]
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


def tampilkan_soal(nomor,soal):
    print(f"\nSOAL {nomor}: {soal['pertanyaan']}")
    for idx, pilihan in enumerate(soal["pilihan"], 1):
        print(f"  {idx}. {pilihan}")


def cek_jawaban(jawaban,soal):
    if jawaban ==  soal["jawaban_benar"]:
        print("BENAR!\n")
        return True
    else:
        jawaban_idx = int(soal["jawaban_benar"]) -1
        print(f"SALAH! jawaban benar: {soal['pilihan'][jawaban_idx]}\n")
        return False


def tampilkan_hasil(skor,total):
    print("===== HASIL AKHIR =====")
    print(f"Skor = {skor}/{total}")
    presentase = (skor / total) * 100
    print(f"Nilai: {presentase:.0f}%")

    if skor == total:
        print("SEMPURNAA!")
    elif presentase >= 60:
        print("LUMAYAN!")
    else:
        print("coba lagi!")


def ambil_highscore():
    if not os.path.exists("highscore.txt"):
        return 0
    with open("highscore.txt", "r" ) as file:
        return int(file.read())



def simpan_highscore(skor_baru, highscore_lama):
    if skor_baru > highscore_lama:
        print(f"SELAMAT! REKOR BARU TELAH TERCAPAI:{skor_baru}")
        with open("highscore.txt","w" ) as file:
            file.write(str(skor_baru))

    else:
        print(f"High score tetap: {highscore_lama}")




def main():
    print("=== QUIZ GAME v4 ===\n")

    highscore_lama = ambil_highscore()
    print(f"High Score Saat Ini: {highscore_lama}\n")


    skor = 0
    total = len(soal_list)

    for nomor, soal in enumerate(soal_list, 1):
        tampilkan_soal(nomor, soal)
        jawaban = input("pilih nomor (1-4): ")
        if cek_jawaban(jawaban, soal):
            skor += 1

    tampilkan_hasil (skor, total)

    simpan_highscore(skor,highscore_lama)


main()

    