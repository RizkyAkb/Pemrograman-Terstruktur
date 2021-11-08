a = [1,5,6,3,6,9,11,20,12]
b = [7,4,5,6,7,1,12,5,9]
print(a)
print(b)

#Menyisipkan nilai ke dalam indeks
a.insert(3,10)
b.insert(2,15)
print(a)
print(b)

#Menambahkan nilai ke indeks terakhir
a.append(4)
b.append(8)
print(a)
print(b)

#Mengurutkan nilai
a.sort()
b.sort()
print(a)
print(b)

#Membuat list yang elemennya merupakan sublist dari list sebelumnya
c = a[:8]
d = b[2:10]
print(c)
print(d)

#Menjumlahkan setiap elemen dari 2 list berbeda yang bersesuaian indeks
e = []
for i in range (len(c)):
    jml = c[i] + d[i]
    e = e + [jml]
print(e)

#Tuple
mytuple = tuple(e)
print(mytuple)

#Nilai min, maks, sum dari elemen e
print('Min: ',min(mytuple))
print('Max: ',max(mytuple))
print('Sum: ',sum(mytuple))

#Menentukan huruf penyusun kata
myString = 'Python adalah bahasa pemrograman yang menyenangkan'
hurufpenyusun = set(myString)
print(hurufpenyusun)

#Mengubah menjadi list dan mengurutkan alfabet
huruf = list(hurufpenyusun)
huruf.sort()
print(huruf)
    
