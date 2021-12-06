file = open('d:\chap10_2.txt','a')

while True:
    nim = input('Masukkan NIM   : ')
    nama = input('Masukkan Nama  : ')
    alamat = input('Masukkan Alamat: ')

    file.write(nim + '|' + nama + '|' + alamat + '\n')
    pick = input('Ingin input lagi? (y/n): ')
    
    if pick == 'y':
        continue
    elif pick == 'n':
        print('Data sudah ditambahkan')
        file.close()
        break
    else:
        print('Pilihan tidak tersedia!!!')
        continue
