import os  # Mengimpor modul 'os' untuk operasi sistem file, seperti membaca folder dan memeriksa keberadaan path
import shutil  # Mengimpor modul 'shutil' untuk memindahkan (move) file

path = input("Enter Path: ")  # Meminta pengguna memasukkan path folder yang akan diorganisir
files = os.listdir(path)  # Mengambil semua nama file dan folder dalam path tersebut

# Melakukan iterasi pada semua file di dalam folder
for file in files:
    filename, extension = os.path.splitext(file)  # Memisahkan nama file dan ekstensi (misalnya: "dokumen.txt" → "dokumen", ".txt")
    extension = extension[1:]  # Menghapus titik (.) di depan ekstensi, misalnya ".txt" → "txt"

    # Cek apakah folder dengan nama ekstensi sudah ada
    if os.path.exists(path + '/' + extension):
        # Jika sudah ada, pindahkan file ke folder tersebut
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)
    else:
        # Jika belum ada, buat folder baru dengan nama ekstensi
        os.makedirs(path + '/' + extension)
        # Lalu pindahkan file ke folder yang baru dibuat
        shutil.move(path + '/' + file, path + '/' + extension + '/' + file)