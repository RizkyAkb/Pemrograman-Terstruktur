tahun = int(input('Masukkan Tahun : '))

if (tahun % 400 == 0):
    print ('Tahun ' + str(tahun) + ' merupakan tahun kabisat')
elif (tahun % 400 != 0):
    if (tahun % 100 == 0):
        print('Tahun ' + str(tahun) + ' bukan tahun kabisat')
    elif (tahun % 100 != 0):
        if (tahun % 4 == 0):
            print('Tahun ' + str(tahun) + ' merupakan tahun kabisat')
        elif (tahun % 4 != 0):
            print('Tahun ' + str(tahun) + ' bukan tahun kabisat')
