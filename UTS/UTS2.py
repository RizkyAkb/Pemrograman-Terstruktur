from random import randint
print('1. Level 1 (Penjumlahan)')
print('2. Level 2 (Pengurangan)')
print('3. Level 3 (Perkalian)')
print('4. Exit')
level = int(input('Pilih nomor pilihan: '))
nyawa = 3
skor = 0

while True:
    X = randint(-100, 100)
    Y = randint(-100, 100)
    if (level == 1):
        kuis = X + Y
        print (X, '+', Y, 'adalah ')
        jawaban = int(input('jawab: '))
        
    elif (level == 2):
        kuis = X - Y
        print (X, '-', Y, 'adalah ')
        jawaban = int(input('jawab: '))
        
    elif (level == 3):
        kuis = X * Y
        print (X, '*', Y, 'adalah ')
        jawaban = int(input('jawab: '))

    elif (level == 4):
        exit()
    else:
        print('Maaf pilihan Anda salah')
        exit()
    
    if (jawaban == kuis):
        skor += 2
        print('Hore... jawaban Anda benar! skor Anda',skor, '(lives: '+str(nyawa)+')')
        print('-----------------------')
        
    elif (jawaban != kuis):
        skor -= 2
        nyawa -= 1
        print('Duh... jawaban Anda salah! skor Anda',skor,'(lives: '+str(nyawa)+')')
        print('-----------------------')
        if(nyawa == 0):
            print('GAME OVER')
            break

