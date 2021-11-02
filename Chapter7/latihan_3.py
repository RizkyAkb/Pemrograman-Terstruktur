print('------------------------')
print('PROGRAM HITUNG RATA_RATA')
print('------------------------')

tambah = 0
hitung = 0
while True:
    try:
        bil = int(input('Masukkan bilangan bulat: '))
        tambah += bil
        hitung += 1
        cek = input('Lagi (y/n)?: ')
        if cek == 'y' or cek == 'Y':
            True
        elif cek == 'n' or cek == 'N':
            rata = tambah / hitung
            print('Rata-rata = ',rata)
            break
        else:
            print('Pilihan tidak tersedia')
            break
                
    except ValueError:
            print('Bukan bilangan bulat')
            continue
