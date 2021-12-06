file = open('d:\chap10_5.txt','r')
file_hasil = open('d:\chap10_52.txt','w')

data = file.readlines()
data_baru = ''

for i in data:
    pecah = i.split('|')
    jml = int(pecah[0]) + int(pecah[1].replace('\n', ''))
    data_baru += str(jml) + '\n'
    
file_hasil.write(data_baru)
file_hasil.close()

