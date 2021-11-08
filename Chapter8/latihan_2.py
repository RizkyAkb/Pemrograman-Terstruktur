def datastat(x):
    a = sum(x)/len(x)
    b = max(x)
    c = min(x)
    return(a,b,c)

data = []
byk = int(input('Berapa banyak angka yang ingin di inputkan?: '))
for i in range(byk):
    angka = int(input('Masukkan angka: '))
    data.append(angka)
    
print('rata2,max,min:',datastat(data))
