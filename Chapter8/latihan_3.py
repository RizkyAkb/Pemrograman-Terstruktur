data = []

mhs = int(input('Berapa banyak mahasiswa yang ingin di inputkan?: '))
for i in range(mhs):
    nama = input('Masukkan nama: ')
    data.append(nama)
 
for nama in data:
    print(nama, '('+ str(len(nama)) +'karakter)')
