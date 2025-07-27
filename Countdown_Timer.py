import time  # Mengimpor modul 'time' untuk menggunakan fungsi time.sleep()

my_time = int(input("Enter the time in seconds: "))  # Meminta input dari pengguna (dalam detik) lalu mengubahnya menjadi integer

# Perulangan mundur mulai dari nilai 'my_time' sampai 1 (tidak termasuk 0)
for x in range(my_time, 0, -1):  
    seconds = x % 60  # Mengambil sisa detik dari total detik yang tersisa
    minutes = int(x / 60) % 60  # Menghitung total menit (modulo 60 agar tidak lebih dari 59)
    hours = int(x / 3600)  # Menghitung total jam (setiap 3600 detik adalah 1 jam)

    # Menampilkan waktu dengan format 2 digit: jam:menit:detik
    print(f"{hours:02}:{minutes:02}:{seconds:02}")  

    time.sleep(1)  # Menjeda program selama 1 detik (agar tampil seperti countdown)

# Setelah loop selesai, cetak pesan bahwa waktu telah habis
print("TIME'S UP!")
