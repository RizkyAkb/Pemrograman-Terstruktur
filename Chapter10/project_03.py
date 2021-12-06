file = open('d:\chap10_2.txt','r')

data = file.readlines()
data_mhs = []

for i in data:
    pecah = i.split('|')
    
    nim = pecah[0]
    nama = pecah[1]
    alamat = pecah[2].replace('\n', '')

    hasil = {'nim':nim,'nama':nama,'alamat':alamat}
    data_mhs.append(hasil)
    
print ('data_mhs =',data_mhs)
file.close()
