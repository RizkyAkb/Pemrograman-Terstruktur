file = open('d:\chap10_2.txt','r')

data = file.readlines()
nim = []
nama = []
alamat = []

cari = input('Masukkan NIM :')

for i in data:
    pecah = i.split('|')
    
    nim.append(pecah[0])
    nama.append(pecah[1])
    alamat.append(pecah[2].replace('\n', ''))

if cari in nim:
    indeks = nim.index(cari)
    print ('NIM\t:',nim[indeks])
    print ('Nama\t:',nama[indeks])
    print ('Alamat\t:',alamat[indeks])

else:
    print ('Data tidak ditemukan')

file.close()
