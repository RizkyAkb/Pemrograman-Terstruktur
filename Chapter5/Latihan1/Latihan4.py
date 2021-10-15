kode_kar = input('Masukkan Kode Karyawan : ')
nama_kar = input('Masukkan Nama Karyawan : ')
gol_kar  = input('Masukkan Golongan      : ')


if (gol_kar == 'A') or (gol_kar == 'a'):
    gaji = 10000000
    potong = 2.5
    potongan = potong / 100 * gaji 
elif (gol_kar == 'B') or (gol_kar == 'b'):
    gaji = 8500000
    potong = 2
    potongan = potong / 100 * gaji 
elif (gol_kar == 'C') or (gol_kar == 'c'):
    gaji = 7000000
    potong = 1.5
    potongan = potong / 100 * gaji 
elif (gol_kar == 'D') or (gol_kar == 'd'):
    gaji = 5500000
    potong = 1
    potongan = potong / 100 * gaji
    
gaji_bersih = gaji - potongan

print ('=================================')
print ('STRUK RINCIAN GAJI KARYAWAN')
print ('---------------------------------')
print ('Nama Karyawan    :', nama_kar, '(Kode:{'+ kode_kar +'})')
print ('Golongan         :', gol_kar)
print ('Gaji Pokok       : Rp.', gaji)
print ('Potongan ('+ str(potong) +'%)  : Rp.', int(potongan))
print ('--------------------------------- -')
print ('Gaji Bersih      : Rp.', int(gaji_bersih))
