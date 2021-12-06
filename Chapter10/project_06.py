try:
    file = open('d:\chap10_asli.txt','r')
    file_hasil = open('d:\chap10_6.txt','w')

    file_read = file.read()


    n = int(input('Masukkan angka pergeseran: '))
    
    data_enkrip = ''
    for i in file_read:
        char = ord(i)
        if char >= 65 and char <= 90:
            char_enc = char + n
            char_final = chr(char_enc)
            if char_enc > 90:
                char_enc = (char_enc - 90) + 64
                char_final = chr(char_enc)
            
            data_enkrip += char_final
        
        elif char >= 97 and char <= 122:
            char_enc = char + n
            char_final = chr(char_enc)
            if char_enc > 122:
                char_enc = (char_enc - 122) + 96
                char_final = chr(char_enc)
            
            data_enkrip += char_final
        else:
            data_enkrip += chr(char)
                
    print(data_enkrip)        
    file_hasil.write(data_enkrip)    
    file_hasil.close()

except ValueError:
    print('Input tidak vaild!')
