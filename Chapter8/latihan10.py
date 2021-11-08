buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}
print(buah)
totharga = 0
try:
    while True:  
        beli = input('Buah yang dibeli: ')
        if beli in buah:
            berat = int(input('Berapa Kg       : '))
            cek = input('Beli buah lain(y/n)? ')
            total = berat * buah[beli]
            totharga += total
            if cek == 'y' or cek == 'Y':
                True
            elif cek == 'n' or cek == 'N':
                print('----------------------------')
                print('Total harga     :',totharga)
                break
            else:
                print('Pilihan tidak tersedia')
                break
        else:
            print('Buah tidak tersedia')
                
except ValueError:
    print('input tidak valid')
    
