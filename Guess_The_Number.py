import random

acak = random.randint(1, 100)
peluang = 10
while peluang > 0:
    data = int(input("Masukkan angka tebakan: "))
    if data > acak:
        peluang -= 1
        print("Angka tebakan nilainya lebih kecil")
        print(f"Tersisa", peluang, "kesempatan lagi\n")

    if data < acak:
        peluang -= 1
        print("Angka tebakan nilainya lebih besar")
        print(f"Tersisa", peluang, "kesempatan lagi\n")

    if data == acak:
        peluang -= 1
        print("Selamat, tebakanmu benar!")
        print(f"Tersisa", peluang, "kesempatan lagi\n")
        break
    
if peluang == 0:
    print("Kesempatanmu telah habis, kamu kalah")
    print(f"Angka tebakan adalah {acak}")