def starFormation1(n):
    for i in range(n):
        for j in range(i+1):
            print('*',end='')
        print()

def starFormation2(n):
    for i in reversed(range(n)):
        for j in range(i+1):
            print('*',end='')
        print()

def starFormation(n):
    starFormation1(n//2)
    starFormation2(n//2+1)

starFormation1(4)
starFormation2(4)
starFormation(7)
