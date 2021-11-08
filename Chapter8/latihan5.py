def kuadrat(bil):
    for i in range(len(bil)):
        bil[i]**=2
    return bil

bil = []
byk = int(input('Berapa banyak angka yang ingin di inputkan?: '))
for i in range(byk):
    angka = int(input('Masukkan angka: '))
    bil.append(angka)

print(bil)    
print(kuadrat(bil))
