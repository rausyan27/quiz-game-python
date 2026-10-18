print("=== PASSWORD GENERATOR ===")
nama = input("Nama kamu: ")
tahun = input("Tahun lahir: ")

nama_clean = nama.replace(" ", "").capitalize()
acak = "xyz123"

password = f"{nama_clean}@{tahun}{acak}"
print(f"Password kamu: {password}")
