import random
bot = ['batu', 'gunting','kertas']

while True:
    x = random.choice(bot)
    data = input('Masukan Pilihan: ')
    if data.lower() == x:
        print(f'pilihanmu adalah {data.capitalize()}')
        print(f'pilihan bot adalah {x.capitalize()}')
        print("Hasil seri\n\n")

    # Bagian Menang
    elif data.lower() == 'batu' and x == 'gunting':
        print(f'pilihanmu adalah {data.capitalize()}')
        print(f'pilihan bot adalah {x.capitalize()}')
        print("Kamu Menang\n\n")
    
    elif data.lower() == 'kertas' and x == 'batu':
        print(f'pilihanmu adalah {data.capitalize()}')
        print(f'pilihan bot adalah {x.capitalize()}')
        print("Kamu Menang\n\n")
    
    elif data.lower() == 'gunting' and x == 'kertas':
        print(f'pilihanmu adalah {data.capitalize()}')
        print(f'pilihan bot adalah {x.capitalize()}')
        print("Kamu Menang\n\n")
    
    # Bagian Kalah
    elif data.lower() == 'gunting' and x == 'batu':
        print(f'pilihanmu adalah {data.capitalize()}')
        print(f'pilihan bot adalah {x.capitalize()}')
        print("Kamu Kalah\n\n")
    
    elif data.lower() == 'batu' and x == 'kertas':
        print(f'pilihanmu adalah {data.capitalize()}')
        print(f'pilihan bot adalah {x.capitalize()}')
        print("Kamu Kalah\n\n")
    
    elif data.lower() == 'kertas' and x == 'gunting':
        print(f'pilihanmu adalah {data.capitalize()}')
        print(f'pilihan bot adalah {x.capitalize()}')
        print("Kamu Kalah\n\n")
    
    else:
        print('Data yang dimasukkan salah\n\n')