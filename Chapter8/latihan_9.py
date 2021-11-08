buah = {'apel' : 5000, 'jeruk' : 8500, 'mangga' : 7800, 'duku' : 6500}

beli = input('Buah yang dibeli: ')
if beli in buah:
    try:
        berat = int(input('Berapa Kg       : '))
        total = berat * buah[beli]
        print('----------------------------')
        print('Total harga     :',total)
    except ValueError:
        print('Input tidak valid')
    
else:
    print('Buah tidak tersedia')

