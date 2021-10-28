from operation import *

print('2 + 4 * 6 - 4 = ', end='')
a = kali(4,6)
b = jumlah(2,a)
c = kurang(b,4)
print(c)

print('(4 + 7)*(6 - 9) = ', end='')
a = jumlah(4,7)
b = kurang(6,9)
c = kali(a,b)
print(c)

print('(10 + 2)/(7 + 5)/(12 - 34) = ', end='')
a = jumlah(10,2)
b = jumlah(7,5)
c = kurang(12,34)
d = bagi(a,b)
e = bagi(d,c)
print(e)
