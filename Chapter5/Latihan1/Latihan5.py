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

stat_nikah = int(input('Masukkan Status(1:menikah,2:belum): '))

if (stat_nikah == 1):
    tnjpasangan = 10 / 100 * gaji 
    jmlanak = int(input('Masukkan Jumlah Anak : '))
    tnjanak = 5 / 100 * gaji
    tnjanak = jmlanak * tnjanak
    stat = 'Menikah'
elif (stat_nikah == 2):
    tnjpasangan = 0
    tnjanak = 0
    stat = 'Belum Menikah'

gaji_kotor = gaji + tnjpasangan + tnjanak
gaji_bersih = gaji_kotor - potongan

print ('=================================')
print ('STRUK RINCIAN GAJI KARYAWAN')
print ('---------------------------------')
print ('Nama Karyawan         :', nama_kar, '(Kode:{'+ kode_kar +'})')
print ('Golongan              :', gol_kar)
print ('Status Menikah        :', stat)
print ('---------------------------------')
print ('Gaji Pokok            : Rp.', gaji)
print ('Tunjangan Istri/Suami : Rp.', tnjpasangan)
print ('Tunjangan Anak        : Rp.', tnjanak)
print ('--------------------------------- +')
print ('Gaji Kotor            : Rp.', int(gaji_kotor))
print ('Potongan ('+ str(potong) +'%)       : Rp.', int(potongan))
print ('--------------------------------- -')
print ('Gaji Bersih           : Rp.', int(gaji_bersih))
