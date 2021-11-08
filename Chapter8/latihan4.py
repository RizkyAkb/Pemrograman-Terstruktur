sayur = ['bayam', 'kangkung', 'wortel', 'selada']
print(sayur)
def menu():
    print('Menu:')
    print('1. Tambah data sayur')
    print('2. Hapus data sayur')
    print('3. Tampilkan data sayur')
    print('4. Keluar')
    pick = input('Pilih...')
    if pick == '1':
        print('--Tambah data sayur--')
        tambah = input('Tambah sayur= ')
        sayur.append(tambah)
        menu()
    elif pick == '2':
        try:
            print('--Hapus data sayur--')
            hapus = input('Hapus sayur= ')
            sayur.remove(hapus)
            menu()
        except ValueError:
            print('Data tidak ditemukan')
            print('')
            menu()
    elif pick == '3':
        print('--Data sayur--')
        print(sayur)
        print('')
        menu()
    elif pick == '4':
        quit()
    else:
        print('Pilihan tidak ada, silahkan ulangi lagi')
        print('')
        menu()
menu()

    
