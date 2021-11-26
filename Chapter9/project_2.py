def bintang(n):
    space = 2*n-1
    for i in range(n):
        print(('*'*(i*2+1)).center(space))
bintang(4)
