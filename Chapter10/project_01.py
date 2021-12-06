file = open('d:\chap10_1.txt','r')

ganjil = 0
genap = 0


for data in file:
    if int(data) % 2 == 0:
        genap += 1
    elif int(data) % 2 != 0:
        ganjil += 1
    
print ('Banyaknya bilangan genap :',genap)
print ('Banyaknya bilangan ganjil:',ganjil)
file.close()
