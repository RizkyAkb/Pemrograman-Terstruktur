from random import randint
score = 100
angka = randint(0, 100)
print ('Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0s/d 100. Silakan tebak ya!!!')
while True:
    tebakan = int(input('Tebakan Anda : '))
    if tebakan > angka :
        print ('HEHEHE bilangan anda terlalu besar')
    elif tebakan < angka :
        print ('HEHEHE bilangan anda terlalu kecil')
    else :
        print ('YEEEEE bilangan tebakan anda benar :)')
        break
    score -= 2
    if score == 0 :
        print ('Score anda sudah 0, anda tidak diperkenankan mencoba lagi')
        break
    
print ('Score anda: ',score)


