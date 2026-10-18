print("=== SIMPLE CALCULATOR ===")
num1 = int(input("Angka pertama: "))
num2 = int(input("Angka kedua: "))
operasi = input("Operasi (+, -, *, /): ")

if operasi == "+":
    hasil = num1 + num2
elif operasi == "-":
    hasil = num1 - num2
elif operasi == "*":
    hasil = num1 * num2
elif operasi == "/":
    hasil = num1 / num2
else:
    print("Operasi tidak valid!")
    hasil = None

if hasil is not None:
    print(f"Hasil: {num1} {operasi} {num2} = {hasil}")
