def faktorial(n):
    faktor = 1
    while (n > 0):
        faktor *= n
        n -= 1
    return faktor

def C(a,b):
    c = faktorial(a) / (faktorial(b) * faktorial(a - b))
    print (c)
        
def P(a,b):
    p = faktorial(a) / faktorial(a-b)
    print (p)

C(5,3)
P(10,7)

