def bintang(n):
    space = 2*n-1
    if n%2 == 0:
        for i in range(n//2):
            print(('*'*(i*2+1)).center(space))
        for i in reversed(range(n//2)):
            print(('*'*(i*2+1)).center(space))
    else:
        for i in range(n//2):
            print(('*'*(i*2+1)).center(space))
        for i in reversed(range(n//2+1)):
            print(('*'*(i*2+1)).center(space))
bintang(7)
