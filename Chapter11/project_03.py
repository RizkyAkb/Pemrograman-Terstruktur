try:
    from datetime import *
    file = open('d:\chap11.txt','r')

    data_perpus = file.readlines()

    search = input('Masukkan Kode Member\t\t: ')


    for i in data_perpus:
    
        pecah = i.replace('\n','')
        pecah = pecah.split('|')
        if search in pecah:
            member = pecah
            break
    
    
    if search in member:
        indeks = member.index(search)
        tgl_pengembalian = datetime.date(datetime.now())
        tgl_kembali = datetime.strptime(member[indeks+4], '%Y-%m-%d').date()

        terlambat = tgl_pengembalian - tgl_kembali
        if int(terlambat.days) < 0:
            terlambat = '0'
            denda = '0'
        else:
            terlambat = int(terlambat.days)
            denda = terlambat * 2000

        print ('\nData Peminjaman Buku')
        print ('Kode Member\t\t\t:', member[indeks])
        print ('Nama Member\t\t\t:', member[indeks+1])
        print ('Judul Buku\t\t\t:', member[indeks+2])
        print ('Tanggal Mulai Pengembalian\t:', member[indeks+3])
        print ('Tanggal Maks Pengembalian\t:', member[indeks+4])
        print ('tanggal Pengembalian\t\t:', str(tgl_pengembalian))
        print ('Terlambat\t\t\t:', str(terlambat),'hari')
        print ('Denda\t\t\t\t: Rp.', denda)
except NameError:
    print('Member tidak ditemukan')
    

   

        
