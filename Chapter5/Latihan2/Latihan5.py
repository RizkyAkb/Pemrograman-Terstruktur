from random import randint
angka = randint(0, 100)
print ('Hai.. nama saya Mr. Lappie, saya telah memilih sebuah bilangan bulat secara acak antara 0s/d 100. Silakan tebak ya!!!')
while True:
    tebakan = int(input('Tebakan Anda : '))
    if tebakan > angka :
        print ('HEHEHE bilangan anda terlalu besar')
    elif tebakan < angka :
        print ('HEHEHE bilangan anda terlalu kecil')
    elif tebakan == angka :
        print ('YEEEEE bilangan tebakan anda benar :)')
        break
    

