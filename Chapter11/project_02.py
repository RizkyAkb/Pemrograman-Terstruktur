from datetime import *
file = open('d:\chap11.txt','a')

while True:
    kode = input('Masukkan Kode Member\t: ')
    nama = input('Masukkan Nama Member\t: ')
    judul_buku = input('Masukkan Judul Buku\t: ')

    tgl_pinjam = datetime.date(datetime.now())
    tgl_kembali = tgl_pinjam + timedelta(days=7)
    

    pick = input('Ingin input lagi? (y/n): ')
    
    if pick == 'y':
        file.write(kode + '|' + nama + '|' + judul_buku +
               '|' + str(tgl_pinjam) + '|' + str(tgl_kembali) + '\n')
        continue
    elif pick == 'n':
        file.write(kode + '|' + nama + '|' + judul_buku +
               '|' + str(tgl_pinjam) + '|' + str(tgl_kembali) + '\n')
        print('Data berhasil ditambahkan')
        file.close()
        break
    else:
        print('Pilihan tidak tersedia!!!')
        continue
