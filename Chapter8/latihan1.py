urut = []
byk = int(input('Berapa banyak angka yang ingin di inputkan?: '))

for i in range(byk):
    angka = int(input('Masukkan angka: '))
    urut.append(angka)
    
urut.sort(reverse=True)
print(urut)
    
