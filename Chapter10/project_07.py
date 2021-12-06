try:
    file = open('d:\chap10_6.txt','r')
    file_hasil = open('d:\chap10_7.txt','w')

    file_read = file.read()

    
    n = int(input('Masukkan angka pergeseran sebelumnya: '))
    
    data_denkrip = ''
    for i in file_read:
        char = ord(i)
        if char >= 65 and char <= 90:
            char_enc = char - n
            char_final = chr(char_enc)
            if char_enc < 65:
                char_enc = (char_enc + 90) - 64
                char_final = chr(char_enc)
            
            data_denkrip += char_final
        
        elif char >= 97 and char <= 122:
            char_enc = char - n
            char_final = chr(char_enc)
            if char_enc < 97:
                char_enc = (char_enc + 122) - 96
                char_final = chr(char_enc)
            
            data_denkrip += char_final
        else:
            data_denkrip += chr(char)
                
    print(data_denkrip)        
    file_hasil.write(data_denkrip)    
    file_hasil.close()

except ValueError:
    print('Input tidak vaild!')
